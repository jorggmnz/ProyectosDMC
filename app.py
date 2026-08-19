import streamlit as st
import numpy as np

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Jorge Muñoz")

st.image("Python_logo.png", width=200)
st.sidebar.image("DMC.png", width=100)

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Módulo Listas", "Módulo Arreglos", "Módulo Funciones"])

if modulos == "Módulo Listas":
  
  st.write("Bienvenido al módulo Listas")
  
  valor_inicial = st.number_input("Ingrese el valor inicial")
  valor_final = st.number_input("Ingrese el valor final")
  
  lista_numeros = list(range(int(valor_inicial), int(valor_final)))
  st.write(lista_numeros)
  
elif modulos == "Módulo Arreglos":
  
  st.write("Bienvenido al módulo de Arreglos")
  
  cantidad_elementos = st.slider("Selecione la cantidad de elementos de su arreglo", 1,100)
  cantidad_arreglo= np.arange(cantidad_elementos)
  st.write(cantidad_arreglo)
else:
  
  st.write("Bienvenido al módulo de Funciones")
