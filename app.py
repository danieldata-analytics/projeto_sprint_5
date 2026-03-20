import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de Veículos", page_icon="🚗", layout="wide")

st.header("Dashboard de Anúncios de Veículos")
st.write("Aplicativo web para análise exploratória de dados de anúncios de venda de carros.")

car_data = pd.read_csv("vehicles_us.csv")

st.subheader("Visualização inicial dos dados")
st.dataframe(car_data.head())

build_histogram = st.checkbox("Construir histograma da quilometragem")

if build_histogram:
    st.write("Histograma da coluna odometer")
    fig = px.histogram(car_data, x="odometer", title="Distribuição da Quilometragem")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Construir gráfico de dispersão entre preço e quilometragem")

if build_scatter:
    st.write("Gráfico de dispersão: price vs odometer")
    fig = px.scatter(car_data, x="odometer", y="price", title="Preço vs Quilometragem")
    st.plotly_chart(fig, use_container_width=True)