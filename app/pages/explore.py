import streamlit as st
import folium
from streamlit_folium import st_folium

from data.cities.catalog import (
    get_city,
    get_coordinates,
    get_attractions,
    get_shopping,
)


# ─────────────────────────────────────────────
# CURRENT DESTINATION
# ─────────────────────────────────────────────

country = st.session_state.get("country", "India")
city = st.session_state.get("city", "Delhi")

city_data = get_city(city)

# Safety fallback
if not city_data:
    city = "Delhi"
    country = "India"
    city_data = get_city(city)

if not city_data:
    st.error("City data could not be loaded.")
    st.stop()

# Always use the country stored in the central catalog
country = city_data.get("country", country)

coordinates = get_coordinates(city)

if not coordinates:
    st.error(f"Coordinates unavailable for {city}.")
    st.stop()

lat = coordinates["lat"]
lon = coordinates["lon"]


# ─────────────────────────────────────────────
# CONVERT CATALOG ITEMS
# ─────────────────────────────────────────────

def normalize_place(item, category):
    """
    Convert the current NOMIA catalog format into
    the internal structure used by Explore.

    Current catalog stores places as simple strings,
    e.g. "Big Ben", "Oxford Street".
    """

    # Current catalog format
    if isinstance(item, str):

        return {
            "name": item,
            "category": category,
            "description": f"{item} in {city}.",
            "lat": None,
            "lon": None,
        }

    # Future-proof support if catalog entries
    # are later upgraded to dictionaries.
    if isinstance(item, dict):

        name = item.get(
            "name",
            "Unknown place",
        )

        description = item.get(
            "description",
            f"{name} in {city}.",
        )

        item_lat = item.get("lat")
        item_lon = item.get("lon")

        return {
            "name": name,
            "category": item.get(
                "category",
                category,
            ),
            "description": description,
            "lat": item_lat,
            "lon": item_lon,
        }

    return None


# ─────────────────────────────────────────────
# LOAD CITY CONTENT
# ─────────────────────────────────────────────

attractions = get_attractions(city)
shopping = get_shopping(city)

places = []

for item in attractions:

    place = normalize_place(
        item,
        "Attraction",
    )

    if place:
        places.append(place)


for item in shopping:

    place = normalize_place(
        item,
        "Shopping",
    )

    if place:
        places.append(place)


# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────

st.html(
    f"""
    <div style="
        padding:25px 0 15px 0;
    ">

        <div style="
            color:#60a5fa;
            font-size:12px;
            font-weight:600;
            letter-spacing:.15em;
            margin-bottom:10px;
        ">
            CITY INTELLIGENCE
        </div>

        <h1 style="
            font-size:48px;
            margin:0;
            font-weight:750;
            color:#f5f7fa;
        ">
            {city}
        </h1>

        <p style="
            color:#8f9aaa;
            font-size:16px;
            margin-top:10px;
        ">
            {country} · Explore the city through NOMIA
        </p>

    </div>
    """
)


# ─────────────────────────────────────────────
# CITY DESCRIPTION
# ─────────────────────────────────────────────

description = city_data.get(
    "description",
    f"Explore {city} through NOMIA's local intelligence layer.",
)

st.html(
    f"""
    <div style="
        padding:16px 18px;
        margin-bottom:18px;
        border-left:3px solid #60a5fa;
        border-radius:8px;
        background:rgba(96,165,250,.045);
        color:#aab3c2;
        font-size:14px;
        line-height:1.6;
    ">
        {description}
    </div>
    """
)


# ─────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────

col1, col2, col3, col4 = st.columns(4)

categories = set(
    place["category"]
    for place in places
)

stats = [
    ("📍", "Places", len(places)),
    ("🏛️", "Categories", len(categories)),
    ("🌍", "Country", country),
    ("🗺️", "Map", "Live"),
]

