# Lyrica - Earth Guardian — Meteor Madness Challenge (NASA Space Apps)

Name: Ridha Alturaiki
Email: yahyahu49@gmail.com


**Challenge:** Meteor Madness  
**Goal:** To visualize, predict, and educate the public about meteor impacts using NASA’s open datasets.  

### The Problem
Most people don’t realize how many meteors enter Earth’s atmosphere every year or how scientists monitor, classify, and assess their risk. NASA collects vast data, but it’s hidden behind complex datasets.

### The Solution
**Lyrica - Earth Guardian** makes NASA’s meteor data understandable to everyone.  
Users can:
- Search for a meteor by name.  
- See its coordinates, past impact events, and potential risk zones.  
- Understand what would happen if it entered the atmosphere today.

### NASA Datasets Used
1. **NASA Fireball and Bolide Data** (https://ssd.jpl.nasa.gov/tools/fireball.html)  
    -Used to retrieve observed meteor events (time, location, energy).  
2. **NASA Small Body Database** (https://ssd.jpl.nasa.gov/tools/sbdb_query.html)  
    -Provides orbital and physical parameters for near-Earth objects.  
3. **NASA CNEOS Meteor Impact Data**  
    -Used to estimate kinetic energy and potential impact force.

### How It Works
Earth Guardian connects with NASA’s public databases and visualizes meteors on an interactive map.  
For each meteor:
- It retrieves data from NASA’s API.
- Converts coordinates into a map visualization.
- Displays a risk analysis (energy, altitude, damage radius).

### Impact
Earth Guardian helps bridge the gap between scientists and the public.  
It transforms raw NASA datasets into something everyone can explore, understand, and learn from — bringing awareness to planetary defense in an engaging way.

### Note: 
This project Has been done solo and my coding skills are limited so AI has been used to assist with the code.
---

### How to Run Locally
```bash
cd ~/Desktop/earth_guardian
source venv/bin/activate
streamlit run app.py

-----

# Earth Guardian - NASA Space Apps Challenge 2025

Earth Guardian is a Streamlit web app that allows users to search for meteors by name and see impact data, risk levels, and expected effects. The project uses NASA-provided meteor data.

## How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/55ll/Lyrica-NASA-Space-App-Hackathon-.git
cd Lyrica-NASA-Space-App-Hackathon-

2. Create a virtual enviornment (optional)
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

3. Install depencies
pip install -r requirements.txt

4. Run the streamlit app
streamlit run app.py




