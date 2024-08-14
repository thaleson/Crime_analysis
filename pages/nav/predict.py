import streamlit as st
import pandas as pd
import numpy as np
import joblib
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

def gerar_coordenadas(num_locais):
    latitude_min, latitude_max = -23.0, -22.0
    longitude_min, longitude_max = -43.5, -43.0
    
    coordenadas = []
    for _ in range(num_locais):
        latitude = np.random.uniform(low=latitude_min, high=latitude_max)
        longitude = np.random.uniform(low=longitude_min, high=longitude_max)
        coordenadas.append((latitude, longitude))
    
    return coordenadas

def gerar_mapa(dados_mapeamento):
    mapa = folium.Map(location=[-22.5, -43.25], zoom_start=10)
    
    for i, row in dados_mapeamento.iterrows():
        location = [row['latitude'], row['longitude']]
        popup = (f"{row['nome_local']}<br>Latrocínio: {row['prob_latrocinio']:.1f}%<br>"
                 f"Roubo de Veículo: {row['prob_roubo_veiculo']:.1f}%<br>"
                 f"Furto de Veículos: {row['prob_furto_veiculos']:.1f}%<br>"
                 f"Tráfico de Drogas: {row['prob_trafico_drogas']:.1f}%")
        
        color = 'green'
        if max(row['prob_latrocinio'], row['prob_roubo_veiculo'], 
               row['prob_furto_veiculos'], row['prob_trafico_drogas']) > 75:
            color = 'red'
        elif max(row['prob_latrocinio'], row['prob_roubo_veiculo'], 
                 row['prob_furto_veiculos'], row['prob_trafico_drogas']) > 50:
            color = 'orange'
        elif max(row['prob_latrocinio'], row['prob_roubo_veiculo'], 
                 row['prob_furto_veiculos'], row['prob_trafico_drogas']) > 25:
            color = 'yellow'

        folium.CircleMarker(location=location, radius=10, color=color, 
                            fill=True, fill_color=color, popup=popup).add_to(mapa)
    
    mapa.save('mapas/mapa_previsoes.html')
    return mapa

def sugerir_acao(probabilidade):
    if probabilidade > 75:
        return "Urgente: Reforçar presença policial e aumentar patrulhamento."
    elif probabilidade > 50:
        return "Moderado: Agendar patrulhas regulares e campanhas de conscientização."
    elif probabilidade > 25:
        return "Baixo: Monitorar a área e realizar patrulhas ocasionalmente."
    else:
        return "Muito Baixo: Continuar com o padrão atual de policiamento."

def show_predict():
    st.title("Previsão do Modelo")
    
    best_model = joblib.load('modelo/best_model.pkl')

    
    st.write("Digite os valores para previsão:")

    latrocinio = st.number_input("Latrocínio", min_value=0, key="latrocinio_input")
    roubo_veiculo = st.number_input("Roubo de Veículo", min_value=0, key="roubo_veiculo_input")
    furto_veiculos = st.number_input("Furto de Veículos", min_value=0, key="furto_veiculos_input")
    trafico_drogas = st.number_input("Tráfico de Drogas", min_value=0, key="trafico_drogas_input")
    
    if st.button('Prever'):
        if latrocinio == 0 and roubo_veiculo == 0 and furto_veiculos == 0 and trafico_drogas == 0:
            st.warning("⚠️ Por favor, insira valores diferentes de zero para a previsão.")
        else:
            # Cria um DataFrame para cada tipo de crime com o respectivo valor inserido
            df_latrocinio = pd.DataFrame({'latrocinio': [latrocinio], 'roubo_veiculo': [0], 'furto_veiculos': [0], 'trafico_drogas': [0]})
            df_roubo_veiculo = pd.DataFrame({'latrocinio': [0], 'roubo_veiculo': [roubo_veiculo], 'furto_veiculos': [0], 'trafico_drogas': [0]})
            df_furto_veiculos = pd.DataFrame({'latrocinio': [0], 'roubo_veiculo': [0], 'furto_veiculos': [furto_veiculos], 'trafico_drogas': [0]})
            df_trafico_drogas = pd.DataFrame({'latrocinio': [0], 'roubo_veiculo': [0], 'furto_veiculos': [0], 'trafico_drogas': [trafico_drogas]})

            # Previsões individuais para cada crime
            previsao_latrocinio = best_model.predict(df_latrocinio)
            previsao_roubo_veiculo = best_model.predict(df_roubo_veiculo)
            previsao_furto_veiculos = best_model.predict(df_furto_veiculos)
            previsao_trafico_drogas = best_model.predict(df_trafico_drogas)
            
            st.write("**Previsões do Modelo:**")
            st.write(f"Latrocínio: {previsao_latrocinio[0]:.2f} casos")
            st.write(f"Roubo de Veículo: {previsao_roubo_veiculo[0]:.2f} casos")
            st.write(f"Furto de Veículos: {previsao_furto_veiculos[0]:.2f} casos")
            st.write(f"Tráfico de Drogas: {previsao_trafico_drogas[0]:.2f} casos")

            st.write("**Mapeamento de Probabilidade de Ocorrências:**")
            
            num_locais = 4
            coordenadas_locais = gerar_coordenadas(num_locais)
            
            locais = {
                'Baixada Fluminense': coordenadas_locais[0],
                'Capital': coordenadas_locais[1],
                'Grande Niterói': coordenadas_locais[2],
                'Interior': coordenadas_locais[3]
            }
            
            nomes_locais = list(locais.keys())
            
            dados_mapeamento = pd.DataFrame({
                'nome_local': nomes_locais,
                'latitude': [coord[0] for coord in coordenadas_locais],
                'longitude': [coord[1] for coord in coordenadas_locais],
                'prob_latrocinio': np.random.uniform(low=0, high=200, size=num_locais),
                'prob_roubo_veiculo': np.random.uniform(low=0, high=300, size=num_locais),
                'prob_furto_veiculos': np.random.uniform(low=0, high=100, size=num_locais),
                'prob_trafico_drogas': np.random.uniform(low=0, high=400, size=num_locais),
            })
            
            mapa = gerar_mapa(dados_mapeamento)
            
            st.components.v1.html(mapa._repr_html_(), height=500)

            st.warning("⚠️ Nota: O modelo de previsão é para fins de estudo e análise.")

            st.write("**Ações Sugeridas:**")
            for i, row in dados_mapeamento.iterrows():
                st.subheader(f"{row['nome_local']}")
                st.write(f"Latrocínio: {row['prob_latrocinio']:.1f}% - {sugerir_acao(row['prob_latrocinio'])}")
                st.write(f"Roubo de Veículo: {row['prob_roubo_veiculo']:.1f}% - {sugerir_acao(row['prob_roubo_veiculo'])}")
                st.write(f"Furto de Veículos: {row['prob_furto_veiculos']:.1f}% - {sugerir_acao(row['prob_furto_veiculos'])}")
                st.write(f"Tráfico de Drogas: {row['prob_trafico_drogas']:.1f}% - {sugerir_acao(row['prob_trafico_drogas'])}")
                st.write("---")
