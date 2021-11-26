import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
from pathlib import Path

st.title('RES Data Visualization Tool')

date = st.date_input("Select a date", datetime.date(2021, 9, 15))

options = st.multiselect('Select what plots to show',
                         [
                             'sorted_timestamp_vs_temp_x_and_ambient_temp',
                             'sorted_timestamp_vs_irradiance',
                             'sorted_timestamp_vs_panel_x_watts',
                             'sorted_normalized_panel_x_watts',
                             'sorted_panel_x_output_watt_hours',
                             'sorted_panel_x_theoretical_max_output_power',
                         ],
                         ['sorted_timestamp_vs_irradiance', 'sorted_timestamp_vs_panel_x_watts', 'sorted_timestamp_vs_temp_x_and_ambient_temp'])

##

#
for x in options:
    file_path = Path(__file__).parents[1] / \
        ('processed_data/' + str(date) + '/' + str(x))
    image = Image.open(str(file_path) + '.png')
    st.image(image, caption=str(x), width=None)