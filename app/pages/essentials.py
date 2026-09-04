import time
from urllib.parse import quote_plus

import requests
import streamlit as st

from data.cities.catalog import get_city


# =========================================================
# CONFIG
# =========================================================

# Multiple public Overpass instances.
# If one is unavailable/overloaded, NOMIA automatically tries
# the next one.
OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
]

# Primary search radius around the city centre.
SEARCH_RADIUS = 8000

# Fallback radius if the first successful query returns no
# useful named locations.
FALLBACK_RADIUS = 12000

# Maximum locations displayed per category.
MAX_RESULTS = 5

# Request timeout for each Overpass server.
REQUEST_TIMEOUT = 75

# Number of retries for temporary server errors.
MAX_RETRIES = 2

# Short pause between retries.
RETRY_DELAY = 2


# =========================================================
# CATEGORY CONFIG
# =========================================================

CATEGORIES = {
    "Hospitals": {
        "icon": "🏥",
        "description": "Hospitals and medical facilities",
    },

    "Pharmacies": {
        "icon": "💊",
        "description": "Pharmacies and healthcare access",
    },

    "ATMs & Banking": {
        "icon": "🏧",
        "description": "ATMs and cash access",
    },

    "Transport": {
        "icon": "🚉",
        "description": "Major public transport connections",
    },

    "Connectivity": {
        "icon": "📶",
        "description": "Mobile phone and connectivity stores",
    },

    "Everyday stores": {
        "icon": "🏪",
        "description": "Convenience stores and everyday shopping",
    },
}


# =========================================================
# CITY-SPECIFIC PRACTICAL TIPS
# =========================================================

LOCAL_TIPS = {

    "Delhi": [
        "Delhi Metro is one of the most useful ways to move around the city.",
        "Keep some cash for smaller local markets and shops.",
        "Distances can be large, so check the area before planning multiple stops.",
    ],

    "Mumbai": [
        "Local trains can be extremely useful for crossing Mumbai quickly.",
        "Traffic can significantly affect road travel times.",
        "Keep your accommodation's exact neighbourhood in mind when planning trips.",
    ],

    "Bengaluru": [
        "Traffic can be heavy, particularly during peak hours.",
        "Metro connectivity is useful on several major corridors.",
        "Check travel time before committing to cross-city plans.",
    ],

    "Dubai": [
        "Dubai Metro is useful for several major visitor areas.",
        "Distances between districts can be significant.",
        "Check transport options before choosing accommodation far from your main activities.",
    ],

    "Abu Dhabi": [
        "The city is spread out, so check distances before planning multiple stops.",
        "Taxis are widely used for areas not convenient by public transport.",
        "Keep your accommodation location handy when planning daily routes.",
    ],

    "Tokyo": [
        "Rail is usually the most practical way to move around Tokyo.",
        "Convenience stores are widely available for everyday travel needs.",
        "Keep your accommodation address available when navigating unfamiliar areas.",
    ],

    "Osaka": [
        "Osaka's railway and metro network covers most major visitor areas.",
        "Keep your hotel address handy when navigating unfamiliar areas.",
        "Convenience stores are widely available for basic everyday needs.",
    ],

    "Kyoto": [
        "Public transport is useful, but some sightseeing routes are easiest on foot.",
        "Kyoto can become crowded around major attractions.",
        "Check the last public transport service when planning evening trips.",
    ],

    "Singapore": [
        "Singapore's MRT is one of the easiest ways to move around the city.",
        "The city is compact, so combining MRT and walking often works well.",
        "Keep a small amount of cash available even though contactless payments are widely useful.",
    ],

    "London": [
        "The Underground and rail network are usually practical for crossing the city.",
        "Contactless payment is useful across much of London's public transport network.",
        "London is large, so group activities by neighbourhood where possible.",
    ],

    "Manchester": [
        "Metrolink is useful for several major areas around Manchester.",
        "The city centre is compact and many attractions can be reached on foot.",
        "Check transport schedules when planning trips outside the centre.",
    ],

    "Paris": [
        "The Paris Metro is usually the fastest practical option for many central journeys.",
        "Many central areas are walkable, so combine Metro rides with walking where convenient.",
        "Keep your accommodation address available when navigating unfamiliar neighbourhoods.",
    ],

    "Rome": [
        "Many central attractions are close enough to combine by walking.",
        "Public transport can help when travelling between distant neighbourhoods.",
        "Crowded tourist areas require extra awareness of your belongings.",
    ],

    "Milan": [
        "Milan's Metro and tram network is useful for moving around the city.",
        "Central Milan can often be explored efficiently on foot.",
        "Check transport times before travelling outside the central districts.",
    ],

    "New York": [
        "The subway is usually the most practical way to cover long distances around New York.",
        "Keep your accommodation address and nearest subway station handy.",
        "Walking is often the easiest way to move between nearby neighbourhood attractions.",
    ],

    "Los Angeles": [
        "Los Angeles is geographically spread out, so check travel times carefully.",
        "Group activities by area to avoid unnecessary cross-city travel.",
        "Public transport is useful on several major corridors.",
    ],

    "Sydney": [
        "Trains, buses and ferries can cover many major visitor areas.",
        "Sydney's geography makes checking travel times useful before planning multiple stops.",
        "Keep your accommodation location handy when switching between transport modes.",
    ],

    "Berlin": [
        "Berlin's U-Bahn, S-Bahn and tram network is useful for most major visitor areas.",
        "Some smaller shops may have different opening schedules than large retail centres.",
        "Check the final transport connection when planning late journeys.",
    ],

    "Toronto": [
        "TTC services cover many central and major visitor areas.",
        "Toronto is spread out, so check travel time before combining distant neighbourhoods.",
        "Keep your accommodation address available when navigating unfamiliar areas.",
    ],

    "Amsterdam": [
        "Trams, metro and walking are useful for many central Amsterdam journeys.",
        "The historic centre is compact, making walking practical for many attractions.",
        "Stay alert around cycle lanes and crossings because cycling is a major part of the city's transport environment.",
    ],
}


