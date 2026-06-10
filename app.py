import pandas as pd
import plotly.express as px
import streamlit as st


st.header('Panel de control de anuncios de vehículos')

st.write(
    'Esta aplicación permite explorar datos de anuncios de venta de vehículos. '
    'Incluye visualizaciones interactivas para analizar el odómetro y el precio.'
)

car_data = pd.read_csv('vehicles_us.csv')

st.subheader('Vista previa de los datos')
st.dataframe(car_data.head())

build_histogram = st.checkbox('Construir histograma del odómetro')

if build_histogram:
    st.write('Histograma de la columna odometer')

    fig_hist = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del odómetro'
    )

    st.plotly_chart(fig_hist, use_container_width=True)


build_scatter = st.checkbox('Construir gráfico de dispersión precio vs odómetro')

if build_scatter:
    st.write('Gráfico de dispersión entre odómetro y precio')

    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relación entre odómetro y precio'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)