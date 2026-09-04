import streamlit as st

from data.cities.catalog import (
    get_city,
    get_city_country,
)


# =========================================================
# INTERNATIONAL SHOPPING DATA
# =========================================================

SHOP_DATA = {

    # =====================================================
    # INDIA
    # =====================================================

    "Delhi": {
        "markets": [
            ("Connaught Place", "Central shopping, brands, cafés and bookstores."),
            ("Sarojini Nagar", "Popular market for affordable fashion and accessories."),
            ("Chandni Chowk", "Traditional markets, textiles, jewellery and local shopping."),
        ],
        "malls": [
            ("Select CITYWALK", "Saket", "Premium shopping and dining destination."),
            ("DLF Promenade", "Vasant Kunj", "Major fashion, lifestyle and dining mall."),
            ("Pacific Mall", "Tagore Garden", "Large shopping and entertainment complex."),
        ],
        "online": [
            ("Amazon India", "Online shopping", "https://www.amazon.in/"),
            ("Flipkart", "Online shopping", "https://www.flipkart.com/"),
        ],
        "tip": "Delhi has very different shopping experiences by neighbourhood — compare markets and malls before heading out.",
    },

    "Mumbai": {
        "markets": [
            ("Colaba Causeway", "Fashion, souvenirs and street shopping."),
            ("Linking Road", "Popular fashion and street-shopping area."),
            ("Crawford Market", "Historic market with a wide range of goods."),
        ],
        "malls": [
            ("Phoenix Palladium", "Lower Parel", "Premium shopping and dining."),
            ("Phoenix Marketcity", "Kurla", "Large shopping and entertainment destination."),
        ],
        "online": [
            ("Amazon India", "Online shopping", "https://www.amazon.in/"),
            ("Flipkart", "Online shopping", "https://www.flipkart.com/"),
        ],
        "tip": "Mumbai shopping areas can be far apart, so check travel time before visiting multiple markets.",
    },

    "Bengaluru": {
        "markets": [
            ("Commercial Street", "Popular fashion, accessories and street-shopping area."),
            ("Brigade Road", "Central shopping and lifestyle destination."),
            ("KR Market", "Traditional market with local goods and produce."),
        ],
        "malls": [
            ("UB City", "Vittal Mallya Road", "Premium shopping and dining destination."),
            ("Phoenix Marketcity", "Mahadevapura", "Large shopping and entertainment complex."),
            ("Orion Mall", "Rajajinagar", "Major lifestyle and entertainment mall."),
        ],
        "online": [
            ("Amazon India", "Online shopping", "https://www.amazon.in/"),
            ("Flipkart", "Online shopping", "https://www.flipkart.com/"),
        ],
        "tip": "Bengaluru traffic can significantly affect shopping plans, especially around central and eastern areas.",
    },


    # =====================================================
    # UAE
    # =====================================================

    "Dubai": {
        "markets": [
            ("Gold Souk", "Traditional gold market in Deira."),
            ("Deira Market", "Traditional shopping and local goods."),
            ("Al Seef", "Heritage-inspired waterfront shopping area."),
        ],
        "malls": [
            ("Dubai Mall", "Downtown Dubai", "Major shopping and entertainment destination."),
            ("Mall of the Emirates", "Al Barsha", "Major shopping and dining complex."),
            ("Dubai Marina Mall", "Dubai Marina", "Waterfront shopping and lifestyle destination."),
        ],
        "online": [
            ("Amazon UAE", "Online shopping", "https://www.amazon.ae/"),
            ("Noon", "UAE online marketplace", "https://www.noon.com/"),
        ],
        "tip": "Dubai's malls are destinations themselves, while traditional souks offer a very different local shopping experience.",
    },

    "Abu Dhabi": {
        "markets": [
            ("Madinat Zayed Shopping Centre", "Traditional shopping and gold market."),
            ("Souk Qaryat Al Beri", "Waterfront market with local and international shops."),
            ("Central Market", "Traditional and modern shopping in the city centre."),
        ],
        "malls": [
            ("Yas Mall", "Yas Island", "Large shopping and entertainment complex."),
            ("Abu Dhabi Mall", "Al Zahiyah", "Central shopping destination."),
        ],
        "online": [
            ("Amazon UAE", "Online shopping", "https://www.amazon.ae/"),
            ("Noon", "UAE online marketplace", "https://www.noon.com/"),
        ],
        "tip": "Abu Dhabi combines modern malls with traditional souks, so choose based on the type of shopping experience you want.",
    },


    # =====================================================
    # JAPAN
    # =====================================================

    "Tokyo": {
        "markets": [
            ("Shibuya", "Fashion, electronics, lifestyle and youth culture."),
            ("Akihabara", "Electronics, gaming, anime and hobby stores."),
            ("Asakusa", "Traditional souvenirs and local shopping."),
        ],
        "malls": [
            ("Shibuya Scramble Square", "Shibuya", "Large modern shopping and observation complex."),
            ("Tokyo Midtown", "Roppongi", "Premium shopping, dining and art."),
            ("Ginza Six", "Ginza", "Upscale shopping and dining."),
        ],
        "online": [
            ("Amazon Japan", "Online shopping", "https://www.amazon.co.jp/"),
            ("Rakuten", "Japanese online marketplace", "https://www.rakuten.co.jp/"),
        ],
        "tip": "Tokyo shopping is highly neighbourhood-based. Electronics, fashion and traditional goods are concentrated in different areas.",
    },

    "Osaka": {
        "markets": [
            ("Dotonbori", "Food, souvenirs, entertainment and shopping."),
            ("Shinsaibashi", "Major shopping street with fashion and lifestyle stores."),
            ("Kuromon Market", "Food market and local shopping."),
        ],
        "malls": [
            ("Abeno Harukas", "Abeno", "Major department store and shopping complex."),
            ("Grand Front Osaka", "Umeda", "Large shopping, dining and lifestyle complex."),
            ("Namba Parks", "Namba", "Shopping, dining and entertainment complex."),
        ],
        "online": [
            ("Amazon Japan", "Online shopping", "https://www.amazon.co.jp/"),
            ("Rakuten", "Japanese online marketplace", "https://www.rakuten.co.jp/"),
        ],
        "tip": "Umeda and Namba are two major shopping hubs, making it easy to combine shopping with sightseeing.",
    },

    "Kyoto": {
        "markets": [
            ("Nishiki Market", "Historic covered market with food, crafts and souvenirs."),
            ("Shijo Kawaramachi", "Major central shopping and lifestyle district."),
            ("Gion", "Traditional streets with crafts, souvenirs and specialty shops."),
        ],
        "malls": [
            ("Kyoto Station Building", "Kyoto Station", "Large shopping, dining and transport complex."),
            ("Kyoto Takashimaya S.C.", "Shijo", "Major department store and shopping destination."),
        ],
        "online": [
            ("Amazon Japan", "Online shopping", "https://www.amazon.co.jp/"),
            ("Rakuten", "Japanese online marketplace", "https://www.rakuten.co.jp/"),
        ],
        "tip": "Kyoto is especially good for traditional crafts, sweets and souvenirs alongside modern shopping around Shijo and Kyoto Station.",
    },


    # =====================================================
    # SINGAPORE
    # =====================================================

    "Singapore": {
        "markets": [
            ("Bugis Street", "Popular market for fashion, souvenirs and affordable shopping."),
            ("Chinatown Street Market", "Local goods, souvenirs and traditional shopping."),
            ("Haji Lane", "Boutiques, independent shops and lifestyle stores."),
        ],
        "malls": [
            ("ION Orchard", "Orchard Road", "Major luxury and lifestyle shopping destination."),
            ("VivoCity", "HarbourFront", "Large shopping and entertainment complex."),
            ("Suntec City", "Marina Centre", "Major shopping, dining and business complex."),
        ],
        "online": [
            ("Shopee Singapore", "Online marketplace", "https://shopee.sg/"),
            ("Lazada Singapore", "Online marketplace", "https://www.lazada.sg/"),
        ],
        "tip": "Orchard Road is ideal for major malls, while neighbourhoods such as Bugis and Chinatown offer a more local shopping experience.",
    },


    # =====================================================
    # UK
    # =====================================================

    "London": {
        "markets": [
            ("Camden Market", "Large market with fashion, food, crafts and independent shops."),
            ("Borough Market", "Historic food-focused market with specialty products."),
            ("Covent Garden", "Shopping, boutiques, crafts and entertainment."),
        ],
        "malls": [
            ("Westfield London", "Shepherd's Bush", "Major shopping and entertainment complex."),
            ("Westfield Stratford City", "Stratford", "Large shopping, dining and entertainment destination."),
        ],
        "online": [
            ("Amazon UK", "Online shopping", "https://www.amazon.co.uk/"),
            ("Argos", "UK retail and online shopping", "https://www.argos.co.uk/"),
        ],
        "tip": "Central London has dense shopping districts, while Westfield centres are convenient when you want many brands in one place.",
    },

    "Manchester": {
        "markets": [
            ("Afflecks", "Independent shops, fashion, art and alternative culture."),
            ("Mackie Mayor", "Food-focused market hall in the Northern Quarter area."),
            ("Manchester Arndale", "Central shopping district with many major retailers."),
        ],
        "malls": [
            ("Trafford Centre", "Trafford", "Large shopping and entertainment complex."),
            ("Manchester Arndale", "City Centre", "Major central shopping centre."),
        ],
        "online": [
            ("Amazon UK", "Online shopping", "https://www.amazon.co.uk/"),
            ("Argos", "UK retail and online shopping", "https://www.argos.co.uk/"),
        ],
        "tip": "Manchester city centre is highly walkable for shopping, while Trafford Centre works well for a full-day mall visit.",
    },


    # =====================================================
    # FRANCE
    # =====================================================

    "Paris": {
        "markets": [
            ("Rue de Rivoli", "Major central shopping street with international brands."),
            ("Le Marais", "Independent boutiques, fashion and lifestyle stores."),
            ("Saint-Ouen Flea Market", "Large flea-market area with vintage and antiques."),
        ],
        "malls": [
            ("Galeries Lafayette Haussmann", "9th arrondissement", "Historic department store and shopping destination."),
            ("Printemps Haussmann", "9th arrondissement", "Major Paris department store."),
        ],
        "online": [
            ("Amazon France", "Online shopping", "https://www.amazon.fr/"),
            ("Cdiscount", "French online marketplace", "https://www.cdiscount.com/"),
        ],
        "tip": "Paris shopping ranges from major department stores to independent neighbourhood boutiques, so choose the district based on what you want to buy.",
    },


    # =====================================================
    # ITALY
    # =====================================================

    "Rome": {
        "markets": [
            ("Campo de' Fiori", "Historic market square with food and local products."),
            ("Porta Portese Market", "Large Sunday market with varied goods and vintage items."),
            ("Via del Corso", "Central shopping street with major brands."),
        ],
        "malls": [
            ("Euroma2", "EUR", "Large modern shopping centre."),
            ("Galleria Alberto Sordi", "City Centre", "Historic central shopping gallery."),
        ],
        "online": [
            ("Amazon Italy", "Online shopping", "https://www.amazon.it/"),
            ("eBay Italy", "Online marketplace", "https://www.ebay.it/"),
        ],
        "tip": "Rome's historic centre is excellent for combining sightseeing and shopping, while larger malls are generally outside the core tourist area.",
    },

    "Milan": {
        "markets": [
            ("Brera", "Boutiques, design stores and independent shopping."),
            ("Navigli", "Vintage shops, boutiques and weekend markets."),
            ("Corso Buenos Aires", "Long shopping street with many mainstream brands."),
        ],
        "malls": [
            ("Galleria Vittorio Emanuele II", "Duomo", "Historic luxury shopping arcade."),
            ("CityLife Shopping District", "CityLife", "Modern shopping and lifestyle destination."),
        ],
        "online": [
            ("Amazon Italy", "Online shopping", "https://www.amazon.it/"),
            ("eBay Italy", "Online marketplace", "https://www.ebay.it/"),
        ],
        "tip": "Milan is particularly strong for fashion and design. Brera and the Quadrilatero are better suited to premium browsing.",
    },


    # =====================================================
    # USA
    # =====================================================

    "New York": {
        "markets": [
            ("SoHo", "Fashion, design stores, boutiques and major brands."),
            ("Chelsea Market", "Food, specialty products and independent vendors."),
            ("Union Square Greenmarket", "Local produce, food and seasonal products."),
        ],
        "malls": [
            ("Westfield World Trade Center", "Financial District", "Major shopping destination beneath the Oculus."),
            ("The Shops at Columbus Circle", "Columbus Circle", "Upscale shopping and dining."),
        ],
        "online": [
            ("Amazon US", "Online shopping", "https://www.amazon.com/"),
            ("Walmart", "US retail and online shopping", "https://www.walmart.com/"),
        ],
        "tip": "New York shopping is neighbourhood-driven. SoHo, Fifth Avenue and local markets offer very different experiences.",
    },

    "Los Angeles": {
        "markets": [
            ("The Grove", "Popular outdoor shopping and entertainment district."),
            ("Melrose Avenue", "Fashion, boutiques, vintage and lifestyle stores."),
            ("Grand Central Market", "Historic food market in Downtown LA."),
        ],
        "malls": [
            ("Westfield Century City", "Century City", "Large modern shopping and dining complex."),
            ("Beverly Center", "Beverly Grove", "Major fashion and lifestyle shopping centre."),
        ],
        "online": [
            ("Amazon US", "Online shopping", "https://www.amazon.com/"),
            ("Walmart", "US retail and online shopping", "https://www.walmart.com/"),
        ],
        "tip": "Los Angeles is spread out, so group shopping stops by neighbourhood rather than trying to cross the city repeatedly.",
    },


    # =====================================================
    # AUSTRALIA
    # =====================================================

    "Sydney": {
        "markets": [
            ("The Rocks Markets", "Historic market with crafts, souvenirs and local products."),
            ("Paddy's Markets", "Large market for produce, souvenirs and everyday goods."),
            ("Glebe Markets", "Weekend market with vintage, fashion and local sellers."),
        ],
        "malls": [
            ("Westfield Sydney", "Sydney CBD", "Major central shopping destination."),
            ("Westfield Bondi Junction", "Bondi Junction", "Large shopping and lifestyle centre."),
        ],
        "online": [
            ("Amazon Australia", "Online shopping", "https://www.amazon.com.au/"),
            ("Kogan", "Australian online marketplace", "https://www.kogan.com/au/"),
        ],
        "tip": "Sydney has strong weekend markets as well as large shopping centres, making it easy to mix local and mainstream shopping.",
    },


    # =====================================================
    # GERMANY
    # =====================================================

    "Berlin": {
        "markets": [
            ("Mauerpark Flea Market", "Popular weekend flea market with vintage and local goods."),
            ("Hackescher Markt", "Boutiques, independent stores and lifestyle shopping."),
            ("Kurfürstendamm", "Major shopping boulevard with international brands."),
        ],
        "malls": [
            ("Mall of Berlin", "Potsdamer Platz", "Large central shopping centre."),
            ("KaDeWe", "Schöneberg", "Historic premium department store."),
        ],
        "online": [
            ("Amazon Germany", "Online shopping", "https://www.amazon.de/"),
            ("OTTO", "German online retailer", "https://www.otto.de/"),
        ],
        "tip": "Berlin is strong for independent design and vintage shopping, while Kurfürstendamm and KaDeWe cover mainstream and premium retail.",
    },


    # =====================================================
    # CANADA
    # =====================================================

    "Toronto": {
        "markets": [
            ("Kensington Market", "Multicultural neighbourhood with independent shops and food."),
            ("St. Lawrence Market", "Historic market with food and local products."),
            ("Queen Street West", "Fashion, design and independent retail."),
        ],
        "malls": [
            ("CF Toronto Eaton Centre", "Downtown", "Major central shopping destination."),
            ("Yorkdale Shopping Centre", "North York", "Large premium shopping centre."),
        ],
        "online": [
            ("Amazon Canada", "Online shopping", "https://www.amazon.ca/"),
            ("Walmart Canada", "Canadian retail and online shopping", "https://www.walmart.ca/"),
        ],
        "tip": "Toronto's neighbourhoods have distinct shopping personalities. Kensington and Queen Street West are good for independent finds.",
    },


    # =====================================================
    # NETHERLANDS
    # =====================================================

    "Amsterdam": {
        "markets": [
            ("Albert Cuyp Market", "Large street market with food, clothing and local products."),
            ("De Negen Straatjes", "Boutiques, vintage stores and independent shopping."),
            ("Waterlooplein Market", "Flea market with vintage and second-hand goods."),
        ],
        "malls": [
            ("Magna Plaza", "Dam Square", "Historic shopping centre near the city centre."),
            ("Kalverpassage", "Kalverstraat", "Central shopping destination."),
        ],
        "online": [
            ("Bol", "Dutch online marketplace", "https://www.bol.com/"),
            ("Amazon Netherlands", "Online shopping", "https://www.amazon.nl/"),
        ],
        "tip": "Amsterdam's compact centre makes it easy to combine markets, independent shops and major retail streets on foot.",
    },
}


