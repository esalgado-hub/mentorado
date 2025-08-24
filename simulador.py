import streamlit as st
from simulador_juros_compostos import simulador_juros_compostos
from app import main

st.set_page_config(
    page_title="Simulador de Juros Compostos",
    page_icon="📈",
    layout="wide"
)

menu = st.sidebar.radio(
    "Escolha uma funcionalidade",
    ("Simulador de Juros Compostos", "Calculadora")
)

if menu == "Simulador de Juros Compostos":
    simulador_juros_compostos()
elif menu == "Calculadora":
    main()
