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
                             'Timestamp_vs_Ambient_Temp',
                             'Timestamp_vs_Irradiance',
                             'Timestamp_vs_panel_output_watt_hours_X',
                             'Timestamp_vs_Panel_X_Watts',
                             'Timestamp_vs_Temp_X',
                             'Timestamp_vs_Temp_X_and_Ambient_Temp',
                         ],
                         ['Timestamp_vs_Irradiance', 'Timestamp_vs_Panel_X_Watts', 'Timestamp_vs_Temp_X_and_Ambient_Temp'])


##
#
for x in options:
    file_path = Path(__file__).parents[1] / \
        ('processed_data/' + str(date) + '/' + str(x))
    image = Image.open(str(file_path) + '.png')
    st.image(image, caption=str(x), width=None)


# ##
# #
# file_path = Path(__file__).parents[1] / \
#     ('processed_data/' + str(date) + '/daily_summmary.txt')

# f = open(str(file_path), "r")
# daily_summary_array = f.read().split('\n')
# #
# st.write('\n----------  Daily Summary   ----------\n')
# #
# st.write(str(daily_summary_array[0]))
# st.write(str(daily_summary_array[1]))
# st.write(str(daily_summary_array[2]))
# st.write(str(daily_summary_array[3]))
# #
# st.write('\n')
# #
# st.write(str(daily_summary_array[5]))
# st.write(str(daily_summary_array[6]))
# st.write(str(daily_summary_array[7]))
# st.write(str(daily_summary_array[8]))
# #
# st.write('\n----------  Daily Summary   ----------\n')
