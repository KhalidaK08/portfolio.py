import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Khalida Khatun | Data Analyst Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN DARK THEME & GLASSMORPHISM STYLING ---
st.markdown("""
    <style>
    /* Global Page Styling */
    .stApp {
        background-color: #0d1117;
        color: #e6edf3;
    }
    
    /* Custom Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Modern Card Containers */
    .portfolio-card {
        background: rgba(22, 27, 34, 0.7);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .portfolio-card:hover {
        border-color: #58a6ff;
        transform: translateY(-2px);
    }

    /* Headings & Text */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #58a6ff 0%, #bc8cff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #8b949e;
        margin-bottom: 24px;
    }

    /* Tech Badges */
    .badge {
        display: inline-block;
        background-color: #21262d;
        color: #58a6ff;
        border: 1px solid #30363d;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
    }

    .badge-purple {
        color: #bc8cff;
    }

    /* Custom Buttons */
    .action-btn {
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
        color: white !important;
        padding: 8px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 10px;
    }

    /* Divider */
    hr {
        border-color: #30363d;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### 📌 Navigation")
menu = st.sidebar.radio(
    "",
    ["Profile & Skills", "Featured Projects", "Certifications", "Technical Writings", "Get In Touch"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💬 Connect")
st.sidebar.markdown("[💼 LinkedIn](https://linkedin.com)", unsafe_allow_html=True)
st.sidebar.markdown("[🐙 GitHub](https://github.com/KhalidaK08)", unsafe_allow_html=True)
st.sidebar.markdown("📧 Khalida08786@gmail.com")

# --- SECTION 1: PROFILE & SKILLS ---
if menu == "Profile & Skills":
    st.markdown('<div class="hero-title">Khalida Khatun</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Data Analyst & Operations Specialist</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="portfolio-card">
        <h3>👋 About Me</h3>
        <p style="color: #c9d1d9; line-height: 1.6;">
            Results-driven Data Analyst with experience optimizing operations, writing complex SQL analytics queries, 
            and building interactive dashboards. Proven track record in converting raw transactional and customer dataset insights into strategic business decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ Technical Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="portfolio-card">
            <h4>📊 SQL & Databases</h4>
            <span class="badge">Window Functions</span>
            <span class="badge">CTEs</span>
            <span class="badge">Joins & Subqueries</span>
            <span class="badge">Query Optimization</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="portfolio-card">
            <h4>🐍 Python Analytics</h4>
            <span class="badge badge-purple">Pandas</span>
            <span class="badge badge-purple">NumPy</span>
            <span class="badge badge-purple">Plotly</span>
            <span class="badge badge-purple">Streamlit</span>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="portfolio-card">
            <h4>📈 BI & Visualization</h4>
            <span class="badge">Power BI</span>
            <span class="badge">DAX Modeling</span>
            <span class="badge">Advanced Excel</span>
            <span class="badge">Jira Workflows</span>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 2: FEATURED PROJECTS ---
elif menu == "Featured Projects":
    st.markdown('<div class="hero-title">Featured Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Interactive case studies and data visualization applications.</div>', unsafe_allow_html=True)

    # PROJECT 1
    st.markdown("""
    <div class="portfolio-card">
        <h3>1. PhonePe Digital Payments Case Study</h3>
        <p style="color: #8b949e;">End-to-end interactive dashboard analyzing transaction growth, payment velocity, and user adoption metrics across Indian states.</p>
        <div>
            <span class="badge">Python</span>
            <span class="badge">Streamlit</span>
            <span class="badge badge-purple">Plotly</span>
            <span class="badge">Pandas</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Chart embedded inside PhonePe Project section
    data = {
        "State": ["Maharashtra", "Karnataka", "Telangana", "Tamil Nadu", "Delhi"],
        "Transactions_Cr": [120, 95, 80, 75, 60],
        "Users_Lakhs": [450, 380, 310, 290, 220]
    }
    df = pd.DataFrame(data)

    fig = px.bar(
        df, x="State", y="Transactions_Cr", color="State", 
        template="plotly_dark", 
        title="Transaction Volume by Region (Crores)",
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # PROJECT 2
    st.markdown("""
    <div class="portfolio-card">
        <h3>2. PayPal Risk & Merchant Performance Analysis</h3>
        <p style="color: #8b949e;">Interactive Power BI dashboard evaluating merchant transaction tiers, user volume distribution, and regional revenue metrics.</p>
        <div>
            <span class="badge">Power BI</span>
            <span class="badge badge-purple">DAX</span>
            <span class="badge">SQL</span>
            <span class="badge">Fintech Analytics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # PROJECT 3
    st.markdown("""
    <div class="portfolio-card">
        <h3>3. Media Catalog & Content Trend Dashboard</h3>
        <p style="color: #8b949e;">Evaluated streaming content distribution models, genre preferences, and release year trends using dynamic Power BI visual models.</p>
        <div>
            <span class="badge">Power BI</span>
            <span class="badge">Data Modeling</span>
            <span class="badge badge-purple">Excel</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 3: CERTIFICATIONS ---
elif menu == "Certifications":
    st.markdown('<div class="hero-title">Certifications & Training</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="portfolio-card">
            🎓 <h4>Data Analytics Track</h4>
            <p style="color: #58a6ff; font-weight: 600;">Coding Ninjas (2024 - 2025)</p>
            <p style="color: #8b949e;">Comprehensive program covering Advanced SQL, Python for Data Science, Data Visualization, and Power BI modeling.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="portfolio-card">
            🏆 <h4>Technical Certifications</h4>
            <p style="color: #bc8cff; font-weight: 600;">HackerRank & LinkedIn Learning</p>
            <ul style="color: #8b949e; padding-left: 18px;">
                <li>SQL (Advanced) Skill Certification</li>
                <li>Data Analysis & Business Intelligence Track</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION 4: TECHNICAL WRITINGS ---
elif menu == "Technical Writings":
    st.markdown('<div class="hero-title">Insights & Articles</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="portfolio-card">
        <h4>⚡ Mastering SQL Window Functions</h4>
        <p style="color: #8b949e;">Exploring practical use cases for LAG(), LEAD(), RANK(), and ROW_NUMBER() in transactional analytics datasets.</p>
    </div>
    
    <div class="portfolio-card">
        <h4>📊 Optimizing Power BI Data Models using DAX</h4>
        <p style="color: #8b949e;">A guide to managing inactive relationships with USERELATIONSHIP and writing efficient CALCULATE expressions.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION 5: GET IN TOUCH ---
elif menu == "Get In Touch":
    st.markdown('<div class="hero-title">Let\'s Connect</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Open for Data Analyst roles and collaborative projects.</div>', unsafe_allow_html=True)

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
        with col2:
            email = st.text_input("Email")
            
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you! Your message has been sent.")
