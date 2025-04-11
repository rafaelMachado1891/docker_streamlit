import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Vendas",layout="wide")

st.title("Dashboar de Vendas")

def gerar_dados():
    dados = {"mes": ['jan', 'fev','mar', 'abr', 'mai','jun','jul','ago', 'set', 'out', 'nov', 'dez'],
     "valor": [5300, 8000, 2000, 1800, 1900, 7000, 10000, 3400, 2500, 1000, 1660, 3000]
     }
    return pd.DataFrame(dados)

df = gerar_dados()

st.subheader("Dados de Vendas")
st.dataframe(df)

st.subheader('Tendencia de Vendas')
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(df["mes"], df['vendas'], markers='0')
ax.set_ylabel('vendas (R$)')
ax.grid(True)
st.pyplot(fig)


st.subheader("Metricas")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vendas", f"R$ {df["vendas"].sum():, 2f}")
with col1:
    st.metric("Média Mensal", f"R$ {df["vendas"].mean():, 2f}")
with col1:
    st.metric("Crescimento", f"{((df['vendas'].iloc[-1] / df['vendas'].iloc[0])-1)*100: 1f}%")