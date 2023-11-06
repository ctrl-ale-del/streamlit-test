import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# San Francisco Map")
st.sidebar.markdown("# San Francisco Map")

#plot data on map of san francisco
# number of points / vertical spread, horizontal spread + coordinates
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [10, 100] + [37.56, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)