# =========================================================
# OSM QUERY
# =========================================================

def build_overpass_query(lat, lon, radius):
    """
    Build one combined Overpass query for all NOMIA
    essentials categories.

    nwr = nodes + ways + relations.
    out center gives ways/relations a representative
    coordinate.
    """

    return f"""
[out:json][timeout:60];

(
    nwr["amenity"="hospital"](around:{radius},{lat},{lon});

    nwr["amenity"="pharmacy"](around:{radius},{lat},{lon});

    nwr["amenity"="atm"](around:{radius},{lat},{lon});
    nwr["amenity"="bank"](around:{radius},{lat},{lon});

    nwr["railway"="station"](around:{radius},{lat},{lon});
    nwr["railway"="halt"](around:{radius},{lat},{lon});
    nwr["amenity"="bus_station"](around:{radius},{lat},{lon});

    nwr["shop"="mobile_phone"](around:{radius},{lat},{lon});
    nwr["shop"="electronics"]["name"](around:{radius},{lat},{lon});

    nwr["shop"="convenience"](around:{radius},{lat},{lon});
    nwr["shop"="supermarket"](around:{radius},{lat},{lon});
);

out center tags;
"""


# =========================================================
# ADDRESS BUILDER
# =========================================================

def build_address(tags, city):
    """
    Build the best available human-readable address
    from OpenStreetMap address tags.
    """

    parts = []

    housenumber = tags.get("addr:housenumber", "").strip()
    street = tags.get("addr:street", "").strip()
    suburb = tags.get("addr:suburb", "").strip()
    district = tags.get("addr:district", "").strip()
    postcode = tags.get("addr:postcode", "").strip()

    if housenumber and street:
        parts.append(f"{housenumber} {street}")

    elif street:
        parts.append(street)

    if suburb:
        parts.append(suburb)

    elif district:
        parts.append(district)

    if postcode:
        parts.append(postcode)

    if parts:
        return ", ".join(parts)

    locality = (
        tags.get("addr:place")
        or tags.get("place")
        or tags.get("description")
    )

    if locality:
        return locality

    return f"{city} · Address not listed in OpenStreetMap"


# =========================================================
# COORDINATE EXTRACTION
# =========================================================

def get_element_coordinates(element):
    """
    Extract coordinates from an OSM node / way / relation.
    """

    if element.get("type") == "node":
        return (
            element.get("lat"),
            element.get("lon"),
        )

    center = element.get("center", {})

    return (
        center.get("lat"),
        center.get("lon"),
    )


# =========================================================
# CATEGORY CLASSIFICATION
# =========================================================

