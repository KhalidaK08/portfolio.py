import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Khalida Khatun Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- MODERN WEB PORTFOLIO STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        scroll-behavior: smooth;
    }

    /* Main Container Background */
    .stApp {
        background: #090d16;
        color: #e2e8f0;
    }

    /* Hide standard Streamlit header & top padding */
    header {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Floating Navigation Header */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 12px 28px;
        border-radius: 50px;
        position: sticky;
        top: 10px;
        z-index: 999;
        margin-bottom: 35px;
    }
    
    .nav-logo {
        font-weight: 800;
        font-size: 1.25rem;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .nav-links a {
        color: #94a3b8;
        text-decoration: none;
        margin: 0 12px;
        font-weight: 500;
        font-size: 0.92rem;
        transition: color 0.2s ease;
    }

    .nav-links a:hover {
        color: #f8fafc;
    }

    .contact-btn {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        text-decoration: none;
        font-size: 0.9rem;
    }

    /* Hero Section */
    .hero-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: #818cf8;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 16px;
    }

    .hero-title {
        font-size: 3.1rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 16px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 24px;
    }

    /* Button Styling */
    .btn-primary {
        background: #6366f1;
        color: white !important;
        padding: 10px 22px;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        margin-right: 10px;
        display: inline-block;
    }

    .btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 10px 22px;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
    }

    /* Section Headers */
    .section-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        margin-top: 55px;
        margin-bottom: 8px;
    }

    .section-desc {
        text-align: center;
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 35px;
    }

    /* Light Theme Card */
    .light-card {
        background: #f8fafc;
        color: #0f172a;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        height: 100%;
    }

    .light-card h3, .light-card h4 {
        color: #0f172a;
        margin-top: 0;
    }

    /* Dark Theme Cards */
    .dark-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }

    /* Tech Badges */
    .tag {
        display: inline-block;
        background: rgba(99, 102, 241, 0.12);
        color: #6366f1;
        border: 1px solid rgba(99, 102, 241, 0.25);
        padding: 4px 11px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .tag-purple {
        background: rgba(168, 85, 247, 0.12);
        color: #a855f7;
        border: 1px solid rgba(168, 85, 247, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">Khalida Khatun</div>
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Project</a>
        <a href="#certifications">Certifications</a>
        <a href="#contact">Contact</a>
    </div>
    <a href="#contact" class="contact-btn">Contact Me</a>
</div>
""", unsafe_allow_html=True)


# --- HERO SECTION ---
hero_col1, hero_col2 = st.columns([1.0, 0.8])

with hero_col1:
    st.markdown("""
    <div class="hero-badge">Data Analyst | Operations Analyst</div>
    <div class="hero-title">Turning Raw data into insights.</div>
    <div class="hero-subtitle">
        Results-driven Data Analyst with professional experience in SQL, Python, Power BI, and Advanced Excel, 
        specializing in data extraction, validation, reporting, and workflow automation.
    </div>
    <div style="margin-bottom: 22px;">
        <a href="#projects" class="btn-primary">View Projects</a>
        <a href="#contact" class="btn-secondary">Download Resume</a>
    </div>
    <div style="margin-top: 10px;">
        <span class="tag">🟢 Open to Data Analyst Roles</span>
        <a href="https://linkedin.com" target="_blank" style="text-decoration:none;"><span class="tag">💼 LinkedIn</span></a>
        <a href="https://github.com/KhalidaK08" target="_blank" style="text-decoration:none;"><span class="tag">🐙 GitHub</span></a>
        <a href="mailto:Khalida08786@gmail.com" style="text-decoration:none;"><span class="tag">📧 Email</span></a>
    </div>
    """, unsafe_allow_html=True)

with hero_col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(168,85,247,0.2)); border-radius: 20px; padding: 24px; text-align: center; border: 1px solid rgba(255,255,255,0.12);">
        <h3 style="color: #ffffff; margin-bottom: 8px; font-size: 1.35rem;">Operational & Data Impact</h3>
        <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.5;">
            1+ Years Data Analyst Experience + 3 Years Operations Management
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 16px 0;">
        <div style="display: flex; justify-content: space-around;">
            <div>
                <h2 style="color: #818cf8; margin:0; font-size: 1.8rem;">4+ Yrs</h2>
                <span style="color:#94a3b8; font-size: 0.8rem;">Total Experience</span>
            </div>
            <div>
                <h2 style="color: #c084fc; margin:0; font-size: 1.8rem;">100%</h2>
                <span style="color:#94a3b8; font-size: 0.8rem;">Data Focus</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 1: ABOUT ME ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Background, education, and analytical foundation.</div>', unsafe_allow_html=True)

about_col1, about_col2 = st.columns([0.45, 0.55])

with about_col1:
    st.markdown("""
    <div class="light-card">
        <h3 style="margin-bottom:12px;">Tech Stack</h3>
        <p style="font-size: 0.9rem; color: #475569; margin-bottom: 18px;">Primary technical toolset applied across operational analytics projects.</p>
        <div>
            <span class="tag">SQL (MySQL, SQL server BigQuery)</span>
            <span class="tag">Python (Pandas, NumPy, Matplotlib)</span>
            <span class="tag">Power BI & DAX</span>
            <span class="tag">Advanced Excel</span>
            <span class="tag">Looker Studio & Tableau</span>
            <span class="tag">Jira Workflows</span>
            <span class="tag">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with about_col2:
    with st.container():
        st.markdown("""
        <div class="light-card">
            <h3 style="margin-bottom: 15px;">Education & Certification History</h3>
            <div style="border-left: 2px solid #6366f1; padding-left: 14px; margin-bottom: 16px;">
                <h4 style="margin:0; color:#0f172a; font-size: 1.05rem;">Bachelor of Science (B.Sc) - Computer Science</h4>
                <div style="color:#64748b; font-size:0.85rem; font-weight:600;">Nagarjuna Post Graduate College of Science, Raipur (70%)</div>
                <p style="margin-top:4px; font-size:0.88rem; color:#334155;">Specialized in computer applications, database management systems, and relational algorithms.</p>
            </div>
            <div style="border-left: 2px solid #a855f7; padding-left: 14px;">
                <h4 style="margin:0; color:#0f172a; font-size: 1.05rem;">Data Analytics Certification Track</h4>
                <div style="color:#64748b; font-size:0.85rem; font-weight:600;">Coding Ninjas | Jan 2026 - Aug 2026</div>
                <p style="margin-top:4px; font-size:0.88rem; color:#334155;">Solved 1000+ analytical and coding problems covering SQL, Python EDA, and Power BI modeling.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


# --- SECTION 2: TECHNICAL SKILLS ---
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Technical Skills & Tools</div>', unsafe_allow_html=True)

sk1, sk2, sk3 = st.columns(3)

with sk1:
    st.markdown("""
    <div class="light-card">
        <h4>📊 SQL & Databases</h4>
        <p style="color:#64748b; font-size:0.85rem;"> MySQL, SQL Server, BigQuery</p>
        <span class="tag">CTEs & Subqueries</span>
        <span class="tag">Window Functions</span>
        <span class="tag">Table Joins</span>
        <span class="tag">Query Optimization</span>
    </div>
    """, unsafe_allow_html=True)

with sk2:
    st.markdown("""
    <div class="light-card">
        <h4>🐍 Python Automation</h4>
        <p style="color:#64748b; font-size:0.85rem;">Jupyter, EDA & Analytics</p>
        <span class="tag">Pandas</span>
        <span class="tag">NumPy</span>
        <span class="tag">Matplotlib</span>
        <span class="tag">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

with sk3:
    st.markdown("""
    <div class="light-card">
        <h4>📈 BI & Reporting</h4>
        <p style="color:#64748b; font-size:0.85rem;">Dashboards & Data Modeling</p>
        <span class="tag">Power BI & DAX</span>
        <span class="tag">Looker Studio</span>
        <span class="tag">Tableau</span>
        <span class="tag">Advanced Excel</span>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 3: EXPERIENCE ---
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

st.markdown("""
<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <h3 style="color:#ffffff; margin:0;">Operations Analyst</h3>
        <span style="color:#818cf8; font-weight:600;">Loop.Ai | SaaS (Bengaluru) — Dec 2024 - Dec 2025</span>
    </div>
    <ul style="color:#94a3b8; font-size:0.92rem; margin-top:12px; padding-left:18px; line-height:1.6;">
        <li>Developed <b>Power BI KPI dashboards</b> using SQL & Python to monitor <b>50K+ daily transactions</b>, enabling leadership to track SLA adherence and revenue metrics.</li>
        <li>Analyzed <b>1M+ records</b> using SQL (CTEs, joins, window functions) to identify performance gaps and improve product efficiency by 20%.</li>
        <li>Implemented automated data validation workflows, reducing manual audit effort by 40% and improving turnaround time from T-4 to same-day.</li>
    </ul>
    <div><span class="tag">Power BI</span><span class="tag">SQL</span><span class="tag">Python</span><span class="tag">SLA Monitoring</span></div>
</div>

<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <h3 style="color:#ffffff; margin:0;">Team Leader</h3>
        <span style="color:#818cf8; font-weight:600;">CUREFIT (Bengaluru) — Jan 2022 - Mar 2024</span>
    </div>
    <ul style="color:#94a3b8; font-size:0.92rem; margin-top:12px; padding-left:18px; line-height:1.6;">
        <li>Developed Excel and Power BI dashboards across Amazon, Flipkart, and 1P channels to monitor productivity, enabling leadership to reduce SLA breaches by 15% across 5 warehouses.</li>
        <li>Analyzed operational and defect data using <b>Advanced Excel</b>, reducing delivery-related defects by 22%.</li>
        <li>Wrote optimized BigQuery SQL queries to process large-scale operational datasets, reducing reporting time by 50%.</li>
    </ul>
    <div><span class="tag">BigQuery SQL</span><span class="tag">Advanced Excel</span><span class="tag">Power BI</span><span class="tag">Warehouse Analytics</span></div>
</div>

<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <h3 style="color:#ffffff; margin:0;">Team Leader & Executive</h3>
        <span style="color:#818cf8; font-weight:600;">ONEFITPLUS (Raipur) — Apr 2020 - Dec 2021</span>
    </div>
    <ul style="color:#94a3b8; font-size:0.92rem; margin-top:12px; padding-left:18px; line-height:1.6;">
        <li>Built Excel dashboards to monitor response time, resolution rate, and escalation patterns, reducing escalation rate by 15%.</li>
        <li>Analyzed sales data from Amazon and Flipkart to identify high-converting patterns, resulting in a 12% increase in conversion rate.</li>
    </ul>
    <div><span class="tag">E-Commerce Analytics</span><span class="tag">Excel Dashboards</span><span class="tag">Escalation Management</span></div>
</div>
""", unsafe_allow_html=True)


# --- SECTION 4: PROJECTS ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

# Project 1: Payments Geo-Trends & Interactive Chart
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">1. PhonePe Payments Geo-Trends & Adoption Analysis</h3>
    <p style="color:#94a3b8;">Analyzed 100K+ transaction records using Pandas & NumPy to identify regional trends across 10+ states, improving targeting insights by 15% and enhancing decision-making speed by 20%.</p>
    <div>
        <span class="tag">Python</span><span class="tag">Streamlit</span><span class="tag">Plotly</span><span class="tag">Pandas</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Embedded Interactive Visual
df = pd.DataFrame({
    "State": ["Maharashtra", "Karnataka", "Telangana", "Tamil Nadu", "Delhi"],
    "Transactions_Cr": [120, 95, 80, 75, 60]
})
fig = px.bar(df, x="State", y="Transactions_Cr", color="State", template="plotly_dark", title="Regional Transaction Volume (Crores)")
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=340)
st.plotly_chart(fig, use_container_width=True)

# Project 2: PayPal Risk
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">2. Payment Risk & Merchant Performance Analytics</h3>
    <p style="color:#94a3b8;">Analyzed 10,000+ simulated PayPal transactions across users, merchants, and countries to evaluate 15+ business scenarios covering revenue, performance, and risk. Classified 100% of transactions into High Value/Regular using SQL CASE logic.</p>
    <div><span class="tag">SQL CASE Logic</span><span class="tag">Risk Modeling</span><span class="tag">Fintech Analytics</span></div>
</div>
""", unsafe_allow_html=True)

# Project 3: E-Commerce Sales
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">3. E-Commerce Sales & Customer Analysis</h3>
    <p style="color:#94a3b8;">Designed relational database and optimized queries across 100K+ records, reducing query execution time by 25%. Performed customer segmentation, identifying top 20% users contributing 65% revenue.</p>
    <div><span class="tag">Advanced SQL</span><span class="tag">CTEs & Window Functions</span><span class="tag">Customer Segmentation</span></div>
</div>
""", unsafe_allow_html=True)

# Project 4: Movies & TV Shows
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">4. Movies & TV Shows Analysis</h3>
    <p style="color:#94a3b8;">Created interactive Power BI dashboards using DAX to analyze year-over-year (YoY) content by genre, country, release year, ratings, and content type.</p>
    <div><span class="tag">Power BI</span><span class="tag">DAX</span><span class="tag">Catalog Trends</span></div>
</div>
""", unsafe_allow_html=True)

# Project 5: CPI Inflation Analysis
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">5. CPI Inflation Analysis & Trend Modeling</h3>
    <p style="color:#94a3b8;">Developed data-driven analysis on 10+ years of CPI data (food, fuel, core), finding 85% correlation with crude oil prices. Built Excel dashboards using Pivot Tables, VLOOKUP, and conditional formatting.</p>
    <div><span class="tag">Advanced Excel</span><span class="tag">Pivot Tables</span><span class="tag">EDA & Correlation</span></div>
</div>
""", unsafe_allow_html=True)


# --- SECTION 5: CERTIFICATIONS ---
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.markdown("""
    <div class="dark-card">
        <h4 style="color:#ffffff;">Coding Ninjas — Data Analytics</h4>
        <p style="color:#818cf8; font-weight:600;">Jan 2026 - Aug 2026</p>
        <p style="color:#94a3b8; font-size:0.9rem;">1000+ Analytical & Coding Problems Solved covering SQL, Python, and Power BI.</p>
    </div>
    """, unsafe_allow_html=True)

with cert_col2:
    st.markdown("""
    <div class="dark-card">
        <h4 style="color:#ffffff;">HackerRank & LinkedIn Learning</h4>
        <p style="color:#c084fc; font-weight:600;">2024 - 2025</p>
        <p style="color:#94a3b8; font-size:0.9rem;">HackerRank Python & SQL Certifications | LinkedIn Learning Excel Dashboards Track.</p>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 6: CONTACT ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s Connect</div>', unsafe_allow_html=True)

st.markdown("""
<div class="light-card" style="text-align: center;">
    <h3>Get In Touch</h3>
    <p style="color: #475569;">I am open to full-time Data Analyst opportunities and collaborative analytics projects.</p>
    <p style="font-weight: 700; color: #0f172a; font-size: 1.1rem;">Email: Khalida08786@gmail.com</p>
</div>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Your Name")
    with c2:
        st.text_input("Your Email")
    st.text_area("Your Message")
    if st.form_submit_button("Send Message"):
        st.success("Thank you! Your message has been sent.")
