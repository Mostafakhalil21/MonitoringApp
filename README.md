# System Monitoring Dashboard

This repository contains a simple Flask-based web application to monitor real-time CPU and memory usage. The dashboard displays two line charts, one for CPU usage and another for memory usage, that are updated every 5 seconds. The project uses Python's `psutil` library to gather system information and Chart.js for creating the charts.

## Features

- Real-time CPU and memory usage monitoring
- Dynamic line charts with Chart.js
- Responsive layout for different screen sizes
- Alerts when CPU or memory usage exceeds 80%

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/system-monitoring-dashboard.git
   ```

2. Navigate to the project directory:

   ```
   cd system-monitoring-dashboard
   ```

3. Create a virtual environment and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to view the dashboard.

## Dependencies

- Flask: Web framework for Python
- psutil: Cross-platform library for retrieving information on system utilization
- Chart.js: JavaScript library for creating charts

## License

This project is released under the [MIT License](LICENSE).