def classify_element(tags):
    """
    Convert raw OSM tags into one NOMIA category.
    """

    amenity = tags.get("amenity")
    railway = tags.get("railway")
    shop = tags.get("shop")

    name = tags.get("name", "")
    name_lower = name.lower()

    # -----------------------------------------------------
    # HOSPITAL
    # -----------------------------------------------------

    if amenity == "hospital":
        return "Hospitals"

    # -----------------------------------------------------
    # PHARMACY
    # -----------------------------------------------------

    if amenity == "pharmacy":
        return "Pharmacies"

    # -----------------------------------------------------
    # ATM / BANK
    # -----------------------------------------------------

    if amenity in {"atm", "bank"}:
        return "ATMs & Banking"

    # -----------------------------------------------------
    # TRANSPORT
    # -----------------------------------------------------

    if (
        railway in {"station", "halt"}
        or amenity == "bus_station"
    ):
        return "Transport"

    # -----------------------------------------------------
    # CONNECTIVITY
    # -----------------------------------------------------

    if shop == "mobile_phone":
        return "Connectivity"

    if shop == "electronics" and (
        "mobile" in name_lower
        or "phone" in name_lower
        or "telecom" in name_lower
    ):
        return "Connectivity"

    # -----------------------------------------------------
    # EVERYDAY STORES
    # -----------------------------------------------------

    if shop in {"convenience", "supermarket"}:
        return "Everyday stores"

    return None


# =========================================================
# PROCESS OSM RESPONSE
# =========================================================

def process_osm_payload(payload, city):
    """
    Convert raw Overpass JSON into NOMIA's category structure.
    """

    elements = payload.get("elements", [])

    results = {
        category: []
        for category in CATEGORIES
    }

    seen = {
        category: set()
        for category in CATEGORIES
    }

    for element in elements:

        tags = element.get("tags", {})

        name = tags.get("name")

        # We only show named locations.
        if not name:
            continue

        lat_value, lon_value = get_element_coordinates(element)

        if lat_value is None or lon_value is None:
            continue

        category = classify_element(tags)

        if category is None:
            continue

        try:
            lat_value = float(lat_value)
            lon_value = float(lon_value)
        except (TypeError, ValueError):
            continue

        name_lower = name.strip().lower()

        unique_key = (
            category,
            name_lower,
            round(lat_value, 5),
            round(lon_value, 5),
        )

        if unique_key in seen[category]:
            continue

        seen[category].add(unique_key)

        address = build_address(tags, city)

        results[category].append(
            {
                "name": name.strip(),
                "address": address,
                "lat": lat_value,
                "lon": lon_value,
                "type": (
                    tags.get("amenity")
                    or tags.get("shop")
                    or tags.get("railway")
                    or ""
                ),
            }
        )

    # -----------------------------------------------------
    # Limit results per category
    # -----------------------------------------------------

    for category in results:

        # Sort alphabetically for stable presentation.
        results[category].sort(
            key=lambda item: item["name"].lower()
        )

        results[category] = results[category][:MAX_RESULTS]

    return results


# =========================================================
# SINGLE OVERPASS REQUEST
# =========================================================

def request_overpass(url, query):
    """
    Perform one Overpass request with retry handling.
    """

    headers = {
        "User-Agent": (
            "NOMIA-Travel-Intelligence/1.0 "
            "(OpenStreetMap data consumer)"
        ),
        "Accept": "application/json",
    }

    last_error = None

    for attempt in range(MAX_RETRIES + 1):

        try:

            response = requests.post(
                url,
                data={"data": query},
                headers=headers,
                timeout=REQUEST_TIMEOUT,
            )

            # Temporary / rate-limit server errors.
            if response.status_code in {
                429,
                502,
                503,
                504,
            }:

                last_error = RuntimeError(
                    f"HTTP {response.status_code}"
                )

                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
                    continue

                raise last_error

            response.raise_for_status()

            payload = response.json()

            if not isinstance(payload, dict):
                raise ValueError(
                    "Overpass returned an unexpected response."
                )

            return payload

        except requests.RequestException as exc:

            last_error = exc

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue

            raise

        except ValueError as exc:

            last_error = exc

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue

            raise

    raise RuntimeError(
        f"Overpass request failed: {last_error}"
    )


