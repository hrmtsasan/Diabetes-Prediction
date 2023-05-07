import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
import base64

from PIL import Image

pickle_in = open('xg_new_model2.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file2(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file2(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-attachment: scroll;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('health4.png')

st.sidebar.header('**WELCOME!**')
st.sidebar.header('*Tough Times Never Last, but Tough People Do!*') 
st.sidebar.header('*Contact us:* 9897531190')
st.sidebar.header('*email: fastdiabetescheck@gmail.com*')

original_title = '<p style="font-family:sans-serif;color:white; font-size: 60px;">DIABETES PREDICTION</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 20px;">Name :</p>', unsafe_allow_html=True)
name = st.text_input("1")
st.markdown('<p style="font-family:sans-serif;color:Black; font-size: 20px;">No. of times pregnant :</p>', unsafe_allow_html=True)
Pregnancies = st.number_input("2",step=1)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Plasma Glucose Concentration :</p>', unsafe_allow_html=True)
glucose = st.number_input("3",step=1)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Blood pressure (mm Hg) :</p>', unsafe_allow_html=True)
bp =  st.number_input("4",step=1)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Triceps skin fold thickness (mm) :</p>', unsafe_allow_html=True)
skin = st.number_input("5",step=1)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Insulin (mu U/ml) :</p>', unsafe_allow_html=True)
insulin = st.number_input("6",step=1)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Body mass index (weight in kg/(height in m)^2) :</p>', unsafe_allow_html=True)
bmi = st.number_input("7",step=0.01)
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Diabetes Pedigree Function :</p>', unsafe_allow_html=True)
dpf = st.number_input("8",format="%.3f")
st.markdown('<p style="font-family:sans-serif; color:Black;font-size: 20px;">Age :</p>', unsafe_allow_html=True)
age = st.number_input("9",step=1)

submit = st.button('Outcome')

if submit:
    prediction = classifier.predict([[Pregnancies, glucose, skin, bmi, age]])
    if prediction == 0:
        st.title('Congratulations!',name,'You are **not diabetic**.Stay healthy.')
    else:
        st.write(name,", we regret to inform you that you appear to be **diabetic**.")
