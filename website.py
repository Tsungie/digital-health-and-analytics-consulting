import streamlit as st
from PIL import Image

im = Image.open("logob.png")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Digital Health & Analytics Consulting",
    page_icon=im, 
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS (Styling) ---
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* 1. SIDEBAR BACKGROUND */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #dee2e6;
    }
    
    /* MOBILE RESPONSIVE FIXES */
    @media (max-width: 768px) {
        /* Make main content use full width on mobile when sidebar is collapsed */
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        
        /* Make hero section more compact on mobile */
        .hero-title {
            font-size: 1.8rem !important;
            line-height: 1.3 !important;
        }
        
        .hero-container {
            padding: 30px 20px !important;
        }
        
        .hero-container p {
            font-size: 1rem !important;
        }
        
        /* Service cards spacing on mobile */
        .service-card, .service-card-pro {
            margin-bottom: 20px;
        }
        
        /* Metrics on mobile */
        [data-testid="stMetric"] {
            font-size: 0.9rem;
        }
    }
    
    /* TABLET RESPONSIVE */
    @media (max-width: 1024px) {
        .hero-title {
            font-size: 2.2rem !important;
        }
    }

    /* 2. COLORED NAVIGATION BUTTONS */
    div.row-widget.stRadio > div {
        background-color: transparent;
    }
    
    /* Default Button Style (Colored!) */
    .stRadio > div > label {
        background-color: #E3F2FD; /* Light Blue Background */
        padding: 12px 20px;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border: 1px solid #BBDEFB;
        transition: all 0.3s ease;
        cursor: pointer;
        color: #0F4C81; /* Dark Blue Text */
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center; /* Center text */
    }
    
    /* Hover Effect */
    .stRadio > div > label:hover {
        background-color: #0F4C81; /* Dark Blue Hover */
        color: white !important;
        transform: translateX(5px);
        box-shadow: 0 4px 10px rgba(15, 76, 129, 0.3);
    }

    /* 3. HERO SECTION */
    .hero-container {
        background: linear-gradient(135deg, #0F4C81 0%, #008080 100%);
        padding: 60px 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(15, 76, 129, 0.2);
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: white !important;
    }

    /* 4. SERVICE CARDS */
    .service-card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        border-top: 5px solid #008080;
    }
    .service-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    .card-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        background: #f0fdf4;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
    }

</style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Try to load your logo, otherwise use a generic medical icon
    try:
        st.image("logo.png", use_container_width=True) 
    except:
        # Replaced the "watch" with a Health/Medical Folder icon
        st.image("website.png", width=80)
        st.header("Digital Health & Analytics") 
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🧭 Menu")
    
    # NAVIGATION BUTTONS
    page = st.radio("Go to:", ["Home", "Our Services", "About Us", "Contact"], label_visibility="collapsed")
    
    st.markdown("---")
    
    # STATUS BADGE
    st.markdown("""
    <div style="background-color: #d1fae5; padding: 10px; border-radius: 8px; border: 1px solid #6ee7b7; color: #065f46; font-size: 0.9rem; text-align: center;">
        <strong>✅ OPEN FOR PROJECTS</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("[Visit LinkedIn Page ↗](https://www.linkedin.com/company/111742935/)")

# --- 1. HOME PAGE ---
if page == "Home":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Don't Just Build Software.<br>Build Resilience.</div>
        <p style="font-size: 1.2rem; opacity: 0.9;">Strategic advisory, architecture, and data analytics for digital health in emerging markets.</p>
    </div>
    """, unsafe_allow_html=True)

    # FIX: Adjusted column width ratio so the narrow video doesn't take up too much width
    col1, col2 = st.columns([0.7, 1.3], gap="large")
    
    with col1:
        # Vertical Video
        st.video("6097001-uhd_2160_3840_24fps.mp4", autoplay=True, muted=True, loop=True)
    
    with col2:
        st.markdown("### 🛑 The Problem")
        st.info("A Ministry or NGO spends millions on an EHR system. Six months later, doctors are back to using paper because workflows are clunky and the internet is slow.")
        
        st.markdown("### ✅ The Solution")
        st.success("We act as the **Architect** and **Translator** between clinical reality and technical teams.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Explore Our Services →"):
            st.toast("Click 'Our Services' on the left!")

        # --- FIX: MOVED STATS HERE TO FILL THE BLANK SPACE ---
        st.markdown("---")
        st.markdown("#### 🏆 Our Impact")
        
        # Created mini-columns inside this column to stack stats neatly
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            st.metric("Experience", "9+ Years", "National Scale EHRs")
            st.markdown("<br>", unsafe_allow_html=True) # Spacer
            st.metric("Data Managed", "500k+", "Patient Records")
        with sub_c2:
            st.metric("Facilities", "700+", "Across Zimbabwe")
