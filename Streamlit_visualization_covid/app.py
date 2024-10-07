# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Covid-19 EDA and Visualization")

st.markdown('''
A Web App to visualize and analyze the Covid-19 data from India
* **Libraries Used:** Streamlit, Pandas, Plotly
* **Data Source:** Kaggle
''')
# Inserting Image
st.image('Covid-Banner.png', caption="Image by Sachin")
# Reading csv data
data = pd.read_csv('Covid-19.csv')
# Displaying Data and its Shape
st.write("**Covid-19 dataset**", data)
st.write("Shape of data", data.shape)
# Header of sidebar
st.sidebar.header("User Input")
# Creating selectbox for Graphs & Plots
graphs = st.sidebar.selectbox("Graphs & Plots", ("Bar Graph", "Scatter Plot", "HeatMap", "Pie Chart"))
# Sorting the columns
index = sorted(data.columns.unique())
# Setting default value for x, y, and color
default_index_x = index.index('State/UTs')
default_index_y = index.index('Total Cases')
default_index_col = index.index('Death Ratio (%)')

# Creating selectbox for x, y and color label and setting default value
x_label = st.sidebar.selectbox("X label Parameter", index, index=default_index_x)
y_label = st.sidebar.selectbox("Y label Parameter", index, index=default_index_y)
col = st.sidebar.selectbox("Color", index, index=default_index_col)

st.markdown('''
## **Visualization**
''')

# function to plot graphs
def visualize_plotly(graph):
    if graph == "Bar Graph":
        st.write(graph)
        fig = px.bar(data, x=x_label, y=y_label, color=col)

    elif graph == "Scatter Plot":
        st.write(graph)
        fig = px.scatter(data, x=x_label, y=y_label, color=col)

    elif graph == "HeatMap":
        st.write(graph)
        fig = px.density_heatmap(data, x=x_label, y=y_label, nbinsx=20, nbinsy=20)

    else:
        st.write(graph)
        fig = px.pie(data, values=x_label, names=data[y_label])

    return fig

figure = visualize_plotly(graphs)
st.plotly_chart(figure)

st.markdown('''
## **Report**
''')
# Creating buttons to display reports
if st.button("Highest Cases"):
    st.header("Highest Cases in a State/UT")
    highest_cases = data[data['Total Cases'] == max(data['Total Cases'])]
    st.write(highest_cases)

if st.button("Lowest Cases"):
    st.header("Lowest Cases in a State/UT")
    lowest_cases = data[data['Total Cases'] == min(data['Total Cases'])]
    st.write(lowest_cases)

if st.button("Highest Active Cases"):
    st.header("Highest Active Cases in a State/UT")
    high_active_cases = data[data['Active'] == max(data['Active'])]
    st.write(high_active_cases)

if st.button("Lowest Active Cases"):
    st.header("Lowest Active Cases in a State/UT")
    low_active_cases = data[data['Total Cases'] == min(data['Total Cases'])]
    st.write(low_active_cases)

if st.button("Highest Death Ratio (%)"):
    st.header("Highest Death Ratio (%) in a State/UT")
    high_death = data[data['Death Ratio (%)'] == max(data['Death Ratio (%)'])]
    st.write(high_death)

if st.button("Lowest Death Ratio (%)"):
    st.header("Lowest Death Ratio (%) in a State/UT")
    low_death = data[data['Death Ratio (%)'] == min(data['Death Ratio (%)'])]
    st.write(low_death)