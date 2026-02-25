appimport streamlit as st

# Configuración de página de lujo
st.set_page_config(page_title="ALTAMIRA NOVIAS - Consulta Privada", page_icon="👰")

# Estilo visual refinado
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a1a1a; text-align: center; font-family: 'Serif'; letter-spacing: 3px; text-transform: uppercase; }
    .stButton>button { background-color: #1a1a1a; color: white; border-radius: 0px; width: 100%; height: 50px; font-weight: bold; border: none; }
    .servicio-header { color: #1a1a1a; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-top: 30px; font-family: 'Serif'; }
    .desc-text { color: #555; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo (puedes subir el archivo logo.jpg a tu GitHub)
st.title("ALTAMIRA NOVIAS")
st.markdown("<p style='text-align: center; color: #888; letter-spacing: 1px;'>CONSULTA PRIVADA · LAS CONDES</p>", unsafe_allow_html=True)

st.write("---")

# Función para crear botones de WhatsApp
def boton_whatsapp(texto_boton, mensaje_personalizado):
    numero = "56986224404"
    url = f"https://wa.me/{numero}?text={mensaje_personalizado.replace(' ', '%20')}"
    st.markdown(f'<a href="{url}" target="_blank"><button style="width:100%; background-color:#1a1a1a; color:white; padding:12px; cursor:pointer; border:none; margin-bottom:20px;">{texto_boton}</button></a>', unsafe_allow_html=True)

# SECCIÓN 1: VESTIDOS (NOVIAS E INVITADAS)
st.markdown("<h3 class='servicio-header'>DISEÑO DE VESTUARIO</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write("**Novias con Aguante**")
    st.write("Piezas únicas de alta costura diseñadas para reflejar tu pasión y personalidad.")
    boton_whatsapp("COTIZAR VESTIDO DE NOVIA", "Hola MYSTIK, me gustaría solicitar una cita para el diseño de mi vestido de novia.")

with col2:
    st.write("**Vestidos de Invitada**")
    st.write("Elegancia y distinción para acompañar en eventos inolvidables con calce perfecto.")
    boton_whatsapp("COTIZAR VESTIDO INVITADA", "Hola MYSTIK, quiero información sobre vestidos a medida para invitadas.")

# SECCIÓN 2: COMPLEMENTOS (RAMOS Y TOCADOS)
st.markdown("<h3 class='servicio-header'>COMPLEMENTOS EXCLUSIVOS</h3>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    st.write("**Ramos Eternos**")
    st.write("Creaciones artesanales en alambrismo. Un tesoro que perdura para siempre (Solo a pedido).")
    boton_whatsapp("PEDIR RAMO ETERNO", "Hola MYSTIK, quiero consultar por el servicio de ramos eternos en alambrismo.")

with col4:
    st.write("**Tocados de Novia**")
    st.write("Detalles finos y personalizados que armonizan con tu peinado y estilo.")
    boton_whatsapp("CONSULTAR POR TOCADOS", "Hola MYSTIK, me encantaría ver opciones de tocados personalizados.")

# SECCIÓN 3: BORDADOS PERSONALIZADOS
st.markdown("<h3 class='servicio-header'>DETALLES DE AUTOR</h3>", unsafe_allow_html=True)
st.write("**Bordados para Novia**")
st.write("Personalizamos tu prenda con bordados significativos, iniciales o diseños exclusivos que cuentan tu historia.")
boton_whatsapp("SOLICITAR SERVICIO DE BORDADO", "Hola MYSTIK, me interesa el servicio de bordado personalizado para mi vestuario.")

st.write("---")

# Cierre y Ubicación
st.markdown("""
    <div style='text-align: center;'>
        <p class='desc-text'>Agende su visita para una atención personalizada en nuestra consulta en Las Condes.</p>
        <p style='font-weight: bold;'>SANTIAGO, CHILE</p>
    </div>
    """, unsafe_allow_html=True)
