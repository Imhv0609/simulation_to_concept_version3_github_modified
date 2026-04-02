import streamlit as st
import streamlit.components.v1 as components
import os

st.title("Component Test")

component_path = os.path.join(os.path.dirname(__file__), "streamlit_app/components/simulation_wrapper")
_simulation_component = components.declare_component("simulation_wrapper", path=component_path)

url = "https://example.com"
st.write(f"Loading {url}")

ret = _simulation_component(url=url, height=400, key="test_sim")
st.write("Return value:")
st.write(ret)
