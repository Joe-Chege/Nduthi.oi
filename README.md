# Nduthi.oi USSD Service

Nduthi.oi is a USSD-based application designed to estimate the fuel efficiency and travel distance of motorcycles based on their engine capacity (cc) and average travel speed (km/hr). The application allows users to make informed decisions about fuel usage and costs for their motorcycle trips.

## Features

- Select motorcycle engine capacity (100cc, 125cc, 150cc, 200cc)
- Select average travel speed (20 km/hr, 30 km/hr, 40 km/hr)
- Calculate and display the estimated distance that can be covered on a full tank (10 liters) based on the selected engine capacity and speed
- Calculate and display the estimated fuel cost for the trip

## Project Structure

- `app.py`: Main application file containing the USSD service logic and calculation methods.
- `requirements.txt`: List of dependencies required to run the application.

## Dependencies

- Flask: A lightweight WSGI web application framework in Python.
- gunicorn: A Python WSGI HTTP server for UNIX.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nduthi-oi.git
   ```
2. Navigate to the project directory:
   ```bash
   cd nduthi-oi
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally, use the following command:
```bash
flask run
```
By default, the application will be accessible at `http://127.0.0.1:5000/`.

## USSD Interaction Flow

1. **Welcome Screen**:
   ```
   CON Welcome to Nduthi.oi!
   1. Estimate Fuel Efficiency
   2. More Information (Coming Soon)
   ```

2. **Select Engine Capacity**:
   ```
   CON Select your motorcycle engine capacity:
   1. 100cc
   2. 125cc
   3. 150cc
   4. 200cc
   ```

3. **Select Average Travel Speed**:
   ```
   CON Select your average travel speed (km/hr):
   1. 20 km/hr
   2. 30 km/hr
   3. 40 km/hr
   ```

4. **Display Estimated Distance and Fuel Cost**:
   ```
   END Estimated distance on full tank: X.XX km
   Estimated fuel cost: KES Y.YY
   ```

## Calculation Methods

### `calculate_distance(engine_capacity, average_speed)`
Calculates the estimated distance that can be covered on a full tank of 10 liters based on the given engine capacity and average speed.

### `calculate_cost(distance)`
Calculates the estimated fuel cost based on the given distance and a fixed fuel price per liter.

## Example Calculations

1. **100cc engine at 20 km/hr**:
   - Distance: `(40 km/l * 10 liters) = 400 km`
   - Fuel Cost: `(400 km * 193 KES/l) / 40 km/l = KES 1930`

2. **125cc engine at 30 km/hr**:
   - Distance: `(45 km/l * 10 liters) = 450 km`
   - Fuel Cost: `(450 km * 193 KES/l) / 45 km/l = KES 1930`

## Handling Errors

The application includes basic error handling to manage invalid inputs and ensure a smooth user experience.

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or issues, please contact [njorogejosephchege@gmail.com](Joe-Chege).

.