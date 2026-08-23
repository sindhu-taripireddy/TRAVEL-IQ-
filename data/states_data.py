"""
TRAVELIQ — Curated Travel Datasets for Indian States
Comprehensive travel intelligence with Exact Locations, Distance in Kilometers (km), and Nearby Food Spots.
"""

from typing import Dict, Any, List

STATES_DATA: Dict[str, Dict[str, Any]] = {
    # 1. ANDHRA PRADESH
    "andhra_pradesh": {
        "id": "andhra_pradesh",
        "name": "Andhra Pradesh",
        "tagline": "The Sunrise State — Pristine Coastlines, Ancient Temples & Majestic Canyons",
        "capital": "Amaravati",
        "best_time_to_visit": "October to March (Pleasant coastal weather, 20°C - 30°C)",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,200 - ₹2,000 / day (Budget lodges, RTC buses, local messes)",
            "mid_range": "₹3,000 - ₹5,500 / day (3-star hotels, cab hires, coastal restaurants)",
            "luxury": "₹8,000+ / day (Beachfront luxury resorts, private guided tours)"
        },
        "top_destinations": [
            {
                "name": "Visakhapatnam (RK Beach & Submarine Museum)",
                "category": "Coastal City & Heritage",
                "exact_location": "Beach Road, Pandurangapuram, Visakhapatnam, Andhra Pradesh 530003",
                "distance_from_hub": "4.5 km from Visakhapatnam Railway Station | 14 km from Vizag International Airport (VTZ)",
                "highlights": [
                    "INS Kursura Submarine Museum (historic decommissioned submarine on the sands of RK Beach)",
                    "TU-142 Aircraft Museum directly opposite the Submarine Museum",
                    "Kali Temple & Matsyadarsini Aquarium on Beach Road",
                    "Rushikonda Blue Flag Beach (12 km north along the scenic coastal road)",
                    "Kailasagiri Hilltop Park with ropeway (7 km north)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Subbayya Gari Hotel",
                        "location": "Diamond Park Road, Dwaraka Nagar, Visakhapatnam",
                        "distance_km": "3.8 km from RK Beach",
                        "specialty": "Iconic Butta Bhojanam (traditional Andhra full meal in a woven basket with Podis & Ghee)"
                    },
                    {
                        "name": "Sea Inn (Raju Gari Dhaba)",
                        "location": "Near Rushikonda Beach Road, Visakhapatnam",
                        "distance_km": "11.5 km from RK Beach (Next to Rushikonda)",
                        "specialty": "Spicy Chepala Vepudu (Fish Fry), Prawn Masala, and Natu Kodi Biryani"
                    },
                    {
                        "name": "Daspalla Executive Court (Heritage Restaurant)",
                        "location": "Waltair Main Road, Ram Nagar, Visakhapatnam",
                        "distance_km": "2.2 km from RK Beach",
                        "specialty": "Traditional Andhra Thali with Gongura Pachadi and Poori Korma"
                    }
                ]
            },
            {
                "name": "Araku Valley & Borra Caves",
                "category": "Hill Station & Geological Wonders",
                "exact_location": "Borra Caves, Ananthagiri Hills, Alluri Sitharama Raju District, Andhra Pradesh 531149",
                "distance_from_hub": "90 km from Visakhapatnam city center (Borra Caves) | 115 km from Vizag to Araku Valley",
                "highlights": [
                    "Million-year-old Borra Caves with natural limestone stalactites and stalagmites",
                    "Scenic Vistadome train passing through 58 tunnels and 84 bridges",
                    "Organic Arabica coffee plantations and Araku Tribal Museum",
                    "Katiki Waterfalls (7 km off-road from Borra Caves)",
                    "Chaparai Water Cascade (15 km from Araku Town)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Araku Bamboo Chicken Stalls",
                        "location": "Outside Borra Caves Gate & Araku Main Road",
                        "distance_km": "0.2 km from Borra Caves entrance",
                        "specialty": "Authentic Bamboo Chicken (chicken marinated in tribal spices, cooked oil-free inside green bamboo stalks)"
                    },
                    {
                        "name": "Vasundhara Restaurant (APTDC Haritha Valley Resort)",
                        "location": "Sarabhaguda, Araku Valley",
                        "distance_km": "1.5 km from Araku Tribal Museum",
                        "specialty": "South Indian Thali, Freshly Brewed Araku Filter Coffee, and Hot Mirchi Bajji"
                    }
                ]
            },
            {
                "name": "Gandikota (Grand Canyon of India) & Belum Caves",
                "category": "Geological Gorge & Heritage Fort",
                "exact_location": "Gandikota Village, Jammalamadugu Mandal, YSR Kadapa District, Andhra Pradesh 516434",
                "distance_from_hub": "15 km from Jammalamadugu | 78 km from Kadapa | 62 km from Belum Caves",
                "highlights": [
                    "Spectacular 300-foot deep river gorge carved through Erramala hills by the Penna River",
                    "13th-century Gandikota Fort, Raghunathaswamy Temple, and Jamia Masjid",
                    "Belum Caves with 3.5 km subterranean limestone passages and subterranean stream (Patalganga)",
                    "Cliffside sunrise viewpoint and riverside adventure camping"
                ],
                "nearby_food_places": [
                    {
                        "name": "Haritha Resort Restaurant (APTDC)",
                        "location": "Near Gandikota Fort Entrance, Gandikota",
                        "distance_km": "0.5 km from Gorge Viewpoint",
                        "specialty": "Rayalaseema Ragi Mudde with Natu Kodi Pulusu (Country Chicken Curry) & Andhra Meals"
                    },
                    {
                        "name": "Sri Balaji Mess",
                        "location": "Jammalamadugu Main Road, Jammalamadugu",
                        "distance_km": "14.5 km from Gandikota",
                        "specialty": "Spicy Rayalaseema Uggani Bajji (seasoned puffed rice with fried gram powder & mirchi bajji)"
                    }
                ]
            },
            {
                "name": "Tirupati & Tirumala",
                "category": "Sacred Pilgrimage & Hills",
                "exact_location": "Tirumala Hills, Tirupati District, Andhra Pradesh 517504",
                "distance_from_hub": "22 km from Tirupati City Railway Station (via Alipiri Ghat Road) | 38 km from Renigunta Airport (TIR)",
                "highlights": [
                    "Sri Venkateswara Temple atop the Seven Hills of Tirumala (world-renowned sacred shrine)",
                    "Silathoranam (rare geological natural rock arch, 1 km from temple)",
                    "Kapila Theertham waterfall and temple at the foot of Tirumala hills",
                    "Chandragiri Fort & Palaces (14 km southwest of Tirupati)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Tirumala Srivari Nitya Annaprasadam Complex",
                        "location": "Near East Mada Street, Tirumala",
                        "distance_km": "0.4 km from Main Venkateswara Temple",
                        "specialty": "Sacred free Annaprasadam feast with Sambar Rice, Chitrannam, Sweet Pongal & Srivari Laddu"
                    },
                    {
                        "name": "Bhimas Deluxe Hotel Restaurant",
                        "location": "G. Car Street, Near Railway Station, Tirupati",
                        "distance_km": "1.2 km from Tirupati Railway Station (foot of hills)",
                        "specialty": "Crisp Ghee Roast Dosa, Rava Dosa, Filter Coffee, and Pure Vegetarian Meals"
                    },
                    {
                        "name": "Andhra Spice Restaurant",
                        "location": "Air Bypass Road, Tirupati",
                        "distance_km": "3.5 km from Tirupati Bus Stand",
                        "specialty": "Andhra Biryani, Prawn Vepudu, and Gongura Mamsam (mutton curry)"
                    }
                ]
            },
            {
                "name": "Lepakshi & Veerabhadra Temple",
                "category": "Vijayanagara Art & Architecture",
                "exact_location": "Lepakshi Village, Sri Sathya Sai District, Andhra Pradesh 515331",
                "distance_from_hub": "14 km from Hindupur Railway Station | 120 km from Bengaluru Airport (BLR)",
                "highlights": [
                    "16th-century Veerabhadra Temple with 70 carved granite pillars and famous 'Hanging Pillar'",
                    "Monolithic Basavanna (Nandi) statue (4.5m high, 8.2m long carved from a single granite boulder)",
                    "Seven-hooded monolithic Nagalinga protecting a granite Shiva Linga"
                ],
                "nearby_food_places": [
                    {
                        "name": "Haritha Hotel Restaurant (APTDC)",
                        "location": "Opposite Monolithic Nandi, Lepakshi",
                        "distance_km": "0.3 km from Nandi Statue | 0.8 km from Temple",
                        "specialty": "Traditional Andhra Vegetarian Lunch with Pappu, Sambar, Rasam & Curd"
                    },
                    {
                        "name": "Hindupur Kamat Tiffin Center",
                        "location": "Main Road, Hindupur",
                        "distance_km": "13.5 km from Lepakshi",
                        "specialty": "Crisp Benne Dosa, Thatte Idli with spicy coconut chutney, and piping hot Filter Coffee"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Andhra Meals on Banana Leaf with spicy Pappu, Gongura Pachadi, Avakaya pickle, and pure Ghee",
            "Bamboo Chicken (Kodi) in Araku Valley cooked inside green bamboo over wood fire",
            "Pesarattu Upma (green gram crepe with semolina upma) and allam (ginger) chutney",
            "Rayalaseema Ragi Mudde with Natu Kodi Pulusu (country chicken curry)",
            "Royyala Vepudu (spicy coastal prawn fry) and Chepala Pulusu (tangy tamarind fish curry)",
            "Pootharekulu (paper-thin rice sweet from Atreyapuram) and Madugula Halwa"
        ],
        "local_transport": [
            "APSRTC Express, Ultra Deluxe & Garuda AC buses connect all districts.",
            "Scenic Vistadome train (08551/08552) operates daily on the Vizag - Araku route.",
            "Taxis & self-drive cars available at Vizag Airport, Tirupati, and Vijayawada."
        ],
        "travel_tips_and_rules": [
            "Book Tirumala Special Entry Darshan (₹300) tickets online 2-3 months ahead via the official TTD portal.",
            "Strict traditional dress code: Dhoti/Kurta or Pyjama for men; Saree or Chudidar with Dupatta for women at Tirumala.",
            "For Gandikota, visit early morning (6:00-8:30 AM) or sunset (5:00-6:30 PM) for comfortable temperatures and best light."
        ]
    },

    # 2. KERALA
    "kerala": {
        "id": "kerala",
        "name": "Kerala",
        "tagline": "God's Own Country — Emerald Backwaters, Misty Tea Hills & Ayurvedic Coastlines",
        "capital": "Thiruvananthapuram",
        "best_time_to_visit": "September to March (Pleasant weather); June to August for Monsoon Ayurveda",
        "ideal_duration": "5 to 8 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day (Homestays, KSRTC buses, local eateries)",
            "mid_range": "₹3,500 - ₹6,500 / day (Boutique heritage stays, AC cab, backwater cruises)",
            "luxury": "₹10,000+ / day (Luxury houseboat charters, 5-star backwater & wellness resorts)"
        },
        "top_destinations": [
            {
                "name": "Munnar & Tea Highlands",
                "category": "Hill Station & Wildlife",
                "exact_location": "Munnar, Idukki District, Kerala 685612",
                "distance_from_hub": "110 km from Cochin International Airport (COK) | 115 km from Aluva Railway Station",
                "highlights": [
                    "Eravikulam National Park (home to the endangered Nilgiri Tahr and Anamudi Peak)",
                    "Kolukkumalai Tea Estate (highest organic tea estate in the world at 2,160m)",
                    "Mattupetty Dam (13 km from Munnar Town) and Kundala Lake speed boating",
                    "Tata Tea Museum and KDHP tea tasting center (2 km from town)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Rapsy Restaurant",
                        "location": "Main Bazaar Road, Munnar Town",
                        "distance_km": "0.8 km from Munnar Central Bus Stand",
                        "specialty": "Kerala Parotta with Beef Fry / Chicken Roast, Spanish Omelette, and Cardamom Tea"
                    },
                    {
                        "name": "Saravana Bhavan (Pure Veg)",
                        "location": "Near KSRTC Bus Station, Munnar",
                        "distance_km": "0.4 km from Munnar Town Center",
                        "specialty": "Traditional Kerala Sadhya on banana leaf, Ghee Dosa, and Filter Coffee"
                    },
                    {
                        "name": "Guru's Restaurant",
                        "location": "Colony Road, Near Post Office, Munnar",
                        "distance_km": "1.1 km from Munnar Town",
                        "specialty": "Appam with Vegetable Stew, Fish Moilee, and Puttu with Kadala Curry"
                    }
                ]
            },
            {
                "name": "Alleppey (Alappuzha Backwaters)",
                "category": "Backwaters & Houseboat Cruises",
                "exact_location": "Punnamada Jetty & Finishing Point, Alappuzha, Kerala 688006",
                "distance_from_hub": "4 km from Alappuzha Railway Station | 82 km from Cochin International Airport (COK)",
                "highlights": [
                    "Overnight luxury Kettuvallam houseboat cruise along Vembanad Lake and Kuttanad canals",
                    "Shikara village canoe boat rides through narrow, peaceful waterways",
                    "Kumarakom Bird Sanctuary (32 km around the lake)",
                    "Alleppey Beach and 150-year-old historic pier (4.5 km from jetty)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Thaff Restaurant",
                        "location": "General Hospital Junction, CCSB Road, Alleppey",
                        "distance_km": "2.8 km from Punnamada Jetty",
                        "specialty": "Authentic Karimeen Pollichathu (Pearl spot fish roasted in banana leaf), Prawn Roast, and Appam"
                    },
                    {
                        "name": "Halais Restaurant",
                        "location": "Near Iron Bridge, Boat Jetty Road, Alleppey",
                        "distance_km": "2.2 km from Jetty",
                        "specialty": "Malabar Chicken Biryani, Thalassery Dum Biryani, and Dragon Chicken"
                    },
                    {
                        "name": "Brothers Hotel",
                        "location": "NH 66, Near Kommady Junction, Alleppey",
                        "distance_km": "3.5 km from Punnamada",
                        "specialty": "Traditional Duck Roast (Tharav Roast) and Kuttanad Fish Curry Meals"
                    }
                ]
            },
            {
                "name": "Fort Kochi & Mattancherry",
                "category": "Colonial Heritage & Arts",
                "exact_location": "Fort Kochi Beach & Princess Street, Kochi, Kerala 682001",
                "distance_from_hub": "12 km from Ernakulam South Railway Station | 42 km from Cochin Airport (COK)",
                "highlights": [
                    "Chinese Fishing Nets (Cheena Vala) along Vasco da Gama Square beach",
                    "St. Francis Church (oldest European church in India built in 1503)",
                    "Mattancherry Dutch Palace (3 km away) and Jewish Synagogue in Jew Town",
                    "Kathakali dance & Kalaripayattu martial art shows at Kerala Kathakali Centre"
                ],
                "nearby_food_places": [
                    {
                        "name": "Kashi Art Cafe",
                        "location": "Burgher Street, Fort Kochi",
                        "distance_km": "0.3 km from Fort Kochi Beach",
                        "specialty": "Artisan French Toast, Roasted Chicken Sandwiches, Cold Coffee, and Signature Chocolate Cake"
                    },
                    {
                        "name": "Oceanos Restaurant",
                        "location": "Elphinstone Residency, Jawahar Lane, Fort Kochi",
                        "distance_km": "0.5 km from Chinese Fishing Nets",
                        "specialty": "Fish Moilee with Appam, Tiger Prawn Masala, and Squid Pepper Fry"
                    },
                    {
                        "name": "Kayees Rahmathulla Hotel",
                        "location": "Gujarati Road, Mattancherry, Kochi",
                        "distance_km": "3.1 km from Fort Kochi Beach",
                        "specialty": "Legendary Kochi Mutton Dum Biryani cooked with pure ghee and special dates pickle"
                    }
                ]
            },
            {
                "name": "Varkala Cliff & Papanasam Beach",
                "category": "Coastal Cliffs & Spiritual Wellness",
                "exact_location": "North Cliff, Varkala, Thiruvananthapuram District, Kerala 695141",
                "distance_from_hub": "3.5 km from Varkala Sivagiri Railway Station | 45 km from Trivandrum International Airport (TRV)",
                "highlights": [
                    "Stunning red laterite cliffs towering directly above the Arabian Sea with seaside cafes",
                    "Papanasam Beach (holy mineral water springs believed to cleanse sins)",
                    "Janardhana Swami Temple (2,000-year-old shrine dedicated to Lord Vishnu, 1.5 km away)",
                    "Kapil Lake & Beach (6 km north where the lake meets the sea)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Cafe del Mar",
                        "location": "North Cliff, Varkala",
                        "distance_km": "0.1 km from Cliff Viewpoint",
                        "specialty": "Fresh Tandoori Fish Catch of the Day, Wood-fired Pizzas, and Fresh Tropical Smoothies"
                    },
                    {
                        "name": "Darjeeling Cafe",
                        "location": "Middle Cliff, Varkala",
                        "distance_km": "0.3 km along the cliff walkway",
                        "specialty": "Tibetan Momos, Shakshuka, Fresh Falafel Platter, and Sunset Brews"
                    },
                    {
                        "name": "Suprabhatham Vegetarian Restaurant",
                        "location": "Near Janardhana Temple, Temple Road, Varkala",
                        "distance_km": "1.4 km from North Cliff",
                        "specialty": "Organic Ayurvedic Kerala Thali with fresh coconut dishes and herbal water"
                    }
                ]
            },
            {
                "name": "Wayanad (Edakkal Caves & Banasura Dam)",
                "category": "Rainforests, Waterfalls & Prehistoric Heritage",
                "exact_location": "Nenmeni, Wayanad District, Kerala 673595",
                "distance_from_hub": "85 km from Kozhikode (Calicut) Railway Station (CCJ) & Airport",
                "highlights": [
                    "Edakkal Caves with Stone Age petroglyphs and rock carvings dating back to 6000 BCE",
                    "Banasura Sagar Dam — Largest earthen dam in India with speedboating (28 km from Kalpetta)",
                    "Chembra Peak trek and heart-shaped natural lake (Hridaya Saras)",
                    "Soochipara (Sentinel Rock) 3-tiered waterfall"
                ],
                "nearby_food_places": [
                    {
                        "name": "1980's A Nostalgic Restaurant",
                        "location": "Kalpetta Bypass Road, Wayanad",
                        "distance_km": "12 km from Edakkal Caves (in Kalpetta hub)",
                        "specialty": "Traditional Kerala Sadhya, Bamboo Biryani, Kanthari Chicken, and Payasam"
                    },
                    {
                        "name": "Wilton Restaurant",
                        "location": "Sultan Bathery Main Road, Wayanad",
                        "distance_km": "11 km from Edakkal Caves",
                        "specialty": "Malabar Chicken Dum Biryani, Al Faham Chicken with Kubboos, and Neychoru with Beef Roast"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Kerala Traditional Sadhya on banana leaf with 24+ vegetarian dishes, Sambar, Avial, Thoran, and Payasam",
            "Appam with creamy Vegetable Stew or spiced Chicken Stew",
            "Karimeen Pollichathu (Pearl Spot fish wrapped in banana leaf and pan-roasted with shallot masala)",
            "Malabar Parotta with Kerala Beef Roast or Chicken Pepper Fry",
            "Puttu and Kadala Curry (steamed rice cylinder with black chickpea curry)",
            "Thalassery Biryani with fragrant Kaima/Jeerakasala rice"
        ],
        "local_transport": [
            "KSRTC State Transport buses run frequent express routes connecting all districts.",
            "State Water Transport Department (SWTD) passenger ferries offer budget canal rides (₹10 - ₹30).",
            "Pre-paid taxis and auto-rickshaws available at all major railway stations."
        ],
        "travel_tips_and_rules": [
            "Book government DTPC-approved houseboats at Alleppey Punnamada Jetty with certified safety gear.",
            "Modest clothing is strictly enforced at traditional temples like Sree Padmanabhaswamy Temple in Trivandrum.",
            "Wear sturdy shoes for the steep hike up to Edakkal Caves in Wayanad (~1 km uphill climb)."
        ]
    },

    # 3. GOA
    "goa": {
        "id": "goa",
        "name": "Goa",
        "tagline": "Pearl of the Orient — Golden Sands, Portuguese Heritage & Vibrant Coastal Culture",
        "capital": "Panaji",
        "best_time_to_visit": "November to February (Sunny, breezy, festive season)",
        "ideal_duration": "3 to 5 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day",
            "mid_range": "₹3,500 - ₹6,500 / day",
            "luxury": "₹10,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Aguada Fort & Calangute-Baga Beaches",
                "category": "Historic Fort & Vibrant Coast",
                "exact_location": "Fort Aguada Road, Candolim, North Goa 403515",
                "distance_from_hub": "15 km from Panaji Capital | 40 km from Dabolim Airport (GOI) | 30 km from Mopa Airport (GOX)",
                "highlights": [
                    "17th-century Portuguese coastal fort with historic 4-storey lighthouse (1864)",
                    "Massive freshwater storage cistern holding 2.3 million gallons",
                    "Calangute & Baga Beaches (6 km north) with watersports: parasailing, banana boat, jet skiing",
                    "Baga Tito's Lane and lively seaside beach shacks"
                ],
                "nearby_food_places": [
                    {
                        "name": "Britto's Beach Shack",
                        "location": "Baga Beach, Calangute, Goa",
                        "distance_km": "7.2 km from Aguada Fort (on Baga Sands)",
                        "specialty": "Goan Prawn Curry with Rice, Butter Garlic Crab, Baked Crab, and Seafood Platters"
                    },
                    {
                        "name": "Fisherman's Wharf",
                        "location": "Fort Aguada Road, Candolim, Goa",
                        "distance_km": "2.1 km from Aguada Fort",
                        "specialty": "Goan Fish Curry (Kingfish), Pork Vindaloo, Rawa Fried Prawns, and Bebinca"
                    },
                    {
                        "name": "Infantaria Cafe & Bakery",
                        "location": "Calangute-Baga Junction, Calangute, Goa",
                        "distance_km": "5.8 km from Aguada Fort",
                        "specialty": "Fresh Goan Bebinca, Croissants, English Breakfast, and Poi Bread"
                    }
                ]
            },
            {
                "name": "Old Goa (Basilica of Bom Jesus & Se Cathedral)",
                "category": "UNESCO World Heritage Monuments",
                "exact_location": "Old Goa Road, Velha Goa, Goa 403402",
                "distance_from_hub": "10 km east of Panaji Capital | 25 km from Karmali Railway Station",
                "highlights": [
                    "Basilica of Bom Jesus (1605) holding mortal sacred remains of St. Francis Xavier",
                    "Se Cathedral (Sé Catedral de Santa Catarina) housing the famous acoustic Golden Bell",
                    "Church of St. Francis of Assisi and Archaeological Museum",
                    "Fontainhas Latin Quarter in Panaji (10 km west)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Viva Panjim",
                        "location": "House No 178, 31st January Road, Fontainhas, Panaji",
                        "distance_km": "10.2 km from Old Goa (in Fontainhas)",
                        "specialty": "Authentic Goan Prawn Balchão, Chicken Xacuti, Pork Sorpotel, and Fish Curry Rice"
                    },
                    {
                        "name": "The Caravela Cafe and Bistro",
                        "location": "31st January Road, Fontainhas, Panaji",
                        "distance_km": "10.5 km from Old Goa",
                        "specialty": "Artisan Goan Roast Coffee, Serradura (Portuguese dessert), and Bebinca with Ice Cream"
                    }
                ]
            },
            {
                "name": "Dudhsagar Waterfalls & Palolem Beach",
                "category": "Waterfall & Scenic South Goa Coast",
                "exact_location": "Sonaulim, Goa 403410 | Palolem Beach, Canacona, South Goa 403702",
                "distance_from_hub": "60 km from Panaji Capital | 46 km from Margao Railway Station",
                "highlights": [
                    "Spectacular 4-tiered 310m high Dudhsagar Waterfall (Sea of Milk)",
                    "Jeep safari through Bhagwan Mahavir Wildlife Sanctuary & Mollem National Park",
                    "Palolem Crescent Beach in South Goa with calm swimming waters and kayaking",
                    "Cabo de Rama Fort offering panoramic sea views"
                ],
                "nearby_food_places": [
                    {
                        "name": "Dropadi Restaurant",
                        "location": "Palolem Beachfront, Canacona, Goa",
                        "distance_km": "0.1 km from Palolem Shore",
                        "specialty": "Tandoori Lobster, Garlic Butter Prawns, and Fresh Seafood Grills"
                    },
                    {
                        "name": "Space Goa Organic Cafe",
                        "location": "Canacona-Agonda Road, South Goa",
                        "distance_km": "2.5 km from Palolem Beach",
                        "specialty": "Organic Smoothies, Vegan Pancakes, and Fresh Farm Salads"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Goan Fish Curry (Xitt Codi) with Kingfish in coconut-kokum gravy",
            "Pork/Chicken Vindaloo with palm vinegar and red Kashmiri chilies",
            "Prawn Balchão (fiery tangy pickled prawn delicacy)",
            "Chicken Xacuti cooked with roasted spices and toasted poppy seeds",
            "Traditional Bebinca (7-layer coconut milk and ghee dessert)"
        ],
        "local_transport": [
            "Self-drive scooter/bike rental: ₹350 - ₹600/day (helmet & valid license mandatory).",
            "GoaMiles government app for transparent metered taxi bookings."
        ],
        "travel_tips_and_rules": [
            "Drinking alcohol on open public beaches is illegal with fines up to ₹2,000 - ₹10,000.",
            "Modest clothing covering shoulders and knees required inside Basilica of Bom Jesus."
        ]
    },

    # 4. RAJASTHAN
    "rajasthan": {
        "id": "rajasthan",
        "name": "Rajasthan",
        "tagline": "Land of Kings — Majestic Forts, Golden Deserts & Royal Palaces",
        "capital": "Jaipur",
        "best_time_to_visit": "October to March (Pleasant days, cool desert nights)",
        "ideal_duration": "5 to 9 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day",
            "mid_range": "₹3,500 - ₹7,000 / day",
            "luxury": "₹12,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Jaipur (Amber Fort & Hawa Mahal)",
                "category": "Royal Heritage & Palaces",
                "exact_location": "Devisinghpura, Amer, Jaipur, Rajasthan 302001",
                "distance_from_hub": "11 km from Jaipur City Center | 13 km from Jaipur Junction Railway Station",
                "highlights": [
                    "Amber Fort & Palace with Sheesh Mahal (Mirror Palace) overlooking Maota Lake",
                    "Hawa Mahal (Palace of Winds, 10 km south in the walled Pink City) with 953 jharokhas",
                    "City Palace complex and UNESCO Jantar Mantar observatory",
                    "Nahargarh Fort sunset panoramic viewpoint (6 km from Amber)"
                ],
                "nearby_food_places": [
                    {
                        "name": "1135 AD (Royal Heritage Dining)",
                        "location": "Inside Amber Fort, Level 2, Jaleb Chowk, Amer, Jaipur",
                        "distance_km": "0.1 km inside Amber Fort",
                        "specialty": "Royal Rajasthani Thali, Laal Maas, Junglee Maas, and Shahi Ghevar"
                    },
                    {
                        "name": "Laxmi Mishthan Bhandar (LMB)",
                        "location": "Johari Bazaar, Pink City, Jaipur",
                        "distance_km": "9.8 km from Amber Fort (Near Hawa Mahal)",
                        "specialty": "Authentic Pyaaz Kachori, Paneer Ghevar, Dal Baati Churma, and Rajbhog"
                    },
                    {
                        "name": "Rawat Mishthan Bhandar",
                        "location": "Station Road, Sindhi Camp, Jaipur",
                        "distance_km": "12.5 km from Amber Fort",
                        "specialty": "World-famous piping hot Pyaaz Kachori and Mawa Kachori"
                    }
                ]
            },
            {
                "name": "Udaipur (City Palace & Lake Pichola)",
                "category": "Romantic Palaces & Lakes",
                "exact_location": "City Palace Complex, Udaipur, Rajasthan 313001",
                "distance_from_hub": "3.5 km from Udaipur City Railway Station | 24 km from Maharana Pratap Airport (UDR)",
                "highlights": [
                    "City Palace on the eastern banks of Lake Pichola (largest palace complex in Rajasthan)",
                    "Boat cruise across Lake Pichola visiting Jag Mandir island palace",
                    "Bagore Ki Haveli at Gangaur Ghat with evening folk dance & puppet show (0.4 km)",
                    "Saheliyon-ki-Bari (Courtyard of Maidens, 4 km north)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Ambrai Restaurant (Amet Haveli)",
                        "location": "Naga Nagri, Outside Chandpole, Udaipur",
                        "distance_km": "1.2 km from City Palace (Directly opposite palace across lake)",
                        "specialty": "Lakeside dining with Laal Maas, Ker Sangri, Murg Tikka, and Garlic Naan"
                    },
                    {
                        "name": "Traditional Khana Restaurant",
                        "location": "Panchwati, Udaipur",
                        "distance_km": "3.8 km from City Palace",
                        "specialty": "Unlimited Rajasthani Thali with 5 types of Baati, Gatte Ki Sabzi, and Churma"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Dal Baati Churma (baked wheat balls with spiced lentils, pure ghee, and sweet churma)",
            "Laal Maas (fiery royal mutton curry with Mathania red chilies)",
            "Ker Sangri (desert bean and wild berry delicacy)",
            "Pyaaz Kachori and Mirchi Vada with tangy tamarind chutney",
            "Ghevar (traditional honeycomb dessert topped with rabri)"
        ],
        "local_transport": [
            "RSRTC Deluxe and Volvo buses connect major cities.",
            "Auto-rickshaws, Ola, and Uber active across Jaipur, Udaipur, and Jodhpur."
        ],
        "travel_tips_and_rules": [
            "Buy Composite Entry Tickets in Jaipur to save money across multiple monuments.",
            "Carry warm layers for chilly desert nights in Jodhpur, Jaisalmer, and Bikaner."
        ]
    },

    # 5. UTTARAKHAND
    "uttarakhand": {
        "id": "uttarakhand",
        "name": "Uttarakhand",
        "tagline": "Devbhoomi — Sacred Rivers, Himalayan Treks & Yoga Capital of the World",
        "capital": "Dehradun",
        "best_time_to_visit": "March to June (Pleasant weather); October to February for Snow in Auli",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,400 - ₹2,200 / day",
            "mid_range": "₹3,200 - ₹6,000 / day",
            "luxury": "₹9,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Rishikesh (Triveni Ghat & White Water Rafting)",
                "category": "Yoga, River Rafting & Spiritual",
                "exact_location": "Triveni Ghat & Tapovan, Rishikesh, Dehradun District, Uttarakhand 249201",
                "distance_from_hub": "2 km from Rishikesh Railway Station | 21 km from Jolly Grant Airport Dehradun (DED)",
                "highlights": [
                    "Triveni Ghat Evening Maha Ganga Aarti with synchronized chanting and floating diyas",
                    "White water river rafting on the Ganges (Marine Drive/Shivpuri to NIM Beach: 16 km / 24 km)",
                    "Lakshman Jhula, Ram Jhula, and Beatles Ashram (Chaurasi Kutia)",
                    "Neelkanth Mahadev Temple in the Pauri Garhwal foothills (30 km)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Chotiwala Restaurant",
                        "location": "Near Ram Jhula, Swargashram, Rishikesh",
                        "distance_km": "2.8 km from Triveni Ghat (via Ram Jhula)",
                        "specialty": "Iconic Garhwali & North Indian Vegetarian Thali, Paneer Butter Masala, and Lassi"
                    },
                    {
                        "name": "The Sitting Elephant (Hotel EllBee Ganga View)",
                        "location": "Haridwar Road, Palika Nagar, Rishikesh",
                        "distance_km": "0.6 km from Triveni Ghat",
                        "specialty": "Rooftop Ganges view dining with Kafuli, Aloo Ke Gutke, Dal Makhani, and Kheer"
                    },
                    {
                        "name": "Beatles Cafe (Cafe 60's)",
                        "location": "Paidal Marg, Tapovan, Rishikesh",
                        "distance_km": "4.5 km from Triveni Ghat (in Tapovan hub)",
                        "specialty": "Vegan burgers, Gluten-free pastas, Masala Chai, and panoramic river views"
                    }
                ]
            },
            {
                "name": "Nainital (Naini Lake & Mall Road)",
                "category": "Lake District & Hill Station",
                "exact_location": "Mallital, Nainital, Uttarakhand 263001",
                "distance_from_hub": "34 km from Kathgodam Railway Station | 70 km from Pantnagar Airport (PGH)",
                "highlights": [
                    "Naini Lake yachting and paddle boating surrounded by seven emerald mountain peaks",
                    "Naina Devi Temple on the northern shore of Naini Lake",
                    "Snow View Point cable car ride overlooking the high Himalayas",
                    "Tiffin Top (Dorothy's Seat) 4 km trek with 360-degree valley views"
                ],
                "nearby_food_places": [
                    {
                        "name": "Machan Restaurant",
                        "location": "The Mall Road, Nainital",
                        "distance_km": "0.3 km along Mall Road by the lake",
                        "specialty": "Kumaoni Thali, Aloo Ke Gutke, Paneer Tikka, and Lemon Pepper Chicken"
                    },
                    {
                        "name": "Sakley's Restaurant & Pastry Shop",
                        "location": "Poplar Building, Mallital, Nainital",
                        "distance_km": "0.6 km from Naina Devi Temple",
                        "specialty": "Roasted Lamb Chops, Apple Pie, Sizzlers, and Hot Chocolate"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Kafuli (thick spinach and fenugreek leaf curry cooked in iron kadhai with rice)",
            "Chainsoo (roasted black gram dal curry with aromatic garlic and cumin)",
            "Aloo Ke Gutke (crispy spiced mountain potatoes with fried red chilies)",
            "Bhatt ki Churkani (black soybean curry)",
            "Bal Mithai (roasted khoya sweet coated with sugar balls) and Singodi"
        ],
        "local_transport": [
            "UTC State buses and shared taxis connect Dehradun, Rishikesh, Haridwar, and Nainital.",
            "Dehradun Jolly Grant Airport connects to major metros."
        ],
        "travel_tips_and_rules": [
            "Always wear life jackets during river rafting in Rishikesh.",
            "Avoid driving on steep mountain ghat roads during peak monsoon landslides (July-August)."
        ]
    },

    # 6. JAMMU & KASHMIR / LADAKH
    "kashmir_ladakh": {
        "id": "kashmir_ladakh",
        "name": "Jammu & Kashmir & Ladakh",
        "tagline": "Paradise on Earth & Land of High Mountain Passes",
        "capital": "Srinagar / Leh",
        "best_time_to_visit": "April to October (Pleasant meadows & lakes); Dec to Feb for Gulmarg Snow",
        "ideal_duration": "6 to 9 Days",
        "estimated_daily_budget": {
            "budget": "₹1,800 - ₹2,800 / day",
            "mid_range": "₹4,000 - ₹7,500 / day",
            "luxury": "₹12,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Srinagar (Dal Lake & Mughal Gardens)",
                "category": "Lakes & Mughal Gardens",
                "exact_location": "Boulevard Road, Dal Lake, Srinagar, Jammu & Kashmir 190001",
                "distance_from_hub": "12 km from Srinagar Railway Station | 14 km from Sheikh ul-Alam Airport (SXR)",
                "highlights": [
                    "Shikara rides on Dal Lake past floating lotus gardens and craft houseboats",
                    "Mughal Gardens: Shalimar Bagh (built by Jahangir in 1619) & Nishat Bagh",
                    "Shankaracharya Temple atop Gopadari Hill (5 km from Dal Lake)",
                    "Gulmarg Gondola & Meadow of Flowers (50 km west from Srinagar)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Ahdoos Restaurant",
                        "location": "Residency Road, Regal Chowk, Srinagar",
                        "distance_km": "2.8 km from Dal Lake Boulevard",
                        "specialty": "Authentic Kashmiri Wazwan: Rogan Josh, Gushtaba, Rista, Tabak Maaz, and Kashmiri Kahwa"
                    },
                    {
                        "name": "Mughal Darbar",
                        "location": "Residency Road, Srinagar",
                        "distance_km": "3.0 km from Dal Lake",
                        "specialty": "Traditional Trami Wazwan Feast, Kashmiri Dum Aloo, and Seekh Tujj (kebabs)"
                    },
                    {
                        "name": "Chai Jaai Tea Room",
                        "location": "The Bund Road, Munshi Bagh, Srinagar",
                        "distance_km": "2.5 km from Dal Lake",
                        "specialty": "Traditional Saffron Kahwa, Noon Chai (pink salted tea), and freshly baked Kashmiri Bakarkhani"
                    }
                ]
            },
            {
                "name": "Ladakh (Pangong Lake & Leh Palace)",
                "category": "High Passes & Monasteries",
                "exact_location": "Leh & Pangong Tso, UT of Ladakh 194101",
                "distance_from_hub": "4.5 km from Kushok Bakula Rimpochee Airport (IXL) | 160 km from Leh to Pangong Tso via Chang La",
                "highlights": [
                    "Pangong Tso high-altitude lake (4,350m) famous for vivid shades of turquoise and deep blue",
                    "17th-century 9-storey Leh Palace overlooking the town and Shanti Stupa",
                    "Nubra Valley sand dunes & double-humped camel rides (via Khardung La at 5,359m)",
                    "Thiksey Monastery with 49-foot Maitreya Buddha statue (19 km from Leh)"
                ],
                "nearby_food_places": [
                    {
                        "name": "The Tibetan Kitchen",
                        "location": "Fort Road, Near Hotel Yak Tail, Leh",
                        "distance_km": "0.6 km from Leh Main Bazaar | 1.5 km from Leh Palace",
                        "specialty": "Traditional Gyathuk (noodle soup), Steamed Mutton Momos, Tingmo (steamed bread), and Shaphalay"
                    },
                    {
                        "name": "Bon Appetit",
                        "location": "Changspa Road, Below Moravian Mission School, Leh",
                        "distance_km": "1.4 km from Leh Palace",
                        "specialty": "Ladakhi Platter, Wood-fired Pizzas, and Apricot Crumble with Mountain views"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Kashmiri Wazwan multi-course feast with Rogan Josh, Gushtaba, Rista, and Tabak Maaz",
            "Kahwa (aromatic green tea brewed with saffron, crushed almonds, and cardamom)",
            "Yakhni (tender mutton cooked in mild yogurt gravy with fennel)",
            "Ladakhi Thukpa (steamed noodle soup), Momos, and Butter Tea"
        ],
        "local_transport": [
            "Prepaid union taxis for Gulmarg, Pahalgam, and Sonamarg.",
            "4x4 SUV hires (Scorpio/Innova) required for Leh-Ladakh circuits."
        ],
        "travel_tips_and_rules": [
            "Acclimatize in Leh for at least 24-48 hours before ascending to Khardung La or Pangong Lake.",
            "Book Gulmarg Gondola tickets online weeks ahead on the official portal."
        ]
    },

    # 7. MAHARASHTRA
    "maharashtra": {
        "id": "maharashtra",
        "name": "Maharashtra",
        "tagline": "Gateway of India — Maratha Forts, Western Ghats & Dynamic Metros",
        "capital": "Mumbai",
        "best_time_to_visit": "October to March (Pleasant); July to Sept for lush monsoon waterfalls",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day",
            "mid_range": "₹3,500 - ₹6,500 / day",
            "luxury": "₹10,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Mumbai (Gateway of India & Marine Drive)",
                "category": "Colonial Icons & Coastal Promenade",
                "exact_location": "Apollo Bunder, Colaba, Mumbai, Maharashtra 400001",
                "distance_from_hub": "2.8 km from Chhatrapati Shivaji Maharaj Terminus (CSMT) | 24 km from Mumbai Airport (BOM)",
                "highlights": [
                    "Gateway of India overlooking Mumbai Harbour and historic Taj Mahal Palace Hotel",
                    "Marine Drive (Queen's Necklace) 3.6 km crescent boulevard",
                    "Elephanta Caves UNESCO rock-cut cave temples (1-hour ferry from Gateway)",
                    "Chhatrapati Shivaji Maharaj Terminus (CSMT) UNESCO gothic architectural wonder"
                ],
                "nearby_food_places": [
                    {
                        "name": "Bademiya",
                        "location": "Tulloch Road, Behind Taj Mahal Palace Hotel, Colaba, Mumbai",
                        "distance_km": "0.3 km from Gateway of India",
                        "specialty": "Legendary Chicken Tikka Rolls, Seekh Kebabs, and Baida Roti"
                    },
                    {
                        "name": "Cafe Mondegar & Leopold Cafe",
                        "location": "Colaba Causeway, Near Regal Cinema, Mumbai",
                        "distance_km": "0.6 km from Gateway of India",
                        "specialty": "Vintage cafe ambience, Draught Beer, Keema Pav, and Fish & Chips"
                    },
                    {
                        "name": "Sardar Pav Bhaji",
                        "location": "166-A, Tardeo Road, Junction, Mumbai",
                        "distance_km": "6.8 km from Gateway of India (Near Mumbai Central)",
                        "specialty": "Extra butter Pav Bhaji served with soft butter-toasted pav and lemon"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Vada Pav, Pav Bhaji, and Mumbai Street Style Sev Puri / Pani Puri",
            "Misal Pav (spicy sprouted moth bean curry with farsan and lemon)",
            "Puran Poli (sweet flatbread stuffed with spiced jaggery and chana dal)",
            "Malvani Fish Curry (Surmai / Pomfret in coconut-kokum gravy with Vade)"
        ],
        "local_transport": [
            "Mumbai Local Trains and Metro system offer fast commute.",
            "MSRTC Shivneri AC Volvo buses connect Mumbai to Pune and Lonavala."
        ],
        "travel_tips_and_rules": [
            "Avoid local trains during peak rush hours (8:30-10:30 AM and 6:00-8:30 PM).",
            "Take the government-approved ferry from Gateway of India to Elephanta Caves."
        ]
    },

    # 8. GUJARAT
    "gujarat": {
        "id": "gujarat",
        "name": "Gujarat",
        "tagline": "Land of Legends — White Salt Desert, Asiatic Lions & Vibrant Heritage",
        "capital": "Gandhinagar",
        "best_time_to_visit": "November to February (Rann Utsav Season, pleasant weather)",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,300 - ₹2,200 / day",
            "mid_range": "₹3,000 - ₹6,000 / day",
            "luxury": "₹9,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Rann of Kutch (White Desert & Dhordo)",
                "category": "Geological Salt Desert & Cultural Festival",
                "exact_location": "Dhordo Village, Kutch District, Gujarat 370510",
                "distance_from_hub": "80 km from Bhuj Railway Station & Airport (BHJ)",
                "highlights": [
                    "Great Rann of Kutch — World's largest white salt desert gleaming under moonlight",
                    "Rann Utsav cultural tent city with Kutchi folk dance and handicraft bazaars",
                    "Kala Dungar (Black Hill) highest point in Kutch (45 km from Dhordo)",
                    "Dholavira UNESCO Harappan Indus Valley archaeological ruins"
                ],
                "nearby_food_places": [
                    {
                        "name": "Rann Utsav Dining Halls (Dhordo)",
                        "location": "Tent City, Dhordo, Kutch",
                        "distance_km": "0.5 km from White Desert Gate",
                        "specialty": "Authentic Kutchi Thali with Bajra No Rotlo, Ringna No Oro (eggplant mash), and fresh Gulab Pak"
                    },
                    {
                        "name": "Toran Dining Hall (Bhuj)",
                        "location": "Near Jubilee Ground, Bhuj",
                        "distance_km": "80 km from Dhordo (in transit city Bhuj)",
                        "specialty": "Unlimited Gujarati Thali with sweet Kadhi, Farsan, Dal, and Shrikhand"
                    }
                ]
            },
            {
                "name": "Statue of Unity & Kevadia",
                "category": "Modern Monument & Engineering Marvel",
                "exact_location": "Sardar Sarovar Dam, Kevadia, Narmada District, Gujarat 393155",
                "distance_from_hub": "5 km from Ekta Nagar (Kevadiya) Railway Station | 90 km from Vadodara Airport (BDQ)",
                "highlights": [
                    "World's tallest statue (182 meters) dedicated to Sardar Vallabhbhai Patel",
                    "Viewing gallery at 153 meters overlooking Narmada River and dam reservoir",
                    "Valley of Flowers, Jungle Safari, and Glow Garden"
                ],
                "nearby_food_places": [
                    {
                        "name": "Ekta Food Court",
                        "location": "Near Statue of Unity Entrance, Kevadia",
                        "distance_km": "0.4 km from Statue Gate",
                        "specialty": "Gujarati Snacks (Dhokla, Khandvi, Thepla), South Indian meals, and North Indian Thali"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Authentic Gujarati Thali with sweet-tangy Dal, Kadhi, Rotli, Shaak, and Farsan",
            "Khaman Dhokla, Khandvi, and Handvo with mustard tempering",
            "Fafda-Jalebi with raw papaya sambharo and fried green chilies",
            "Undhiyu (winter mixed vegetable stew with fenugreek dumplings)"
        ],
        "local_transport": [
            "GSRTC Volvo & Gurjarnagri buses connect all towns.",
            "Vande Bharat Express connects Mumbai, Surat, and Ahmedabad."
        ],
        "travel_tips_and_rules": [
            "Gujarat is a dry state; alcohol is prohibited without an authorized tourist permit.",
            "Book Statue of Unity and Rann Utsav tickets online in advance to avoid long weekend lines."
        ]
    },

    # 9. UTTAR PRADESH
    "uttar_pradesh": {
        "id": "uttar_pradesh",
        "name": "Uttar Pradesh",
        "tagline": "Heartland of India — The Taj Mahal, Eternal Ghats of Varanasi & Sacred Rivers",
        "capital": "Lucknow",
        "best_time_to_visit": "October to March (Cool, pleasant weather)",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,200 - ₹2,000 / day",
            "mid_range": "₹2,800 - ₹5,500 / day",
            "luxury": "₹8,500+ / day"
        },
        "top_destinations": [
            {
                "name": "Agra (Taj Mahal & Agra Fort)",
                "category": "UNESCO World Heritage Wonder",
                "exact_location": "Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh 282001",
                "distance_from_hub": "4.5 km from Agra Cantt Railway Station | 12 km from Agra Airport (AGR)",
                "highlights": [
                    "Taj Mahal — White marble masterpiece built by Emperor Shah Jahan on Yamuna banks",
                    "Agra Fort (2.5 km away, red sandstone citadel housing Jahangiri Mahal)",
                    "Mehtab Bagh sunset viewpoint across the Yamuna River",
                    "Fatehpur Sikri (36 km west, royal capital built by Akbar)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Pinch of Spice",
                        "location": "1076/2, Fatehabad Road, Tajganj, Agra",
                        "distance_km": "2.1 km from Taj Mahal East Gate",
                        "specialty": "Murg Boti Masala, Dal Makhani, Paneer Lababdar, and Garlic Naan"
                    },
                    {
                        "name": "Panchhi Petha Store",
                        "location": "Near Taj East Gate & Sadar Bazaar, Agra",
                        "distance_km": "0.8 km from Taj Mahal",
                        "specialty": "Famous Agra Petha (Kesar Petha, Paan Petha, Chocolate Petha, and Angoori Petha)"
                    },
                    {
                        "name": "Dasaprakash (Pure Veg)",
                        "location": "Meher Cinema Complex, Gwalior Road, Agra Cantt",
                        "distance_km": "4.2 km from Taj Mahal",
                        "specialty": "Crispy Ghee Roast Dosa, North Indian Thali, and Ice Cream sundaes"
                    }
                ]
            },
            {
                "name": "Varanasi (Dashashwamedh Ghat & Kashi Vishwanath)",
                "category": "Spiritual Capital & Ancient Ghats",
                "exact_location": "Dashashwamedh Ghat Road, Bangali Tola, Varanasi, Uttar Pradesh 221001",
                "distance_from_hub": "4.2 km from Varanasi Junction Railway Station | 25 km from Lal Bahadur Shastri Airport (VNS)",
                "highlights": [
                    "Grand Evening Ganga Aarti at Dashashwamedh Ghat with synchronized brass lamps",
                    "Sunrise boat ride along the Ganges past 84 sacred stone ghats",
                    "Kashi Vishwanath Temple and the Grand Vishwanath Corridor (0.5 km)",
                    "Sarnath Dhamek Stupa (10 km northeast where Lord Buddha gave his first sermon)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Kashi Chaat Bhandar",
                        "location": "D.53/98, Luxa Road, Godowlia, Varanasi",
                        "distance_km": "0.6 km from Dashashwamedh Ghat",
                        "specialty": "Famous Banarasi Tamatar Chaat, Palak Chaat, Dahi Golgappe, and Gulab Jamun"
                    },
                    {
                        "name": "Blue Lassi Shop",
                        "location": "CK 12/68, Bangali Tola, Near Manikarnika Ghat, Varanasi",
                        "distance_km": "0.9 km along the river alleyways",
                        "specialty": "Over 70 varieties of fresh hand-churned fruit lassi in earthen clay cups (Kullad)"
                    },
                    {
                        "name": "Shree Ram Bhandar",
                        "location": "Thatheri Bazaar, Godowlia, Varanasi",
                        "distance_km": "0.8 km from Kashi Vishwanath Temple",
                        "specialty": "Morning breakfast of Crispy Kachori-Sabzi with hot Jalebis and winter Malaiyo"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Lucknowi Awadhi Dum Biryani and Galouti / Tunday Kebabs with Ulte Tawe Ka Paratha",
            "Banarasi Tamatar Chaat and Crispy Kachori-Sabzi with Jalebi at dawn",
            "Banarasi Paan and Malaiyo (winter saffron milk froth dessert in clay pots)",
            "Agra Petha (sweet ash gourd candy in saffron, paan, and gulab flavors)"
        ],
        "local_transport": [
            "Vande Bharat & Gatimaan Express connect Delhi to Agra, Kanpur, and Varanasi.",
            "E-rickshaws and auto-rickshaws widely popular for navigating historic lanes."
        ],
        "travel_tips_and_rules": [
            "Taj Mahal is closed on Fridays for public visits.",
            "Book Taj Mahal tickets online on the official ASI portal to skip ticket counter lines."
        ]
    },

    # 10. WEST BENGAL & SIKKIM
    "west_bengal_sikkim": {
        "id": "west_bengal_sikkim",
        "name": "West Bengal & Sikkim",
        "tagline": "Sweetest Part of India & Himalayan Wonderland",
        "capital": "Kolkata / Gangtok",
        "best_time_to_visit": "October to April (Festive, clear mountain views)",
        "ideal_duration": "5 to 8 Days",
        "estimated_daily_budget": {
            "budget": "₹1,400 - ₹2,400 / day",
            "mid_range": "₹3,200 - ₹6,500 / day",
            "luxury": "₹9,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Darjeeling (Tiger Hill & Himalayan Toy Train)",
                "category": "Tea Estates & Himalayan Peaks",
                "exact_location": "Tiger Hill & Mall Road, Darjeeling, West Bengal 734101",
                "distance_from_hub": "70 km from New Jalpaiguri (NJP) Railway Station | 75 km from Bagdogra Airport (IXB)",
                "highlights": [
                    "Tiger Hill sunrise over Mount Kanchenjunga (world's 3rd highest mountain)",
                    "Darjeeling Himalayan Railway (UNESCO Toy Train) ride through Batasia Loop",
                    "Happy Valley Tea Estate tours and tasting world-famous Darjeeling Muscatel tea",
                    "Himalayan Mountaineering Institute (HMI) and Padmaja Naidu Himalayan Zoo"
                ],
                "nearby_food_places": [
                    {
                        "name": "Glenary's Bakery & Cafe",
                        "location": "Nehru Road, Near Chowrasta, Darjeeling",
                        "distance_km": "0.3 km from Chowrasta Mall",
                        "specialty": "Fresh Apple Pie, Scones, Darjeeling First Flush Tea, and Roast Pork with Mashed Potatoes"
                    },
                    {
                        "name": "Keventers Restaurant",
                        "location": "1, Clubside, Gandhi Road, Darjeeling",
                        "distance_km": "0.4 km from Chowrasta",
                        "specialty": "Open rooftop English breakfast with Pork Sausages, Salami, Ham, Fried Eggs, and Hot Chocolate"
                    },
                    {
                        "name": "Kunga Restaurant",
                        "location": "Gandhi Road, Near Taxi Stand, Darjeeling",
                        "distance_km": "0.5 km from Mall Road",
                        "specialty": "Authentic Steamed Pork/Chicken Momos, Gyathuk, and Wonton Soup"
                    }
                ]
            },
            {
                "name": "Kolkata (Victoria Memorial & Howrah Bridge)",
                "category": "Colonial Heritage & Cultural Capital",
                "exact_location": "Queens Way, Maidan, Kolkata, West Bengal 700071",
                "distance_from_hub": "4.5 km from Howrah Railway Station | 18 km from Netaji Subhash Chandra Bose Airport (CCU)",
                "highlights": [
                    "Victoria Memorial white marble palace surrounded by 64 acres of gardens",
                    "Howrah Bridge cantilever engineering marvel over the Hooghly River",
                    "Dakshineswar Kali Temple and Belur Math (12 km north)",
                    "Park Street culinary avenue and historic College Street book market"
                ],
                "nearby_food_places": [
                    {
                        "name": "Peter Cat",
                        "location": "18A, Park Street, Kolkata",
                        "distance_km": "1.8 km from Victoria Memorial",
                        "specialty": "Legendary Chelo Kebab (buttered rice with grilled chicken & mutton seekh kebabs) and Iranian Tea"
                    },
                    {
                        "name": "6 Ballygunge Place",
                        "location": "6, Ballygunge Place, Kolkata",
                        "distance_km": "3.5 km from Victoria Memorial",
                        "specialty": "Authentic Bengali Feast: Daab Chingri (prawns in tender coconut), Kosha Mangsho, and Bhetki Paturi"
                    },
                    {
                        "name": "K.C. Das Sweets",
                        "location": "Esplanade East, Kolkata",
                        "distance_km": "2.2 km from Victoria Memorial",
                        "specialty": "Original Canned Rosogolla, Sondesh, and Mishti Doi"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Macher Jhol (traditional Bengali fish curry in mustard paste) with steamed rice",
            "Kosha Mangsho (rich slow-cooked mutton curry) with fluffy Lucchi",
            "Kolkata Style Biryani with aromatic rice, tender meat, and spiced potato",
            "Authentic Rosogolla, Mishti Doi, Sandesh, and Chomchom"
        ],
        "local_transport": [
            "Kolkata Metro, yellow Ambassador taxis, and Hooghly river ferries.",
            "Shared 4x4 Bolero / Scorpio taxis for Siliguri to Darjeeling / Gangtok."
        ],
        "travel_tips_and_rules": [
            "Start early at 3:45 AM for the Tiger Hill sunrise in Darjeeling to beat traffic.",
            "Protected Area Permits (PAP) are required for visiting Nathula Pass in Sikkim."
        ]
    },

    # 11. KARNATAKA
    "karnataka": {
        "id": "karnataka",
        "name": "Karnataka",
        "tagline": "One State, Many Worlds — UNESCO Heritage, Coffee Highlands & Pristine Coast",
        "capital": "Bengaluru",
        "best_time_to_visit": "October to March",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,400 - ₹2,200 / day",
            "mid_range": "₹3,200 - ₹6,000 / day",
            "luxury": "₹8,500+ / day"
        },
        "top_destinations": [
            {
                "name": "Hampi (Vijayanagara UNESCO Ruins)",
                "category": "UNESCO Ancient Ruins & Boulders",
                "exact_location": "Hampi, Vijayanagara District, Karnataka 583239",
                "distance_from_hub": "13 km from Hospet Junction Railway Station | 350 km from Bengaluru",
                "highlights": [
                    "Virupaksha Temple on the banks of Tungabhadra River",
                    "Vijaya Vittala Temple with iconic Stone Chariot and Musical Pillars (3.5 km from Virupaksha)",
                    "Lotus Mahal and Elephant Stables inside Zenana Enclosure",
                    "Matanga Hill sunrise panoramic view of the boulder landscape"
                ],
                "nearby_food_places": [
                    {
                        "name": "Mango Tree Restaurant",
                        "location": "Near Virupaksha Temple Bazaar, Hampi",
                        "distance_km": "0.4 km from Virupaksha Temple",
                        "specialty": "South Indian Thali, Israeli Shakshuka, Banana Nut Lassi, and Fresh Fruit Smoothies"
                    },
                    {
                        "name": "Laughing Buddha Cafe",
                        "location": "Hampi Island (Hippies Island), Sanapur Road",
                        "distance_km": "4.2 km across Tungabhadra River (via Sanapur)",
                        "specialty": "Riverside floor seating with Wood-fired Pizza, Falafel Platters, and Filter Coffee"
                    }
                ]
            },
            {
                "name": "Mysore (Mysuru Palace & Chamundi Hills)",
                "category": "Royal Heritage & Palaces",
                "exact_location": "Sayyaji Rao Road, Agrahara, Chamrajpura, Mysuru, Karnataka 570001",
                "distance_from_hub": "2 km from Mysuru Junction Railway Station | 140 km from Bengaluru Airport",
                "highlights": [
                    "Mysore Palace (Amba Vilas) illuminated with 100,000 bulbs on Sunday evenings",
                    "Chamundeshwari Temple atop Chamundi Hills with giant monolithic Nandi (13 km away)",
                    "Devaraja Market for sandalwood, silk sarees, and spices (1 km from Palace)",
                    "Brindavan Gardens with musical fountain show (18 km)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Mylari Hotel (Original Vinayaka Mylari)",
                        "location": "Shop No. 79, Nazarbad Main Road, Mysuru",
                        "distance_km": "1.8 km from Mysore Palace",
                        "specialty": "World-famous Mylari Benne Dosa (ultra-soft butter dosa with coconut-onion paste) and Filter Coffee"
                    },
                    {
                        "name": "Guru Sweets",
                        "location": "Sayyaji Rao Road, Devaraja Market, Mysuru",
                        "distance_km": "0.9 km from Mysore Palace",
                        "specialty": "Original Mysore Pak (invented by the royal chef of Mysore Palace in 1935)"
                    },
                    {
                        "name": "RRR Restaurant",
                        "location": "Gandhi Square, Near Mysore Palace, Mysuru",
                        "distance_km": "0.6 km from Palace North Gate",
                        "specialty": "Authentic Andhra & Mysore style spicy Mutton/Chicken Biryani served on banana leaf"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Bisi Bele Bath with boondi and ghee",
            "Mysore Masala Dosa with red chili-garlic chutney paste",
            "Neer Dosa with Mangalorean Kori Rotti (chicken curry)",
            "Coorg Pandi Curry (pork curry with Kachampuli fruit vinegar)",
            "Mysore Pak and Filter Coffee"
        ],
        "local_transport": [
            "KSRTC Airavat & Rajahamsa buses connect all major hubs.",
            "Rental bikes widely popular for exploring Hampi and Gokarna."
        ],
        "travel_tips_and_rules": [
            "Rent a bicycle or moped to explore Hampi's expansive archaeological area.",
            "Check Mysore Palace illumination timings (Sundays & holidays: 7:00 PM - 7:45 PM)."
        ]
    },

    # 12. TAMIL NADU
    "tamil_nadu": {
        "id": "tamil_nadu",
        "name": "Tamil Nadu",
        "tagline": "Land of Living Chola Temples, Classical Heritage & Misty Nilgiris",
        "capital": "Chennai",
        "best_time_to_visit": "November to February",
        "ideal_duration": "5 to 8 Days",
        "estimated_daily_budget": {
            "budget": "₹1,200 - ₹2,000 / day",
            "mid_range": "₹3,000 - ₹5,500 / day",
            "luxury": "₹8,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Mahabalipuram (Shore Temple & Pancha Rathas)",
                "category": "UNESCO Rock Reliefs & Shore Temples",
                "exact_location": "Shore Temple Road, Mamallapuram, Chengalpattu District, Tamil Nadu 603104",
                "distance_from_hub": "55 km south of Chennai along the East Coast Road (ECR)",
                "highlights": [
                    "7th-century Shore Temple overlooking the Bay of Bengal",
                    "Arjuna's Penance (Descent of the Ganges) giant open-air rock relief (1 km away)",
                    "Pancha Rathas monolithic five chariots carved from single granite boulders",
                    "Krishna's Butterball natural precariously balanced boulder"
                ],
                "nearby_food_places": [
                    {
                        "name": "Moonrakers Restaurant",
                        "location": "Othavadai Street, Fisherman's Colony, Mahabalipuram",
                        "distance_km": "0.7 km from Shore Temple",
                        "specialty": "Fresh Catch Grilled Tiger Prawns, Butter Garlic Crab, Calamari, and Fish Curry Meals"
                    },
                    {
                        "name": "Seashore Restaurant",
                        "location": "Near Shore Temple Gate, Mahabalipuram",
                        "distance_km": "0.2 km from Shore Temple",
                        "specialty": "Beachfront seafood platter, Chettinad Crab Masala, and Tender Coconut"
                    }
                ]
            },
            {
                "name": "Madurai (Meenakshi Amman Temple)",
                "category": "Monumental Dravidian Architecture",
                "exact_location": "Madurai Main, Madurai, Tamil Nadu 625001",
                "distance_from_hub": "1.5 km from Madurai Junction Railway Station | 12 km from Madurai Airport (IXM)",
                "highlights": [
                    "Meenakshi Amman Temple with 14 towering colorful gopurams and Hall of Thousand Pillars",
                    "Thirumalai Nayakkar Mahal with giant stucco pillars (2 km from temple)",
                    "Pudhu Mandapam traditional tailor and brass market outside temple gate"
                ],
                "nearby_food_places": [
                    {
                        "name": "Famous Jigarthanda Shop",
                        "location": "East Marret Street, Madurai",
                        "distance_km": "0.8 km from Meenakshi Temple East Gate",
                        "specialty": "Original Famous Jigarthanda (rich almond gum, condensed milk, nannari syrup, and ice cream)"
                    },
                    {
                        "name": "Amma Mess",
                        "location": "Alagar Kovil Main Road, Tallakulam, Madurai",
                        "distance_km": "3.5 km from Meenakshi Temple",
                        "specialty": "Bone Marrow Omelette, Crab Omelette, Chettinad Mutton Chops, and Fish Curry"
                    },
                    {
                        "name": "Murugan Idli Shop",
                        "location": "West Mada Street, Near Meenakshi Temple, Madurai",
                        "distance_km": "0.2 km from Temple West Tower",
                        "specialty": "Ultra-soft Steamed Idlis served with 4 types of fresh chutneys and Podi with Ghee"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Chettinad Pepper Chicken and Kozhi Varuval with aromatic whole roasted spices",
            "Crispy Medu Vada, Steamed Idlis, and Pongal with coconut chutney and Sambar",
            "Madurai Jigarthanda (sweet cold beverage with almond gum and ice cream)",
            "Kothu Parotta tossed on iron griddle with eggs/meat and salna"
        ],
        "local_transport": [
            "SETC & TNSTC state buses offer affordable transit to all towns.",
            "Southern Railway connects all major temple and coastal cities."
        ],
        "travel_tips_and_rules": [
            "Strict temple dress code: Dhoti/Shirt for men, Saree/Salwar for women across Madurai and Thanjavur temples.",
            "Deposit mobile phones and cameras at designated counters outside Meenakshi Amman Temple."
        ]
    },

    # 13. HIMACHAL PRADESH
    "himachal_pradesh": {
        "id": "himachal_pradesh",
        "name": "Himachal Pradesh",
        "tagline": "Devbhoomi — Snow Peaks, Serene Pine Valleys & Himalayan Thrills",
        "capital": "Shimla",
        "best_time_to_visit": "March to June (Summer flowers & trekking); Dec to Feb (Snowfall)",
        "ideal_duration": "5 to 8 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day",
            "mid_range": "₹3,500 - ₹6,500 / day",
            "luxury": "₹9,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Manali (Solang Valley & Atal Tunnel)",
                "category": "Snow Adventures & Valley of Gods",
                "exact_location": "Solang Valley & Old Manali, Kullu District, Himachal Pradesh 175131",
                "distance_from_hub": "13 km from Manali Town to Solang Valley | 28 km to Atal Tunnel (South Portal)",
                "highlights": [
                    "Solang Valley adventure sports (paragliding, zorbing, skiing in winter)",
                    "Atal Tunnel (9.02 km long engineering marvel) leading to Sissu waterfalls in Lahaul",
                    "Hadimba Temple (1553) surrounded by cedar deodar forests (2 km from Mall Road)",
                    "Old Manali vibrant riverside cafes and music live spots"
                ],
                "nearby_food_places": [
                    {
                        "name": "Johnson's Cafe",
                        "location": "Circuit House Road, Siyal, Manali",
                        "distance_km": "0.8 km from Mall Road Manali",
                        "specialty": "Wood-fired Trout Fish in almond butter sauce, Thin-crust Pizzas, and Apple Crumble"
                    },
                    {
                        "name": "Cafe 1947",
                        "location": "Near Nehru Kund, Old Manali",
                        "distance_km": "3.5 km from Mall Road (on Manalsu riverbanks)",
                        "specialty": "Handmade Ravioli, Risotto, Burgers, and Fresh Ginger Lemon Honey Tea"
                    },
                    {
                        "name": "Chopsticks Restaurant",
                        "location": "The Mall Road, Manali",
                        "distance_km": "0.1 km on Mall Road",
                        "specialty": "Tibetan Momos, Thukpa, Gyathuk, and Himachali Siddu"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Himachali Siddu (steamed wheat bun stuffed with spiced walnut/poppy seed paste with ghee)",
            "Dham (traditional festive feast with Madra, Khatta, and Chana Dal)",
            "Chha Gosht (marinated mutton curry in yogurt gravy)",
            "Kullu Trout Fish pan-fried in butter with lemon"
        ],
        "local_transport": [
            "HRTC Volvo buses connect Chandigarh/Delhi to Shimla, Manali, and Dharamshala.",
            "Local 4x4 taxis recommended for high passes in winter."
        ],
        "travel_tips_and_rules": [
            "Rohtang Pass requires an online permit issued by Himachal Tourism.",
            "Dress in layers as temperatures can drop quickly near Atal Tunnel and mountain passes."
        ]
    },

    # 14. MADHYA PRADESH
    "madhya_pradesh": {
        "id": "madhya_pradesh",
        "name": "Madhya Pradesh",
        "tagline": "The Heart of Incredible India — Tiger Safaris, Khajuraho Sculptures & Sacred Ghats",
        "capital": "Bhopal",
        "best_time_to_visit": "October to March",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,200 - ₹2,000 / day",
            "mid_range": "₹2,800 - ₹5,500 / day",
            "luxury": "₹8,500+ / day"
        },
        "top_destinations": [
            {
                "name": "Khajuraho Group of Temples",
                "category": "UNESCO World Heritage Architecture",
                "exact_location": "Sevagram, Khajuraho, Chhatarpur District, Madhya Pradesh 471606",
                "distance_from_hub": "5 km from Khajuraho Railway Station | 4 km from Khajuraho Airport (HJR)",
                "highlights": [
                    "Western Group of Temples: Kandariya Mahadeva Temple, Lakshmana Temple, and Chitragupta Temple",
                    "Eastern Group: Parsvanatha Jain Temple and Ghantai Temple (2 km)",
                    "Raneh Falls & Canyon on Ken River (20 km away)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Raja Cafe",
                        "location": "Main Temple Road, Opposite Western Group of Temples, Khajuraho",
                        "distance_km": "0.1 km directly opposite temple complex",
                        "specialty": "Temple view dining with Dal Bafla, Paneer Butter Masala, Fresh Salads, and Cold Coffee"
                    },
                    {
                        "name": "Agrasen Dining Hall",
                        "location": "Near Jain Temple, Khajuraho",
                        "distance_km": "1.2 km from Western Temples",
                        "specialty": "Authentic Bundelkhandi Thali with Dal Bafla, Kadhi, and Mawa Bati sweet"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Indori Poha-Jalebi with sev and jeeravan masala",
            "Dal Bafla (boiled and baked wheat balls dipped in ghee with dal)",
            "Bhutte Ka Kees (spiced grated corn cooked in milk)"
        ],
        "local_transport": [
            "MP Tourism buses connect all heritage and wildlife circuits."
        ],
        "travel_tips_and_rules": [
            "Book National Park safaris (Kanha/Bandhavgarh) months ahead on the MP Forest portal."
        ]
    },

    # 15. ODISHA
    "odisha": {
        "id": "odisha",
        "name": "Odisha",
        "tagline": "India's Best Kept Secret — Golden Triangle, Sun Temple & Chilika Lagoon",
        "capital": "Bhubaneswar",
        "best_time_to_visit": "October to March",
        "ideal_duration": "4 to 6 Days",
        "estimated_daily_budget": {
            "budget": "₹1,200 - ₹1,900 / day",
            "mid_range": "₹2,600 - ₹5,000 / day",
            "luxury": "₹7,500+ / day"
        },
        "top_destinations": [
            {
                "name": "Puri & Konark Sun Temple",
                "category": "UNESCO World Heritage & Coastal Shrine",
                "exact_location": "Konark, Puri District, Odisha 752111",
                "distance_from_hub": "35 km from Puri Railway Station (via Marine Drive) | 65 km from Bhubaneswar Airport (BBI)",
                "highlights": [
                    "13th-century Konark Sun Temple designed as a colossal chariot of Surya with 24 carved stone wheels",
                    "Shree Jagannath Temple in Puri (35 km west)",
                    "Puri Golden Beach (Blue Flag certified) and Chandrabhaga Beach (3 km from Konark)",
                    "Chilika Lake dolphin sanctuary at Satapada (50 km from Puri)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Wildgrass Restaurant",
                        "location": "VIP Road, Near Police Line, Puri",
                        "distance_km": "2.5 km from Jagannath Temple | 32 km from Konark",
                        "specialty": "Machha Besara (mustard fish curry), Prawn Malai Curry, Dalma, and Chhena Poda"
                    },
                    {
                        "name": "Kamath Restaurant (OTDC Yatri Nivas)",
                        "location": "Near Konark Sun Temple, Konark",
                        "distance_km": "0.4 km from Sun Temple entrance",
                        "specialty": "Traditional Odia Vegetarian Thali, Kanika (sweet pulao), and hot Chhena Jhili"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Chhena Poda (caramelized roasted cottage cheese dessert with cardamom)",
            "Dalma (wholesome lentils cooked with raw papaya, pumpkin, and panch phoron)",
            "Machha Besara (fish curry in pungent mustard paste)"
        ],
        "local_transport": [
            "OSRTC buses and Marine Drive taxis connect Bhubaneswar, Puri, and Konark."
        ],
        "travel_tips_and_rules": [
            "Non-Hindus are not permitted inside Jagannath Temple."
        ]
    },

    # 16. MEGHALAYA
    "meghalaya": {
        "id": "meghalaya",
        "name": "Meghalaya",
        "tagline": "Abode of Clouds — Living Root Bridges, Crystal Rivers & Cascading Waterfalls",
        "capital": "Shillong",
        "best_time_to_visit": "October to April",
        "ideal_duration": "4 to 7 Days",
        "estimated_daily_budget": {
            "budget": "₹1,500 - ₹2,500 / day",
            "mid_range": "₹3,500 - ₹6,500 / day",
            "luxury": "₹9,000+ / day"
        },
        "top_destinations": [
            {
                "name": "Cherrapunji (Sohra & Living Root Bridges)",
                "category": "Waterfalls & Bio-Engineering Wonders",
                "exact_location": "Nongriat Village & Sohra, East Khasi Hills, Meghalaya 793108",
                "distance_from_hub": "54 km south of Shillong Capital | 150 km from Guwahati Airport (GAU)",
                "highlights": [
                    "Double Decker Living Root Bridge in Nongriat (intertwined rubber tree roots)",
                    "Nohkalikai Falls (India's tallest plunge waterfall dropping 340m, 7 km from Sohra)",
                    "Seven Sisters Falls and Wei Sawdong 3-tier cascade",
                    "Dawki Umngot crystal river (85 km east from Cherrapunji)"
                ],
                "nearby_food_places": [
                    {
                        "name": "Orange Roots Restaurant (Pure Veg)",
                        "location": "Sohra-Shella Road, Cherrapunji",
                        "distance_km": "3.2 km from Nohkalikai Falls",
                        "specialty": "South Indian Thali, Dosa, Khasi style vegetarian meals, and Mountain Ginger Tea"
                    },
                    {
                        "name": "Dylan's Cafe",
                        "location": "Tripura Castle Road, Dhankheti, Shillong",
                        "distance_km": "52 km from Cherrapunji (in Shillong hub)",
                        "specialty": "Bob Dylan tribute cafe, Burgers, Pork Ribs, Waffles, and Hot Chocolate"
                    },
                    {
                        "name": "Trattoria",
                        "location": "Police Bazar, Shillong",
                        "distance_km": "54 km from Cherrapunji",
                        "specialty": "Authentic Khasi dishes: Jadoh (rice with meat broth), Dohneiiong (black sesame pork), and Tungrymbai"
                    }
                ]
            }
        ],
        "authentic_cuisine": [
            "Jadoh (rice cooked with meat broth, ginger, and turmeric)",
            "Dohneiiong (pork curry prepared with black sesame seeds)",
            "Tungrymbai and Pukhlein (sweet fried rice flour cake)"
        ],
        "local_transport": [
            "Local tourist cabs in Shillong for day trips to Cherrapunji and Dawki."
        ],
        "travel_tips_and_rules": [
            "The trek to Double Decker Root Bridge requires descending and climbing ~3,500 stone steps.",
            "Dawki river is most crystal clear from November to March."
        ]
    }
}


def get_all_states() -> List[Dict[str, Any]]:
    """Return list of all states with summary metadata."""
    summaries = []
    for sid, s in STATES_DATA.items():
        summaries.append({
            "id": s["id"],
            "name": s["name"],
            "tagline": s["tagline"],
            "capital": s["capital"],
            "best_time_to_visit": s["best_time_to_visit"],
            "ideal_duration": s["ideal_duration"],
            "top_attractions_count": len(s["top_destinations"]),
            "sample_attractions": [d["name"] for d in s["top_destinations"][:3]]
        })
    return summaries


def get_state_by_id(state_id: str) -> Dict[str, Any]:
    """Retrieve full data for a specific state by ID or normalized name."""
    normalized = state_id.strip().lower().replace(" ", "_").replace("-", "_")
    
    if normalized in STATES_DATA:
        return STATES_DATA[normalized]
        
    for sid, s in STATES_DATA.items():
        if normalized in sid or normalized in s["name"].lower():
            return s
            
    return STATES_DATA["andhra_pradesh"]
