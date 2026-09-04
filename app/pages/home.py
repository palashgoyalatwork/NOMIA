import streamlit as st

from data.countries.countries import COUNTRIES, get_cities


# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────

st.html(
    """
    <div style="
        padding:55px 0 35px 0;
    ">

        <div style="
            color:#60a5fa;
            font-size:13px;
            font-weight:700;
            letter-spacing:.16em;
            margin-bottom:18px;
        ">
            YOUR LOCAL INTELLIGENCE LAYER
        </div>

        <h1 style="
            font-size:58px;
            line-height:1.08;
            margin:0;
            font-weight:750;
            color:#f5f7fa;
        ">
            Know the city<br>
            <span style="color:#60a5fa;">
                before you explore it.
            </span>
        </h1>

        <p style="
            color:#9aa5b5;
            font-size:17px;
            line-height:1.7;
            max-width:780px;
            margin-top:25px;
            margin-bottom:0;
        ">
            NOMIA brings together the places, transport, food, shopping
            and essential information you need when entering a new city.
        </p>

    </div>
    """
)


# ─────────────────────────────────────────────
# DESTINATION SELECTOR
# ─────────────────────────────────────────────

st.html(
    """
    <div style="
        margin-top:10px;
        margin-bottom:12px;
    ">
        <div style="
            font-size:24px;
            font-weight:700;
            color:#f5f7fa;
        ">
            Where are you going?
        </div>

        <div style="
            color:#718096;
            font-size:13px;
            margin-top:6px;
        ">
            Choose your destination to unlock the local guide.
        </div>
    </div>
    """
)


countries = list(COUNTRIES.keys())

saved_country = st.session_state.get("country", "India")

if saved_country in countries:
    country_index = countries.index(saved_country)
else:
    country_index = 0

country = st.selectbox(
    "Country",
    countries,
    index=country_index,
)


cities = get_cities(country)

previous_city = st.session_state.get("city")

if previous_city in cities:
    city_index = cities.index(previous_city)
else:
    city_index = 0

city = st.selectbox(
    "City",
    cities,
    index=city_index,
)


# Keep selection synchronized even before pressing Explore.
st.session_state["country"] = country
st.session_state["city"] = city


# ─────────────────────────────────────────────
# EXPLORE CTA
# ─────────────────────────────────────────────

if st.button(
    f"Explore {city} →",
    use_container_width=True,
    type="secondary",
):
    st.switch_page("pages/explore.py")


# ─────────────────────────────────────────────
# CATALOG STATS
# ─────────────────────────────────────────────

total_countries = len(COUNTRIES)
total_cities = sum(len(city_list) for city_list in COUNTRIES.values())

st.markdown("---")

st.html(
    f"""
    <div style="
        display:grid;
        grid-template-columns:repeat(3, 1fr);
        gap:14px;
        margin:8px 0 30px 0;
    ">

        <div style="
            padding:22px;
            border:1px solid rgba(255,255,255,.08);
            border-radius:15px;
            background:rgba(255,255,255,.025);
        ">
            <div style="
                color:#60a5fa;
                font-size:27px;
                font-weight:750;
            ">
                {total_countries}
            </div>

            <div style="
                color:#8b96a8;
                font-size:12px;
                margin-top:5px;
                letter-spacing:.08em;
                text-transform:uppercase;
            ">
                Countries
            </div>
        </div>

        <div style="
            padding:22px;
            border:1px solid rgba(255,255,255,.08);
            border-radius:15px;
            background:rgba(255,255,255,.025);
        ">
            <div style="
                color:#60a5fa;
                font-size:27px;
                font-weight:750;
            ">
                {total_cities}
            </div>

            <div style="
                color:#8b96a8;
                font-size:12px;
                margin-top:5px;
                letter-spacing:.08em;
                text-transform:uppercase;
            ">
                Supported Cities
            </div>
        </div>

        <div style="
            padding:22px;
            border:1px solid rgba(255,255,255,.08);
            border-radius:15px;
            background:rgba(255,255,255,.025);
        ">
            <div style="
                color:#60a5fa;
                font-size:27px;
                font-weight:750;
            ">
                5
            </div>

            <div style="
                color:#8b96a8;
                font-size:12px;
                margin-top:5px;
                letter-spacing:.08em;
                text-transform:uppercase;
            ">
                Local Intelligence Layers
            </div>
        </div>

    </div>
    """
)


# ─────────────────────────────────────────────
# WHAT NOMIA COVERS
# ─────────────────────────────────────────────

st.html(
    """
    <div style="
        margin-bottom:18px;
    ">
        <div style="
            font-size:22px;
            font-weight:700;
            color:#f5f7fa;
        ">
            Everything you need locally.
        </div>

        <div style="
            color:#718096;
            font-size:13px;
            margin-top:6px;
        ">
            One destination. Five practical layers of city intelligence.
        </div>
    </div>
    """
)


features = [
    ("📍", "Explore", "Places worth knowing"),
    ("🚕", "Move", "Get around locally"),
    ("🍜", "Eat", "Food & delivery"),
    ("🛍️", "Shop", "Malls & shopping"),
    ("🧭", "Essentials", "What you need nearby"),
]


columns = st.columns(5)

for column, (icon, title, description) in zip(columns, features):

    with column:

        st.html(
            f"""
            <div style="
                padding:22px 18px;
                min-height:150px;
                border:1px solid rgba(255,255,255,.08);
                border-radius:15px;
                background:rgba(255,255,255,.025);
                transition:all .2s ease;
            ">

                <div style="
                    font-size:25px;
                    line-height:1;
                ">
                    {icon}
                </div>

                <div style="
                    font-size:16px;
                    font-weight:700;
                    color:#f5f7fa;
                    margin-top:17px;
                ">
                    {title}
                </div>

                <div style="
                    color:#718096;
                    font-size:12px;
                    line-height:1.5;
                    margin-top:8px;
                ">
                    {description}
                </div>

            </div>
            """
        )


# ─────────────────────────────────────────────
# BOTTOM PRODUCT STATEMENT
# ─────────────────────────────────────────────

st.markdown("---")

st.html(
    """
    <div style="
        padding:24px 0 10px 0;
        text-align:center;
    ">

        <div style="
            color:#60a5fa;
            font-size:11px;
            font-weight:700;
            letter-spacing:.18em;
        ">
            NOMIA
        </div>

        <div style="
            color:#d5dbe5;
            font-size:18px;
            font-weight:600;
            margin-top:10px;
        ">
            Discover smarter. Move easier. Experience locally.
        </div>

        <div style="
            color:#626d7d;
            font-size:12px;
            margin-top:8px;
        ">
            Built for the moment you arrive in a new city.
        </div>

    </div>
    """
)