# =========================================================
# FALLBACK
# =========================================================

DEFAULT_DATA = {
    "markets": [
        ("Central Market", "Popular local shopping district."),
        ("City Centre", "Convenient area for everyday shopping."),
    ],
    "malls": [
        ("Major City Mall", "Central District", "Large shopping and lifestyle destination."),
    ],
    "online": [
        ("Local marketplace", "Online shopping", "#"),
    ],
    "tip": "Shopping options vary by neighbourhood. Check current opening hours before visiting.",
}


# =========================================================
# CURRENT CITY
# =========================================================

city = st.session_state.get("city", "Delhi")

city_info = get_city(city)

if city_info:
    country = city_info.get("country", "India")
else:
    country = st.session_state.get("country", "India")

# Keep session state synchronized with central catalog
st.session_state["country"] = country

data = SHOP_DATA.get(city, DEFAULT_DATA)


# =========================================================
# HEADER
# =========================================================

st.html(f"""
<div style="margin-top:18px;margin-bottom:35px;">

    <div style="
        color:#58a6ff;
        font-size:13px;
        font-weight:700;
        letter-spacing:2px;
        margin-bottom:28px;">
        LOCAL SHOPPING INTELLIGENCE
    </div>

    <h1 style="
        font-size:52px;
        margin:0;
        color:#f5f7fa;
        letter-spacing:-2px;">
        Shop in {city}.
    </h1>

    <p style="
        color:#91a4bd;
        font-size:18px;
        margin-top:22px;">
        Markets, malls and online shopping options for your city.
    </p>

</div>
""")


