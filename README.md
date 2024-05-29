### Earthquake Data Analysis

This repository contains Python code for analyzing earthquake data using various data visualization techniques. The code is designed to load earthquake data from a CSV file, preprocess it, and then visualize it using libraries such as Pandas, Matplotlib, Seaborn, and Plotly.

# Data Credit : Kaggle Dataset

#### Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

#### Introduction

Earthquake data analysis is crucial for understanding seismic activity and its patterns over time. This Python script provides a comprehensive analysis of earthquake data, including visualization of earthquake types, magnitudes, locations, and trends over the years.

#### Setup

To run the code, make sure you have Python installed on your system along with the necessary libraries mentioned in the script, including Pandas, NumPy, Matplotlib, Seaborn, and Plotly.

#### Usage

1. **Loading Data**: The script loads earthquake data from a CSV file located at a specified file path.
   
2. **Preprocessing Data**: The loaded data is preprocessed to handle missing values and convert data types as necessary. The preprocessing includes splitting the "DateTime" column into separate date and time columns, extracting the year from the date, and converting the "Magnitude" column to numeric type.

3. **Displaying Data Information**: Information and statistics about the data are displayed, including the first few rows, column names, data types, and descriptive statistics.

4. **Visualizing Data**: Various visualization techniques are applied to the data, including:
   - Pairplot to visualize relationships between different numerical variables.
   - Pie chart to visualize earthquake types.
   - Barplot to show the average magnitude by earthquake type.
   - 3D scatter plot to visualize the relationship between depth, magnitude, and year.
   - Kernel density estimation plot to visualize the distribution of depth and magnitude.
   - Barplot to show locations with the most recorded earthquakes and their average magnitudes.
   - Pie chart to visualize the percentage of earthquakes per location.
![Figure_1](https://github.com/bara080/Earthquake/assets/122848219/c805c9cd-a129-412e-9902-941b16c29e28)

![Figure_2](https://github.com/bara080/Earthquake/assets/122848219/45cba8bf-2246-4482-a474-dd2d528936d7)

![Figure_3](https://github.com/bara080/Earthquake/assets/122848219/d3801e30-cd96-4837-95d5-a2999f017eeb)

![Figure_4](https://github.com/bara080/Earthquake/assets/122848219/8a9bcf70-3f5e-4c46-a052-629c9b82d375)





5. **HTML Output**: The visualizations are saved as HTML files in a directory named "plotly_html" for easy sharing and viewing.

#### Contributing

Contributions to improve the code or add new features are welcome. Feel free to open an issue or submit a pull request.

#### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
