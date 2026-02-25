import streamlit as st

# Configuración Boutique de Lujo
st.set_page_config(page_title="ALTAMIRA NOVIAS - Consulta Privada", page_icon="👰")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #1a1a1a; text-align: center; font-family: 'Serif'; letter-spacing: 2px; }
    .stButton>button { background-color: #1a1a1a; color: white; border-radius: 0px; width: 100%; font-weight: bold; }
    .card { border: 1px solid #f0f0f0; padding: 15px; border-radius: 2px; background-color: #fafafa; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("ALTAMIRA NOVIAS")
st.markdown("<p style='text-align: center; color: #888;'>CONSULTA PRIVADA · LAS CONDES</p>", unsafe_allow_html=True)
st.write("---")

# Función para links de WhatsApp
def ws_link(msj):
    return f"https://wa.me/56986224404?text={msj.replace(' ', '%20')}"

# --- SECCIÓN 1: VESTIDOS ---
st.header("👗 Vestuario de Alta Costura")
c1, c2 = st.columns(2)
with c1:
    st.markdown("<div class='card'><h4>Novias con Aguante</h4><p>Diseños únicos y personalizados.</p></div>", unsafe_allow_html=True)
    st.link_button("COTIZAR NOVIA", ws_link("Hola MYSTIK, solicito cita para mi vestido de Novia."))
with c2:
    st.markdown("<div class='card'><h4>Invitadas</h4><p>Elegancia para acompañantes y gala.</p></div>", unsafe_allow_html=True)
    st.link_button("COTIZAR INVITADA", ws_link("Hola MYSTIK, solicito información para vestido de invitada."))

# --- SECCIÓN 2: ARTE Y COMPLEMENTOS ---
st.header("✨ Detalles de Autor")

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("🌸 Ramos Eternos")
    st.write("Arte en alambrismo y perlas (Solo a pedido).")
    st.link_button("PEDIR RAMO", ws_link("Hola MYSTIK, quiero un ramo eterno en alambrismo."))

with col_b:
    st.subheader("👑 Tocados")
    st.write("Piezas únicas para un peinado de ensueño.")
    st.link_button("VER TOCADOS", ws_link("Hola MYSTIK, busco un tocado personalizado."))

# --- SECCIÓN 3: BORDADOS ---
st.write("---")
st.subheader("🪡 Bordados Personalizados")
st.write("Servicio de bordado para novias: iniciales, figuras (como el búho) y diseños con historia.")
st.link_button("SOLICITAR BORDADO", ws_link("Hola MYSTIK, me interesa el servicio de bordado personalizado."))

st.write("---")
st.caption("📍 Santiago, Las Condes | Atencion solo previa cita")
