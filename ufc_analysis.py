import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("ufc_names.csv")


df.loc[df['total_rounds_fought'] > 1]
df.loc[df['avg_TD_att'] < 400] # There was one fighter who averaged more than 400 attempts per game, which is not physically possible.


# create MinMaxScaler object
scaler = MinMaxScaler()

# normalize 'income' column
df['avg_SIG_STR_att_normalized'] = scaler.fit_transform(df[['avg_SIG_STR_att']])
df['avg_SUB_ATT_normalized'] = scaler.fit_transform(df[['avg_SUB_ATT']])
df['avg_TD_att_normalized'] = scaler.fit_transform(df[['avg_TD_att']])





from sklearn.cluster import KMeans
import numpy as np


# initialize KMeans object
kmeans = KMeans(n_clusters=3)



# fit KMeans object to data
kmeans.fit(df[['avg_TD_att_normalized','avg_SUB_ATT_normalized','avg_TD_att_normalized']])

# retrieve cluster labels
labels = kmeans.labels_


print(labels)
df['style'] = labels

print(df[df['fighter'] == 'Israel Adesanya'])
print(df[df['fighter'] == 'Khabib Nurmagomedov'])
print(df[df['fighter'] == 'Gavin Tucker'])


z = df['avg_SUB_ATT_normalized']
x = df['avg_TD_att_normalized']
y = df['avg_SIG_STR_att_normalized']

# Create a 3D figure
ax = plt.axes(projection='3d')

# Plot the data as a 3D scatter plot
ax.scatter(x, y, z, c=labels, labels = ["one", "two","three"])

# Add labels and title
ax.set_xlabel('Average Significat Strikes')
ax.set_ylabel('Average Submission Attempts')
ax.set_zlabel('Average Takedown Attempts')
ax.set_title('3D Scatter Plot')

ax.legend('asdf',loc = "lower left")
ax.legend(['one'],loc = "lower left")
# Display the plot
plt.figure(1)
plt.show()



import pickle
filename = 'ufc_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(kmeans, file)



df.to_csv("ufc_names3.csv")