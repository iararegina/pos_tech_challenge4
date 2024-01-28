import streamlit as st
import pandas as pd
import datetime
import base64

st.set_page_config(page_title="Previsão Preço do Petróleo")

with st.container():
    #st.subheader("Preço por Barril de Petróleo (US$)")
    st.title("Preço por Barril de Petróleo (US$)")
    st.write("Para a previsão do preço por barril de petróleo foi utilizado Séries Temporais, dentre os modelos o ARIMA foi escolhido por apresentar um melhor desempenho")
    st.write("Para mais insigths [CLIQUE AQUI](https://app.powerbi.com/view?r=eyJrIjoiZTYxZTlmMjYtYzJjNi00NzZkLWJlZGUtMmZhOWMxNzIzZWNiIiwidCI6IjM3YTAxM2ZiLWYxZmEtNDdhOS1iYTJjLTI2MmMwZjIwMGFmYyJ9)")


def carregar_dados():
    dados = pd.read_csv("predict_final.csv")
    return dados

with st.container():
    st.write("---")
    qtde_dias = st.sidebar.selectbox("Quantos dias você quer prever após 2024-16-01?", ["5", "10", "20", "30"])
    dados = carregar_dados()
    qtde_dias = int(qtde_dias)
    dados_exibidos = dados.iloc[:qtde_dias]
    dados = dados.iloc[:qtde_dias]
    
    st.write(f"Resultado dos próximos {qtde_dias} dias:")
    st.table(dados)
    
   # Classificar os dados pela coluna de data em ordem decrescente
    dados_exibidos = dados_exibidos.sort_values(by="Data", ascending=False)

    # Exibição do gráfico de barras com Streamlit
    st.bar_chart(dados_exibidos.set_index("Data")["Previsao"])

def convert_df(df):
   
    return df.to_csv().encode('utf-8')

csv = convert_df(dados_exibidos)


st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<a href="data:file/csv;base64,{base64.b64encode(csv).decode()}" '
        f'download="large_df.csv">'
        f'<button style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;">'
        f'Download Previsões em CSV'
        f'</button></a></div>',
        unsafe_allow_html=True
    )
