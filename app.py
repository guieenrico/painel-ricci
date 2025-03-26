
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Painel Ricci Burguer",
    page_icon="🍔",
    layout="wide"
)

col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo-clara.png", width=260)
with col_titulo:
    st.markdown("## Enrico Tráfego Profissional")
    st.markdown("### Painel de Resultados - Ricci Burguer")

df = pd.read_csv("dados.csv")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Gasto", f'R$ {df["gasto"].sum():,.2f}')
col2.metric("Total de Compras", int(df["compras"].sum()))
col3.metric("ROAS Médio", f'{df["roas"].mean():.2f}')
col4.metric("💰 Valor de Vendas", f'R$ {df["valor_conversao"].sum():,.2f}')

st.markdown("### 📊 Gráfico por Campanha")
fig = px.bar(df, x="campanha", y="roas", color="campanha", text="roas")
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(yaxis_title="ROAS", xaxis_title="Campanha")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📋 Dados Detalhados")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>Desenvolvido por <b>Enrico Tráfego Profissional</b> • Painel exclusivo Ricci</p>",
    unsafe_allow_html=True
)
