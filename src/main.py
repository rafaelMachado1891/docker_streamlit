import pandas as pd
import streamlit as st
import matplotlib

st.set_page_config(page_title="Dashboard de Vendas",layout="wide")

st.title("Dashboar de Vendas")

def gerar_dados():
    dados = {"mes": ['jan', 'fev','mar', 'abr', 'mai','jun','jul','ago', 'set', 'out', 'nov', 'dez'],
     "valor": [5300, 8000, 2000, 1800, 1900, 7000, 10000, 3400, 2500, 1000, 1660, 3000]
     }
    return pd.DataFrame(dados)

df = gerar_dados()

print(df)