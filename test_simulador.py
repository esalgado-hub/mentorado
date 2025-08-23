import streamlit as st
from simulador_juros_compostos import simulador_juros_compostos

st.set_page_config(
    page_title="Teste - Simulador de Juros Compostos",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Teste do Simulador de Juros Compostos")

simulador_juros_compostos()

