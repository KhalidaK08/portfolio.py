import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Data Analyst Portfolio | Khalida Khatun",
    page_icon="📊",
    layout="wide"
)

# --- CUSTOM CSS FOR PORTFOLIO STYLING ---
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #A0AEC0;
        margin-bottom: 25px;
    }
    .card {
        background-color: #1A202C;
        border: 1px solid #2D3748;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .badge {
        background-color: #2B6CB0;
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        margin-right: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["About & Skills", "Projects Showcase", "Certifications", "Insights & Blogs", "Let's Connect"])

# --- SECTION 1: ABOUT & SKILLS ---
if menu == "About & Skills":
    st.markdown('<div class="main-title">Khalida Khatun</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Data Analyst | SQL, Python, Power BI, Advanced Excel</div>', unsafe_allow_html=True)
    
    st.write("""
    Passionate Data Analyst with experience turning raw transactional, operational, and customer data into actionable business insights. 
    Skilled in writing optimized SQL queries, constructing interactive Power BI dashboards, performing EDA in Python, and modeling in Excel.
    """)
    
    st.markdown("### Technical Core")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**SQL & Databases**")
        st.caption("CTEs, Window Functions, Joins, Query Optimization")
    with col2:
        st.markdown("**Python**")
        st.caption("Pandas, NumPy, Plotly, Streamlit, Matplotlib")
    with col3:
        st.markdown("**Business Intelligence**")
        st.caption("Power BI, DAX Modeling, Data Visualization")
    with col4:
        st.markdown("**Spreadsheets & Tools**")
        st.caption("Advanced Excel, Jira, GitHub, Automation Workflows")

# --- SECTION 2: PROJECTS SHOWCASE ---
elif menu == "Projects Showcase":
    st.title("📂 Featured Projects")
    
    # Project 1: PhonePe Case Study
    st.subheader("1. PhonePe Digital Payments Case Study")
    st.markdown("""
    <span class="badge">Python</span><span class="badge">Streamlit</span><span class="badge">Plotly</span><span class="badge">EDA</span>
    """, unsafe_allow_html=True)
    
    st.write("Interactive dashboard examining transaction volume trends, regional adoption metrics, and payment dynamics across Indian states.")
    
    # Embedded PhonePe Visual
    data = {
        "State": ["Maharashtra", "Karnataka", "Telangana", "Tamil Nadu", "Delhi"],
        "Transactions_Cr": [120, 95, 80, 75, 60],
        "Users_Lakhs": [450, 380, 310, 290, 220]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x="State", y="Transactions_Cr", color="State", title="Transaction Volume by Top States (in Cr)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Project 2: PayPal Risk & Merchant Performance Analysis
    st.subheader("2. PayPal Risk & Merchant Performance Analysis")
    st.markdown("""
    <span class="badge">Power BI</span><span class="badge">DAX</span><span class="badge">SQL</span><span class="badge">Fintech</span>
    """, unsafe_allow_html=True)
    st.write("Designed a comprehensive Power BI dashboard analyzing merchant risk tiering, transaction volume distributions, and regional performance trends.")

    st.markdown("---")

    # Project 3: Media Catalog & Content Trend Analysis
    st.subheader("3. Media Catalog Trend Analysis")
    st.markdown("""
    <span class="badge">Power BI</span><span class="badge">Data Modeling</span><span class="badge">Content Analytics</span>
    """, unsafe_allow_html=True)
    st.write("Evaluated movie and TV show distribution trends, release timeline patterns, and genre ratings using dynamic Power BI visual models.")

# --- SECTION 3: CERTIFICATIONS ---
elif menu == "Certifications":
    st.title("📜 Certifications & Credentials")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### Data Analytics Track
        **Coding Ninjas** (2024 - 2025)
        * Advanced SQL, Data Analysis, Python, Power BI.
        """)
    with col2:
        st.markdown("""
        #### Technical Certifications
        * **HackerRank**: SQL (Advanced) Certification
        * **LinkedIn Learning**: Data Analysis & Business Intelligence
        """)

# --- SECTION 4: INSIGHTS & BLOGS ---
elif menu == "Insights & Blogs":
    st.title("✍️ Technical Insights & Learning")
    
    st.markdown("### Featured Articles")
    st.markdown("""
    * **SQL & Data**: *Understanding Window Functions (LAG, LEAD, RANK) for Event Sequencing*
    * **Data Visualization**: *Power BI DAX Best Practices: CALCULATE and USERELATIONSHIP*
    * **Python Automation**: *Automating Data Cleaning Workflows using Pandas*
    * **Spreadsheet Modeling**: *Correlation Analysis of Economic Indicators in Excel*
    """)

# --- SECTION 5: LET'S CONNECT ---
elif menu == "Let's Connect":
    st.title("📬 Let's Connect")
    st.write("I am open to opportunities where I can contribute, learn, and grow as a Data Analyst.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * 💼 **LinkedIn**: [linkedin.com/in/your-profile](https://linkedin.com)
        * 🐙 **GitHub**: [github.com/KhalidaK08](https://github.com/KhalidaK08)
        * 📧 **Email**: Khalida08786@gmail.com
        """)
    with col2:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you for reaching out!")
