import streamlit as st

@st.cache_data
def load_data(value):

    import google.generativeai as genai
    API_KEY = 'AIzaSyBVCi6C7WYXB39p-6xUaZDnjlULaE6LS6E'
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    r1 = chat.send_message(value)
    return r1.text

st.header("Рекомендации AI для набора массы")

height = st.number_input("Рост (см)", value=170)
weight = st.number_input("Вес (кг)", value=60)
gender = st.selectbox("Пол", ['Мужчина', 'Женщина'])

btn = st.button("Отправить")
if btn:
    query = f"Как можно похудеть или набрать массуы при весе {weight} кг и при росте {height} см {gender}"

    r = load_data(query)
    if r:
        st.write(r)
