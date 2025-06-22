import streamlit as st
import pandas as pd

st.set_page_config(page_title="ClubOG Salary Formatter", page_icon="💰")

st.title("🧾 ClubOG Staff Salary Formatter")

uploaded_file = st.file_uploader("Upload your salary Excel file (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        output = "# <a:Crown_01_Owner:1343290737533386773> Weekly Staff Reward\n\n"

        for index, row in df.iterrows():
            role = str(row['Role']).upper()
            salary = row['Salary']
            members = row['Members'] if pd.notna(row['Members']) else "--"

            output += f"**<:Trophy:1250545231850635284> ROLE - {role}\n"
            output += f"<a:HS_paisa:1107218122806669413> Sal - {salary}\n"
            output += f"<:Members:1370679388579827783>  Members - {members}\n\n"

        output += "<a:rs_ticket:1368948083404181515> create tickets to claim your rewards\nStay with us .gg/catfish**"
        st.text_area("📋 Generated Message", value=output, height=400)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
