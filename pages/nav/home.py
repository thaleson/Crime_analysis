import streamlit as st
import json
from streamlit_lottie import st_lottie

def show_home():
    # Título principal
    st.title("Análise de Crimes 🚨🔍")

    # Subtítulo
    st.subheader("Olá! Eu sou Thaleson Silva 👋")

    # Colunas que organizam a página
    col1, col2 = st.columns(2)

    # Animações
    with open("anims/pagina_inicial1.json") as source:
        animacao_1 = json.load(source)

    with open("anims/pagina_inicial2.json") as source:
        animacao_2 = json.load(source)

    # Conteúdo a ser exibido na coluna 1
    with col1:
        st_lottie(animacao_1, height=550, width=550)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("""
            <h5 style='text-align: justify; line-height: 1.6;'>
                O Sistema de Recomendação para Ações Policiais visa melhorar a alocação de recursos policiais com base na análise de dados de crimes. Utilizando técnicas de aprendizado de máquina, nosso objetivo é prever a probabilidade de ocorrência de diferentes tipos de crimes em diferentes áreas e sugerir ações específicas para cada local com base nessas previsões.
            </h5>
        """, unsafe_allow_html=True)

    # Conteúdo a ser exibido na coluna 2
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("""
            <h5 style='text-align: justify; line-height: 1.6;'>
                Bem-vindo ao Sistema de Recomendação para Ações Policiais! 🚓📈
                Neste projeto, você pode explorar e analisar os dados de crimes em diferentes regiões, visualizar previsões de ocorrências e receber sugestões de ações para aumentar a segurança pública. Utilizamos técnicas avançadas de aprendizado de máquina para fornecer recomendações baseadas em dados e ajudar na tomada de decisões estratégicas.
            </h5>
        """, unsafe_allow_html=True)
        st_lottie(animacao_2, height=400, width=540)
