import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NOMIA — Local Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    """
<style>

:root {
    --nomia-bg: #07090d;
    --nomia-panel: #0b0e13;
    --nomia-border: rgba(255,255,255,.07);
    --nomia-text: #f5f7fa;
    --nomia-muted: #8f9aaa;
    --nomia-blue: #60a5fa;
}


/* =====================================================
   APP BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(59,130,246,.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(16,185,129,.07),
            transparent 30%
        ),
        #07090d;

    color: var(--nomia-text);
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {
    background: #0b0e13;
    border-right: 1px solid var(--nomia-border);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.2rem;
}


/* Sidebar navigation */

[data-testid="stSidebarNav"] {
    padding-top: 8px;
}

[data-testid="stSidebarNav"] span {
    font-size: 14px;
}


/* =====================================================
   HIDE STREAMLIT CHROME
   ===================================================== */

#MainMenu,
footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}


/* =====================================================
   GLOBAL BUTTONS
   ===================================================== */

.stButton > button,
.stLinkButton > a {
    border-radius: 10px !important;

    border: 1px solid rgba(255,255,255,.10) !important;

    background: rgba(255,255,255,.04) !important;

    color: #f5f7fa !important;

    transition:
        border-color .2s ease,
        background .2s ease,
        transform .2s ease;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    border-color: rgba(96,165,250,.45) !important;

    background: rgba(96,165,250,.08) !important;

    transform: translateY(-1px);
}


/* =====================================================
   INPUTS
   ===================================================== */

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background: rgba(255,255,255,.035) !important;

    border-color: rgba(255,255,255,.10) !important;

    border-radius: 10px !important;
}


/* =====================================================
   METRICS
   ===================================================== */

[data-testid="stMetric"] {
    background: rgba(10,14,20,.35);

    border: 1px solid rgba(255,255,255,.06);

    border-radius: 14px;

    padding: 16px 18px;
}

[data-testid="stMetricLabel"] {
    color: #91a4bd !important;
}

[data-testid="stMetricValue"] {
    color: #f5f7fa !important;
}


/* =====================================================
   DIVIDERS
   ===================================================== */

hr {
    border-color: rgba(255,255,255,.07) !important;
}


/* =====================================================
   INFO / WARNING / SUCCESS BOXES
   ===================================================== */

[data-testid="stAlert"] {
    border-radius: 12px;
}


/* =====================================================
   LINK BUTTON TEXT
   ===================================================== */

.stLinkButton > a {
    text-decoration: none !important;
}


/* =====================================================
   SCROLLBAR
   ===================================================== */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #07090d;
}

::-webkit-scrollbar-thumb {
    background: #202630;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #303846;
}


/* =====================================================
   SELECTION
   ===================================================== */

::selection {
    background: rgba(96,165,250,.25);
    color: #ffffff;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# NOMIA GLOBAL HEADER
# =========================================================

st.html(
    """
<div style="
    display:flex;
    align-items:center;
    justify-content:space-between;

    padding:10px 0 24px 0;

    border-bottom:1px solid rgba(255,255,255,.07);

    margin-bottom:25px;
">

    <!-- BRAND -->

    <div style="
        display:flex;
        align-items:center;
        gap:12px;
    ">

        <div style="
            width:38px;
            height:38px;

            border-radius:11px;

            background:
                linear-gradient(
                    135deg,
                    #2563eb,
                    #06b6d4
                );

            display:flex;
            align-items:center;
            justify-content:center;

            font-size:20px;
            font-weight:700;

            color:white;

            box-shadow:
                0 6px 20px rgba(37,99,235,.20);
        ">
            N
        </div>


        <div>

            <div style="
                font-size:20px;
                font-weight:700;
                letter-spacing:.08em;
                color:#f5f7fa;
            ">
                NOMIA
            </div>


            <div style="
                font-size:11px;
                color:#7d8795;
                letter-spacing:.12em;
                margin-top:2px;
            ">
                LOCAL INTELLIGENCE
            </div>

        </div>

    </div>


    <!-- TAGLINE -->

    <div style="
        font-size:12px;
        color:#7d8795;
        letter-spacing:.08em;
    ">
        DISCOVER • MOVE • EXPERIENCE
    </div>

</div>
"""
)


# =========================================================
# NAVIGATION
# =========================================================

pages = {
    "NOMIA": [

        st.Page(
            "pages/home.py",
            title="Home",
            icon=":material/home:",
            default=True,
        ),

        st.Page(
            "pages/explore.py",
            title="Explore",
            icon=":material/explore:",
        ),

        st.Page(
            "pages/move.py",
            title="Move",
            icon=":material/directions_car:",
        ),

        st.Page(
            "pages/eat.py",
            title="Eat",
            icon=":material/restaurant:",
        ),

        st.Page(
            "pages/shop.py",
            title="Shop",
            icon=":material/shopping_bag:",
        ),

        st.Page(
            "pages/essentials.py",
            title="Essentials",
            icon=":material/health_and_safety:",
        ),
    ]
}


# =========================================================
# RUN NAVIGATION
# =========================================================

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True,
)

pg.run()