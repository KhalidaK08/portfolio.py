import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(
    page_title="PhonePe Case Study Analytics",
    page_icon="📱",
    layout="wide"
)

# Header Section
st.title("📱 PhonePe Case Study & Data Analysis")
st.markdown("""
This interactive portfolio application showcases key findings on transaction growth, 
user adoption metrics, and geographic trends across the PhonePe ecosystem.
""")

# Sidebar Navigation / Filters
st.sidebar.header("Filter & Navigation")
selected_view = st.sidebar.radio(
    "Select View:",
    ["Executive Overview", "Transaction Dynamics", "User Demographics"]
)

# Sample Data (Replace with your cleaned dataset/CSV when ready)
data = {
    "State": ["Maharashtra", "Karnataka", "Telangana", "Tamil Nadu", "Delhi"],
    "Transactions_Cr": [120, 95, 80, 75, 60],
    "Users_Lakhs": [450, 380, 310, 290, 220],
    "Avg_Transaction_Value": [650, 720, 580, 610, 800]
}
df = pd.DataFrame(data)

# Tab/Page Views
if selected_view == "Executive Overview":
    st.subheader("Key Business Metrics")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Transactions (Cr)", value="430 Cr", delta="+12%")
    col2.metric(label="Active Users", value="1,650 Lakhs", delta="+18%")
    col3.metric(label="Avg Transaction Value", value="₹ 672", delta="+5%")

    st.markdown("---")
    st.subheader("Regional Transaction Breakdown")
    fig_bar = px.bar(
        df, 
        x="State", 
        y="Transactions_Cr", 
        color="State",
        title="Top States by Transaction Volume (in Crores)",
        labels={"Transactions_Cr": "Transactions (in Cr)"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

elif selected_view == "Transaction Dynamics":
    st.subheader("Transaction Trends & Distributions")
    
    fig_scatter = px.scatter(
        df, 
        x="Transactions_Cr", 
        y="Avg_Transaction_Value",
        size="Users_Lakhs", 
        color="State",
        hover_name="State",
        title="Avg Transaction Value vs. Total Transactions"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

elif selected_view == "User Demographics":
    st.subheader("User Adoption Metrics")
    
    fig_pie = px.pie(
        df, 
        names="State", 
        values="Users_Lakhs", 
        title="Active User Distribution by State"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Data Table Display
with st.expander("View Raw Case Study Data"):
    st.dataframe(df)
