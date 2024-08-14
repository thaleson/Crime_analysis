import streamlit as st

def show_about():
    st.title("Sobre o Projeto")
    st.write("""
        ### Etapas do Desenvolvimento 📊
        
        1. **Coleta de Dados** 🗂️: 
           Obtivemos dados sobre crimes a partir de diversas fontes, incluindo registros de ocorrências policiais e dados públicos. As informações coletadas incluem:
           - **Tipo de Crime**: Categorias como latrocínio, roubo de veículo, furto de veículos e tráfico de drogas.
           - **Localização**: Coordenadas geográficas e bairros.
           - **Datas**: Datas e horários das ocorrências para análise temporal.
           - **Outras Variáveis**: Informações adicionais que podem impactar a ocorrência dos crimes, como condições meteorológicas e eventos especiais.

        2. **Pré-processamento** 🔧:
           Limpamos e preparamos os dados para análise. As etapas incluem:
           - **Tratamento de Valores Ausentes**: Imputação de valores ou remoção de registros incompletos.
           - **Transformação de Variáveis**: Conversão de variáveis categóricas em numéricas, normalização de dados e criação de novas features relevantes.
           - **Eliminação de Outliers**: Identificação e tratamento de valores atípicos que podem distorcer a análise.

        3. **Análise Exploratória** 🔍:
           Realizamos uma análise detalhada dos dados para entender padrões e tendências. As atividades incluíram:
           - **Visualização de Dados**: Gráficos de distribuição, histogramas e mapas para identificar padrões espaciais e temporais.
           - **Estatísticas Descritivas**: Cálculo de médias, medianas, variâncias e correlações para entender as relações entre variáveis.
           - **Detecção de Anomalias**: Identificação de anomalias nos dados que poderiam afetar a modelagem.

        4. **Modelagem** 📈:
           Utilizamos vários modelos de machine learning para prever a demanda de crimes. Os principais modelos foram:
           - **Regressão Linear**: Modelo simples que relaciona a variável dependente com uma ou mais variáveis independentes.
           - **Gradient Boosting**: Modelo avançado que combina múltiplos estimadores fracos para criar um modelo mais robusto.
           - **Outros Modelos**: Consideramos também modelos adicionais como Random Forest e Support Vector Machines (SVM) para comparar o desempenho.

        5. **Avaliação do Modelo** 🧪:
           Avaliamos o desempenho dos modelos com várias métricas para garantir a eficácia das previsões. As métricas incluem:
           - **Erro Quadrático Médio (MSE)**: Mede a média dos quadrados dos erros de previsão, indicando a precisão do modelo.
           - **R² (Coeficiente de Determinação)**: Mede a proporção da variabilidade dos dados que é explicada pelo modelo, ajudando a avaliar a qualidade do ajuste.

        6. **Implementação** 💻:
           Desenvolvemos uma aplicação Streamlit para interagir com o modelo e visualizar análises. A aplicação inclui:
           - **Interface do Usuário**: Campos de entrada para fornecer dados e gerar previsões.
           - **Visualização de Resultados**: Exibição de gráficos, tabelas e mapas para interpretar as previsões e os padrões dos dados.
           - **Feedback e Ajustes**: Mecanismos para ajustar os parâmetros do modelo e melhorar a interação com o usuário.

        ### Detalhes Técnicos ⚙️
        - **Modelos Utilizados**:
          - **Regressão Linear**: Simples e interpretável, ideal para entender a relação entre variáveis.
          - **Gradient Boosting**: Mais complexo, capaz de capturar relações não lineares e melhorar a precisão das previsões.
        - **Métricas de Desempenho**:
          - **MSE**: Média dos erros quadráticos, onde valores mais baixos indicam melhor desempenho do modelo.
          - **R²**: Proporção da variância explicada pelo modelo, com valores próximos a 1 indicando uma boa adequação.
        
        ### Resultados e Conclusões 📈🔍
        - **Análise de Desempenho**: Comparação das métricas dos modelos para identificar o melhor desempenho.
        - **Insights**: Identificação de padrões relevantes e recomendações para futuras análises e ajustes no modelo.
        - **Próximos Passos**: Planos para aprimorar o modelo, incluir novas fontes de dados e explorar novas técnicas de análise.
    """)


show_about()