# ============================================================
# NOMIA — GLOBAL CITY INTELLIGENCE CATALOG
# ============================================================
#
# Central source of truth for city-level NOMIA information.
#
# Pages should eventually read from this catalog instead of
# maintaining separate city dictionaries.
# ============================================================


CITY_DATA = {

    # ========================================================
    # INDIA
    # ========================================================

    "Delhi": {
        "country": "India",
        "region": "Asia",

        "coordinates": {
            "lat": 28.6139,
            "lon": 77.2090,
        },

        "description":
            "India's capital, known for historic landmarks, "
            "markets, food districts and extensive public transport.",

        "attractions": [
            "India Gate",
            "Red Fort",
            "Qutub Minar",
            "Lotus Temple",
        ],

        "shopping": [
            "Connaught Place",
            "Chandni Chowk",
            "Dilli Haat",
        ],

        "food_areas": [
            "Old Delhi",
            "Connaught Place",
            "Khan Market",
        ],
    },


    "Mumbai": {
        "country": "India",
        "region": "Asia",

        "coordinates": {
            "lat": 19.0760,
            "lon": 72.8777,
        },

        "description":
            "India's financial capital, famous for its coastline, "
            "markets, neighbourhoods and fast-paced city life.",

        "attractions": [
            "Gateway of India",
            "Marine Drive",
            "Chhatrapati Shivaji Maharaj Terminus",
            "Colaba",
        ],

        "shopping": [
            "Colaba Causeway",
            "Linking Road",
            "Phoenix Palladium",
        ],

        "food_areas": [
            "Colaba",
            "Bandra",
            "Lower Parel",
        ],
    },


    "Bengaluru": {
        "country": "India",
        "region": "Asia",

        "coordinates": {
            "lat": 12.9716,
            "lon": 77.5946,
        },

        "description":
            "A major technology hub known for parks, cafés, "
            "startups and a large metropolitan community.",

        "attractions": [
            "Bengaluru Palace",
            "Lalbagh Botanical Garden",
            "Cubbon Park",
            "Vidhana Soudha",
        ],

        "shopping": [
            "UB City",
            "Commercial Street",
            "Orion Mall",
        ],

        "food_areas": [
            "Indiranagar",
            "Koramangala",
            "Church Street",
        ],
    },


    # ========================================================
    # UAE
    # ========================================================

    "Dubai": {
        "country": "UAE",
        "region": "Middle East",

        "coordinates": {
            "lat": 25.2048,
            "lon": 55.2708,
        },

        "description":
            "A global travel hub known for modern architecture, "
            "shopping, beaches and large-scale attractions.",

        "attractions": [
            "Burj Khalifa",
            "Dubai Mall",
            "Palm Jumeirah",
            "Dubai Marina",
        ],

        "shopping": [
            "Dubai Mall",
            "Mall of the Emirates",
            "Deira",
        ],

        "food_areas": [
            "Downtown Dubai",
            "Jumeirah",
            "Dubai Marina",
        ],
    },


    "Abu Dhabi": {
        "country": "UAE",
        "region": "Middle East",

        "coordinates": {
            "lat": 24.4539,
            "lon": 54.3773,
        },

        "description":
            "The capital of the UAE, combining modern city districts, "
            "cultural attractions and waterfront areas.",

        "attractions": [
            "Sheikh Zayed Grand Mosque",
            "Louvre Abu Dhabi",
            "Qasr Al Watan",
            "Yas Island",
        ],

        "shopping": [
            "Yas Mall",
            "Marina Mall",
            "Abu Dhabi Mall",
        ],

        "food_areas": [
            "Al Zahiyah",
            "Al Maryah Island",
            "Yas Island",
        ],
    },


    # ========================================================
    # JAPAN
    # ========================================================

    "Tokyo": {
        "country": "Japan",
        "region": "Asia",

        "coordinates": {
            "lat": 35.6762,
            "lon": 139.6503,
        },

        "description":
            "A huge metropolitan centre combining technology, "
            "traditional districts, shopping and one of the world's "
            "largest urban rail networks.",

        "attractions": [
            "Senso-ji",
            "Tokyo Skytree",
            "Meiji Shrine",
            "Shibuya Crossing",
        ],

        "shopping": [
            "Shibuya",
            "Ginza",
            "Akihabara",
        ],

        "food_areas": [
            "Shinjuku",
            "Shibuya",
            "Tsukiji",
        ],
    },


    "Osaka": {
        "country": "Japan",
        "region": "Asia",

        "coordinates": {
            "lat": 34.6937,
            "lon": 135.5023,
        },

        "description":
            "A major Japanese city known for food, nightlife, "
            "shopping and easy access to the Kansai region.",

        "attractions": [
            "Osaka Castle",
            "Dotonbori",
            "Umeda Sky Building",
            "Universal City",
        ],

        "shopping": [
            "Shinsaibashi",
            "Namba",
            "Umeda",
        ],

        "food_areas": [
            "Dotonbori",
            "Namba",
            "Shinsekai",
        ],
    },


    "Kyoto": {
        "country": "Japan",
        "region": "Asia",

        "coordinates": {
            "lat": 35.0116,
            "lon": 135.7681,
        },

        "description":
            "A historic Japanese city known for temples, gardens, "
            "traditional districts and cultural landmarks.",

        "attractions": [
            "Fushimi Inari Taisha",
            "Kiyomizu-dera",
            "Arashiyama",
            "Kinkaku-ji",
        ],

        "shopping": [
            "Nishiki Market",
            "Shijo",
            "Kawaramachi",
        ],

        "food_areas": [
            "Gion",
            "Pontocho",
            "Nishiki Market",
        ],
    },


    # ========================================================
    # SINGAPORE
    # ========================================================

    "Singapore": {
        "country": "Singapore",
        "region": "Southeast Asia",

        "coordinates": {
            "lat": 1.3521,
            "lon": 103.8198,
        },

        "description":
            "A compact global city known for efficient transport, "
            "food centres, shopping districts and modern attractions.",

        "attractions": [
            "Gardens by the Bay",
            "Marina Bay Sands",
            "Sentosa",
            "Merlion Park",
        ],

        "shopping": [
            "Orchard Road",
            "VivoCity",
            "Bugis",
        ],

        "food_areas": [
            "Chinatown",
            "Little India",
            "Lau Pa Sat",
        ],
    },


    # ========================================================
    # UNITED KINGDOM
    # ========================================================

    "London": {
        "country": "UK",
        "region": "Europe",

        "coordinates": {
            "lat": 51.5074,
            "lon": -0.1278,
        },

        "description":
            "A major global city with extensive public transport, "
            "historic landmarks, museums and diverse neighbourhoods.",

        "attractions": [
            "Tower of London",
            "Big Ben",
            "Buckingham Palace",
            "London Eye",
        ],

        "shopping": [
            "Oxford Street",
            "Covent Garden",
            "Westfield London",
        ],

        "food_areas": [
            "Soho",
            "Borough Market",
            "Brick Lane",
        ],
    },


    "Manchester": {
        "country": "UK",
        "region": "Europe",

        "coordinates": {
            "lat": 53.4808,
            "lon": -2.2426,
        },

        "description":
            "A major northern English city known for football, "
            "music, shopping and a large student population.",

        "attractions": [
            "Manchester Cathedral",
            "Science and Industry Museum",
            "Old Trafford",
            "Northern Quarter",
        ],

        "shopping": [
            "Manchester Arndale",
            "Trafford Centre",
            "Market Street",
        ],

        "food_areas": [
            "Northern Quarter",
            "Ancoats",
            "Curry Mile",
        ],
    },


    # ========================================================
    # FRANCE
    # ========================================================

    "Paris": {
        "country": "France",
        "region": "Europe",

        "coordinates": {
            "lat": 48.8566,
            "lon": 2.3522,
        },

        "description":
            "France's capital, known for architecture, museums, "
            "food, shopping and iconic landmarks.",

        "attractions": [
            "Eiffel Tower",
            "Louvre Museum",
            "Notre-Dame area",
            "Arc de Triomphe",
        ],

        "shopping": [
            "Champs-Élysées",
            "Le Marais",
            "Galeries Lafayette",
        ],

        "food_areas": [
            "Le Marais",
            "Latin Quarter",
            "Montmartre",
        ],
    },


    # ========================================================
    # ITALY
    # ========================================================

    "Rome": {
        "country": "Italy",
        "region": "Europe",

        "coordinates": {
            "lat": 41.9028,
            "lon": 12.4964,
        },

        "description":
            "Italy's capital and a historic city filled with "
            "ancient sites, museums, neighbourhoods and Italian cuisine.",

        "attractions": [
            "Colosseum",
            "Trevi Fountain",
            "Pantheon",
            "Vatican City area",
        ],

        "shopping": [
            "Via del Corso",
            "Via Condotti",
            "Campo de' Fiori",
        ],

        "food_areas": [
            "Trastevere",
            "Testaccio",
            "Monti",
        ],
    },


    "Milan": {
        "country": "Italy",
        "region": "Europe",

        "coordinates": {
            "lat": 45.4642,
            "lon": 9.1900,
        },

        "description":
            "Italy's fashion and business capital, known for design, "
            "shopping, architecture and modern city life.",

        "attractions": [
            "Duomo di Milano",
            "Galleria Vittorio Emanuele II",
            "Sforza Castle",
            "Navigli",
        ],

        "shopping": [
            "Quadrilatero della Moda",
            "Corso Buenos Aires",
            "Galleria Vittorio Emanuele II",
        ],

        "food_areas": [
            "Navigli",
            "Brera",
            "Isola",
        ],
    },


    # ========================================================
    # USA
    # ========================================================

    "New York": {
        "country": "USA",
        "region": "North America",

        "coordinates": {
            "lat": 40.7128,
            "lon": -74.0060,
        },

        "description":
            "A global metropolis known for iconic landmarks, "
            "neighbourhood diversity, culture and extensive transit.",

        "attractions": [
            "Central Park",
            "Times Square",
            "Statue of Liberty",
            "Empire State Building",
        ],

        "shopping": [
            "Fifth Avenue",
            "SoHo",
            "Chelsea Market",
        ],

        "food_areas": [
            "Chinatown",
            "Koreatown",
            "Chelsea",
        ],
    },


    "Los Angeles": {
        "country": "USA",
        "region": "North America",

        "coordinates": {
            "lat": 34.0522,
            "lon": -118.2437,
        },

        "description":
            "A large Southern California city known for entertainment, "
            "beaches, neighbourhoods and car-oriented travel.",

        "attractions": [
            "Hollywood",
            "Santa Monica",
            "Griffith Observatory",
            "The Getty",
        ],

        "shopping": [
            "Rodeo Drive",
            "The Grove",
            "Westfield Century City",
        ],

        "food_areas": [
            "Koreatown",
            "West Hollywood",
            "Downtown LA",
        ],
    },


    # ========================================================
    # AUSTRALIA
    # ========================================================

    "Sydney": {
        "country": "Australia",
        "region": "Oceania",

        "coordinates": {
            "lat": -33.8688,
            "lon": 151.2093,
        },

        "description":
            "Australia's largest city, known for its harbour, "
            "beaches, food districts and outdoor lifestyle.",

        "attractions": [
            "Sydney Opera House",
            "Sydney Harbour Bridge",
            "Bondi Beach",
            "The Rocks",
        ],

        "shopping": [
            "Queen Victoria Building",
            "Pitt Street Mall",
            "Westfield Sydney",
        ],

        "food_areas": [
            "Haymarket",
            "Surry Hills",
            "The Rocks",
        ],
    },


    # ========================================================
    # GERMANY
    # ========================================================

    "Berlin": {
        "country": "Germany",
        "region": "Europe",

        "coordinates": {
            "lat": 52.5200,
            "lon": 13.4050,
        },

        "description":
            "Germany's capital, known for history, creative districts, "
            "museums, nightlife and extensive public transport.",

        "attractions": [
            "Brandenburg Gate",
            "Reichstag",
            "Museum Island",
            "East Side Gallery",
        ],

        "shopping": [
            "Kurfürstendamm",
            "Alexanderplatz",
            "Hackescher Markt",
        ],

        "food_areas": [
            "Kreuzberg",
            "Neukölln",
            "Prenzlauer Berg",
        ],
    },


    # ========================================================
    # CANADA
    # ========================================================

    "Toronto": {
        "country": "Canada",
        "region": "North America",

        "coordinates": {
            "lat": 43.6532,
            "lon": -79.3832,
        },

        "description":
            "Canada's largest city and a highly diverse urban centre "
            "with major neighbourhoods, shopping and waterfront areas.",

        "attractions": [
            "CN Tower",
            "Royal Ontario Museum",
            "Toronto Islands",
            "St. Lawrence Market",
        ],

        "shopping": [
            "CF Toronto Eaton Centre",
            "Yorkville",
            "Queen Street West",
        ],

        "food_areas": [
            "Kensington Market",
            "Chinatown",
            "Little Italy",
        ],
    },


    # ========================================================
    # NETHERLANDS
    # ========================================================

    "Amsterdam": {
        "country": "Netherlands",
        "region": "Europe",

        "coordinates": {
            "lat": 52.3676,
            "lon": 4.9041,
        },

        "description":
            "The Dutch capital, known for canals, museums, cycling, "
            "historic districts and compact urban travel.",

        "attractions": [
            "Rijksmuseum",
            "Anne Frank House",
            "Van Gogh Museum",
            "Jordaan",
        ],

        "shopping": [
            "Kalverstraat",
            "De Negen Straatjes",
            "P.C. Hooftstraat",
        ],

        "food_areas": [
            "De Pijp",
            "Jordaan",
            "Albert Cuyp Market",
        ],
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_city(city):
    """
    Return complete information for a city.
    """

    return CITY_DATA.get(city)


def get_coordinates(city):
    """
    Return latitude and longitude for a city.
    """

    data = CITY_DATA.get(city)

    if not data:
        return None

    return data["coordinates"]


def get_attractions(city):
    """
    Return attraction list for a city.
    """

    data = CITY_DATA.get(city)

    if not data:
        return []

    return data.get("attractions", [])


def get_shopping(city):
    """
    Return shopping areas for a city.
    """

    data = CITY_DATA.get(city)

    if not data:
        return []

    return data.get("shopping", [])


def get_food_areas(city):
    """
    Return food areas for a city.
    """

    data = CITY_DATA.get(city)

    if not data:
        return []

    return data.get("food_areas", [])


def get_city_country(city):
    """
    Return country for a city.
    """

    data = CITY_DATA.get(city)

    if not data:
        return None

    return data["country"]


def city_available(city):
    """
    Check whether NOMIA has city intelligence.
    """

    return city in CITY_DATA


def get_all_cities():
    """
    Return all cities currently supported.
    """

    return list(CITY_DATA.keys())


def get_cities_by_country(country):
    """
    Return all supported cities belonging to a country.
    """

    return [
        city
        for city, data in CITY_DATA.items()
        if data["country"] == country
    ]


def total_supported_cities():
    """
    Return total number of cities in the intelligence catalog.
    """

    return len(CITY_DATA)