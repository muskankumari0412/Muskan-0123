import streamlit as st
import pickle
import pickle

st.title("SVM Implementation")
Age=st.number_input("Enter AGE")
ES=st.number_input("Enter Estimated Salary")
button=st.button("Predict")

if button:
    model=pickle.load(open("svm.pkl","rb"))
    res=model.predict([[Age,ES]])[0]
    st.markdown(f"Predicted SVM Class: {res}")