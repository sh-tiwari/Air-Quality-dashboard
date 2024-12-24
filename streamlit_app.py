import streamlit as st
import pandas as pd
import requests
import time

# API URL for real-time data
API_URL = "https://api.thingspeak.com/channels/1596152/feeds.json?results=50"

# Streamlit app configuration
st.set_page_config(page_title="AQMD Dashboard", layout="wide")
st.title("Air Quality Monitoring Dashboard")

# Sidebar configuration
refresh_rate = 30 * 60  # Set refresh rate to 30 minutes
options = ["All", "PM2.5", "PM10", "Ozone", "Humidity", "Temperature", "CO"]
selected_option = st.sidebar.selectbox("Select Data to Visualize", options)

# Fetch data from API
def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Extract fields
        feeds = data['feeds']
        if not feeds:
            st.error("No data available.")
            return None

        # Convert to DataFrame
        df = pd.DataFrame(feeds)
        df['created_at'] = pd.to_datetime(df['created_at'])

        # Rename fields for clarity
        df = df.rename(columns={
            'field1': 'PM2.5',
            'field2': 'PM10',
            'field3': 'Ozone',
            'field4': 'Humidity',
            'field5': 'Temperature',
            'field6': 'CO'
        })

        # Ensure numeric data
        for column in ['PM2.5', 'PM10', 'Ozone', 'Humidity', 'Temperature', 'CO']:
            df[column] = pd.to_numeric(df[column], errors='coerce')

        return df

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Live data display
placeholder = st.empty()

while True:
    data = fetch_data()

    if data is not None:
        with placeholder.container():
            st.subheader("Latest Data")
            st.dataframe(data.tail(5))

            st.subheader("Key Metrics")
            col1, col2, col3 = st.columns(3)

            # Display average metrics (adjust as necessary)
            col1.metric("PM2.5 (Latest)", data['PM2.5'].iloc[-1] if 'PM2.5' in data else "N/A")
            col2.metric("Temperature (Latest)", data['Temperature'].iloc[-1] if 'Temperature' in data else "N/A")
            col3.metric("Humidity (Latest)", data['Humidity'].iloc[-1] if 'Humidity' in data else "N/A")

            st.subheader("Time Series Analysis (Last 10 Hours)")
            last_10 = data.tail(10).set_index('created_at')

            if selected_option == "All":
                st.subheader("Air Composition (Last 10 Records)")
                latest_data = last_10[['PM2.5', 'PM10', 'Ozone', 'Humidity', 'CO']].mean(skipna=True)
                st.plotly_chart(
                    {
                        "data": [
                            {
                                "values": latest_data.tolist(),
                                "labels": latest_data.index.tolist(),
                                "type": "pie"
                            }
                        ],
                        "layout": {
                            "title": "Percentage of Particles in Air"
                        }
                    }
                )
            else:
                st.line_chart(last_10[[selected_option]])

    time.sleep(refresh_rate)
