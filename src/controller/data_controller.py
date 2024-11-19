from functools import lru_cache
from flask import jsonify
from src.process_data import calculate_delays, average_delay, clean_flight_data


class DataController:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/flight_delay_by_airline', methods=['GET'])
        @lru_cache
        def get_average_delay():
            df = self.get_data()
            df = average_delay(df)
            return df.to_json(orient='records')
        
        @self.app.route('/flight_delay_by_reason', methods=['GET'])
        @lru_cache
        def get_delay_reason():
            df = self.get_data()
            delay_columns = ['weather_delay', 'technical_delay', 'operational_delay', 'atc_delay', 'security_delay']
            total_delays = df[delay_columns].sum() # Sum the delays for each cause
            delay_breakdown = [{"reason": col, "value": total_delays[col]} for col in delay_columns]  # List of dicts
            return delay_breakdown

        @self.app.route('/get_delay_flight_data/<string:airline>', methods=['GET'])
        @lru_cache
        def get_delay_flight_data(airline):
            df = self.get_data()
            airline_df = df[df['Airline'] == airline]

            if airline_df.empty:
                return jsonify({'error': f'No data found for airline: {airline}'}), 404

            rows = airline_df.to_dict(orient='records')

            data = []
            for row in rows:
                data.append({
                    'date': row['Date'],
                    'flightNumber': row['Flight Number'],
                    'origin': row['Origin'],
                    'destination': row['Destination'],
                    'scheduledDeparture': row['Scheduled Departure Time'],
                    'actualDeparture': row['Actual Departure Time'],
                    'delay': row['ttl_delay']
            })
            return jsonify(data)
        
        @self.app.route('/get_insights', methods=['GET'])
        def get_insights():
            df = self.get_data()
            data = {
            'total_flights': len(df),
            'total_delays': df[df['ttl_delay'] > 0].shape[0],
            'cancelled_flights': df[df['Cancelled'] == 1].shape[0],
            'average_delay': round(df['ttl_delay'].mean(), 2) if not df['ttl_delay'].isnull().all() else 0
            }
            return data

    @lru_cache
    def get_data(self):
        df = clean_flight_data('data/flight_delays(2023-2024).csv')
        df = calculate_delays(df)
        return df;
        