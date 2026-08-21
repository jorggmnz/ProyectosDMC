import streamlit as st
import numpy as np

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
# Descripción breve
st.markdown("### Ejercicio 1: Flujo de Caja")
st.markdown("Registra tus ingresos y gastos para calcular el saldo final.")

# Inicializar la lista guardada
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Inputs sencillos
concepto = st.text_input("Concepto")
tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
valor = st.number_input("Valor", min_value=0.0)

# Botón para agregar a la lista
  if st.button("Agregar"):
    st.session_state.movimientos.append({
        "Concepto": concepto,
        "Tipo": tipo,
        "Valor": valor
    })

# Tabla de movimientos
st.dataframe(pd.DataFrame(st.session_state.movimientos))

# Cálculos directos
total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
saldo = total_ingresos - total_gastos

# Resultados requeridos
st.metric("Total Ingresos", total_ingresos)
st.metric("Total Gastos", total_gastos)
st.metric("Saldo Final", saldo)

# Estado del flujo de caja
  if saldo >= 0:
    st.success("El flujo de caja está A FAVOR")
  else:
    st.error("El flujo de caja está EN CONTRA")
  
elif modulos == "Ejercicio 2: Arreglos":
  
  st.write("Bienvenido al módulo de Arreglos")
  
  cantidad_elementos = st.slider("Selecione la cantidad de elementos de su arreglo", 1,100)
  cantidad_arreglo= np.arange(cantidad_elementos)
  st.write(cantidad_arreglo)
else:
  
  st.write("Bienvenido al módulo de Ejercicio 3: Funciones")