# =========================================================
# STATS
# =========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.html(f"""
    <div>
        <div style="color:#91a4bd;font-size:14px;">
            Local markets
        </div>

        <div style="
            font-size:36px;
            color:#f5f7fa;
            margin-top:6px;">
            {len(data["markets"])}
        </div>
    </div>
    """)


with c2:
    st.html(f"""
    <div>
        <div style="color:#91a4bd;font-size:14px;">
            Shopping centres
        </div>

        <div style="
            font-size:36px;
            color:#f5f7fa;
            margin-top:6px;">
            {len(data["malls"])}
        </div>
    </div>
    """)


with c3:
    st.html(f"""
    <div>
        <div style="color:#91a4bd;font-size:14px;">
            Online options
        </div>

        <div style="
            font-size:36px;
            color:#f5f7fa;
            margin-top:6px;">
            {len(data["online"])}
        </div>
    </div>
    """)


st.divider()


# =========================================================
# LOCAL MARKETS
# =========================================================

st.html("""
<h2 style="margin-bottom:20px;">
    🛍️ Local markets
</h2>
""")


cols = st.columns(3)

for i, (name, description) in enumerate(data["markets"]):

    with cols[i % 3]:

        st.html(f"""
        <div style="
            border:1px solid #202630;
            border-radius:16px;
            padding:24px;
            min-height:155px;
            background:rgba(10,14,20,0.45);
            margin-bottom:20px;">

            <div style="
                color:#58a6ff;
                font-size:12px;
                font-weight:700;
                letter-spacing:1.5px;
                margin-bottom:16px;">
                LOCAL MARKET
            </div>

            <div style="
                color:#f5f7fa;
                font-size:21px;
                font-weight:700;">
                {name}
            </div>

            <div style="
                color:#91a4bd;
                font-size:14px;
                margin-top:12px;
                line-height:1.6;">
                {description}
            </div>

        </div>
        """)


st.divider()


# =========================================================
# SHOPPING CENTRES
# =========================================================

st.html("""
<h2 style="margin-bottom:20px;">
    🏬 Shopping centres
