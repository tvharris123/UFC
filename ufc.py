import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''

The point of this script is to get the most recent per game averages by fighter of relevant detailes (average submission, takedown, and strike attemtps).

It then exports this data to a csv where the columns are name, followed by relevant categories.

'''





print('started')
df = pd.read_csv("data.csv")
df = df.sort_values(by='date')

df = df.dropna(subset=["B_fighter", "B_avg_SIG_STR_att", "B_avg_SUB_ATT", "B_avg_TD_att","B_avg_LEG_att", "B_avg_GROUND_att", "B_total_rounds_fought", "R_avg_LEG_att", "R_avg_GROUND_att", "R_fighter", "R_avg_SIG_STR_att", "R_avg_SUB_ATT", "R_avg_TD_att", "R_total_rounds_fought"])
df_blue_unique = df.drop_duplicates(subset = ['B_fighter'], keep = "first")

blue_csv = df_blue_unique[["B_fighter", "B_avg_SIG_STR_att", "B_avg_SUB_ATT", "B_avg_TD_att","B_avg_LEG_att", "B_avg_GROUND_att", "B_total_rounds_fought"]]

blue_csv['total_strikes_b'] = np.multiply(df["B_avg_SIG_STR_att"], df['B_total_rounds_fought'])


blue_csv['total_tds_b'] = np.multiply(df['B_avg_TD_att'],df['B_total_rounds_fought'])
blue_csv['total_sbs_b'] = np.multiply(df['B_avg_SUB_ATT'],df['B_total_rounds_fought'])


df_red_unique = df.drop_duplicates(subset = ['R_fighter'], keep = "last")

red_csv = df_red_unique[["R_fighter", "R_avg_SIG_STR_att", "R_avg_SUB_ATT", "R_avg_TD_att","R_avg_LEG_att", "R_avg_GROUND_att", "R_total_rounds_fought"]]
red_csv['total_strikes_r'] = np.multiply(df["R_avg_SIG_STR_att"],df['R_total_rounds_fought'])
red_csv['total_tds_r'] = np.multiply(df['R_avg_TD_att'],df['R_total_rounds_fought'])
red_csv['total_sbs_r'] = np.multiply(df['R_avg_SUB_ATT'],df['R_total_rounds_fought'])


final = pd.concat([blue_csv, red_csv], axis=0)


final.to_csv("ufc_final.csv")
#corr = final['B_avg_SIG_STR_att'].corr(final['B_avg_SUB_ATT'])

# print the correlation
#print(corr)

ufc_names = pd.DataFrame(columns= ["fighter", "avg_SIG_STR_att", "avg_SUB_ATT", "avg_TD_att", "total_rounds_fought", "avg_LEG_att", "avg_GROUND_att"])

_lst = []
for i in range(len(final)):
    name = final['B_fighter'].iloc[i]
    if (name != ""):
        for j in range(len(final)):
            if(final['R_fighter'].iloc[j] == name):
                if (final['B_total_rounds_fought'].iloc[i] > final['B_total_rounds_fought'].iloc[j]):
                    fighter = [final['B_fighter'].iloc[i], final['B_avg_SIG_STR_att'].iloc[i],final['B_avg_SUB_ATT'].iloc[i],final['B_avg_TD_att'].iloc[i],final['B_total_rounds_fought'].iloc[i], final["B_avg_LEG_att"].iloc[i], final["B_avg_GROUND_att"].iloc[i] ]
                    fighter = pd.Series(fighter)
                    ufc_names = pd.concat([ufc_names, fighter], ignore_index=False, axis = 1)
                    break

                else:
                    fighter = [final['R_fighter'].iloc[j], final['R_avg_SIG_STR_att'].iloc[j],final['R_avg_SUB_ATT'].iloc[j],final['R_avg_TD_att'].iloc[j],final['R_total_rounds_fought'].iloc[j], final["R_avg_LEG_att"].iloc[j], final["R_avg_GROUND_att"].iloc[j]]
                    fighter = pd.Series(fighter)
                    ufc_names = pd.concat([ufc_names, fighter], ignore_index=False, axis = 1)
                    break



ufc_names = ufc_names.transpose()
ufc_names.to_csv("ufc_names3.csv")
print("done")