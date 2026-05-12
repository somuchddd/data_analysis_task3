import streamlit as st
import pandas as pd

from agent import analysis_data
st.title('Аналитика данных')

file = st.file_uploader('Выберите .csv файл с данными', type=['csv'])
api_key = st.text_input('Введите GROQ API ключ:')
prompt = st.text_area('Что должна сделать модель?')


if file:
    df = pd.read_csv(file)

    st.subheader('Предпросмотр загруженных данных:')
    st.dataframe(df)

    if st.button('Анализировать данные'):
        with st.spinner('Модель анализирует данные...'):
            result = analysis_data(df, prompt, api_key)
            
        st.subheader('Результат аналаза:')
        st.write(result)