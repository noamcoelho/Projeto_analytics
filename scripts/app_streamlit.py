
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title='Análise de Saúde - Medicaldataset', layout='wide')
st.title('Dashboard Interativo - Análise de Saúde')

# Carregar dataset
df = pd.read_csv('dados/Medicaldataset.csv')

# Sidebar para filtros
st.sidebar.header('Filtros')
idade = st.sidebar.slider('Idade', int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())), help='Selecione o intervalo de idade dos pacientes')
pressao = st.sidebar.slider('Pressão Sistólica', int(df['Systolic blood pressure'].min()), int(df['Systolic blood pressure'].max()), (int(df['Systolic blood pressure'].min()), int(df['Systolic blood pressure'].max())), help='Selecione o intervalo de pressão sistólica')
glicose = st.sidebar.slider('Glicose', int(df['Blood sugar'].min()), int(df['Blood sugar'].max()), (int(df['Blood sugar'].min()), int(df['Blood sugar'].max())), help='Selecione o intervalo de glicose')

# Aplicar filtros
df_filt = df[(df['Age'] >= idade[0]) & (df['Age'] <= idade[1]) &
             (df['Systolic blood pressure'] >= pressao[0]) & (df['Systolic blood pressure'] <= pressao[1]) &
             (df['Blood sugar'] >= glicose[0]) & (df['Blood sugar'] <= glicose[1])]

# Métricas rápidas
col1, col2, col3, col4 = st.columns(4)
col1.metric('Total filtrado', df_filt.shape[0])
col2.metric('Idade média', f"{df_filt['Age'].mean():.1f}")
col3.metric('Glicose média', f"{df_filt['Blood sugar'].mean():.1f}")
percent_positivo = 100 * (df_filt['Result'] == 'positive').mean() if not df_filt.empty else 0
col4.metric('% Resultado Positivo', f"{percent_positivo:.1f}%")

st.markdown('---')

# Layout dos gráficos
st.subheader('Visualizações Interativas')
colg1, colg2 = st.columns(2)
with colg1:
    fig = px.scatter(df_filt, x='Age', y='Systolic blood pressure', color='Result',
                     title='Idade vs Pressão Sistólica por Resultado',
                     labels={'Age': 'Idade', 'Systolic blood pressure': 'Pressão Sistólica'},
                     hover_data=['Blood sugar'])
    st.plotly_chart(fig, use_container_width=True)
with colg2:
    fig2 = px.box(df_filt, x='Result', y='Blood sugar', color='Result',
                  title='Distribuição da Glicose por Resultado',
                  labels={'Blood sugar': 'Glicose', 'Result': 'Resultado'})
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('---')

# Treinar modelo apenas uma vez
@st.cache_resource(show_spinner=False)
def treina_modelo(df):
    X = df[['Age', 'Blood sugar', 'Systolic blood pressure']]
    y = (df['Result'] == 'positive').astype(int)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

modelo = treina_modelo(df)

st.header('Predição de Risco para Novo Paciente')
st.markdown('Preencha os dados abaixo para estimar o risco de resultado positivo.')
colf1, colf2, colf3 = st.columns(3)
with colf1:
    id_input = st.number_input('Idade', min_value=0, max_value=120, value=40, help='Idade do paciente')
with colf2:
    pressao_input = st.number_input('Pressão Sistólica', min_value=0, max_value=300, value=120, help='Pressão sistólica do paciente')
with colf3:
    glicose_input = st.number_input('Glicose', min_value=0, max_value=500, value=100, help='Glicose do paciente')

if st.button('Prever Risco'):
    entrada = [[id_input, glicose_input, pressao_input]]
    pred = modelo.predict(entrada)[0]
    prob = modelo.predict_proba(entrada)[0][1]
    st.write(f"Probabilidade de resultado positivo: {prob:.2%}")
    st.success('Risco Elevado!' if pred == 1 else 'Risco Baixo.')

st.markdown('---')
st.info('Projeto desenvolvido para análise exploratória, visualização interativa e predição de risco em saúde. Utilize os filtros para explorar diferentes cenários e utilize a predição para simular novos pacientes.')
