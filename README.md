# 🌍 NOMIA

### Your Local Intelligence Layer

> **Know the city before you explore it.**

NOMIA is an international travel and city-intelligence platform designed to help people understand a new city before they start exploring it.

Instead of trying to be another maps application, NOMIA focuses on the practical information travelers actually need after arriving somewhere:

**Explore → Move → Eat → Shop → Essentials**

Select a country, choose a city, and get a focused local guide with places, transportation, food delivery services, shopping areas, essential services, directions, and practical local information.

---

## ✨ Features

### 🌍 International Destination System

Choose from supported countries and cities through a simple:

**Country → City → Local Guide**

NOMIA currently supports destinations across multiple regions including:

- 🇮🇳 India
- 🇦🇪 UAE
- 🇯🇵 Japan
- 🇸🇬 Singapore
- 🇬🇧 UK
- 🇫🇷 France
- 🇮🇹 Italy
- 🇺🇸 USA
- 🇦🇺 Australia
- 🇩🇪 Germany
- 🇨🇦 Canada
- 🇳🇱 Netherlands

---

## 📍 Explore

Discover places worth knowing in the selected city.

The Explore layer provides:

- City overview
- Attractions
- Shopping locations
- Food areas
- Interactive map
- Search/filter functionality
- Direct map navigation

The current city catalog provides the structured foundation for NOMIA's destination intelligence.

---

## 🚕 Move

Understand how to get around locally.

Move provides city-specific transportation information including:

- Ride-hailing services
- Taxi services
- Public transportation
- Metro/subway systems
- Local transport applications
- Useful official service links
- Local transportation tips

The available services change according to the selected city.

---

## 🍜 Eat

Find out how locals order food and where different food areas are located.

Eat includes:

- Food delivery platforms
- City-specific delivery applications
- Popular food areas
- Local food tips
- Direct service links

Examples of supported platforms include services such as:

- Zomato
- Swiggy
- Uber Eats
- Deliveroo
- Talabat
- Careem
- GrabFood
- foodpanda
- DoorDash
- Just Eat
- Lieferando
- Thuisbezorgd

Availability depends on the selected city.

---

## 🛍️ Shop

Explore shopping destinations in the selected city.

The Shop layer focuses on:

- Major shopping areas
- Malls
- Retail destinations
- City-specific shopping information
- Map-based discovery

---

## 🧭 Essentials

Find important everyday services around the selected city.

NOMIA's Essentials layer can retrieve real-world locations using OpenStreetMap-based geographic data.

Categories include:

- 🏥 Hospitals
- 💊 Pharmacies
- 🏧 ATMs & banking
- 🚆 Transport
- 📱 Connectivity/mobile stores
- 🛒 Everyday stores

Where geographic data is available, NOMIA provides:

- Real place names
- Addresses
- Coordinates
- Directions

This layer uses geographic data rather than manually hardcoding large lists of individual businesses.

---

## 🗺️ Maps

NOMIA uses **OpenStreetMap**-based geographic information for mapping and location discovery.

Maps are intended to provide geographic context and help users understand where relevant places are located.

---

## 🧠 Design Philosophy

NOMIA is built around one simple idea:

> **A map tells you where something is. NOMIA helps you understand what matters when you're there.**

The project deliberately avoids becoming a full replacement for large navigation platforms.

Instead, NOMIA acts as a **local intelligence layer** sitting above basic geographic information.

---

# 🛠️ Tech Stack

### Frontend / Application

- Python
- Streamlit

### Mapping

- Folium
- Streamlit-Folium
- OpenStreetMap

### Geographic Data

- OpenStreetMap
- Overpass API

### Architecture

- Modular Python application
- Centralized city catalog
- Country → city navigation
- Reusable UI components
- Session-state based destination selection

---

# 📁 Project Structure

