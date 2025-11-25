import streamlit as st
import joblib
import pandas as pd
model=joblib.load("spam_clf.pkl")

st.set_page_config(layout="centered")

st.sidebar.image("spampic.jpg")
st.sidebar.title("ℹ️About US")
st.sidebar.text("Hello Tell me About your detection")

st.sidebar.title("📞Contact US")
st.sidebar.text("826598435756")
st.sidebar.text("Email"
"-uddrastogi6@gmail.com")

import streamlit as st

st.markdown("""
    <style>
        .main {
            max-width: 100% !important;
            padding: 0;
        }
        .block-container {
            padding: 0;
            margin: 0;
            
        }
            🚫spam Classifier Project
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <div style="background: linear-gradient(90deg, #4b6cb7, #182848);
                padding:25px;border-radius:12px;">
        <h1 style="color:white;text-align:center;font-size:40px;">
            Spam Classifier Project
        </h1>
    </div>
""", unsafe_allow_html=True)



st.text("")
col1,col2=st.columns([2.2,2],gap="large")
with col1:
    
    st.markdown("""
    <div style="
        background:linear-gradient(90deg,#ff8a00,#e52e71);
        padding:15px;
        border-radius:10px;
        text-align:center;
        color:white;
        font-size:30px;
        font-weight:500;
        box-shadow:0 4px 10px rgba(0,0,0,0.2);">
        Single Msg Prediction
    </div>
""", unsafe_allow_html=True)

    st.text("")
    text=st.text_input("Enter MSG")
    if st.button("Predict"):
      result=model.predict([text])
      if result=="spam":
        st.error("Spam->Irrelevent")
      else:
        st.success("Ham->Relevent")

with col2:
   st.markdown("""
    <div style="
        background:linear-gradient(90deg,#ff8a00,#e52e71);
        padding:15px;
        border-radius:10px;
        text-align:center;
        color:white;
        font-size:30px;
        font-weight:500;
        box-shadow:0 4px 10px rgba(0,0,0,0.2);">
        Single Msg Prediction
    </div>
""", unsafe_allow_html=True)
   st.text("")
   file=st.file_uploader("select file containg bulk msgs",type=['txt','csv'],)
   if file!=None:
      df=pd.read_csv(file,header=None,names=["Msg"])
      place=st.empty()
      place.dataframe(df)
      if st.button("Predict",key="b2"):
         df['result']=model.predict(df.Msg)
         place.dataframe(df)
