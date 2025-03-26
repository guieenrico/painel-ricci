
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Calcular métricas principais
total_gasto = df["Valor usado (BRL)"].sum()
total_compras = df["Compras"].sum()
roas_medio = df["Retorno sobre o investimento em publicidade (ROAS) das compras"].mean()
valor_vendas = df["Valor de conversão da compra"].sum()
custo_por_compra = df["Custo por compra (BRL)"].mean()

# Layout
st.image("logo-clara.png", width=150)
st.markdown("## Enrico Tráfego Profissional")
st.markdown("### Painel de Resultados - Ricci Burguer")

col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f"R$ {total_gasto:,.2f}")
col2.metric("Total de Compras", f"{total_compras}")
col3.metric("ROAS Médio", f"{roas_medio:.2f}")

col4, col5 = st.columns(2)
col4.metric("Valor de Vendas", f"R$ {valor_vendas:,.2f}")
col5.metric("Custo por Compra Médio", f"R$ {custo_por_compra:,.2f}")

# Gráficos
fig_gasto = px.bar(df, x="Nome da campanha", y="Valor usado (BRL)", title="Gasto por Campanha")
fig_compras = px.bar(df, x="Nome da campanha", y="Compras", title="Compras por Campanha")
st.plotly_chart(fig_gasto, use_container_width=True)
st.plotly_chart(fig_compras, use_container_width=True)

# Tabela
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