for column, (icon, label, value) in zip(
    [col1, col2, col3, col4],
    stats,
):

    with column:

        st.html(
            f"""
            <div style="
                padding:18px;
                border:1px solid rgba(255,255,255,.08);
                border-radius:14px;
                background:rgba(255,255,255,.025);
            ">

                <div style="
                    font-size:22px;
                ">
                    {icon}
                </div>

                <div style="
                    font-size:12px;
                    color:#7d8795;
                    margin-top:10px;
                ">
                    {label}
                </div>

                <div style="
                    font-size:20px;
                    font-weight:700;
                    margin-top:4px;
                ">
                    {value}
                </div>

            </div>
            """
        )


st.html("<br>")


# ─────────────────────────────────────────────
# FILTERS
# ─────────────────────────────────────────────

map_col, control_col = st.columns([2.2, 1])

with control_col:

    st.markdown("### Discover")

    category_options = [
        "All"
    ] + sorted(categories)

    selected_category = st.selectbox(
        "Category",
        category_options,
    )

    search = st.text_input(
        "Search places",
        placeholder=f"Search {city}...",
    )


# ─────────────────────────────────────────────
# FILTER LOGIC
# ─────────────────────────────────────────────

filtered_places = places

if selected_category != "All":

    filtered_places = [
        place
        for place in filtered_places
        if place["category"] == selected_category
    ]

if search:

    search_lower = search.lower()

    filtered_places = [
        place
        for place in filtered_places
        if (
            search_lower in place["name"].lower()
            or search_lower in place["description"].lower()
            or search_lower in place["category"].lower()
        )
    ]


# ─────────────────────────────────────────────
# MAP
# ─────────────────────────────────────────────

with map_col:

    city_map = folium.Map(
        location=[
            lat,
            lon,
        ],
        zoom_start=12,
        tiles="OpenStreetMap",
    )

    # City-level marker.
    # Individual place coordinates are not currently
    # stored in catalog.py, so we do not invent them.
    folium.Marker(
        location=[
            lat,
            lon,
        ],
        tooltip=f"{city} — NOMIA",
        popup=folium.Popup(
            f"""
            <b>{city}</b><br>
            {country}<br><br>
            NOMIA city intelligence
            """,
            max_width=300,
        ),
        icon=folium.Icon(
            color="blue",
            icon="globe",
        ),
    ).add_to(city_map)

    # Add individual markers only when coordinates
    # actually exist in the catalog.
    for place in filtered_places:

        if (
            place["lat"] is not None
            and place["lon"] is not None
        ):

            folium.Marker(
                location=[
                    place["lat"],
                    place["lon"],
                ],
                tooltip=place["name"],
                popup=folium.Popup(
                    f"""
                    <b>{place["name"]}</b><br>
                    {place["category"]}<br><br>
                    {place["description"]}
                    """,
                    max_width=300,
                ),
            ).add_to(city_map)

    st_folium(
        city_map,
        width=None,
        height=520,
        returned_objects=[],
    )


# ─────────────────────────────────────────────
# PLACES
# ─────────────────────────────────────────────

st.markdown("---")

st.markdown("### Places worth knowing")


if not filtered_places:

    st.info(
        "No places match your search. "
        "Try another category or search term."
    )

else:

    columns = st.columns(2)

    for index, place in enumerate(filtered_places):

        with columns[index % 2]:

            st.html(
                f"""
                <div style="
                    padding:20px;
                    margin-bottom:14px;
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
                        {place["category"].upper()}
                    </div>

                    <div style="
                        font-size:20px;
                        font-weight:700;
                        margin-top:8px;
                    ">
                        {place["name"]}
                    </div>

                    <div style="
                        color:#8f9aaa;
                        font-size:14px;
                        line-height:1.5;
                        margin-top:8px;
                    ">
                        {place["description"]}
                    </div>

                    <div style="
                        color:#667085;
                        font-size:12px;
                        margin-top:12px;
                    ">
                        📍 {city}, {country}
                    </div>

                </div>
                """
            )