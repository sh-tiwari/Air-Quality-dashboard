# Air Quality Monitoring Dashboard

A real-time dashboard to monitor air quality metrics including PM2.5, PM10, Ozone, Humidity, Temperature, and CO levels using data from [ThingSpeak API](https://thingspeak.com/).

## Features

- **Real-Time Updates**: Automatically refreshes data every 30 minutes.
- **Interactive Visualizations**:
  - Line charts for individual metrics.
  - Pie chart displaying the air composition (PM2.5, PM10, Ozone, Humidity, CO).
- **User-Friendly Interface**:
  - Sidebar to select specific metrics or view all metrics combined.
  - Default "All" view to display air composition as a pie chart.
- **Responsive Design**: Optimized for desktop and mobile use.

## Deployed Application

[Access the AQMD Dashboard here](https://aqmd-dashboard-2tlp06vuein.streamlit.app/)

## Installation Instructions

### Prerequisites
- Python 3.8 or above.
- Recommended: Virtual Environment.

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   streamlit run streamlit_aqmd_dashboard.py
   ```

4. Access the application at `http://localhost:8501` in your browser.

## File Structure
- `streamlit_aqmd_dashboard.py`: Main Streamlit application script.
- `requirements.txt`: List of Python dependencies.

## API Details
The data is fetched from [ThingSpeak API](https://thingspeak.com/):
- URL: `https://api.thingspeak.com/channels/1596152/feeds.json?results=50`

Metrics:
- **PM2.5**: Particulate matter of diameter ≤2.5 µm.
- **PM10**: Particulate matter of diameter ≤10 µm.
- **Ozone**: Ozone levels.
- **Humidity**: Humidity percentage.
- **Temperature**: Air temperature in degrees Celsius.
- **CO**: Carbon Monoxide concentration.

## Usage Guide
- Select the desired metric from the sidebar dropdown.
- View the line chart or pie chart based on the selection.
- Pie chart is displayed by default showing all metrics except Temperature.
- Latest data and metrics are prominently displayed at the top.

## Future Enhancements
- Add historical data analysis.
- Incorporate alerts for hazardous air quality levels.
- Enable customization of refresh rate and time ranges.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact
For any questions or support, please reach out via the issues section of the repository.

