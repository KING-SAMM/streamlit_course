import streamlit as st 
import pandas as pd 

#  Title 
st.title("Streamlit Data Elements")

# Dataframe Section
st.subheader("Dataframe")
df = pd.DataFrame({
    "Name": ["Nkechi", "Florence", "Chuks", "Daniel"],
    "Age": [25, 32, 37, 45],
    "Occupation": ["Engineer", "Doctor", "Artist", "Chef"]
})
st.dataframe(df)

# Data Editor Section (Editable dataframe) 
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)
#  NOTE: Every single cell-edit reruns the entire script

# Static Table Section (No interactability)
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean(), 1))

# JSON and Dict Section
st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "Nkechi",
    "age": 25,
    "skills": ["Python", "Data Science", "Mschine Learnning"]
}
st.json(sample_dict)

# Also show as dictionary
st.write("Dictionary: ", sample_dict)