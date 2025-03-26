
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Calcular métricas principais
total_gasto = df["valor usado (BRL)"].sum()
total_compras = df["compras"].sum()
roas_medio = (df["valor_conversao"].sum() / total_gasto) if total_gasto > 0 else 0
valor_vendas = df["valor_conversao"].sum()
custo_por_compra = (total_gasto / total_compras) if total_compras > 0 else 0

# Layout principal
st.markdown("<div style='text-align: center;'><img src='https://raw.githubusercontent.com/guieenrico/dashboard-clientes/main/logo-clara.png' width='150'></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - Ricci Burguer")

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f"R$ {total_gasto:,.2f}")
col2.metric("Total de Compras", f"{total_compras}")
col3.metric("ROAS Médio", f"{roas_medio:.2f}")

col4, col5 = st.columns(2)
col4.metric("Valor de Vendas", f"R$ {valor_vendas:,.2f}")
col5.metric("Custo por Compra Médio", f"R$ {custo_por_compra:,.2f}")

# Gráficos
st.markdown("### 📊 Gasto por Campanha")
fig_gasto = px.bar(df, x="campanha", y="valor usado (BRL)", title="", labels={"valor usado (BRL)": "Gasto (R$)"})
st.plotly_chart(fig_gasto, use_container_width=True)

st.markdown("### 📈 Compras por Campanha")
fig_compras = px.bar(df, x="campanha", y="compras", title="", labels={"compras": "Compras"})
st.plotly_chart(fig_compras, use_container_width=True)

# Tabela detalhada
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
