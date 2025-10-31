import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

API_URL = "http://localhost:5000"

st.set_page_config(page_title="EnergIA 2.0 Automação Residencial por Cômodos", layout="centered")
st.title("⚡ EnergIA 2.0 - Automação Residencial por Cômodos")

st_autorefresh(interval=2000, key="refresh")

def atualizar_status():
    try:
        r = requests.get(f"{API_URL}/status")
        if r.status_code == 200:
            return r.json()
    except:
        st.error("Não foi possível conectar ao servidor Flask.")
    return None

data = atualizar_status()
if data:
    st.metric("Bateria Restante", f"{data['bateria_restante']:.2f} Wh")
    st.progress(data['bateria_restante'] / data['bateria_total'])

    st.subheader("Controle de Cômodos")
    todos_ligados = True

    for room, info in data["comodos"].items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(room.capitalize())
        with col2:
            # Reflete o estado atual
            ligado = st.checkbox("Ligado", value=info["on"], key=room)
            if ligado != info["on"]:
                # Atualiza o backend e bateria
                requests.post(f"{API_URL}/toggle", json={"room": room, "state": ligado})

            if not ligado:
                todos_ligados = False

    if todos_ligados:
        st.error("⚠️ Alto consumo de energia detectado! Todos os cômodos estão ligados. "
                 "Recomenda-se desligar algum para economizar energia.")

