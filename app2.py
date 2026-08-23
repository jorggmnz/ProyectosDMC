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
    tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

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
