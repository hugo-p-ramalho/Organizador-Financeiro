import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import carregar_dados, salvar_dados, criar_tabela

st.set_page_config(page_title="Organizador Financeiro 2.0", page_icon="💰")

st.title("💰 Organizador Financeiro 2.0")
st.write("De CSV para Banco de Dados + Dashboard")

criar_tabela()

# Sidebar para upload
st.sidebar.header("Adicionar dados")
arquivo = st.sidebar.file_uploader("Suba seu CSV", type=["csv"])

if arquivo:
    df = pd.read_csv(arquivo)
    salvar_dados(df)
    st.sidebar.success("Dados salvos!")

# Carrega do banco
df = carregar_dados()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Gasto", f"R$ {df['valor'].sum():.2f}")
    col2.metric("Transações", len(df))
    col3.metric("Ticket Médio", f"R$ {df['valor'].mean():.2f}")

    st.subheader("Gastos por Categoria")
    gastos_cat = df.groupby('categoria')['valor'].sum()
    
    fig, ax = plt.subplots()
    ax.pie(gastos_cat, labels=gastos_cat.index, autopct='%1.1f%%')
    st.pyplot(fig)

    st.subheader("Tabela Completa")
    st.dataframe(df)
else:
    st.info("Banco vazio. Faça upload do `gastos_exemplo.csv` na barra lateral.")