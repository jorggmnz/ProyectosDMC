import streamlit as st
import numpy as np
import pandas as pd
import librería_funciones_proyecto1 as lf


st.title("Proyecto aplicado N°1")
st.write("Módulo: N°1 de Python Fundamentals")
st.write("Año: 2026")

# Separador visual
st.divider()

st.image("Python_logo.png", width=200)
st.sidebar.image("DMC.png", width=100)

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Home","Ejercicio 1: Listas", "Ejercicio 2: Arreglos con Numpy", "Ejercicio 3: Funciones", "Ejercicio 4: CRUD"])

if modulos == "Home":

  st.sidebar.title("Parámetros")

  st.subheader("Información General del Estudiante")
  st.write("**Elaborado por:** Jorge Enrique Muñoz Ccasa")
  st.write("**Carrera:** Estadística")
  st.write("**Universidad:** Universidad Nacional Mayor de San Marcos")

  st.divider()

  st.markdown("""Esta aplicación permite poner en practica todo lo aprendido y desarrollado en las primeras clases
del módulo 1 Python for Analytics 
                Las tecnologías empleadas en este proyecto son Github, Streamlit y Python""") 

elif modulos == "Ejercicio 1: Listas":

    st.write("Bienvenido al módulo Listas")
    st.markdown("Registra tus ingresos y gastos")

    #1 Inicio
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    #2 Movimientos
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingresos", "Gastos"])
    valor = st.number_input("Valor", min_value=0.0)

    #3 Creacion de boton movimiento
    if st.button("Agregar movimiento"):
        st.session_state.movimientos.append({
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        })

    #4 Tabla
    st.dataframe(pd.DataFrame(st.session_state.movimientos))

    # 5. Calculo de Ingresos y Gastos
    total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingresos")
    total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gastos")
    saldo = total_ingresos - total_gastos

    st.metric("Total Ingresos", f"${total_ingresos:,.2f}")
    st.metric("Total Gastos", f"${total_gastos:,.2f}")
    st.metric("Saldo Final", f"${saldo:,.2f}")

    # 7. Indicador del estado del flujo de caja
    if saldo > 0:
        st.success("El flujo de caja está A FAVOR")
    elif saldo == 0:
        st.success("El flujo de caja no está ni A FAVOR NI EN CONTRA")
    else:
        st.error("El flujo de caja está EN CONTRA")

elif modulos == "Ejercicio 2: Arreglos con Numpy":
    
    st.write("Bienvenido al módulo Arreglos con Numpy")
    st.markdown("Registro productos")

    #Inicio
    if "nombres" not in st.session_state:
        st.session_state.nombres = np.array([], dtype=str)
        st.session_state.categorias = np.array([], dtype=str)
        st.session_state.precios = np.array([], dtype=float)
        st.session_state.cantidades = np.array([], dtype=int)
        st.session_state.totales = np.array([], dtype=float)

    #Formulario
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Ropa", "Alimentos", "Electrodomésticos"])
    precio = st.number_input("Precio ($)", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    total = precio * cantidad

    #Botn
    if st.button("Agregar producto"):
        st.session_state.nombres = np.append(st.session_state.nombres, nombre)
        st.session_state.categorias = np.append(st.session_state.categorias, categoria)
        st.session_state.precios = np.append(st.session_state.precios, precio)
        st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
        st.session_state.totales = np.append(st.session_state.totales, total)

    #Dataframee
    datos = {
        "Producto": st.session_state.nombres,
        "Categoría": st.session_state.categorias,
        "Precio": st.session_state.precios,
        "Cantidad": st.session_state.cantidades,
        "Total": st.session_state.totales
    }
    
    df_productos = pd.DataFrame(datos)

    #Tabla con actualizaciones
    st.dataframe(df_productos)

elif modulos == "Ejercicio 3: Funciones":
    st.write("Bienvenido al módulo Funciones")
    st.markdown("Calcula la rentabilidad esperada de tu inversión.")

    #Inicio
    if "historial_funciones" not in st.session_state:
        st.session_state.historial_funciones = []

    #Datos
    proyecto = st.text_input("Nombre del proyecto", value="Proyecto 1")
    capital_invertido = st.number_input("Capital invertido", min_value=0.0, value=1000.0)
    utilidad_esperada = st.number_input("Utilidad esperada", min_value=0.0, value=150.0)

    #Boton
    if st.button("Calcular Rentabilidad"):
        salida = lf.calcular_rentabilidad_esperada(capital_invertido, utilidad_esperada)
        resultado = salida["rentabilidad_esperada_pct"]

        st.session_state.historial_funciones.append({
            "Proyecto": proyecto,
            "Capital": capital_invertido,
            "Utilidad": utilidad_esperada,
            "Rentabilidad (%)": resultado
        })

    #Tablas
    st.subheader("Histórico de resultados")
    df_resultado = pd.DataFrame(st.session_state.historial_funciones)
    st.dataframe(df_resultado)

elif modulos == "Ejercicio 4: CRUD":
    st.write("Bienvenido al módulo CRUD")
    # 1. Clase reducida al mínimo
    class InventarioProducto:
        def __init__(self, nombre, costo, precio, stock):
            self.nombre = nombre
            self.costo = costo
            self.precio = precio
            self.stock = stock

        def resumen(self):
            return {
                "Producto": self.nombre,
                "Costo": self.costo,
                "Precio": self.precio,
                "Stock": self.stock,
                "Valor Total": self.costo * self.stock,
                "Margen Unitario": self.precio - self.costo
            }

    # 2. Inicializar la lista en session_state
    if "productos_crud" not in st.session_state:
        st.session_state.productos_crud = []

    # 3. Solapas para C, R, U, D
    tab1, tab2, tab3, tab4 = st.tabs(["Create", "Read", "Update", "Delete"])

    # CREAR
    with tab1:
        st.subheader("Agregar Producto")
        nom = st.text_input("Nombre")
        cos = st.number_input("Costo", min_value=0.0, value=10.0)
        pre = st.number_input("Precio", min_value=0.0, value=15.0)
        stk = st.number_input("Stock", min_value=0, value=10)

        if st.button("Guardar"):
            obj = InventarioProducto(nom, cos, pre, stk)
            st.session_state.productos_crud.append(obj)
            st.success(f"Producto '{nom}' agregado")

    # LEER
    with tab2:
        st.subheader("Lista de Productos")
        if st.session_state.productos_crud:
            datos = [p.resumen() for p in st.session_state.productos_crud]
            st.dataframe(pd.DataFrame(datos))
        else:
            st.info("No hay productos")

    # ACTUALIZAR
    with tab3:
        st.subheader("Modificar Stock")
        if st.session_state.productos_crud:
            nombres = [p.nombre for p in st.session_state.productos_crud]
            p_sel = st.selectbox("Selecciona producto a editar", nombres)
            nuevo_stk = st.number_input("Nuevo Stock", min_value=0, value=5)

            if st.button("Actualizar Stock"):
                obj = next(p for p in st.session_state.productos_crud if p.nombre == p_sel)
                obj.stock = nuevo_stk
                st.success("Stock actualizado")
        else:
            st.info("No hay productos")

    # ELIMINAR
    with tab4:
        st.subheader("Eliminar Producto")
        if st.session_state.productos_crud:
            nombres = [p.nombre for p in st.session_state.productos_crud]
            p_del = st.selectbox("Selecciona producto a borrar", nombres)

            if st.button("Eliminar"):
                st.session_state.productos_crud = [
                    p for p in st.session_state.productos_crud if p.nombre != p_del
                ]
                st.success("Producto eliminado")
                st.rerun()
        else:
            st.info("No hay productos")
