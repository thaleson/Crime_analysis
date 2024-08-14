import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from streamlit_extras.colored_header import colored_header

# Configuração da página
st.set_page_config(page_title="Análise de Crimes", page_icon=":guardsman:", layout="wide")



# animações
with open("anims/animacao_lottie.json") as source:
    animacao_1 = json.load(source)


 # Aplicar estilos de CSS à página
with open("static/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Menu de navegação
with st.sidebar:



     #exibir animação
    st_lottie(animacao_1, height=200, width=290)

        # marcador azul
    colored_header(
            label="",
            description="",
            color_name="light-blue-70"
            )
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Sobre", "Previsão do Modelo", "Análise de Dados"],
        icons=["house", "info", "clipboard-data", "journals"],
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da opção selecionada por padrão
        orientation="vertical"  # Orientação do menu (vertical ou horizontal)
    )

    st.markdown("""
        <p style="text-align: center;">Meus contatos</p>
        """, unsafe_allow_html=True)

    # Badges
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Redirecionar para a página selecionada
if selected == "Home":
    from pages.nav.home import show_home
    show_home()
elif selected == "Sobre":
    from pages.nav.about import show_about
    show_about()
elif selected == "Previsão do Modelo":
    from pages.nav.predict import show_predict
    show_predict()
elif selected == "Análise de Dados":
    from pages.nav.analysis import show_analysis
    show_analysis()
else:
    st.error("Página não encontrada. Verifique as opções do menu.")
