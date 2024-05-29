# TODO: Import all necessary libraries
import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py
from IPython.display import display
from plotly.offline import iplot

# Read data using pandas
dp = pd.read_csv(r"/Users/bara/Desktop/Kaggle /archive (2)/earthquakes1970-2014.csv")



# Split the "DateTime" column into separate date and time columns
dp[['Date', 'Time']] = dp['DateTime'].str.split(' ', n =1, expand=True)

# Extracting year from the Date column
dp['Year'] = pd.to_datetime(dp['Date']).dt.year

# Print the first few rows to verify the result
print(dp[['Date', 'Time']].head())

print(dp.columns)


# print(dp.columns)

# Display first few rows
print(dp.head())

# Display info and statistics about the data_frame
print(dp.info())
print(dp.describe())

# Set display options for pandas
pd.set_option("display.max_columns", None)

# Set styles for seaborn and matplotlib
sns.set_style("whitegrid")
plt.style.use("dark_background")

# Since 'Magnitude' seems to be a numerical column, ensure it's correctly typed
dp['Magnitude'] = pd.to_numeric(dp['Magnitude'], errors='coerce')

# Remove rows with missing values in 'Magnitude' column
dp = dp.dropna(subset=['Magnitude'])

# Create a pairplot with seaborn
sns.pairplot(dp, palette="tab20", hue="Magnitude")
plt.show()

# Display pie chart using the 'MagType' column
fig = px.pie(dp, names="MagType", title="Earthquake Types", color="MagType", hole=0.4)
fig.show()

# Create subplots for barplot and pie chart
fig, axes = plt.subplots(1, 2, figsize=(18, 5))

# Generate random colors
colors = [(
    random.uniform(0, 0.3),
    random.uniform(0, 0.5),
    random.uniform(0, 0.5)
) for _ in range(10)]

# Create a barplot for the average Magnitude by MagType
bar_data = dp.groupby(["MagType"], as_index=False)["Magnitude"].mean().sort_values(by="Magnitude")
sns.barplot(ax=axes[1], data=bar_data, x="Magnitude", y="MagType", palette="tab20")

# Create a pie chart for the MagType count
dp["MagType"].value_counts()[:6].plot(
    ax=axes[0],
    kind="pie",
    ylabel=" ",
    autopct="%1.0f%%",
    colors=colors,
    explode=[0.1, 0, 0, 0, 0, 0],
    title="Magnitude Type Count"
)

plt.show()

# Print the value counts for MagType
print(dp["MagType"].value_counts())

# Print all unique sources in the 'Source' column
print("Unique Sources:", dp["Source"].unique())

# Print the counts of each unique source in the 'Source' column
print("Source Counts:\n", dp["Source"].value_counts())

# Scatter plot of Depth and Magnitude using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=dp.Depth, y=dp.Magnitude, mode="markers", marker_color=dp.Magnitude, text=dp.MagType, marker=dict(showscale=True)))
fig.update_layout(title="Depth and Magnitude", xaxis_title="Depth", yaxis_title="Magnitude")
fig.show()

# Kernel density estimation plot
plt.figure(figsize=(15, 5))
sns.kdeplot(data=dp, x="Depth", y="Magnitude", cmap="coolwarm", shade=True)
plt.show()

# Create subplots for bar plots
fig, axes = plt.subplots(1, 2, figsize=(20, 5), dpi=100)
l = sns.barplot(ax=axes[0], data=dp.groupby("Source", as_index=False)["Magnitude"].count().sort_values(by="Magnitude", ascending=False)[:10], x="Magnitude", y="Source")
sns.barplot(ax=axes[1], data=dp.groupby("Source", as_index=False)["Magnitude"].mean().sort_values(by="Magnitude")[:10], x="Magnitude", y="Source", palette="tab10")
axes[0].set_title("Locations With Most Recorded Earthquakes")
axes[1].set_title("Average Magnitude of Locations")
l.set_xlabel("Earthquakes")
plt.show()

# Filter locations
location = dp.loc[dp["Source"].str.contains("NN|CI|HV|UU|WY|NC|UW|PGC|CAS|ISK|ROM|MDD|GUC|UNM|REN|JMA|WEL|SJA|AEI|ATH|UCR|us_|us|AK|NEI|")]
fig = px.pie(location, names="Source", title="Percentage of Earthquakes per Location", hole=0.4)
fig.show()
print(dp["Source"].value_counts()[:8])

# Scatter plot of Date and Magnitude using Plotly
fig = px.scatter(dp, x="Year", y="Magnitude", color="MagType")
fig.show()

print(dp["Magnitude"].value_counts().head(20))


# 3D Scatter plot
trace1 = go.Scatter3d(
    z=dp.Magnitude,
    x=dp.Depth,
    y=dp.Year, 
    mode='markers',
    marker=dict(
        size=3,
        color='rgb(120,0,0)',
    )
)
data1 = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

fig = go.Figure(data=data1, layout=layout)

# Save the plot as an HTML file
fig.write_html("3d_scatter_plot.html")


# Margins of error
error_ = pd.DataFrame({"Type": dp[["Depth_Error", "Magnitude_Error"]].dtypes})
error_["Margins of Error"] = (5304 - dp["Depth_Error"].isnull().sum())
error_.iloc[1, 1] = (5304 - dp["Magnitude_Error"].isnull().sum())
display(error_)
print("Margin of Error Shows out of 5, 304 data points margins of error show pieces of data that have some sort of error")

px.scatter(dp, x="Year", y="Depth_Error", color="MagType").show()
px.scatter(dp, x="Year", y="Magnitude_Error", color="MagType").show()


