import streamlit as st

# Configuración de página
st.set_page_config(page_title="ALTAMIRA NOVIAS", page_icon="👰")

# Estilo visual
st.markdown("""
<style>
.main { background-color: #ffffff; }
h1 { color: #1a1a1a; text-align: center; font-family: 'Serif'; }
.stButton>button { background-color: #1a1a1a; color: white; border-radius: 0px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# Cabecera
try:
    st.image("logo.png", width=250)
except:
    st.title("ALTAMIRA NOVIAS")

st.markdown("<p style='text-align: center;'>CONSULTA PRIVADA · LAS CONDES</p>", unsafe_allow_html=True)
st.write("---")

# Sección Vestidos
st.header("👗 Diseño de Vestuario")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Novias")
    try:
        st.image("novia.jpg", use_container_width=True)
    except:
        st.info("📷 Espacio para foto de Novia")
    st.link_button("COTIZAR NOVIA", "https://wa.me/56986224404?text=Hola%20solicito%20cita%20para%20Novia")

with col2:
    st.subheader("Invitadas")
    try:
        st.image("invitada.jpg", use_container_width=True)
    except:
        st.info("📷 Espacio para foto de Invitada")
    st.link_button("COTIZAR INVITADA", "https://wa.me/56986224404?text=Hola%20solicito%20cita%20para%20Invitada")

st.write("---")

# Sección Complementos
st.header("✨ Complementos de Autor")
col3, col4 = st.columns(2)

with col3:
    st.write("**Tocados**")
    try:
        st.image("tocado.jpg", use_container_width=True)
    except:
        st.info("📷 Foto Tocado")
    st.link_button("VER TOCADOS", "https://wa.me/56986224404?text=Me%20interesan%20los%20tocados")

with col4:
    st.write("**Ramos Eternos**")
    try:
        st.image("ramo.jpg", use_container_width=True)
    except:
        st.info("📷 Foto Ramo")
    st.link_button("PEDIR RAMO", "https://wa.me/56986224404?text=Quiero%20un%20ramo%20en%20alambrismo")

# Sección Bordados
st.write("---")
st.header("🪡 Bordados con Historia")
try:
    st.image("bordado.jpg", use_container_width=True)
except:
    st.info("📷 Foto Bordado Búho")
st.write("Personaliza tu prenda con diseños únicos que cuentan tu historia.")
st.link_button("SOLICITAR BORDADO", "https://wa.me/56986224404?text=Consulta%20por%20bordado%20personalizado")

st.write("---")
st.caption("📍 Las Condes, Santiago | +56 9 8622 4404")
