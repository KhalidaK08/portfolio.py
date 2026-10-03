import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Khalida Khatun | Data Analyst Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

    /* Hide standard Streamlit header & padding */
    header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Floating Navigation Header */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 12px 28px;
        border-radius: 50px;
        position: sticky;
        top: 10px;
        z-index: 999;
        margin-bottom: 40px;
    }
    
    .nav-logo {
        font-weight: 800;
        font-size: 1.2rem;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .nav-links a {
        color: #94a3b8;
        text-decoration: none;
        margin: 0 14px;
        font-weight: 500;
        font-size: 0.95rem;
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
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 16px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    /* Button Styling */
    .btn-primary {
        background: #6366f1;
        color: white !important;
        padding: 10px 24px;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        margin-right: 12px;
        display: inline-block;
    }

    .btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 10px 24px;
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
        margin-top: 60px;
        margin-bottom: 10px;
    }

    .section-desc {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 40px;
    }

    /* Light Theme Cards (for About & Skills Sections) */
    .light-card {
        background: #f8fafc;
        color: #0f172a;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }

    .light-card h3, .light-card h4 {
        color: #0f172a;
        margin-top: 0;
    }

    /* Dark Theme Cards (for Experience & Projects Sections) */
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
        background: rgba(99, 102, 241, 0.1);
        color: #6366f1;
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    /* Timeline items */
    .timeline-item {
        border-left: 2px solid #334155;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }

    .timeline-item::before {
        content: '';
        width: 10px;
        height: 10px;
        background: #6366f1;
        border-radius: 50%;
        position: absolute;
        left: -6px;
        top: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">KK.</div>
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
hero_col1, hero_col2 = st.columns([1.2, 0.8])

with hero_col1:
    st.markdown("""
    <div class="hero-badge">Data Analyst | Operations Analyst</div>
    <div class="hero-title">Turning Raw data into insights.</div>
    <div class="hero-subtitle">
        B.Sc Computer Science graduate passionate about data analytics, operations, visualization, and solving real-world business problems with data.
    </div>
    <div style="margin-bottom: 24px;">
        <a href="#projects" class="btn-primary">View Projects</a>
        <a href="#contact" class="btn-secondary">Download Resume</a>
    </div>
    <div>
        <span class="tag">🟢 Open to Data Analyst Roles</span>
        <span class="tag">💼 LinkedIn</span>
        <span class="tag">🐙 GitHub</span>
        <span class="tag">📧 Email</span>
    </div>
    """, unsafe_allow_html=True)

with hero_col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(168,85,247,0.2)); border-radius: 20px; padding: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
        <h3 style="color: #ffffff; margin-bottom: 10px;">Operational & Data Impact</h3>
        <p style="color: #94a3b8; font-size: 0.95rem;">5+ Years in Support Operations, Contact Centre Management, & Analytics Workflows.</p>
        <hr style="border-color: #334155; margin: 15px 0;">
        <div style="display: flex; justify-content: space-around;">
            <div>
                <h2 style="color: #818cf8; margin:0;">5+ Yrs</h2>
                <span style="color:#94a3b8; font-size: 0.8rem;">Experience</span>
            </div>
            <div>
                <h2 style="color: #c084fc; margin:0;">100%</h2>
                <span style="color:#94a3b8; font-size: 0.8rem;">Data Focus</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 1: ABOUT ME ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Background, education, and analytical foundation.</div>', unsafe_allow_html=True)

about_col1, about_col2 = st.columns([0.4, 0.6])

with about_col1:
    st.markdown("""
    <div class="light-card">
        <h3>Core Stack</h3>
        <p style="font-size: 0.9rem; color: #475569;">Primary technical toolset applied across operational analytics projects.</p>
        <div style="margin-top: 15px;">
            <span class="tag">Python & Pandas</span>
            <span class="tag">SQL Databases</span>
            <span class="tag">Power BI & DAX</span>
            <span class="tag">Advanced Excel</span>
            <span class="tag">Jira Workflows</span>
            <span class="tag">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with about_col2:
    st.markdown("""
    <div class="light-card">
        <h3>Education History</h3>
        
        <div class="timeline-item">
            <h4 style="margin:0; color:#0f172a;">Bachelor of Science (B.Sc) - Computer Science</h4>
            <span style="color:#64748b; font-size:0.85rem;">Nagarjuna Post Graduate College of Science, Raipur</span>
            <p style="margin-top:5px; font-size:0.9rem; color:#334155;">Specialized in computer applications, core software concepts, and databases.</p>
        </div>

        <div class="timeline-item">
            <h4 style="margin:0; color:#0f172a;">Data Analytics Program</h4>
            <span style="color:#64748b; font-size:0.85rem;">Coding Ninjas (2024 - 2025)</span>
            <p style="margin-top:5px; font-size:0.9rem; color:#334155;">Comprehensive training in Advanced SQL, Python for Data Science, Data Visualization, and Power BI dashboard development.</p>
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
        <p style="color:#64748b; font-size:0.85rem;">Querying, Aggregation, & CTEs</p>
        <span class="tag">CTEs & Subqueries</span>
        <span class="tag">Window Functions</span>
        <span class="tag">Table Joins</span>
        <span class="tag">Optimization</span>
    </div>
    """, unsafe_allow_html=True)

with sk2:
    st.markdown("""
    <div class="light-card">
        <h4>🐍 Python & EDA</h4>
        <p style="color:#64748b; font-size:0.85rem;">Data Manipulation & Modeling</p>
        <span class="tag">Pandas</span>
        <span class="tag">NumPy</span>
        <span class="tag">Plotly</span>
        <span class="tag">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)

with sk3:
    st.markdown("""
    <div class="light-card">
        <h4>📈 BI & Dashboards</h4>
        <p style="color:#64748b; font-size:0.85rem;">Business Intelligence & Reporting</p>
        <span class="tag">Power BI</span>
        <span class="tag">DAX Calculations</span>
        <span class="tag">Advanced Excel</span>
        <span class="tag">Jira Metrics</span>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 3: EXPERIENCE ---
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

st.markdown("""
<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="color:#ffffff; margin:0;">Operations Analyst</h3>
        <span style="color:#818cf8; font-weight:600;">Loop.AI | Dec 2024 - Dec 2025</span>
    </div>
    <p style="color:#94a3b8; font-size:0.95rem; margin-top:8px;">
        Automated operational reporting workflows, built monitoring models, and applied Python analytics to evaluate service metrics and efficiency improvements.
    </p>
    <span class="tag">Python</span><span class="tag">SQL</span><span class="tag">Workflow Automation</span><span class="tag">Process Improvement</span>
</div>

<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="color:#ffffff; margin:0;">Operations Team Lead</h3>
        <span style="color:#818cf8; font-weight:600;">Curefit | Jan 2022 - Mar 2024</span>
    </div>
    <p style="color:#94a3b8; font-size:0.95rem; margin-top:8px;">
        Managed operational workflows, tracked performance key performance indicators (KPIs) via Jira dashboards, and led support resolution teams.
    </p>
    <span class="tag">Operations Lead</span><span class="tag">Jira</span><span class="tag">KPI Tracking</span><span class="tag">Team Leadership</span>
</div>

<div class="dark-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="color:#ffffff; margin:0;">Customer Support Team Lead</h3>
        <span style="color:#818cf8; font-weight:600;">OneFitPlus | Apr 2020 - Dec 2021</span>
    </div>
    <p style="color:#94a3b8; font-size:0.95rem; margin-top:8px;">
        Supervised customer support operations, handled escalation workflows, and structured team resolution benchmarks.
    </p>
    <span class="tag">Contact Centre Operations</span><span class="tag">Escalation Management</span><span class="tag">Reporting</span>
</div>
""", unsafe_allow_html=True)


# --- SECTION 4: PROJECTS ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)

# Project 1
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">1. PhonePe Digital Payments Case Study</h3>
    <p style="color:#94a3b8;">Interactive analytics dashboard analyzing transaction volume growth, payment dynamics, and user adoption metrics across Indian states.</p>
    <div>
        <span class="tag">Python</span><span class="tag">Streamlit</span><span class="tag">Plotly</span><span class="tag">Pandas</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Embedded Plotly visual
df = pd.DataFrame({
    "State": ["Maharashtra", "Karnataka", "Telangana", "Tamil Nadu", "Delhi"],
    "Transactions_Cr": [120, 95, 80, 75, 60]
})
fig = px.bar(df, x="State", y="Transactions_Cr", color="State", template="plotly_dark", title="Transaction Volume by Top States (Crores)")
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=350)
st.plotly_chart(fig, use_container_width=True)

# Project 2
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">2. PayPal Risk & Merchant Analytics</h3>
    <p style="color:#94a3b8;">Constructed a Power BI and SQL dashboard evaluating merchant transaction tiers, risk distributions, and regional volume trends.</p>
    <div>
        <span class="tag">Power BI</span><span class="tag">DAX</span><span class="tag">SQL</span><span class="tag">Fintech</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Project 3
st.markdown("""
<div class="dark-card">
    <h3 style="color:#ffffff;">3. Media Catalog & Content Trend Dashboard</h3>
    <p style="color:#94a3b8;">Evaluated streaming content distribution models, release trends, and genre ratings using dynamic Power BI visual models.</p>
    <div>
        <span class="tag">Power BI</span><span class="tag">Data Modeling</span><span class="tag">Advanced Excel</span>
    </div>
</div>
""", unsafe_allow_html=True)


# --- SECTION 5: CERTIFICATIONS ---
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Certifications & Education</div>', unsafe_allow_html=True)

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.markdown("""
    <div class="dark-card">
        <h4 style="color:#ffffff;">Data Analytics Certification</h4>
        <p style="color:#818cf8; font-weight:600;">Coding Ninjas (2024 - 2025)</p>
        <p style="color:#94a3b8; font-size:0.9rem;">Validated proficiency across SQL, Python data manipulation libraries, and Power BI visualization.</p>
    </div>
    """, unsafe_allow_html=True)

with cert_col2:
    st.markdown("""
    <div class="dark-card">
        <h4 style="color:#ffffff;">SQL & Business Intelligence</h4>
        <p style="color:#c084fc; font-weight:600;">HackerRank & LinkedIn Learning</p>
        <p style="color:#94a3b8; font-size:0.9rem;">HackerRank Advanced SQL Skill Certification and LinkedIn Learning Data Analysis Credentials.</p>
    </div>
    """, unsafe_allow_html=True)


# --- SECTION 6: CONTACT ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s Connect</div>', unsafe_allow_html=True)

st.markdown("""
<div class="light-card" style="text-align: center;">
    <h3>Get In Touch</h3>
    <p style="color: #475569;">Open to Data Analyst roles and collaborative analytics projects.</p>
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
        st.success("Thank you! Message sent.")