# --- 2. SERVICES PAGE ---
elif page == "Our Services":
    
    # Header Section with gradient underline
    st.markdown("""
    <div style="text-align: center; margin-bottom: 50px;">
        <h1 style="color: #0F4C81; font-size: 3rem; margin-bottom: 0px; display: inline-block;">How We Help You</h1>
        <div style="height: 4px; width: 100px; background: linear-gradient(90deg, #008080, #0F4C81); margin: 10px auto 20px auto; border-radius: 2px;"></div>
        <p style="font-size: 1.2rem; color: #555; max-width: 700px; margin: 0 auto;">
            We specialize in the critical <strong>pre-development</strong> and <strong>optimization</strong> phases. 
            We bridge the gap between clinical needs and technical delivery.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Custom CSS for the More Colorful Cards
    st.markdown("""
    <style>
        .service-card-pro {
            background: linear-gradient(to bottom right, #ffffff, #f8fcfd); /* Subtle gradient background */
            padding: 35px;
            border-radius: 20px;
            border: 1px solid #f0f0f0;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            position: relative; /* For the top border */
            overflow: hidden; /* Ensures the border follows the corner radius */
        }
        
        /* HOVER EFFECT: Lifts up and glows deeper */
        .service-card-pro:hover {
            transform: translateY(-10px);
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
        }

        /* Colored Top Border Indicator */
        .card-top-border {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 6px;
        }

        .icon-box {
            width: 70px; /* Larger icon box */
            height: 70px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            margin-bottom: 25px;
            color: white; /* White icons on colored background */
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }
        
        /* New Gradient Backgrounds for Icons */
        .teal-gradient { background: linear-gradient(135deg, #008080, #4db6ac); }
        .blue-gradient { background: linear-gradient(135deg, #0F4C81, #4fc3f7); }
        
        .card-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 10px;
        }
        
        .card-subtitle {
            font-size: 0.9rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 10px;
        }
        
        .card-text {
            color: #6b7280;
            line-height: 1.7;
            font-size: 1.05rem;
        }
        
        .tagline {
            font-weight: 700;
            margin-bottom: 8px;
            display: block;
        }
        
        /* RESPONSIVE SERVICE CARDS */
        @media (max-width: 768px) {
            .service-card-pro {
                padding: 25px;
                margin-bottom: 20px;
            }
            .card-title {
                font-size: 1.3rem;
            }
            .card-text {
                font-size: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # --- ROW 1 ---
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="service-card-pro">
            <div class="card-top-border" style="background: #008080;"></div>
            <div class="icon-box teal-gradient">🏗️</div>
            <div class="card-subtitle" style="color: #008080;">Architecture</div>
            <div class="card-title">Solution Architecture</div>
            <div class="card-text">
                <span class="tagline" style="color: #005f5f;">The Blueprint before the Build.</span>
                We design the logic, workflows, and offline-first capabilities of your system before a single line of code is written. This prevents costly rewrites later.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="service-card-pro">
            <div class="card-top-border" style="background: #0F4C81;"></div>
            <div class="icon-box blue-gradient">📊</div>
            <div class="card-subtitle" style="color: #0F4C81;">Analytics</div>
            <div class="card-title">Healthcare Data Analytics</div>
            <div class="card-text">
                <span class="tagline" style="color: #0a355c;">Turn data into funding.</span>
                We clean, organize, and visualize your healthcare data (TX_CURR, Viral Loads) so you can finally see the impact of your programs and report to donors.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ROW 2 ---
    col3, col4 = st.columns(2, gap="medium")
    
    with col3:
        st.markdown("""
        <div class="service-card-pro">
            <div class="card-top-border" style="background: #0F4C81;"></div>
            <div class="icon-box blue-gradient">📝</div>
            <div class="card-subtitle" style="color: #0F4C81;">Translation</div>
            <div class="card-title">Requirements Engineering</div>
            <div class="card-text">
                <span class="tagline" style="color: #0a355c;">Clinical to Technical.</span>
                Developers can't build what they don't understand. We translate your complex clinical needs into detailed user stories and technical specifications.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="service-card-pro">
            <div class="card-top-border" style="background: #008080;"></div>
            <div class="icon-box teal-gradient">🔍</div>
            <div class="card-subtitle" style="color: #008080;">Strategy</div>
            <div class="card-title">Vendor Selection</div>
            <div class="card-text">
                <span class="tagline" style="color: #005f5f;">Hire the right team.</span>
                We act as your technical hiring guide—drafting RFPs, vetting software developers, and ensuring you choose a partner who can actually deliver.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    # --- CTA SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0F4C81, #008080); color: white; padding: 50px; border-radius: 25px; text-align: center; box-shadow: 0 20px 40px rgba(15, 76, 129, 0.2);">
        <h2 style="color: white; margin-bottom: 15px; font-size: 2.2rem;">Not sure where to start?</h2>
        <p style="font-size: 1.2rem; opacity: 0.95; margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto;">
            Let's hop on a 15-minute call to diagnose your current system challenges.
        </p>
        <a href="mailto:misstsungie@gmail.com?subject=Consulting Inquiry" style="text-decoration: none;">
            <div style="background-color: white; color: #0F4C81; padding: 15px 40px; border-radius: 50px; display: inline-block; font-weight: 700; font-size: 1.1rem; transition: 0.3s; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                Book a Free Discovery Call →
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)
# --- 3. ABOUT PAGE ---
elif page == "About Us":
    st.markdown("# The Founder")
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image("profile.png", caption="Tsungie Ncube")
        
        # --- LEFT COLUMN: CREDENTIALS ---
        st.markdown("""
        <div style="background-color: #f0fdf4; padding: 15px; border-radius: 10px; border: 1px solid #bbf7d0; text-align: center; margin-bottom: 20px;">
            <p style="margin: 0; font-weight: bold; color: #065f46;">🎓 MBA in Artificial Intelligence</p>
            <p style="margin: 5px 0; font-size: 0.9rem;">MIT Data Science Cert</p>
            <p style="margin: 5px 0; font-size: 0.9rem;">BSc Software Engineering</p>
            <hr style="margin: 10px 0; border: 0; border-top: 1px solid #bbf7d0;">
            <p style="margin: 0; font-size: 0.95rem; color: #047857; font-weight: 700;">Degree in Monitoring & Evaluation</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- BOOK WAITLIST ---
        st.markdown("""
        <div style="background-color: #fffbeb; padding: 20px; border-radius: 10px; border: 1px solid #fcd34d; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <div style="font-size: 2rem; margin-bottom: 10px;">📖</div>
            <strong>Coming Soon: The Book</strong><br>
            <p style="font-size: 0.9rem; color: #555;">
                I am writing a guide on <em>"Building Resilient EHR Systems in Emerging Markets."</em>
            </p>
            <p style="font-size: 0.9rem; font-weight: bold; color: #0F4C81;">
                Want a free copy when it launches?
            </p>
            <a href="mailto:misstsungie@gmail.com?subject=I want the free book!" style="text-decoration: none;">
                <button style="background-color: #0F4C81; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer; width: 100%; font-size: 0.9rem;">
                    Join the Waitlist →
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # --- RIGHT COLUMN: THE STORY ---
        st.markdown("""
        ### From Junior Developer to National Strategist.
        
        I didn't just study digital health; I built it from the ground up. My journey mirrors the lifecycle of a healthcare system:
        """)
        
        # --- TIMELINE VISUALIZATION ---
        st.markdown("""
        <div style="border-left: 4px solid #e5e7eb; padding-left: 20px; margin-left: 5px;">
            <div style="margin-bottom: 20px;">
                <strong style="color: #0F4C81; font-size: 1.1rem;">🛠️ 2016: The Builder (Junior to Senior Dev)</strong>
                <p style="margin: 5px 0; color: #444;">Joined the team building <strong>Zimbabwe's first EHR</strong>. I wrote the code that piloted in small rural clinics and scaled it to major central hospitals.</p>
            </div>
            <div style="margin-bottom: 20px;">
                <strong style="color: #008080; font-size: 1.1rem;">👥 The Team Lead & Coordinator</strong>
                <p style="margin: 5px 0; color: #444;">Promoted to lead the expansion into Bulawayo, Mat North, and Mat South. I <strong>managed a technical team</strong>, oversaw server installations, and personally trained over <strong>5,000 clinicians</strong>.</p>
            </div>
            <div style="margin-bottom: 20px;">
                <strong style="color: #b91c1c; font-size: 1.1rem;">📊 The Analyst (Data Scientist)</strong>
                <p style="margin: 5px 0; color: #444;">Realized that data is only useful if it drives decisions. I specialized in Data Science to turn millions of EHR records into actionable insights for the Ministry.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # --- THE LESSONS (THE "WHY") ---
        st.success("""
        **💡 Why I Started This Firm**
        
        Having been in **all cycles of the EHR system**—from the first line of code to the final data report—I have seen exactly where projects succeed and where they fail.
        
        **I want to share these hard-won lessons with you.** My goal is to ensure that your organization learns from my experience, rather than learning the hard way.
        """)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- EXPERIENCE GRID ---
        st.markdown("### 🌍 Experience in Action")
        st.markdown("""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #e9ecef;">
                <strong>🇿🇼 National Scale</strong><br>
                <span style="font-size: 0.9rem; color: #555;">From rural pilots to a system serving <strong>7 million+ patients</strong>. I know how to scale.</span>
            </div>
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #e9ecef;">
                <strong>👥 Team Leadership</strong><br>
                <span style="font-size: 0.9rem; color: #555;">Led technical teams and trained <strong>5,000+ clinicians</strong>. I understand adoption & change management.</span>
            </div>
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #e9ecef;">
                <strong>📡 Infrastructure</strong><br>
                <span style="font-size: 0.9rem; color: #555;">Hands-on experience installing servers and networking in remote areas.</span>
            </div>
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #e9ecef;">
                <strong>📈 Data Science</strong><br>
                <span style="font-size: 0.9rem; color: #555;">Generating high-level reports from raw EHR data to guide public health policy.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- 4. CONTACT PAGE ---
elif page == "Contact":
    st.markdown("# Let's Start a Project")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Vertical Video
        st.video("4487121-uhd_3840_2160_25fps.mp4", autoplay=True, muted=True, loop=True)
    
    with col2:
        st.markdown("### Send a Message")
        
        # --- FORM SUBMIT CODE (HTML) ---
        contact_form = """
        <form action="https://formsubmit.co/misstsungie@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-bottom: 10px;">
             <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-bottom: 10px;">
             <textarea name="message" placeholder="How can we help?" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-bottom: 10px; height: 150px;"></textarea>
             <button type="submit" style="background-color: #0F4C81; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%;">Send Message</button>
        </form>
        """
        
        st.markdown(contact_form, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("#### 🔗 Connect")
        st.markdown("💼 **LinkedIn:** [Digital Health & Analytics Consulting](https://www.linkedin.com/company/111742935/)")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
    © 2026 Digital Health & Analytics Consulting • Harare, Zimbabwe
</div>
""", unsafe_allow_html=True)