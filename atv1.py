import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os
# Importando bibliotecas necessárias para executar o código

#git push

# Importando o arquivo csv com os dados e criando uma listagem dos anos e meses disponíveis.
df = pd.read_csv("listagem_billboard.csv")
years = list(range(2000, 2025))
years = [str(x) for x in years]

#Formatando as colunas.
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
df["Year"] = df["Year"].astype(str)
df["mes-ano"] = df["Month"].astype(str) + "-" + df["Year"].astype(str)


# Titulo do projeto e descrição
st.title('Quais músicas estavam no top 100 billboards naquela época? 👀')
""" Esta aplicação permite consultar o top 100 billboards por data (ano e mês) e exibir os resultados em uma tabela que lista as músicas em ranking, assim como o link que redireciona para a página do Spotify."""

# Caixa de seleção para o ano
year_selec = st.selectbox( 
    'Selecione o ano da sua consulta', 
    years)

# Caixa de seleção para o mês
month_selec = st.selectbox( 
    'Selecione o mês da sua consulta', 
    months)

"""Agora clique no botão 'Consultar' para exibir os resultados."""

if st.button('Consultar'):
    st.write(f'Eis abaixo o que todos estavam ouvindo em {month_selec} de {year_selec}: 🎵🎵')
    periodo_selec=month_selec + "-" + year_selec
    df_periodo = df[df['mes-ano'] == periodo_selec]
    df_periodof = df_periodo[["Year", "Month", "Ranking", "Title", "Artist", "Spotify Link"]]
    st.write(df_periodof)







