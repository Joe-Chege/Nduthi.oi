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

    elif text == '2':
        response = "CON More Information (Coming Soon)"

    else:
        response = "ERR Invalid Input"

    return response
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"


    elif text == '1*2':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"

    elif text == '1*3':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"

    elif text == '1*4':
        # Display options for average travel speed
        response = "CON Select your average travel speed (km/hr):\n"
        response += "1. 20 km/hr\n"
        response += "2. 30 km/hr\n"
        response += "3. 40 km/hr"

    elif text == '1':
        # Request engine capacity if not already provided
        if "engine_capacity" not in user_data:
            response = "CON Select your motorcycle engine capacity:\n"
            response += "1. 100cc\n"
            response += "2. 125cc\n"
            response += "3. 150cc\n"
            response += "4. 200cc\n"
        
        elif text == '1*1':
            # Display options for average travel speed
            response = "CON Select your average travel speed (km/hr):\n"
            response += "1. 20 km/hr\n"
            response += "2. 30 km/hr\n"
            response += "3. 40 km/hr\n"

    elif text == '2':
        response = "CON More Information (Coming Soon)"

    else:
        response = "ERR Invalid Input"

    return response
