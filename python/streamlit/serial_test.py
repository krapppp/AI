import streamlit as st

def unserializable_data():
    return lambda x: x


st.session_state.unserializable = unserializable_data()
