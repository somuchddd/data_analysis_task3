import streamlit as st
import pandas as pd
import os
from agent import analysis_data
from security import is_prompt_safe

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
        if not is_prompt_safe(prompt):
            st.error('Обнаружен небезопасный промпт')
            st.stop()

        os.makedirs("charts", exist_ok=True)
        chart_files = os.listdir("charts")

        for chart in chart_files:
            file_path = os.path.join("charts", chart)
            if os.path.isfile(file_path):
                os.remove(file_path)

        with st.spinner('Модель анализирует данные...'):
            try:
                result = analysis_data(df, prompt, api_key)
            except Exception as e:
                st.error(f'Возникла ошибка при анализе: {e}')
                st.stop()

        st.subheader('Результат анализа:')
        st.write(result)

        if os.path.exists("charts"):
            chart_files = os.listdir("charts")
            for chart in chart_files:
                st.image(f"charts/{chart}", caption=chart)