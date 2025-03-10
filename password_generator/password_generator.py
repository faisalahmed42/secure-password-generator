import streamlit as st
import random
import string
import pyperclip       

# 🌟 Custom Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f5f5;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔑 Password Generator Function
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # A-Z, a-z

    if use_digits:
        characters += string.digits  # 0-9

    if use_special:
        characters += string.punctuation  # ! @ # $ % ^ & *()

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 🎯 App UI
st.markdown("<h1 style='text-align: center; color: #333;'>🔐 Secure Password Generator</h1>", unsafe_allow_html=True)

st.markdown("### 🔢 Select Password Preferences:")

# 🎚️ Password Length Slider
length = st.slider("🔢 Select Password Length:", min_value=6, max_value=32, value=12)

# ✅ Checkboxes for options
use_digits = st.checkbox("🔢 Include Digits (0-9)")
use_special = st.checkbox("🔣 Include Special Characters (!@#$%^&*)")

# 🚀 Generate Password Button
if st.button("🔑 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    
    # 📋 Copy Password to Clipboard
    pyperclip.copy(password)

    # ✅ Show Password
    st.success("✅ Password Generated Successfully!")
    st.code(password, language="plaintext")  # Highlighted password output
    
    # 🎉 Notify User
    st.toast("🔗 Password copied to clipboard!")

# 🌟 Footer
st.markdown("""
---
**🔨 Built with ❤️ by [Faisal Ahmed](https://github.com/faisalahmed007)**  
""")
