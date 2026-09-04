import streamlit as st

from data.cities.catalog import (
    get_city,
    get_city_country,
)


# ============================================================
# NOMIA — MOVE PAGE
# ============================================================

st.set_page_config(
    page_title="NOMIA • Move",
    page_icon="🚇",
    layout="wide",
)


# ============================================================
# CURRENT LOCATION
# ============================================================

city = st.session_state.get("city", "Delhi")
country = st.session_state.get("country", "India")

city_data = get_city(city)

# Safety fallback
if not city_data:
    city = "Delhi"
    country = "India"
    city_data = get_city(city)

# Always synchronize country with the central city catalog
catalog_country = get_city_country(city)

if catalog_country:
    country = catalog_country


# ============================================================
# TRANSPORT DATA
# ============================================================

TRANSPORT_DATA = {

    # --------------------------------------------------------
    # INDIA
    # --------------------------------------------------------

    "Delhi": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Delhi Metro",
                "Fast and practical for major routes across Delhi."
            ),
            (
                "🚕",
                "RIDE-HAILING",
                "Uber / Ola",
                "Convenient for direct point-to-point travel."
            ),
            (
                "🚌",
                "BUS",
                "DTC / Cluster Bus",
                "Extensive coverage across Delhi."
            ),
        ],
        "apps": [
            (
                "Delhi Metro",
                "https://delhimetrorail.com/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    "Mumbai": {
        "transport": [
            (
                "🚆",
                "LOCAL RAIL",
                "Mumbai Local",
                "One of Mumbai's main transport networks."
            ),
            (
                "🚇",
                "METRO",
                "Mumbai Metro",
                "Useful across several major corridors."
            ),
            (
                "🚕",
                "RIDE-HAILING",
                "Uber / Ola",
                "Useful for direct point-to-point travel."
            ),
        ],
        "apps": [
            (
                "Mumbai Metro",
                "https://www.mmrda.maharashtra.gov.in/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    "Bengaluru": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Namma Metro",
                "Useful for avoiding major road congestion."
            ),
            (
                "🚕",
                "RIDE-HAILING",
                "Uber / Ola",
                "Convenient for direct trips."
            ),
            (
                "🚌",
                "BUS",
                "BMTC",
                "Large city-wide bus network."
            ),
        ],
        "apps": [
            (
                "Namma Metro",
                "https://english.bmrc.co.in/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # UAE
    # --------------------------------------------------------

    "Dubai": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Dubai Metro",
                "Fast option along major city corridors."
            ),
            (
                "🚕",
                "TAXI",
                "Dubai Taxi",
                "Widely available across the city."
            ),
            (
                "🚌",
                "BUS",
                "RTA Bus",
                "Connects Metro stations and neighbourhoods."
            ),
        ],
        "apps": [
            (
                "Dubai RTA",
                "https://www.rta.ae/"
            ),
            (
                "Careem",
                "https://www.careem.com/"
            ),
        ],
    },


    "Abu Dhabi": {
        "transport": [
            (
                "🚌",
                "BUS",
                "Abu Dhabi Bus",
                "Main public transport option."
            ),
            (
                "🚕",
                "TAXI",
                "Abu Dhabi Taxi",
                "Useful for direct city travel."
            ),
            (
                "🚗",
                "RIDE-HAILING",
                "Careem",
                "Convenient point-to-point option."
            ),
        ],
        "apps": [
            (
                "Abu Dhabi Mobility",
                "https://admobility.gov.ae/"
            ),
            (
                "Careem",
                "https://www.careem.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # JAPAN
    # --------------------------------------------------------

    "Tokyo": {
        "transport": [
            (
                "🚆",
                "RAIL",
                "JR / Private Rail",
                "Extensive rail network covering the metropolitan area."
            ),
            (
                "🚇",
                "METRO",
                "Tokyo Metro",
                "Useful for dense central-city travel."
            ),
            (
                "🚕",
                "TAXI",
                "Tokyo Taxi",
                "Useful for direct journeys."
            ),
        ],
        "apps": [
            (
                "Tokyo Metro",
                "https://www.tokyometro.jp/en/"
            ),
            (
                "JR East",
                "https://www.jreast.co.jp/e/"
            ),
        ],
    },


    "Osaka": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Osaka Metro",
                "Convenient for central Osaka."
            ),
            (
                "🚆",
                "RAIL",
                "JR West",
                "Useful for regional and city travel."
            ),
            (
                "🚕",
                "TAXI",
                "Local Taxi",
                "Useful for direct short journeys."
            ),
        ],
        "apps": [
            (
                "Osaka Metro",
                "https://www.osakametro.co.jp/en/"
            ),
            (
                "JR West",
                "https://www.westjr.co.jp/global/en/"
            ),
        ],
    },


    "Kyoto": {
        "transport": [
            (
                "🚌",
                "BUS",
                "Kyoto City Bus",
                "Important for many tourist areas."
            ),
            (
                "🚆",
                "RAIL",
                "JR / Private Rail",
                "Useful for longer city and regional trips."
            ),
            (
                "🚇",
                "SUBWAY",
                "Kyoto Subway",
                "Useful for selected central corridors."
            ),
        ],
        "apps": [
            (
                "Kyoto City Transportation",
                "https://www2.city.kyoto.lg.jp/koho/eng/"
            ),
            (
                "JR West",
                "https://www.westjr.co.jp/global/en/"
            ),
        ],
    },


    # --------------------------------------------------------
    # SINGAPORE
    # --------------------------------------------------------

    "Singapore": {
        "transport": [
            (
                "🚇",
                "MRT",
                "Singapore MRT",
                "Fast and efficient option for most city journeys."
            ),
            (
                "🚌",
                "BUS",
                "Singapore Bus Network",
                "Extensive coverage across neighbourhoods."
            ),
            (
                "🚕",
                "RIDE-HAILING",
                "Grab",
                "Useful for direct point-to-point travel."
            ),
        ],
        "apps": [
            (
                "SMRT",
                "https://www.smrt.com.sg/"
            ),
            (
                "Grab",
                "https://www.grab.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # UNITED KINGDOM
    # --------------------------------------------------------

    "London": {
        "transport": [
            (
                "🚇",
                "UNDERGROUND",
                "London Underground",
                "One of the easiest ways to move around central London."
            ),
            (
                "🚌",
                "BUS",
                "London Buses",
                "Extensive coverage across Greater London."
            ),
            (
                "🚆",
                "RAIL",
                "National Rail",
                "Useful for journeys across London and beyond."
            ),
        ],
        "apps": [
            (
                "Transport for London",
                "https://tfl.gov.uk/"
            ),
            (
                "National Rail",
                "https://www.nationalrail.co.uk/"
            ),
        ],
    },


    "Manchester": {
        "transport": [
            (
                "🚊",
                "TRAM",
                "Metrolink",
                "Convenient for major areas across Greater Manchester."
            ),
            (
                "🚌",
                "BUS",
                "Bee Network",
                "Large bus network covering Greater Manchester."
            ),
            (
                "🚆",
                "RAIL",
                "National Rail",
                "Useful for regional and intercity journeys."
            ),
        ],
        "apps": [
            (
                "Bee Network",
                "https://tfgm.com/"
            ),
            (
                "National Rail",
                "https://www.nationalrail.co.uk/"
            ),
        ],
    },


    # --------------------------------------------------------
    # FRANCE
    # --------------------------------------------------------

    "Paris": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Paris Métro",
                "Fast and practical for central Paris."
            ),
            (
                "🚆",
                "RER",
                "RER",
                "Useful for longer journeys across the Paris region."
            ),
            (
                "🚌",
                "BUS",
                "RATP Bus",
                "Useful for neighbourhood-level travel."
            ),
        ],
        "apps": [
            (
                "RATP",
                "https://www.ratp.fr/"
            ),
            (
                "Île-de-France Mobilités",
                "https://www.iledefrance-mobilites.fr/"
            ),
        ],
    },


    # --------------------------------------------------------
    # ITALY
    # --------------------------------------------------------

    "Rome": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Rome Metro",
                "Useful for major tourist and central corridors."
            ),
            (
                "🚌",
                "BUS",
                "ATAC Bus",
                "Extensive bus network across Rome."
            ),
            (
                "🚆",
                "RAIL",
                "Regional Rail",
                "Useful for longer journeys around Rome."
            ),
        ],
        "apps": [
            (
                "ATAC Roma",
                "https://www.atac.roma.it/"
            ),
            (
                "Trenitalia",
                "https://www.trenitalia.com/"
            ),
        ],
    },


    "Milan": {
        "transport": [
            (
                "🚇",
                "METRO",
                "Milan Metro",
                "Fast option for central and suburban journeys."
            ),
            (
                "🚋",
                "TRAM",
                "Milan Trams",
                "Useful for neighbourhood-level city travel."
            ),
            (
                "🚆",
                "RAIL",
                "Trenord",
                "Useful for regional and airport-related journeys."
            ),
        ],
        "apps": [
            (
                "ATM Milano",
                "https://www.atm.it/"
            ),
            (
                "Trenord",
                "https://www.trenord.it/"
            ),
        ],
    },


    # --------------------------------------------------------
    # USA
    # --------------------------------------------------------

    "New York": {
        "transport": [
            (
                "🚇",
                "SUBWAY",
                "New York City Subway",
                "The main public transport network for city-wide travel."
            ),
            (
                "🚌",
                "BUS",
                "MTA Bus",
                "Useful for neighbourhood-level coverage."
            ),
            (
                "🚕",
                "TAXI",
                "Yellow Taxi",
                "Convenient for direct trips around the city."
            ),
        ],
        "apps": [
            (
                "MTA",
                "https://new.mta.info/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    "Los Angeles": {
        "transport": [
            (
                "🚇",
                "METRO",
                "LA Metro",
                "Useful across major rail corridors."
            ),
            (
                "🚌",
                "BUS",
                "Metro Bus",
                "Extensive bus coverage across Los Angeles County."
            ),
            (
                "🚗",
                "RIDE-HAILING",
                "Uber / Lyft",
                "Useful for direct journeys across the spread-out city."
            ),
        ],
        "apps": [
            (
                "LA Metro",
                "https://www.metro.net/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # AUSTRALIA
    # --------------------------------------------------------

    "Sydney": {
        "transport": [
            (
                "🚆",
                "RAIL",
                "Sydney Trains",
                "Useful for major city and suburban journeys."
            ),
            (
                "🚋",
                "LIGHT RAIL",
                "Sydney Light Rail",
                "Useful for selected central and inner-city routes."
            ),
            (
                "🚌",
                "BUS",
                "Sydney Buses",
                "Extensive coverage across Sydney."
            ),
        ],
        "apps": [
            (
                "Transport for NSW",
                "https://transportnsw.info/"
            ),
            (
                "Uber",
                "https://www.uber.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # GERMANY
    # --------------------------------------------------------

    "Berlin": {
        "transport": [
            (
                "🚇",
                "U-BAHN",
                "Berlin U-Bahn",
                "Fast way to travel across central Berlin."
            ),
            (
                "🚆",
                "S-BAHN",
                "Berlin S-Bahn",
                "Useful for cross-city and suburban journeys."
            ),
            (
                "🚌",
                "BUS",
                "Berlin Bus",
                "Useful for neighbourhood-level travel."
            ),
        ],
        "apps": [
            (
                "BVG",
                "https://www.bvg.de/en"
            ),
            (
                "Deutsche Bahn",
                "https://int.bahn.de/en"
            ),
        ],
    },


    # --------------------------------------------------------
    # CANADA
    # --------------------------------------------------------

    "Toronto": {
        "transport": [
            (
                "🚇",
                "SUBWAY",
                "TTC Subway",
                "Fast option for major Toronto corridors."
            ),
            (
                "🚋",
                "STREETCAR",
                "TTC Streetcar",
                "Useful for many central neighbourhoods."
            ),
            (
                "🚌",
                "BUS",
                "TTC Bus",
                "Extensive coverage across Toronto."
            ),
        ],
        "apps": [
            (
                "TTC",
                "https://www.ttc.ca/"
            ),
            (
                "GO Transit",
                "https://www.gotransit.com/"
            ),
        ],
    },


    # --------------------------------------------------------
    # NETHERLANDS
    # --------------------------------------------------------

    "Amsterdam": {
        "transport": [
            (
                "🚋",
                "TRAM",
                "Amsterdam Tram",
                "One of the most practical ways to move around central Amsterdam."
            ),
            (
                "🚆",
                "RAIL",
                "NS",
                "Useful for city, airport and intercity journeys."
            ),
            (
                "🚲",
                "CYCLING",
                "Cycling",
                "A major part of everyday travel across Amsterdam."
            ),
        ],
        "apps": [
            (
                "GVB",
                "https://www.gvb.nl/en"
            ),
            (
                "NS",
                "https://www.ns.nl/en"
            ),
        ],
    },
}


# ============================================================
# DEFAULT DATA
# ============================================================

DEFAULT_DATA = {
    "transport": [
        (
            "🚇",
            "PUBLIC TRANSPORT",
            "Metro / Rail",
            "Check the city's official transport network for routes and fares."
        ),
        (
            "🚕",
            "TAXI / RIDE-HAILING",
            "Local Taxi / Ride Service",
            "Useful for direct point-to-point travel."
        ),
        (
            "🚌",
            "BUS",
            "City Bus",
            "Useful for neighbourhood-level coverage."
        ),
    ],
    "apps": [],
}


# ============================================================
# SELECT CITY DATA
# ============================================================

data = TRANSPORT_DATA.get(
    city,
    DEFAULT_DATA,
)


# ============================================================
# HEADER
# ============================================================

st.html(
    f"""
    <div style="
        padding: 8px 0 24px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 28px;
    ">

        <div style="
            color:#6ea8ff;
            font-size:12px;
            font-weight:700;
            letter-spacing:2px;
            margin-bottom:10px;
        ">
            MOVE • {country.upper()}
        </div>

        <h1 style="
            margin:0;
            font-size:42px;
            line-height:1.1;
            font-weight:700;
            color:#f5f7fb;
        ">
            Move around {city}.
        </h1>

        <p style="
            margin:12px 0 0 0;
            color:#9299a8;
            font-size:16px;
            line-height:1.6;
        ">
            Navigate the city using the transport options
            locals and visitors are most likely to need.
        </p>

    </div>
    """
)


# ============================================================
# STATS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Transport options",
        len(data["transport"])
    )


with col2:

    st.metric(
        "Useful services",
        len(data["apps"])
    )


with col3:

    st.metric(
        "City",
        city
    )


# ============================================================
# SPACING
# ============================================================

st.html(
    "<div style='height:12px;'></div>"
)


# ============================================================
# GETTING AROUND HEADER
# ============================================================

st.html(
    """
    <div style="
        margin:10px 0 18px 0;
        color:#f5f7fb;
        font-size:22px;
        font-weight:650;
    ">
        Getting around
    </div>
    """
)


# ============================================================
# TRANSPORT CARDS
# ============================================================

for icon, category, name, description in data["transport"]:

    st.html(
        f"""
        <div style="
            padding:20px;
            margin-bottom:14px;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:14px;
            background:rgba(255,255,255,0.025);
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:14px;
            ">

                <div style="
                    width:46px;
                    height:46px;
                    min-width:46px;
                    border-radius:12px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:rgba(110,168,255,0.10);
                    font-size:23px;
                ">
                    {icon}
                </div>

                <div>

                    <div style="
                        color:#707989;
                        font-size:11px;
                        font-weight:700;
                        letter-spacing:1.5px;
                        text-transform:uppercase;
                        margin-bottom:4px;
                    ">
                        {category}
                    </div>

                    <div style="
                        color:#f5f7fb;
                        font-size:18px;
                        font-weight:650;
                    ">
                        {name}
                    </div>

                    <div style="
                        color:#8d95a5;
                        font-size:13px;
                        margin-top:5px;
                        line-height:1.5;
                    ">
                        {description}
                    </div>

                </div>

            </div>

        </div>
        """
    )


# ============================================================
# USEFUL SERVICES
# ============================================================

if data["apps"]:

    st.html(
        """
        <div style="
            margin:32px 0 18px 0;
            color:#f5f7fb;
            font-size:22px;
            font-weight:650;
        ">
            Useful services
        </div>
        """
    )

    app_cols = st.columns(
        len(data["apps"])
    )

    for index, (name, url) in enumerate(
        data["apps"]
    ):

        with app_cols[index]:

            st.html(
                f"""
                <a href="{url}" target="_blank" style="
                    text-decoration:none;
                    display:block;
                    padding:20px;
                    min-height:105px;
                    border:1px solid rgba(255,255,255,0.08);
                    border-radius:14px;
                    background:rgba(255,255,255,0.025);
                    box-sizing:border-box;
                ">

                    <div style="
                        color:#f5f7fb;
                        font-size:16px;
                        font-weight:650;
                        margin-bottom:8px;
                    ">
                        {name}
                    </div>

                    <div style="
                        color:#6ea8ff;
                        font-size:12px;
                    ">
                        Open official service ↗
                    </div>

                </a>
                """
            )


# ============================================================
# NOMIA TIP
# ============================================================

st.html(
    f"""
    <div style="
        margin-top:32px;
        padding:20px;
        border-left:3px solid #6ea8ff;
        border-radius:8px;
        background:rgba(110,168,255,0.055);
    ">

        <div style="
            color:#6ea8ff;
            font-size:11px;
            font-weight:700;
            letter-spacing:1.5px;
            margin-bottom:8px;
        ">
            NOMIA TIP
        </div>

        <div style="
            color:#aeb5c2;
            font-size:14px;
            line-height:1.65;
        ">
            Transport availability, routes, fares and operating hours
            can change. Check the official service before making an
            important journey.
        </div>

    </div>
    """
)