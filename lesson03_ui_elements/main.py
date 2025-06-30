import streamlit as st 
import os

# Title
st.title("Streamlit Text Elements")
# Header
st.header("This is a header")
# Subheader
st.subheader("This is a subheader")
st.divider()

# Markdown
st.write("Markdown Text:")
st.markdown("_italics_")
st.markdown("### Large")
st.markdown("## Larger")
st.markdown("# Largest")
st.markdown("- Bullet")
st.markdown("*Emphasis*")
st.markdown("**Bold**")
st.markdown("***Strong emphasis***")
st.divider()

#  Caption
st.caption("Caption: small text")

# Code
code_example = """
def greet(name):
    print('Hello, ', name)
"""
st.code(code_example, language="python")
st.divider()

os.path.join(os.getcwd())

st.image(os.path.join(os.getcwd(), "lesson3_ui_elements", "static", "neon-robot-guardian.jpg"))