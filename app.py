import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Venta de vehículos') #encabezado

st.write('Anuncios de ventas de coches') 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
data_build = st.checkbox('Visualizar una muestra de los datos')
hist_build = st.checkbox('Construir histograma') # crear un botón para generar un histograma
disp_build = st.checkbox('Construir gráfico de dispersión') #crear un botón para generar un gráfico de dispersión
car_sample = car_data.sample(n = 50)      

if data_build: #al seleccionar la casilla

            st.write('Visualiza una muestra del conjunto de datos de anuncios de coches')

            print(car_sample)

if hist_build: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Construir un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if disp_build: #al hacer clic en el botón
            #escribir mensaje
            st.write('Construir un gráfico de dispersión para el conjunto de datos de los anuncios de ventas de coches')

            #crear un gráfico
            fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
            st.plotly_chart(fig, use_conteiner_width=True) #crear gráfico de dispersión