# =========================================================
# FETCH FROM MULTIPLE OVERPASS SERVERS
# =========================================================

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_essential_locations(city, lat, lon):
    """
    Fetch real-world essential locations around the city
    using OpenStreetMap Overpass.

    Important:
    Exceptions are raised if every endpoint fails.
    This prevents a temporary API outage from being cached
    as an empty result for 24 hours.
    """

    errors = []

    # -----------------------------------------------------
    # PASS 1
    # Primary radius
    # -----------------------------------------------------

    query = build_overpass_query(
        lat=lat,
        lon=lon,
        radius=SEARCH_RADIUS,
    )

    for endpoint in OVERPASS_URLS:

        try:

            payload = request_overpass(
                endpoint,
                query,
            )

            results = process_osm_payload(
                payload,
                city,
            )

            total = sum(
                len(items)
                for items in results.values()
            )

            # A successful response with useful locations.
            if total > 0:
                return results

            # Successful API response but no useful named
            # locations. Try a wider radius next.
            errors.append(
                f"{endpoint}: response contained no named locations"
            )

        except Exception as exc:

            errors.append(
                f"{endpoint}: {str(exc)}"
            )

    # -----------------------------------------------------
    # PASS 2
    # Wider radius
    # -----------------------------------------------------

    fallback_query = build_overpass_query(
        lat=lat,
        lon=lon,
        radius=FALLBACK_RADIUS,
    )

    for endpoint in OVERPASS_URLS:

        try:

            payload = request_overpass(
                endpoint,
                fallback_query,
            )

            results = process_osm_payload(
                payload,
                city,
            )

            total = sum(
                len(items)
                for items in results.values()
            )

            if total > 0:
                return results

            errors.append(
                f"{endpoint}: wider search also returned no named locations"
            )

        except Exception as exc:

            errors.append(
                f"{endpoint}: wider search failed - {str(exc)}"
            )

    # -----------------------------------------------------
    # Everything failed
    # -----------------------------------------------------

    error_summary = "\n".join(
        f"• {error}"
        for error in errors[-8:]
    )

    raise RuntimeError(
        "NOMIA could not retrieve OpenStreetMap locations "
        "from the available Overpass servers.\n\n"
        f"{error_summary}"
    )


# =========================================================
# DIRECTIONS
# =========================================================

def directions_url(name, lat, lon):
    """
    Google Maps directions/search URL.
    """

    destination = quote_plus(
        f"{name} {lat},{lon}"
    )

    return (
        "https://www.google.com/maps/dir/?api=1"
        f"&destination={destination}"
    )


# =========================================================
# CURRENT CITY
# =========================================================

city = st.session_state.get(
    "city",
    "Delhi",
)

city_info = get_city(city)

if not city_info:

    st.warning(
        f"City information for {city} is not available yet."
    )

    st.stop()


country = city_info.get(
    "country",
    "India",
)

st.session_state["country"] = country

coordinates = city_info.get(
    "coordinates",
    {},
)

city_lat = coordinates.get("lat")
city_lon = coordinates.get("lon")

if city_lat is None or city_lon is None:

    st.error(
        "NOMIA could not find coordinates for this city."
    )

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.html(
    f"""
    <div style="
        padding:30px 0 20px 0;
        margin-top:10px;
    ">

        <div style="
            color:#60a5fa;
            font-size:12px;
            font-weight:700;
            letter-spacing:.16em;
        ">
            CITY ESSENTIALS
        </div>

        <h1 style="
            font-size:48px;
            margin:10px 0 0 0;
            font-weight:750;
            color:#f5f7fa;
        ">
            Be ready for {city}.
        </h1>

        <p style="
            color:#8f9aaa;
            font-size:16px;
            margin-top:10px;
        ">
            Real essential locations around your city.
        </p>

    </div>
    """
)


# =========================================================
# LOAD OSM DATA
# =========================================================

locations = None
fetch_error = None

with st.spinner(
    f"Finding essential locations around {city}..."
):

    try:

        locations = fetch_essential_locations(
            city,
            city_lat,
            city_lon,
        )

    except Exception as exc:

        fetch_error = str(exc)

        locations = {
            category: []
            for category in CATEGORIES
        }


# =========================================================
# API ERROR STATE
# =========================================================

if fetch_error:

    st.error(
        "NOMIA could not load live OpenStreetMap locations right now."
    )

    st.caption(
        "The page itself is working. The external map-data "
        "service did not return usable results."
    )

    with st.expander("Technical details"):

        st.code(
            fetch_error,
            language="text",
        )


# =========================================================
# STATS
# =========================================================

total_locations = sum(
    len(items)
    for items in locations.values()
)

categories_found = sum(
    1
    for items in locations.values()
    if items
)

tips = LOCAL_TIPS.get(
    city,
    [
        "Always verify opening hours and service availability before visiting.",
        "Check travel time before planning multiple stops.",
        "Keep your accommodation address available when navigating unfamiliar areas.",
    ],
)


