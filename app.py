import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Venta de vehículos') #encabezado

st.write('Anuncios de ventas de coches') 
car_data = pd.read_csv('vehicles_us.csv') # leer los datos


hist_odom = st.checkbox('Odómetro') # crear un botón para generar un histograma
disp_odom = st.checkbox('Relación odómetro/precio') #crear un botón para generar un gráfico de dispersión         
disp_cond = st.checkbox('Relación condición/precio') #crear botón para diagrama de dispersión
hist_tipo = st.checkbox('Tipos de coches')

if hist_odom: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Construir un histograma de la distancia recorrida de los vehículos en venta')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if disp_odom: #al hacer clic en el botón
            #escribir mensaje
            st.write('Construir un gráfico de la relación entre la distancia recorrida y el precio de los coches')

            #crear un gráfico
            fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
            st.plotly_chart(fig, use_conteiner_width=True) #crear gráfico de dispersión

if disp_cond: #al hacer clic en el botón
            #escribir mensaje
            st.write('Construir un gráfico de la relación de la condición del vehículo y el precio de venta')
            #crear un gráfico
            fig = px.scatter(car_data, x="condition", y="price") # crear un gráfico de dispersión
            st.plotly_chart(fig, use_conteiner_width=True) #crear gráfico de dispersión

if hist_tipo: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Construir un histograma de los tipos de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="type")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)