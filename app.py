import os
from flask import Flask, request


app = Flask(__name__)

# Motorcycle engine capacity data (replace with actual data source)
motorcycle_data = {
    100: {  # Engine capacity in cc
        "average_fuel_efficiency": 40  # kilometers per liter
    },
    125: {
        "average_fuel_efficiency": 45
    },
    150: {
        "average_fuel_efficiency": 50
    },
    200: {
        "average_fuel_efficiency": 55
    }
}

# Fuel price (replace with logic to fetch real-time price)
fuel_price_per_liter = 193  # Kenyan shillings

def calculate_distance(engine_capacity, average_speed):
    # Access data based on engine capacity
    average_fuel_efficiency = motorcycle_data.get(engine_capacity, None)
    if not average_fuel_efficiency:
        return "ERR No data for engine capacity " + str(engine_capacity)
    # Calculate distance achievable on a full tank (assuming full tank capacity of 10 liters)
    distance = average_fuel_efficiency * 10
    # Consider average speed for a more accurate estimate (optional)
    distance = distance / average_speed * 100
    return distance

def calculate_cost(distance):
    # Calculate estimated fuel cost for the trip
    fuel_cost = distance * fuel_price_per_liter / 100
    return fuel_cost

user_session_data = {}  # Store data specific to each user session

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    text = request.values.get("text", "default")

    # Manage user session data
    user_data = user_session_data.get(session_id, {})

    if text == '':
        response = "CON Welcome to Nduthi.oi!\n"
        response += "1. Estimate Fuel Efficiency\n"
        response += "2. More Information (Coming Soon)"

    elif text == '1':
        # Request engine capacity if not already provided
        if "engine_capacity" not in user_data:
            response = "CON Select your motorcycle engine capacity:\n"
            response += "1. 100cc\n"
            response += "2. 125cc\n"
            response += "3. 150cc\n"
            response += "4. 200cc\n"
        elif "average_speed" not in user_data:
            # Request average speed if engine capacity is already provided
            response = "CON Select your average travel speed (km/hr):\n"
            response += "1. 20 km/hr\n"
            response += "2. 30 km/hr\n"
            response += "3. 40 km/hr\n"
        else:
            # Calculate and display estimated distance and fuel cost
            distance = calculate_distance(user_data["engine_capacity"], user_data["average_speed"])
            fuel_cost = calculate_cost(distance)
            response = "END Estimated distance on full tank: {} km\n".format(distance)
            response += "Estimated fuel cost: KES {:.2f}".format(fuel_cost)

    elif text.isdigit() and "engine_capacity" not in user_data:
        # Store engine capacity entered by user
        engine_capacity = int(text)
        if engine_capacity not in motorcycle_data:
            response = "ERR Invalid engine capacity"
        else:
            user_data["engine_capacity"] = engine_capacity
            response = "CON Select your average travel speed (km/hr):\n"
            response += "1. 20 km/hr\n"
            response += "2. 30 km/hr\n"
            response += "3. 40 km/hr"
            user_session_data[session_id] = user_data  # Update session data

    elif text.isdigit() and "engine_capacity" in user_data and "average_speed" not in user_data:
        # Store average speed entered by user
        average_speed = int(text)
        if average_speed not in [20, 30, 40]:
            response = "ERR Invalid average speed"
        else:
            user_data["average_speed"] = average_speed
            # Calculate and display estimated distance and fuel cost
            distance = calculate_distance(user_data["engine_capacity"], user_data["average_speed"])
            fuel_cost = calculate_cost(distance)
            response = "END Estimated distance on full tank: {} km\n".format(distance)
            response += "Estimated fuel cost: KES {:.2f}".format(fuel_cost)

    elif text == '2':
        response = "CON More Information (Coming Soon)"

    else:
        response = "ERR Invalid Input"

    return response
