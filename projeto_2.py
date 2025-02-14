import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon=":?:",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')


st.markdown("#### Escolha o período a ser analisado:")

# Supondo que renda seja um DataFrame já carregado
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

data_minima = renda['data_ref'].min()
data_maxima = renda['data_ref'].max()

# Adicione os inputs na barra lateral
with st.sidebar:
    st.markdown("### Filtros de Data")
    min_selecionado = st.date_input(
        label="Data Inicial",
        min_value=data_minima,
        max_value=data_maxima,
        value=data_minima,
        key="data_inicial"
    )

    max_selecionado = st.date_input(
        label="Data Final",
        min_value=data_minima,
        max_value=data_maxima,
        value=data_maxima,
        key="data_final"
    )

st.write(min_selecionado, max_selecionado)

renda = renda[ (renda['data_ref'] >= pd.to_datetime(min_selecionado)) & (renda['data_ref'] <= pd.to_datetime(max_selecionado)) ].copy()

#plots
fig, ax = plt.subplots(8,1,figsize=(15,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)