c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "Locations found",
        total_locations,
    )


with c2:

    st.metric(
        "Categories",
        categories_found,
    )


with c3:

    st.metric(
        "City",
        city,
    )


st.divider()


# =========================================================
# ESSENTIAL LOCATIONS
# =========================================================

st.html(
    """
    <h2 style="margin-bottom:8px;">
        🧭 What you may need
    </h2>

    <p style="
        color:#8f9aaa;
        font-size:14px;
        margin-top:0;
        margin-bottom:22px;
    ">
        Real places discovered from OpenStreetMap around your city centre.
    </p>
    """
)


# =========================================================
# CATEGORY SECTIONS
# =========================================================

for category, config in CATEGORIES.items():

    category_locations = locations.get(
        category,
        [],
    )

    icon = config["icon"]
    description = config["description"]

    # -----------------------------------------------------
    # CATEGORY HEADER
    # -----------------------------------------------------

    st.html(
        f"""
        <div style="
            margin-top:24px;
            margin-bottom:16px;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:10px;
            ">

                <span style="font-size:22px;">
                    {icon}
                </span>

                <span style="
                    color:#f5f7fa;
                    font-size:22px;
                    font-weight:700;
                ">
                    {category}
                </span>

                <span style="
                    color:#71849d;
                    font-size:13px;
                ">
                    {len(category_locations)} found
                </span>

            </div>

            <div style="
                color:#71849d;
                font-size:13px;
                margin-top:5px;
            ">
                {description}
            </div>

        </div>
        """
    )


    # -----------------------------------------------------
    # LOCATIONS
    # -----------------------------------------------------

    if category_locations:

        cols = st.columns(2)

        for i, place in enumerate(
            category_locations
        ):

            with cols[i % 2]:

                name = place["name"]
                address = place["address"]
                lat = place["lat"]
                lon = place["lon"]

                st.html(
                    f"""
                    <div style="
                        border:1px solid #202630;
                        border-radius:16px;
                        padding:20px;
                        min-height:145px;
                        margin-bottom:14px;
                        background:rgba(10,14,20,0.45);
                    ">

                        <div style="
                            color:#f5f7fa;
                            font-size:18px;
                            font-weight:700;
                            line-height:1.35;
                        ">
                            {name}
                        </div>

                        <div style="
                            color:#91a4bd;
                            font-size:13px;
                            line-height:1.5;
                            margin-top:10px;
                        ">
                            📍 {address}
                        </div>

                    </div>
                    """
                )

                st.link_button(
                    "Directions ↗",
                    directions_url(
                        name,
                        lat,
                        lon,
                    ),
                    use_container_width=True,
                )

    else:

        if fetch_error:

            empty_message = (
                "Live location data could not be loaded "
                "from OpenStreetMap right now."
            )

        else:

            empty_message = (
                f"No named {category.lower()} locations were "
                "returned by OpenStreetMap around the selected city."
            )

        st.html(
            f"""
            <div style="
                border:1px solid #202630;
                border-radius:14px;
                padding:16px 18px;
                margin-bottom:18px;
                color:#71849d;
                font-size:13px;
                background:rgba(10,14,20,0.25);
            ">

                {empty_message}

            </div>
            """
        )


st.divider()


# =========================================================
# NOMIA LOCAL KNOWLEDGE
# =========================================================

st.html(
    """
    <h2 style="margin-bottom:18px;">
        💡 NOMIA local knowledge
    </h2>
    """
)


for tip in tips:

    st.info(tip)


# =========================================================
# DATA SOURCE NOTE
# =========================================================

st.html(
    """
    <div style="
        margin-top:28px;
        padding:16px 18px;
        border:1px solid rgba(96,165,250,.15);
        border-radius:12px;
        background:rgba(96,165,250,.04);
        color:#71849d;
        font-size:12px;
        line-height:1.6;
    ">

        <strong style="color:#91a4bd;">
            Location data
        </strong><br>

        Essential places are discovered from OpenStreetMap.
        NOMIA automatically uses available Overpass servers
        and caches successful results for 24 hours.

        Availability, opening hours and business details can change,
        so verify important information before travelling.

    </div>
    """
)


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div style="
        margin-top:20px;
        padding:18px;
        border:1px solid #202630;
        border-radius:14px;
        color:#71849d;
        font-size:13px;
    ">

        NOMIA provides a starting layer for local discovery.
        Always verify current opening hours, transport schedules
        and service availability before travelling.

    </div>
    """
)