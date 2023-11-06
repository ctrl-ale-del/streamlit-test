#Create a data table

import streamlit as st
import pandas as pd
import numpy as np


st.markdown("# Uber Pickups") #Set title of page
st.sidebar.markdown("# Uber Pickups") #Write into sidebar
st.divider()

#Create a column for data and get the url
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#cache data so it doesn't have to load again when running
@st.cache_data
#Create a function to read and load the data from the url
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using cache)')

#printout raw data 
dataTog = st.toggle(':purple[Show Raw Data]')
if dataTog:
    st.subheader(':green[Raw data]')
    st.write(data)


#histogram of the data
hisTog = st.toggle(':purple[Show Histogram]')
if hisTog:
    st.subheader(':blue[Number of Pickups by Hour]')
    # Generate the histogram
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values) #draw the histogram


#Plot data on a map
hour_to_filter = st.slider('Hour', 0, 23, 17) #min, max, default
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f':red[Map of Uber Pickups at {hour_to_filter}:00]')
st.map(filtered_data)