#!/usr/bin/env python3

"""
api-service README

A high-quality API service for data retrieval and manipulation.

Usage
-----

To run the API service, execute the following command in the project directory:
```bash
python main.py
```
"""

import os

from dotenv import load_dotenv
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    # Load environment variables from.env file
    load_dotenv()

    # Define API routes
    @app.route('/api/data', methods=['GET'])
    def get_data():
        # Simulate data retrieval from database
        data = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
        return jsonify(data)

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)