```text
NOMIA/
│
├── app/
│   ├── main.py
│   │
│   ├── pages/
│   │   ├── home.py
│   │   ├── explore.py
│   │   ├── move.py
│   │   ├── eat.py
│   │   ├── shop.py
│   │   └── essentials.py
│   │
│   ├── components/
│   │   ├── ui/
│   │   │   ├── header.py
│   │   │   └── sidebar.py
│   │   │
│   │   ├── cards/
│   │   │   ├── info_card.py
│   │   │   └── place_card.py
│   │   │
│   │   └── map/
│   │       └── city_map.py
│   │
│   ├── data/
│   │   ├── countries/
│   │   │   └── countries.py
│   │   │
│   │   └── cities/
│   │       ├── india.py
│   │       └── catalog.py
│   │
│   └── utils/
│       ├── helpers.py
│       └── links.py
│
├── assets/
│   ├── images/
│   └── icons/
│
├── .github/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/NOMIA.git
cd NOMIA
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Run NOMIA

From the project root:

```powershell
streamlit run app/main.py
```

The application will open in your browser.

---

# 📦 Requirements

The project uses lightweight Python dependencies.

Core dependencies include:

```text
streamlit
folium
streamlit-folium
requests
```

See `requirements.txt` for the exact environment used by the project.

---

# 🌐 Data Sources

NOMIA uses different sources depending on the feature.

### OpenStreetMap

OpenStreetMap provides geographic and place information used by NOMIA's map and Essentials functionality.

OpenStreetMap data is available under the **Open Data Commons Open Database License (ODbL)**.

Attribution is required when using OpenStreetMap data.

### Overpass API

NOMIA uses the Overpass API to query OpenStreetMap data for relevant geographic features and places.

External service availability and query limits may affect live location results.

---

# ⚠️ Data Accuracy

NOMIA is designed as a travel-information and discovery tool.

Information such as:

- Opening hours
- Transport availability
- Business availability
- Service coverage
- Place listings

can change over time.

Users should verify important information with the relevant official service before relying on it for time-sensitive decisions.

---

# 💰 Cost

NOMIA is designed as a **₹0 development project**.

The project does not require:

- Paid APIs
- Paid hosting
- Paid domains
- Google Maps API billing
- Proprietary mapping subscriptions

The application is designed to run locally using open technologies and publicly available geographic data.

---

# 🚀 Current Version

## NOMIA V1

The first version focuses on building a useful international city-intelligence foundation.

### V1 includes:

- [x] International country selection
- [x] City selection
- [x] Explore
- [x] Move
- [x] Eat
- [x] Shop
- [x] Essentials
- [x] Interactive maps
- [x] City-specific information
- [x] Real OpenStreetMap-based essential locations
- [x] Directions
- [x] Local tips
- [x] Premium dark interface
- [x] Modular page architecture

---

# 🔮 Future Possibilities

Potential future improvements could include:

- Personalized travel profiles
- Saved destinations
- Multi-city trip planning
- Offline city guides
- Better geographic search
- More cities and countries
- Local event discovery
- Weather-aware recommendations
- Transit-aware route suggestions
- User-contributed local knowledge
- Smarter destination recommendations

These are intentionally outside the current V1 scope.

---

# 🎯 Why NOMIA?

Traveling to a new city often means searching across multiple applications:

**Maps → Transport app → Food app → Shopping → Hospitals → Pharmacies → Local information**

NOMIA brings the first layer of that information together into one destination-aware interface.

The goal is not to replace specialized applications.

The goal is to help users **know what they need before opening them.**

---

# 👨‍💻 Author

**Palash Goyal**

Independent developer & researcher working across:

- Artificial Intelligence
- Software Engineering
- Aerospace & Space Technology
- Robotics
- Computer Vision

NOMIA is part of an ongoing portfolio of experimental software and technology projects.

---

# 📌 Project Status

**NOMIA V1 — International City Intelligence**

🟢 Core application functional  
🟢 International destination system implemented  
🟢 Core pages implemented  
🟢 OpenStreetMap integration implemented  
🟢 Essentials geographic discovery implemented  
🟢 UI polished for portfolio presentation

---

<p align="center">

**NOMIA**

*Know the city before you explore it.*

</p>
