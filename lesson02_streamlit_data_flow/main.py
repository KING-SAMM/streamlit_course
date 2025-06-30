import streamlit as st

# Anytime something must be updated on the screen streamlit reruns your entire script from top to bottom

# print("Run")
# pressed = st.button("Press Me!")
# print(pressed)

#  Output: 
# a. when the page first loads (before button press)
# Run
# False

# b. when the button is pressed
# Run
# True
# (i.e entire script runs again and the state within the button changes to True)

# -------------------------------------

pressed1 = st.button("First Button")
print("First: ", pressed1)

pressed2 = st.button("Second Button")
print("Second: ", pressed2)
#  Output:
# a. Initial load:
# First: False
# Second: False

# b. Click first button:
# First: True
# Second: False

# c. Click second button:
# First: False
# Second: True