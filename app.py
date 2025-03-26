
import streamlit as st
import pandas as pd

# Carrega os dados
df = pd.read_csv("dados.csv")

# Título
st.image("logo-clara.png", width=200)
st.title("Enrico Tráfego Profissional")
st.header("Painel de Resultados - Ricci Burguer")

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f'R$ {df["Valor usado (BRL)"].sum():,.2f}')
col2.metric("Total de Compras", int(df["Compras"].sum()))
col3.metric("ROAS Médio", round(df["Retorno sobre o investimento em publicidade (ROAS) das compras"].mean(), 2))

col4, col5 = st.columns(2)
col4.metric("Valor de Vendas", f'R$ {df["Valor de conversão da compra"].sum():,.2f}')
col5.metric("Custo por Compra Médio", f'R$ {df["Custo por compra (BRL)"].mean():,.2f}')

# Detalhamento
st.subheader("📋 Campanhas detalhadas")
st.dataframe(df)
