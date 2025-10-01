import streamlit as st
import os

st.title("🔍 API Key Checker")

st.write("### Kiểm tra Streamlit Secrets:")
try:
    key = st.secrets["ANTHROPIC_API_KEY"]
    st.success(f"✅ Tìm thấy API key trong secrets")
    st.code(f"Key: {key[:20]}...{key[-10:]}")
except Exception as e:
    st.error(f"❌ Không tìm thấy: {e}")

st.write("### Kiểm tra Environment Variable:")
key_env = os.getenv("ANTHROPIC_API_KEY")
if key_env:
    st.success(f"✅ Tìm thấy trong ENV")
    st.code(f"Key: {key_env[:20]}...{key_env[-10:]}")
else:
    st.warning("⚠️ Không tìm thấy trong ENV")
