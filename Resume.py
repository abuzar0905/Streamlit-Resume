import streamlit as st


# Profile

st.image("Passport Size.jpg", caption="Abu Zar", width=180)

col1 = st.columns([1, 3])

with col1:
st.title("Abu Zar's Resume")
st.write("📧 **Email:** abuzar0905@gmail.com")
st.write("📱 **Phone:** (+60) 11-26612895")

#Education
st.header("🎓 Education")
st.write("Degree in Information Technology, Universiti Malaysia Kelantan (2023 - 2026)")

#Work
st.header("💼 Work Experience")
st.write("Technician, Suruhanjaya Pilihan Raya (2019)")
st.write("- Managed and maintained every automated systems in the buildings(e.g Elevator, lift, AC, PA systems, lighting).")

#Skills
st.header("🛠️ Skills")
st.write("- Internet Networking")
st.write("- Electrical wiring")
st.write("- IOT systems")
st.write("- Professional Audio")
st.write("- Server OS (Windows & Linux)")

#Project
st.header("📂 Project")
st.write("NinJaVan Smart Tracking Systems")
