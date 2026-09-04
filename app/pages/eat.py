import streamlit as st

from data.cities.catalog import (
    get_city,
    get_food_areas,
    get_city_country,
)


# ============================================================
# NOMIA — EAT PAGE
# ============================================================


# ============================================================
# FOOD DELIVERY DATA
# ============================================================

DELIVERY_DATA = {

    # --------------------------------------------------------
    # INDIA
    # --------------------------------------------------------

    "Delhi": [
        ("Zomato", "Food delivery", "https://www.zomato.com/"),
        ("Swiggy", "Food delivery", "https://www.swiggy.com/"),
    ],

    "Mumbai": [
        ("Zomato", "Food delivery", "https://www.zomato.com/"),
        ("Swiggy", "Food delivery", "https://www.swiggy.com/"),
    ],

    "Bengaluru": [
        ("Zomato", "Food delivery", "https://www.zomato.com/"),
        ("Swiggy", "Food delivery", "https://www.swiggy.com/"),
    ],


    # --------------------------------------------------------
    # UAE
    # --------------------------------------------------------

    "Dubai": [
        ("Talabat", "Food delivery", "https://www.talabat.com/"),
        ("Careem", "Food & local services", "https://www.careem.com/"),
    ],

    "Abu Dhabi": [
        ("Talabat", "Food delivery", "https://www.talabat.com/"),
        ("Careem", "Food & local services", "https://www.careem.com/"),
    ],


    # --------------------------------------------------------
    # JAPAN
    # --------------------------------------------------------

    "Tokyo": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/jp"),
        ("Demae-can", "Food delivery", "https://demae-can.com/"),
    ],

    "Osaka": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/jp"),
        ("Demae-can", "Food delivery", "https://demae-can.com/"),
    ],

    "Kyoto": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/jp"),
        ("Demae-can", "Food delivery", "https://demae-can.com/"),
    ],


    # --------------------------------------------------------
    # SINGAPORE
    # --------------------------------------------------------

    "Singapore": [
        ("GrabFood", "Food delivery", "https://food.grab.com/"),
        ("foodpanda", "Food delivery", "https://www.foodpanda.sg/"),
    ],


    # --------------------------------------------------------
    # UNITED KINGDOM
    # --------------------------------------------------------

    "London": [
        ("Deliveroo", "Food delivery", "https://deliveroo.co.uk/"),
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/gb"),
    ],

    "Manchester": [
        ("Deliveroo", "Food delivery", "https://deliveroo.co.uk/"),
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/gb"),
    ],


    # --------------------------------------------------------
    # FRANCE
    # --------------------------------------------------------

    "Paris": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/fr"),
        ("Deliveroo", "Food delivery", "https://deliveroo.fr/"),
    ],


    # --------------------------------------------------------
    # ITALY
    # --------------------------------------------------------

    "Rome": [
        ("Deliveroo", "Food delivery", "https://deliveroo.it/"),
        ("Just Eat", "Food delivery", "https://www.justeat.it/"),
    ],

    "Milan": [
        ("Deliveroo", "Food delivery", "https://deliveroo.it/"),
        ("Just Eat", "Food delivery", "https://www.justeat.it/"),
    ],


    # --------------------------------------------------------
    # USA
    # --------------------------------------------------------

    "New York": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/"),
        ("DoorDash", "Food delivery", "https://www.doordash.com/"),
    ],

    "Los Angeles": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/"),
        ("DoorDash", "Food delivery", "https://www.doordash.com/"),
    ],


    # --------------------------------------------------------
    # AUSTRALIA
    # --------------------------------------------------------

    "Sydney": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/au"),
        ("DoorDash", "Food delivery", "https://www.doordash.com/"),
    ],


    # --------------------------------------------------------
    # GERMANY
    # --------------------------------------------------------

    "Berlin": [
        ("Lieferando", "Food delivery", "https://www.lieferando.de/"),
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/de"),
    ],


    # --------------------------------------------------------
    # CANADA
    # --------------------------------------------------------

    "Toronto": [
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/ca"),
        ("DoorDash", "Food delivery", "https://www.doordash.com/"),
    ],


    # --------------------------------------------------------
    # NETHERLANDS
    # --------------------------------------------------------

    "Amsterdam": [
        ("Thuisbezorgd", "Food delivery", "https://www.thuisbezorgd.nl/"),
        ("Uber Eats", "Food delivery", "https://www.ubereats.com/nl"),
    ],
}


# ============================================================
# LOCAL FOOD TIPS
# ============================================================

LOCAL_TIPS = {

    "Delhi":
        "Delhi's food scene varies heavily by neighborhood. Explore beyond the main tourist areas.",

    "Mumbai":
        "Mumbai has excellent food across very different neighborhoods, so location matters.",

    "Bengaluru":
        "Traffic can make short distances surprisingly slow, so choosing food spots near your area can save time.",

    "Dubai":
        "Dubai has a very international food scene, with options from many cuisines.",

    "Abu Dhabi":
        "Many restaurants offer delivery, making it easy to eat without travelling far.",

    "Tokyo":
        "Tokyo has an enormous range of food. Exploring smaller neighborhood restaurants can be rewarding.",

    "Osaka":
        "Osaka is particularly well known for its casual food culture.",

    "Kyoto":
        "Kyoto's traditional districts can be busy, so plan meals around your sightseeing route.",

    "Singapore":
        "Hawker centres are an important part of Singapore's food culture and offer a wide variety of local dishes.",

    "London":
        "London has an extremely diverse food scene. Different neighbourhoods often have very different cuisines and dining styles.",

    "Manchester":
        "Manchester has a diverse food scene, from traditional local spots to international restaurants.",

    "Paris":
        "Paris has much more than classic French cuisine. Explore neighbourhood bakeries, cafés and markets alongside restaurants.",

    "Rome":
        "Rome is known for traditional Roman dishes, but smaller neighbourhood trattorias can offer a more local experience.",

    "Milan":
        "Milan combines traditional northern Italian food with a large modern restaurant and café scene.",

    "New York":
        "New York's food scene changes dramatically from neighbourhood to neighbourhood, so explore beyond the main tourist areas.",

    "Los Angeles":
        "Los Angeles has a highly diverse food scene. Mexican, Asian and many other cuisines are especially prominent.",

    "Sydney":
        "Sydney combines Australian café culture with a wide range of Asian and international cuisines.",

    "Berlin":
        "Berlin has a diverse and affordable food scene, with everything from traditional German food to international street food.",

    "Toronto":
        "Toronto is highly multicultural, so exploring different neighbourhoods can reveal very different food cultures.",

    "Amsterdam":
        "Amsterdam offers traditional Dutch food alongside a very international restaurant and café scene.",
}


