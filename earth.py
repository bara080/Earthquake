import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display

# Create a directory for HTML files if it doesn't exist
html_dir = "plotly_html"
os.makedirs(html_dir, exist_ok=True)

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df[['Date', 'Time']] = df['DateTime'].str.split(' ', n=1, expand=True)
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df['Magnitude'] = pd.to_numeric(df['Magnitude'], errors='coerce')
    df = df.dropna(subset=['Magnitude'])
    return df

def display_data_info(df):
    print(df[['Date', 'Time']].head())
    print(df.columns)
    print(df.head())
    print(df.info())
    print(df.describe())

def visualize_data(df):
    sns.set_style("whitegrid")
    plt.style.use("dark_background")
    
    sns.pairplot(df, palette="tab20", hue="Magnitude")
    plt.show()
    
    fig = px.pie(df, names="MagType", title="Earthquake Types", color="MagType", hole=0.4)
    fig.write_html(os.path.join(html_dir, "earthquake_types_pie.html"))
    
    fig, axes = plt.subplots(1, 2, figsize=(18, 5))
    colors = [(random.uniform(0, 0.3), random.uniform(0, 0.5), random.uniform(0, 0.5)) for _ in range(10)]
    bar_data = df.groupby(["MagType"], as_index=False)["Magnitude"].mean().sort_values(by="Magnitude")
    sns.barplot(ax=axes[1], data=bar_data, x="Magnitude", y="MagType", palette="tab20")
    
    df["MagType"].value_counts()[:6].plot(ax=axes[0], kind="pie", ylabel=" ", autopct="%1.0f%%", colors=colors, explode=[0.1, 0, 0, 0, 0, 0], title="Magnitude Type Count")
    plt.show()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Depth, y=df.Magnitude, mode="markers", marker_color=df.Magnitude, text=df.MagType, marker=dict(showscale=True)))
    fig.update_layout(title="Depth and Magnitude", xaxis_title="Depth", yaxis_title="Magnitude")
    fig.write_html(os.path.join(html_dir, "depth_vs_magnitude_scatter.html"))
    
    plt.figure(figsize=(15, 5))
    sns.kdeplot(data=df, x="Depth", y="Magnitude", cmap="coolwarm", shade=True)
    plt.show()
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 5), dpi=100)
    sns.barplot(ax=axes[0], data=df.groupby("Source", as_index=False)["Magnitude"].count().sort_values(by="Magnitude", ascending=False)[:10], x="Magnitude", y="Source")
    sns.barplot(ax=axes[1], data=df.groupby("Source", as_index=False)["Magnitude"].mean().sort_values(by="Magnitude")[:10], x="Magnitude", y="Source", palette="tab10")
    axes[0].set_title("Locations With Most Recorded Earthquakes")
    axes[1].set_title("Average Magnitude of Locations")
    plt.show()
    
    location = df.loc[df["Source"].str.contains("NN|CI|HV|UU|WY|NC|UW|PGC|CAS|ISK|ROM|MDD|GUC|UNM|REN|JMA|WEL|SJA|AEI|ATH|UCR|us_|us|AK|NEI|")]
    fig = px.pie(location, names="Source", title="Percentage of Earthquakes per Location", hole=0.4)
    fig.write_html(os.path.join(html_dir, "earthquakes_per_location_pie.html"))
    
    fig = px.scatter(df, x="Year", y="Magnitude", color="MagType")
    fig.write_html(os.path.join(html_dir, "year_vs_magnitude_scatter.html"))
    
    trace1 = go.Scatter3d(z=df.Magnitude, x=df.Depth, y=df.Year, mode='markers', marker=dict(size=3, color='rgb(120,0,0)'))
    data1 = [trace1]
    layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
    fig = go.Figure(data=data1, layout=layout)
    fig.write_html(os.path.join(html_dir, "3d_scatter_plot.html"))
    
    error_ = pd.DataFrame({"Type": df[["Depth_Error", "Magnitude_Error"]].dtypes})
    error_["Margins of Error"] = (5304 - df["Depth_Error"].isnull().sum())
    error_.iloc[1, 1] = (5304 - df["Magnitude_Error"].isnull().sum())
    display(error_)
    
    fig = px.scatter(df, x="Year", y="Depth_Error", color="MagType")
    fig.write_html(os.path.join(html_dir, "year_vs_depth_error_scatter.html"))
    
    fig = px.scatter(df, x="Year", y="Magnitude_Error", color="MagType")
    fig.write_html(os.path.join(html_dir, "year_vs_magnitude_error_scatter.html"))

def main():
    file_path = r"/Users/bara/Desktop/Kaggle /archive (2)/earthquakes1970-2014.csv"
    dp = load_data(file_path)
    dp = preprocess_data(dp)
    display_data_info(dp)
    visualize_data(dp)

if __name__ == "__main__":
    main()
