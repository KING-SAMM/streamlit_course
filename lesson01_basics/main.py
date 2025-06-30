import streamlit as st 

# st.write("Hello World!")

# 1. streamlit supports hot reloading
# make a change and refresh the browser to see change

# st.write("Hello World! 123")

# 2. Select "Always rerun" at the top of the browser to update UI automatically when source code changes

st.write("Hello World! 12321212")

# 3. Magic command: st.write()
# This is called a magic command because it will write anything (or any data structure) 
# on the UI/browser in the correct format (based on its type) than just in plain text

st.write({"name": "KC Samm"})
st.write(10 == 10)
st.write((2, "Hey", False))
st.write(["Dave", "Tony", "Samm"])
st.write({2, 6, 8, 2, 6, 8})
st.write(7+3j)

# Write an expression and it will be automatically evaluated

12 + 30         # 42
4 * 12          # 48
3j * 4          # 12j
(3 + 5j) - (5 + 2j)     # (-2+7j)
(3 + 5j) * 5    # (15+25j)
4 + 7 - 12 * 2  # -13

"Hello World" if True else "bye."   # Hello World
"Hello World" if False else "bye."   # Bye