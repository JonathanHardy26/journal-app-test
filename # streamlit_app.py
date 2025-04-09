# streamlit_app.py

import streamlit as st

st.title("AI Journal")

# Prompt the user
journal_entry = st.text_area("🧠 What's on your mind today?", height=200)

# Optional: Show the submitted text
if st.button("Save Entry"):
    if journal_entry.strip():
        st.success("✅ Your journal entry has been saved.")
        # You can add logic here to save the entry to a file or database
    else:
        st.warning("⚠️ Please write something before saving.")