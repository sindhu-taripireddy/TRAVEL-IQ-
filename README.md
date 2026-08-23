# ✈️ TRAVELIQ — AI State Travel Research & Smart Trip Planner

> **"Research destinations. Build smarter trips."**  
> An AI travel research assistant and personalized trip planner pre-loaded with comprehensive datasets for Indian states including **Andhra Pradesh**, **Kerala**, **Goa**, **Rajasthan**, **Karnataka**, **Tamil Nadu**, and **Himachal Pradesh**.

---

## 📌 Overview
TRAVELIQ delivers instant travel intelligence, authentic food guides, budget breakdowns, transportation advice, and personalized day-by-day itineraries tailored to specific Indian states without requiring document uploads.

---

## 🌟 Supported States & Curated Datasets

| State | Highlights & Hubs | Culinary Delights | Best Season |
| :--- | :--- | :--- | :--- |
| **Andhra Pradesh** | Visakhapatnam, Araku Valley, Borra Caves, Gandikota Gorge, Tirupati, Lepakshi | Andhra Banana Leaf Meals, Gongura Pachadi, Bamboo Chicken, Pesarattu | Oct - Mar |
| **Kerala** | Munnar Tea Hills, Alleppey Backwaters, Fort Kochi, Wayanad, Varkala Cliffs | Kerala Sadya, Appam with Stew, Karimeen Pollichathu, Malabar Parotta | Sep - Mar |
| **Goa** | Calangute, Baga, Palolem, Old Goa Churches, Aguada Fort, Dudhsagar Falls | Goan Fish Curry, Vindaloo, Bebinca, Prawn Balchão | Nov - Feb |
| **Rajasthan** | Jaipur Pink City, Udaipur Lake Pichola, Jodhpur Mehrangarh, Jaisalmer Dunes | Dal Baati Churma, Laal Maas, Ker Sangri, Ghevar | Oct - Mar |
| **Karnataka** | Hampi Ruins, Coorg Coffee Highlands, Mysore Palace, Gokarna Beaches | Bisi Bele Bath, Mysore Masala Dosa, Pandi Curry, Filter Coffee | Oct - Mar |
| **Tamil Nadu** | Mahabalipuram Shore Temples, Madurai Meenakshi, Ooty Nilgiris, Rameswaram | Chettinad Pepper Chicken, Jigarthanda, Medu Vada, Pongal | Nov - Feb |
| **Himachal Pradesh**| Manali, Solang Valley, Shimla Ridge, Dharamshala Dalai Lama Temple, Spiti | Himachali Siddu, Dham Feast, Chha Gosht, Kullu Trout | Mar - Jun / Dec - Feb |

---

## 🚀 Key Features

1. **State Selector Bar**: Switch instantly between Andhra Pradesh, Kerala, Goa, Rajasthan, Karnataka, Tamil Nadu, and Himachal Pradesh.
2. **State Highlights & Quick Guide**: Real-time display of key destinations, authentic dishes, best season to visit, and ideal duration.
3. **Personalized State Trip Planner**: Formulates customized Day-by-Day itineraries (Morning, Afternoon, Evening) factoring in duration, budget, and travel interests (History, Beaches, Food, Nature, Adventure, Temples, Culture).
4. **AI Travel Research Chatbot**: Conversational assistant answering questions about attractions, timings, transportation, budget estimates, and local safety rules.
5. **Google Gemini LLM Integration with Local Fallback**: Seamlessly runs with Google Gemini when `GEMINI_API_KEY` is provided, and includes a built-in state intelligence engine out of the box.

---

## 📁 Project Structure

```
traveliq/
│
├── app.py                     # Flask web server & REST API endpoints
├── planner.py                 # Direct state travel intelligence & Gemini AI planner
├── test_state_planner.py      # Automated test script for state datasets and APIs
├── requirements.txt           # Python dependencies
├── .env                       # Environment configuration (Gemini API key)
├── .env.example               # Environment template
├── README.md                  # Complete documentation
│
├── data/
│   └── states_data.py         # Curated state datasets (Andhra Pradesh, Kerala, etc.)
│
├── templates/
│   └── index.html             # State travel research dashboard
│
└── static/
    ├── style.css              # Vibrant travel stylesheet
    └── script.js              # Client state management & REST API integration
```

---

## ⚙️ Installation & Setup

### 1. Activate Environment & Install Dependencies
```bash
# Windows:
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Optional: Configure Gemini API Key
In `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run the Application
```bash
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 🎬 How to Use & Demo

1. **Explore States**: Click on any state pill (e.g. **Andhra Pradesh** or **Kerala**).
2. **Review Highlights**: Inspect the left panel for key destinations (Visakhapatnam, Gandikota, Munnar, etc.) and authentic culinary tags.
3. **Generate Itinerary**: Set duration (e.g., `4 days`), budget (`₹18,000`), and interests (`History`, `Food`, `Beaches`), then click **"🗺️ Generate My State Trip"**.
4. **Ask Questions**: In the chat panel, ask *"What is the best way to travel from Vizag to Araku Valley?"* or *"What authentic dishes should I try in Kerala?"*.
