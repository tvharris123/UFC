import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("ufc_names3.csv")

'''

The point of this file is the actual algorithm I used to classify fighters.

It will also plot in 3d and output to the fighters csv where the last column 'style' is 0 1 or 2 

0 = grappler
1 = all-arounder
2 = striker

'''

scaler = MinMaxScaler()

df['avg_SIG_STR_att_normalized'] = scaler.fit_transform(df[['avg_SIG_STR_att']])
df['avg_SUB_ATT_normalized'] = scaler.fit_transform(df[['avg_SUB_ATT']])
df['avg_TD_att_normalized'] = scaler.fit_transform(df[['avg_TD_att']])
df['avg_LEG_att_normalized'] = scaler.fit_transform(df[['avg_LEG_att']])
df['avg_GROUND_att_normalized'] = scaler.fit_transform(df[['avg_GROUND_att']])

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# initialize KMeans object



# fit KMeans object to data
# X = (df[["avg_SIG_STR_att_normalized", "avg_SUB_ATT_normalized", "avg_TD_att_normalized", "avg_LEG_att_normalized", "avg_GROUND_att_normalized"]])



# # retrieve cluster labels
# dbscan = DBSCAN(eps=0.5, min_samples=100)
# dbscan.fit(X)

# labels = dbscan.labels_

# print(labels)

df['combine'] = (df['avg_SUB_ATT'] + df['avg_TD_att'])

df['ratio'] = df['avg_SIG_STR_att'] / df['combine'].replace(0, 1)

labels = pd.qcut(df['ratio'], q=3, labels=[0,1,2])
print(pd.qcut(df['ratio'], q=3, labels=[0,1,2], retbins=True))


df['style'] = labels

print(df[df['fighter'] == 'Israel Adesanya'])

print(df[df['fighter'] == 'Khabib Nurmagomedov'])
print(df[df['fighter'] == 'Gavin Tucker'])



x = df['avg_TD_att']
y = df['avg_SUB_ATT']
z = df['avg_SIG_STR_att']


# Create a 3D figure
ax = plt.axes(projection='3d')

# Plot the data as a 3D scatter plot
ax.scatter(x, y, z, c = labels)

# Add labels and title
ax.set_xlabel('Average Takedown Attempts')
ax.set_ylabel('Average Submission Attempts')
ax.set_zlabel('Average Significant Strike Attempts')
ax.set_title('3D Scatter Plot of UFC Fighters')


# Display the plot
plt.figure(1)
plt.show()

# plt.hist(df['str_sub_rat'])
# plt.show()

plt.scatter(y,z, c = labels)
plt.xlabel("Average Submission Attempts")
plt.ylabel("Average Significant Strike Takedown Atempts")
plt.title("Scatter Plot of UFC Fighters by Style")

plt.legend(['Strikers', 'Grapplers','All-Rounder'])
plt.show()






df.to_csv("ufc_names3.csv")
