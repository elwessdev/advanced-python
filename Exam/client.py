import streamlit as st

st.title("Streamlit Example App")
st.write("This is a demo of a stream-like list:")

def stream_list():
    for i in range(1, 11):
        yield i

for item in stream_list():
    st.write(f"Streaming: {item}")