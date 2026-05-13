import streamlit as st
import pickle
st.write("hello,lets found out the type of iris flower")
petal_length=st.number_input("petal_length")
petal_width=st.number_input("petal_width")
sepal_length=st.number_input("sepal_length")
sepal_width=st.number_input("sepal_width")
if st.button("predict"):
    with open("iris_model.pkl","rb")as file:
        loaded_model=pickle.load(file)
    result=loaded_model.predict([[petal_length,petal_width,sepal_length,sepal_width]])
    st.write(result)