</h2>
""")


for name, area, description in data["malls"]:

    left, right = st.columns([4, 1])

    with left:

        st.html(f"""
        <div style="
            border:1px solid #202630;
            border-radius:16px;
            padding:22px;
            margin-bottom:16px;
            background:rgba(10,14,20,0.45);">

            <div style="
                color:#f5f7fa;
                font-size:20px;
                font-weight:700;">
                {name}
            </div>

            <div style="
                color:#58a6ff;
                font-size:13px;
                margin-top:8px;">
                📍 {area}
            </div>

            <div style="
                color:#91a4bd;
                font-size:14px;
                margin-top:10px;">
                {description}
            </div>

        </div>
        """)

    with right:

        st.write("")

        maps_url = (
            "https://www.google.com/maps/search/"
            f"?api=1&query={name.replace(' ', '+')}+{city.replace(' ', '+')}"
        )

        st.link_button(
            "Directions ↗",
            maps_url,
            use_container_width=True,
        )


st.divider()


# =========================================================
# ONLINE SHOPPING
# =========================================================

st.html("""
<h2 style="margin-bottom:20px;">
    🌐 Online shopping
</h2>
""")


online_options = data.get("online", [])

if online_options:

    cols = st.columns(len(online_options))

    for i, item in enumerate(online_options):

        name = item[0]
        category = item[1]
        url = item[2] if len(item) > 2 else "#"

        with cols[i]:

            st.html(f"""
            <div style="
                border:1px solid #202630;
                border-radius:16px;
                padding:22px;
                min-height:130px;
                background:rgba(10,14,20,0.45);">

                <div style="
                    color:#f5f7fa;
                    font-size:20px;
                    font-weight:700;">
                    {name}
                </div>

                <div style="
                    color:#91a4bd;
                    font-size:14px;
                    margin-top:10px;">
                    {category}
                </div>

            </div>
            """)

            if url != "#":
                st.link_button(
                    "Open ↗",
                    url,
                    use_container_width=True,
                )


else:

    st.info("Online shopping information is not available for this city yet.")


st.divider()


# =========================================================
# NOMIA TIP
# =========================================================

st.html("""
<h2 style="margin-bottom:18px;">
    💡 NOMIA local knowledge
</h2>
""")


st.html(f"""
<div style="
    background:#102b43;
    border-radius:12px;
    padding:20px;
    color:#58a6ff;
    font-size:16px;
    line-height:1.6;">
    {data["tip"]}
</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div style="
    margin-top:34px;
    padding:18px;
    border:1px solid #202630;
    border-radius:14px;
    color:#71849d;
    font-size:13px;">
    NOMIA provides a starting layer for local discovery.
    Always verify current opening hours, availability and local conditions before travelling.
</div>
""")