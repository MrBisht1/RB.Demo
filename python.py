import streamlit as st

st.title("My Trip ")
name = st.text_input("Enter Your Name")
fname = st.text_input("Enter Your father Name")
adr= st.text_area("Enter Your Address")
Ph=st.text("Enter valid Phone Number")
classdata=st.selectbox("Select Your Class : ",(6,7,8,9,10,11,12))

button =st.button("Done")
if button :
    st.markdown(f"""
    name = {name}:
    father name = {fname}:
    Address = {adr}:
    Class = {classdata}""")
    
    dataset=pd.read("Myfriend.csv")
    st.dataframe(dataset)
    