# ============================================================
# CURRENT DESTINATION
# ============================================================

city = st.session_state.get(
    "city",
    "Delhi",
)

country = st.session_state.get(
    "country",
    "India",
)

city_data = get_city(city)

# Safety fallback
if not city_data:

    city = "Delhi"
    country = "India"

    city_data = get_city(city)

if not city_data:

    st.error("City data could not be loaded.")
    st.stop()


# Synchronize country with catalog
catalog_country = get_city_country(city)

if catalog_country:
    country = catalog_country


# ============================================================
# LOAD FOOD DATA
# ============================================================

delivery = DELIVERY_DATA.get(
    city,
    [],
)

food_areas = get_food_areas(city)

if not food_areas:
    food_areas = []


tip = LOCAL_TIPS.get(
    city,
    f"Explore different neighbourhoods in {city} to discover local food and dining options.",
)


# ============================================================
# HEADER
# ============================================================

st.html(
    f"""
    <div style="
        padding:30px 0 20px 0;
    ">

        <div style="
            color:#60a5fa;
            font-size:12px;
            font-weight:700;
            letter-spacing:.16em;
        ">
            LOCAL FOOD INTELLIGENCE
        </div>

        <h1 style="
            font-size:48px;
            margin:10px 0 0 0;
            font-weight:750;
            color:#f5f7fa;
        ">
            Eat in {city}.
        </h1>

        <p style="
            color:#8f9aaa;
            font-size:16px;
            margin-top:10px;
        ">
            Food delivery, dining areas and local food intelligence.
        </p>

    </div>
    """
)


# ============================================================
# OVERVIEW
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Delivery apps",
        len(delivery),
    )


with c2:

    st.metric(
        "Food areas",
        len(food_areas),
    )


with c3:

    st.metric(
        "City",
        city,
    )


st.markdown("---")


# ============================================================
# DELIVERY
# ============================================================

st.markdown("### 🛵 Food delivery")

if not delivery:

    st.info(
        f"Delivery service information for {city} is coming soon."
    )

else:

    delivery_cols = st.columns(2)

    for i, (name, kind, url) in enumerate(
        delivery
    ):

        with delivery_cols[i % 2]:

            st.html(
                f"""
                <div style="
                    padding:20px;
                    margin-bottom:10px;
                    border:1px solid rgba(255,255,255,.08);
                    border-radius:14px;
                    background:rgba(255,255,255,.025);
                ">

                    <div style="
                        font-size:20px;
                        font-weight:700;
                        color:#f5f7fa;
                    ">
                        {name}
                    </div>

                    <div style="
                        color:#8f9aaa;
                        font-size:13px;
                        margin-top:7px;
                    ">
                        {kind}
                    </div>

                </div>
                """
            )

            st.link_button(
                f"Open {name} →",
                url,
                use_container_width=True,
            )


# ============================================================
# FOOD AREAS
# ============================================================

st.markdown("---")

st.markdown("### 🍜 Where to eat")

if not food_areas:

    st.info(
        f"Food area information for {city} is coming soon."
    )

else:

    columns = st.columns(3)

    for i, area in enumerate(food_areas):

        with columns[i % 3]:

            # Current catalog stores food areas as strings.
            # Support dictionaries too for future upgrades.

            if isinstance(area, str):

                area_name = area

                description = (
                    f"Food, restaurants and local dining around {area}."
                )

            elif isinstance(area, dict):

                area_name = area.get(
                    "name",
                    "Food area",
                )

                description = area.get(
                    "description",
                    f"Food and dining around {area_name}.",
                )

            else:

                area_name = str(area)

                description = (
                    f"Food and dining around {area_name}."
                )


            st.html(
                f"""
                <div style="
                    padding:20px;
                    min-height:145px;
                    border:1px solid rgba(255,255,255,.08);
                    border-radius:14px;
                    background:rgba(255,255,255,.025);
                ">

                    <div style="
                        color:#60a5fa;
                        font-size:11px;
                        font-weight:600;
                        letter-spacing:.12em;
                    ">
                        FOOD AREA
                    </div>

                    <div style="
                        font-size:18px;
                        font-weight:700;
                        margin-top:10px;
                        color:#f5f7fa;
                    ">
                        {area_name}
                    </div>

                    <div style="
                        color:#8f9aaa;
                        font-size:13px;
                        line-height:1.5;
                        margin-top:8px;
                    ">
                        {description}
                    </div>

                </div>
                """
            )


# ============================================================
# NOMIA TIP
# ============================================================

st.markdown("---")

st.markdown("### 💡 NOMIA local tip")

st.info(tip)