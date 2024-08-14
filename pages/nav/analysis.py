import streamlit as st
from PIL import Image

def show_analysis():
    st.title("Análise de Dados")

    # Exibir imagem estática de ocorrências de crimes ao longo do tempo
    st.write("### Gráfico Estático de Ocorrências de Crimes ao Longo do Tempo 📅")
    try:
        image_tempo = Image.open('static/imgs/crimes_ao_logo_do_tempo.png')
        st.image(image_tempo, caption='Ocorrências de Crimes ao Longo do Tempo (Imagem Estática)')
    except FileNotFoundError:
        st.error("A imagem estática 'crimes_ao_logo_do_tempo.png' não foi encontrada na pasta 'static'.")

    # Exibir imagem estática de crimes por delegacia
    st.write("### Gráfico Estático de Total de Crimes por Delegacia 🏢")
    try:
        image_delegacia = Image.open('static/imgs/crimes_por_deleg.png')
        st.image(image_delegacia, caption='Total de Crimes por Delegacia (Imagem Estática)')
    except FileNotFoundError:
        st.error("A imagem estática 'crimes_por_deleg.png' não foi encontrada na pasta 'static/img'.")

    # Exibir imagem estática de evolução dos crimes ao longo dos anos
    st.write("### Gráfico Estático de Evolução dos Crimes ao Longo dos Anos 📈")
    try:
        image_anos = Image.open('static/imgs/crimes_ao_logo_dos_anos.png')
        st.image(image_anos, caption='Evolução dos Crimes ao Longo dos Anos (Imagem Estática)')
    except FileNotFoundError:
        st.error("A imagem estática 'crimes_ao_logo_dos_anos.png' não foi encontrada na pasta 'static'.")

    # Exibir imagem estática de crimes por região
    st.write("### Gráfico Estático de Crimes por Região 🌍")
    try:
        image_regiao = Image.open('static/imgs/crimes_por_regiao.png')
        st.image(image_regiao, caption='Total de Crimes por Região (Imagem Estática)')
    except FileNotFoundError:
        st.error("A imagem estática 'crimes_por_regiao.png' não foi encontrada na pasta 'static'.")

    # Adicionar resumo dos gráficos
    st.write("## Resumo dos Gráficos 📊")

    st.write("### Ocorrências de Crimes ao Longo do Tempo 📅")
    st.write("""
        Este gráfico ilustra a evolução das ocorrências de crimes ao longo do tempo. Ele mostra como o número total de crimes varia por período, revelando possíveis padrões sazonais ou tendências. 📉
    """)

    st.write("### Total de Crimes por Delegacia 🏢")
    st.write("""
        O gráfico demonstra a distribuição total de crimes entre diferentes delegacias. Ele ajuda a identificar quais delegacias estão registrando o maior número de crimes, o que é essencial para a alocação de recursos e estratégias de policiamento. 🏘️
    """)

    st.write("### Evolução dos Crimes ao Longo dos Anos 📈")
    st.write("""
        Este gráfico mostra a evolução dos diferentes tipos de crimes ao longo dos anos. Ele permite observar tendências e mudanças na frequência de diversos tipos de crimes, o que pode ser útil para a formulação de políticas públicas e estratégias de prevenção. 📅
    """)

    st.write("### Crimes por Região 🌍")
    st.write("""
        O gráfico mostra a distribuição de crimes entre diferentes regiões. Isso ajuda a entender a concentração de crimes em áreas específicas e pode auxiliar na criação de estratégias mais eficazes para a segurança pública. 🌐
    """)

    # Conclusão
    st.write("## Conclusão e Aprendizado 🔍")

    st.write("""
        A análise dos gráficos fornecidos oferece uma visão detalhada sobre os padrões e tendências dos crimes. A partir dos gráficos, é possível observar como as ocorrências de crimes variam ao longo do tempo e entre diferentes regiões, o que pode informar melhor as políticas de segurança e a alocação de recursos.

        - **Ocorrências de Crimes ao Longo do Tempo**: Permite identificar padrões temporais e ajudar a planejar estratégias de prevenção durante períodos críticos.
        - **Total de Crimes por Delegacia**: Mostra onde há maior concentração de crimes, ajudando a alocar recursos e esforços de policiamento de forma mais eficaz.
        - **Evolução dos Crimes ao Longo dos Anos**: Oferece insights sobre a mudança nos tipos de crimes, o que pode ajudar a adaptar estratégias de segurança e políticas públicas.
        - **Crimes por Região**: Revela quais áreas estão mais afetadas, possibilitando a criação de estratégias específicas para cada região.

        Em resumo, esses gráficos são ferramentas valiosas para entender a dinâmica dos crimes e auxiliar na formulação de estratégias para melhorar a segurança pública. 🛡️
    """)

# Chamar a função para exibir a análise
show_analysis()
