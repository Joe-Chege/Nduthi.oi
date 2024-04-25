import os
from flask import Flask, request

app = Flask(__name__)

# Motorcycle engine capacity data (replace with actual data source)
motorcycle_data = {
    150: {  # Engine capacity in cc
        "average_fuel_efficiency": 50  # kilometers per liter
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
            response = "CON Enter your motorcycle engine capacity (cc): "
        else:
            # Calculate and display estimated distance
            distance = calculate_distance(user_data["engine_capacity"], 40)  # Assuming average speed of 40 km/hr for now
            response = "END Estimated distance on full tank: " + str(distance) + " km"

    elif text.isdigit() and "engine_capacity" not in user_data:  # User enters engine capacity
        # Validate input (check if it's a number)
        try:
            engine_capacity = int(text)
            user_data["engine_capacity"] = engine_capacity
            response = "CON Enter your average travel speed (km/hr): "
            user_session_data[session_id] = user_data  # Update session data
        except ValueError:
            response = "ERR Invalid engine capacity. Please enter a number."

    elif text.isdigit() and "engine_capacity" in user_data:  # User enters average speed
        # Calculate and display results
        average_speed = int(text)
        distance = calculate_distance(user_data["engine_capacity"], average_speed)
        fuel_cost = calculate_cost(distance)
        response = "END Estimated distance: " + str(distance) + " km\n"
        response += "Estimated fuel cost: KES " + str(f"{fuel_cost:.2f}")  # Format fuel cost to two decimal places

    else:
        response = "ERR Invalid Input"

    return response

if __name__ == '__main__':
    app.run()
