import streamlit as st
import pandas as pd
import os

from agent import analysis_data
st.title('Аналитика данных')

file = st.file_uploader('Выберите .csv или .xlsx файл с данными', type=['csv', 'xlsx'])
api_key = st.text_input('Введите GROQ API ключ:')
prompt = st.text_area('На что модель должна обратить внимание?')


if file:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader('Предпросмотр загруженных данных:')
    st.dataframe(df)

    if st.button('Анализировать данные'):
        with st.spinner('Модель анализирует данные...'):
            result = analysis_data(df, prompt, api_key)
            
        st.subheader('Результат анализа:')
        st.write(result)

        if os.path.exists("charts"):
            chart_files = os.listdir("charts")
            for chart in chart_files:
                st.image(f"charts/{chart}", caption=chart)