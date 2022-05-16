import streamlit as st
from utils.predictor import predict

st.title('Depression Detection in Texts')
st.write("")
st.write("You can detect the depression using text... ")
st.write("")
text = st.text_input('Enter your sentence here,', '')
if text:
    with st.spinner('Predicting the emotion...'):
        output, tips = predict(text)
        st.write("The predicted emotion is ", output)
        st.write("")
        st.write("")
        st.write("")
        st.write(tips)
    # st.success('Done!')
