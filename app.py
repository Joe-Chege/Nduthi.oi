from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        response = "CON Welcome to Nduthi.oi!\n"
        response += "1. Estimate Fuel Efficiency\n"
        response += "2. More Information (Coming Soon)"

    elif text == '1':
        # Request engine capacity if not already provided
        user_data = {}  # Define the missing user_data variable
        if "engine_capacity" not in user_data:
            response = "CON Select your motorcycle engine capacity:\n"
            response += "1. 100cc\n"
            response += "2. 125cc\n"
            response += "3. 150cc\n"
            response += "4. 200cc"

    elif text == '1*1':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"

    elif text == '1*1*1':
        # Calculate distance when engine capacity is 100cc and average speed is 20 km/hr
        distance = calculate_distance(100, 20)
        response = "Con Estimated distance on full tank: {:.2f} km".format(distance)
        response = ""
    
    elif text == '1*1*2':
        # Calculate distance when engine capacity is 100cc and average speed is 30 km/hr
        distance = calculate_distance(100, 30)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*1*3':
        # Calculate distance when engine capacity is 100cc and average speed is 40 km/hr
        distance = calculate_distance(100, 40)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*2':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"
    elif text == '1*2*1':
        # Calculate distance when engine capacity is 125cc and average speed is 20 km/hr
        distance = calculate_distance(125, 20)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*2*2':
        # Calculate distance when engine capacity is 125cc and average speed is 30 km/hr
        distance = calculate_distance(125, 30)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*2*3':
        # Calculate distance when engine capacity is 125cc and average speed is 40 km/hr
        distance = calculate_distance(125, 40)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*3':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"
    elif text == '1*3*1':
        # Calculate distance when engine capacity is 150cc and average speed is 20 km/hr
        distance = calculate_distance(150, 20)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*3*2':
        # Calculate distance when engine capacity is 150cc and average speed is 30 km/hr
        distance = calculate_distance(150, 30)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*3*3':
        # Calculate distance when engine capacity is 150cc and average speed is 40 km/hr
        distance = calculate_distance(150, 40)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*4':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"
    elif text == '1*4*1':
        # Calculate distance when engine capacity is 200cc and average speed is 20 km/hr
        distance = calculate_distance(200, 20)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*4*2':
        # Calculate distance when engine capacity is 200cc and average speed is 30 km/hr
        distance = calculate_distance(200, 30)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    elif text == '1*4*3':
        # Calculate distance when engine capacity is 200cc and average speed is 40 km/hr
        distance = calculate_distance(200, 40)
        response = "END Estimated distance on full tank: {:.2f} km".format(distance)
    
    elif text == '2':
        response = "CON More Information (Coming Soon)"

    else:
        response = "ERR Invalid Input"

    return response

def calculate_distance(engine_capacity, average_speed):
    # Access data based on engine capacity
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
    average_fuel_efficiency = motorcycle_data.get(engine_capacity, None)
    if not average_fuel_efficiency:
        return "ERR No data for engine capacity " + str(engine_capacity)
    # Calculate distance achievable on a full tank (assuming full tank capacity of 10 liters)
    distance = average_fuel_efficiency["average_fuel_efficiency"] * 10
    # Calculate distance covered at the selected average speed
    distance = distance * (average_speed / 60)  # Convert average speed from km/hr to km/min
    return distance

if __name__ == "__main__":
    app.run(debug=True)
