# from pathlib import Path
# import pandas as pd
# pd.options.mode.chained_assignment = None  # default='warn'


# df = pd.read_csv('../processed_data/2021-09-15/daily_summmary.txt',
#                 skiprows=1,
#                 )
# print(df)


# f = open("../processed_data/2021-09-15/daily_summmary.txt", "r")
# bingo = f.read().split('\n')
# print(bingo[0]) # panel_1_daily_output_watt_hours
# print(bingo[1]) # panel_2_daily_output_watt_hours
# print(bingo[2]) # panel_3_daily_output_watt_hours
# print(bingo[3]) # panel_4_daily_output_watt_hours
# print(bingo[5]) # panel_1_output_efficiency_max_avg
# print(bingo[6]) # panel_2_output_efficiency_max_avg
# print(bingo[7]) # panel_3_output_efficiency_max_avg
# print(bingo[8]) # panel_4_output_efficiency_max_avg