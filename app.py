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

elif modulos == "Ejercicio 2: Arreglos con Numpy":
    
    st.write("Bienvenido al módulo Arreglos con Numpy")
    st.markdown("Registra productos para calcular su total acumulado usando arreglos de NumPy.")

    # 1. Inicializar los arreglos en session_state si no existen
    if "nombres" not in st.session_state:
        st.session_state.nombres = np.array([], dtype=str)
        st.session_state.categorias = np.array([], dtype=str)
        st.session_state.precios = np.array([], dtype=float)
        st.session_state.cantidades = np.array([], dtype=int)
        st.session_state.totales = np.array([], dtype=float)

    # 2. Formulario de ingreso de datos
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Hogar"])
    precio = st.number_input("Precio ($)", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    # 3. Cálculo automático del total
    total = precio * cantidad

    # 4. Botón para agregar
    if st.button("Agregar producto"):
        # Usamos np.append() para agregar elementos a cada arreglo de NumPy
        st.session_state.nombres = np.append(st.session_state.nombres, nombre)
        st.session_state.categorias = np.append(st.session_state.categorias, categoria)
        st.session_state.precios = np.append(st.session_state.precios, precio)
        st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
        st.session_state.totales = np.append(st.session_state.totales, total)

    # 5. Convertir los arreglos de NumPy en un diccionario y luego en DataFrame
    datos = {
        "Producto": st.session_state.nombres,
        "Categoría": st.session_state.categorias,
        "Precio": st.session_state.precios,
        "Cantidad": st.session_state.cantidades,
        "Total": st.session_state.totales
    }
    
    df_productos = pd.DataFrame(datos)

    # 6. Mostrar la tabla actualizada
    st.dataframe(df_productos)

