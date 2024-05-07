import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
clf = pickle.load(open("insu_model.pkl","rb"))

def predict(data):
    clf = pickle.load(open("insu_model.pkl","rb"))
    return clf.predict(data)

# Add background image CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.claimsjournal.com/app/uploads/2022/01/bigstock-fraud.detection-scaled.jpg")  # URL of your background image
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Insurance Fraud Detection Project using Machine Learning")
st.markdown("This Model detects fraud")

st.header("Parameters to Detect Fraud")
col1,col2,col3 = st.columns(3)

with col1:
    st.text("age")
    ag=st.slider("Age", 18.0,80.0,0.5)
    st.text("witnesses")
    wt = st.slider("Number of Witnesses", 1, 10, 2)
    st.text("Claim amount")
    ca = st.slider("Claim Amout", 5000.0, 1000000.0, 0.5)
    st.text("Incident Serverity")
    si = st.slider("Incident Serverity",1,4,2)
    st.text("Number of Vehical Involved")
    si1 = st.slider("Number of Vehical Involved",1,40,2)

    
with col2:
    st.text("Occupation")
    oc = st.selectbox("Occupation",{1:'adm-clerical',2:'armed-forces',3:'craft-repair',4:'exec-managerial',5:'farming-shing',6:'handlers-cleaners',7:'machine-op-inspct',8:'other-ervice',9:'priv-house-serv',10:'prof-specialty',11:'protective-serv',12:'sales',13:'tech-support',14:'transport-moving'})
    st.text("Type of Incident")
    gr1 = st.selectbox("Type of Incident",{1:"vehicle Collision",2:"Parked Car",3:"Single Vehicle Collision",4:"Vehicle Theft"})
    st.text("Collision Type")
    ct=st.selectbox("Collision Type",{1:'collision_type_?',2:'collision_type_Front Collision',3:'collision_type_Rear 	Collision',4:'collision_type_Side Collision'})
with col3:
    st.text("Contact Person")
    cp=st.slider("ContactPerson",1,5,2)
    st.text("Policy Premium")
    pp=st.slider("Policy Premium",1,5,2)
    st.text("Capital Grain")
    cg=st.slider("capital-gains",0.0,1000000.0,0.5)
    st.text("Capital loss")
    cl=st.slider("capital-loss",0.0,1000000.0,0.5)

st.text('')
if st.button("Predict Performance Rate"):
    result = clf.predict(
        np.array([[ag,wt,ca,oc,gr1,ct,si,cp,pp,cg,si1,cl,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]))
    st.text(result[0])
st.markdown("Developed by External Guide Avinash Pawar and WBL Intern Mampi Hemram at NIELIT Daman")
