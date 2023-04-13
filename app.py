import streamlit as st
import pickle
pickle_in = open("classifier.pkl","rb")
regressor=pickle.load(pickle_in)
st.title("diabetes prediction")

a = float(st.number_input("Pregnencies"))
b = float(st.number_input("Glucose"))
c = float(st.number_input("BloodPressure"))
d = float(st.number_input("skinthickness"))
e = float(st.number_input("insulin"))
f = float(st.number_input("bmi"))
g = float(st.number_input("diabetespedigreefunction"))
h = float(st.number_input("age"))


btn = st.button("predict")

if btn:
    prediction=regressor.predict([[a,b,c,d,e,f,g,h]])
    st.subheader("Predicted diabetes:")
    st.text(prediction[0])

st.markdown(
    """
    ***
    This app was created by Cheekati Karthik.
    
    If you have any queries or feedback, please contact me at [ch.karthik5480@gmail.com](mailto:ch.karthik5480@gmail.com).
    """
)