from flask import Flask, jsonify
from flask_cors import CORS
from src.clean_data import clean_flight_data
from src.process_data import calculate_delays

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Allow CORS for React frontend

@app.route('/get_cleaned_data', methods=['GET'])
def get_cleaned_data():
    df = clean_flight_data('data/Airline_Delay_Cause.csv')
    df = calculate_delays(df)
    df = df.head(10)  # Limit to the first 10 rows
    return df.to_json(orient='records')

@app.route('/get_df', methods=['GET'])
def get_df():
    df = clean_flight_data('data/flights_sample.csv')
    return df.to_json(orient='records')

#To test the application conn.
@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong'

if __name__ == '__main__':
    app.run(debug=True)
