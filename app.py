import streamlit as st

st.set_page_config(page_title="ALTAMIRA NOVIAS", page_icon="👰")

# --- ESTILO ---
st.markdown("""
    <style>
        .main { background-color: #ffffff; }
            h1 { color: #1a1a1a; text-align: center; font-family: 'Serif'; letter-spacing: 2px; }
                .stButton>button { background-color: #1a1a1a; color: white; width: 100%; border-radius: 0px; }
                    </style>
                        """, unsafe_allow_html=True)

                        # --- CABECERA CON LOGO ---
                        try:
                            st.image("logo.png", width=250) # Intenta cargar el logo
                            except:
                                st.title("ALTAMIRA NOVIAS") # Si no hay logo, pone el texto

                                st.markdown("<p style='text-align: center;'>CONSULTA PRIVADA · LAS CONDES</p>", unsafe_allow_html=True)

                                # --- SECCIÓN VESTIDOS ---
                                st.write("---")
                                col1, col2 = st.columns(2)

                                with col1:
                                    st.subheader("Novias")
                                        try: st.image("novia.png", use_container_width=True)
                                            except: st.write("📷 *Espacio para foto de Novia*")
                                                st.link_button("COTIZAR NOVIA", f"https://wa.me/56986224404?text=Hola%20solicito%20cita%20para%20Novia")

                                                with col2:
                                                    st.subheader("Invitadas")
                                                        try: st.image("invitada.png", use_container_width=True)
                                                            except: st.write("📷 *Espacio para foto de Invitada*")
                                                                st.link_button("COTIZAR INVITADA", f"https://wa.me/56986224404?text=Hola%20solicito%20cita%20para%20Invitada")

                                                                # --- SECCIÓN ACCESORIOS ---
                                                                st.write("---")
                                                                st.header("Complementos de Autor")
                                                                col3, col4 = st.columns(2)

                                                                with col3:
                                                                    st.write("**Tocados**")
                                                                        try: st.image("tocado.jpeg", use_container_width=True)
                                                                            except: st.write("📷 *Foto Tocado*")
                                                                                st.link_button("VER TOCADOS", f"https://wa.me/56986224404?text=Me%20interesan%20los%20tocados")

                                                                                with col4:
                                                                                    st.write("**Ramos Eternos**")
                                                                                        try: st.image("ramo.png", use_container_width=True)
                                                                                            except: st.write("📷 *Foto Ramo*")
                                                                                                st.link_button("PEDIR RAMO", f"https://wa.me/56986224404?text=Quiero%20un%20ramo%20en%20alambrismo")

                                                                                                st.write("---")
                                                                                                st.caption("📍 Las Condes, Santiago | +56 9 8622 4404")
