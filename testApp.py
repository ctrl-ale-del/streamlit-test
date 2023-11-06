#Create a data table

import streamlit as st
import pandas as pd
import numpy as np

st.write("Here we are making a table:")
st.write(pd.DataFrame ({
    'first column': [1, 2, 3, 4],
    'second column': [10, 0, 30, 40]
}))


#plot data on map of san francisco
# number of points / vertical spread, horizontal spread + coordinates
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [10, 100] + [37.56, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
