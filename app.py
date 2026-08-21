import streamlit as st
import numpy as np
import pandas as pd

st.title("Proyecto aplicado N°1")
st.write("Módulo: N°1 de Python Fundamentals")
st.write("Año: 2026")

st.sidebar.title("Parámetros")

st.subheader("Información General del Estudiante")
st.write("**Elaborado por:** Jorge Enrique Muñoz Ccasa")
st.write("**Carrera:** Estadística")
st.write("**Universidad:** Universidad Nacional Mayor de San Marcos")

# Separador visual
st.divider()

st.markdown("""Esta aplicación permite poner en practica todo lo aprendido y desarrollado en las primeras clases
del módulo 1 Python for Analytics """)
st.markdown(""" Las tecnologías empleadas en esto es """)

# Separador visual
st.divider()

st.image("Python_logo.png", width=200)
st.sidebar.image("DMC.png", width=100)

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Ejercicio 1: Listas", "Ejercicio 2: Arreglos con Numpy", "Ejercicio 3: Funciones", "Ejercicio 4: CRUD"])

if modulos == "Ejercicio 1: Listas":
  
  st.write("Bienvenido al módulo Listas")
  st.markdown("Registra tus ingresos y gastos para calcular el saldo final.")

concepto = st.text_input("Concepto")
tipo = st.selectbox("Tipo de movimiento", ["Ingresos", "Gastos"])  
valor = st.number_input("Valor", min_value=0.0)


  

