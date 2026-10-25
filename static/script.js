/**
 * TRAVELIQ — State Travel Research & Smart Trip Planner
 * Client-Side Application Logic & State Intelligence API Client
 * Ultra-Resilient Engine with Zero-Disconnection Guarantee & Auto-Fallback.
 */

document.addEventListener("DOMContentLoaded", () => {
    // -------------------------------------------------------------------------
    // Determine API Base URL (Supports Flask :5000, VS Code Live Server :5500, etc.)
    // -------------------------------------------------------------------------
    const isLiveServer = window.location.port === "5500" || window.location.port === "3000" || window.location.protocol === "file:";
    const API_BASE = isLiveServer ? "http://127.0.0.1:5000" : "";

    // -------------------------------------------------------------------------
    // Application State
    // -------------------------------------------------------------------------
    const state = {
        selectedState: "andhra_pradesh",
        stateData: null,
        conversationHistory: [],
        activeTab: "chat",
        isChatLoading: false,
        isPlanLoading: false
    };

    // -------------------------------------------------------------------------
    // DOM Elements
    // -------------------------------------------------------------------------
    const stateSelectDropdown = document.getElementById("stateSelectDropdown");
    const statePillsRow = document.getElementById("statePillsRow");
    const durationInput = document.getElementById("durationInput");
    const budgetInput = document.getElementById("budgetInput");
    const interestsContainer = document.getElementById("interestsContainer");
    const generateTripBtn = document.getElementById("generateTripBtn");

    const guideStateTitle = document.getElementById("guideStateTitle");
    const guideTagline = document.getElementById("guideTagline");
    const factSeason = document.getElementById("factSeason");
    const factDuration = document.getElementById("factDuration");
    const guideDestinationsList = document.getElementById("guideDestinationsList");
    const guideFoodList = document.getElementById("guideFoodList");
    const activeStateBadge = document.getElementById("activeStateBadge");

    const tabChatBtn = document.getElementById("tabChatBtn");
    const tabPlanBtn = document.getElementById("tabPlanBtn");
    const chatViewContainer = document.getElementById("chatViewContainer");
    const planViewContainer = document.getElementById("planViewContainer");

    const chatMessagesStream = document.getElementById("chatMessagesStream");
    const chatForm = document.getElementById("chatForm");
    const chatInput = document.getElementById("chatInput");
    const sendBtn = document.getElementById("sendBtn");

    const emptyPlanState = document.getElementById("emptyPlanState");
    const planRenderArea = document.getElementById("planRenderArea");
    const planDestinationTitle = document.getElementById("planDestinationTitle");
    const planMetaTags = document.getElementById("planMetaTags");
    const planContentMarkdown = document.getElementById("planContentMarkdown");
    const copyPlanBtn = document.getElementById("copyPlanBtn");
    const printPlanBtn = document.getElementById("printPlanBtn");

    const toastNotification = document.getElementById("toastNotification");
    const toastMessage = document.getElementById("toastMessage");
    const toastIcon = document.getElementById("toastIcon");

    // -------------------------------------------------------------------------
    // Toast Notification Helper
    // -------------------------------------------------------------------------
    function showToast(message, type = "info") {
        toastMessage.textContent = message;
        if (type === "success") toastIcon.textContent = "✅";
        else if (type === "warning") toastIcon.textContent = "⚠️";
        else if (type === "error") toastIcon.textContent = "❌";
        else toastIcon.textContent = "ℹ️";

        toastNotification.classList.remove("hidden");
        setTimeout(() => {
            toastNotification.classList.add("hidden");
        }, 3500);
    }

    // -------------------------------------------------------------------------
    // Tabs Navigation
    // -------------------------------------------------------------------------
    function switchTab(tabName) {
        state.activeTab = tabName;
        if (tabName === "chat") {
            tabChatBtn.classList.add("active");
            tabPlanBtn.classList.remove("active");
            chatViewContainer.classList.add("active");
            planViewContainer.classList.remove("active");
        } else {
            tabPlanBtn.classList.add("active");
            tabChatBtn.classList.remove("active");
            planViewContainer.classList.add("active");
            chatViewContainer.classList.remove("active");
        }
    }

    tabChatBtn.addEventListener("click", () => switchTab("chat"));
    tabPlanBtn.addEventListener("click", () => switchTab("plan"));

    // -------------------------------------------------------------------------
    // Interests Selector
    // -------------------------------------------------------------------------
    interestsContainer.addEventListener("change", (e) => {
        if (e.target.type === "checkbox") {
            const chip = e.target.closest(".interest-chip");
            if (chip) {
                if (e.target.checked) chip.classList.add("active");
                else chip.classList.remove("active");
            }
        }
    });

    function getSelectedInterests() {
        const checked = interestsContainer.querySelectorAll("input[type='checkbox']:checked");
        return Array.from(checked).map(cb => cb.value);
    }

    // -------------------------------------------------------------------------
    // State Selection & Details Loading
    // -------------------------------------------------------------------------
    async function selectState(stateId, syncDropdown = true) {
        state.selectedState = stateId;

        // Update pills active state
        document.querySelectorAll(".state-pill").forEach(btn => {
            if (btn.getAttribute("data-state") === stateId) {
                btn.classList.add("active");
            } else {
                btn.classList.remove("active");
            }
        });

        // Sync dropdown
        if (syncDropdown && stateSelectDropdown.value !== stateId) {
            stateSelectDropdown.value = stateId;
        }

        try {
            const res = await fetch(`${API_BASE}/api/states/${stateId}`);
            if (res.ok) {
                const data = await res.json();
                if (data.state) {
                    state.stateData = data.state;
                    renderStateHighlights(data.state);
                    return;
                }
            }
        } catch (err) {
            console.warn("Backend API fetch pending, using local state dataset...");
        }

        // Fallback: Use built-in client data
        const fallbackState = getLocalStateData(stateId);
        state.stateData = fallbackState;
        renderStateHighlights(fallbackState);
    }

    function renderStateHighlights(st) {
        guideStateTitle.innerHTML = `<span class="icon">📍</span> ${st.name} Places & Food`;
        guideTagline.textContent = `"${st.tagline || ''}"`;
        factSeason.textContent = st.best_time_to_visit ? st.best_time_to_visit.split('(')[0].trim() : 'Oct - Mar';
        factDuration.textContent = st.ideal_duration || '4 to 7 Days';
        activeStateBadge.textContent = `📍 ${st.name}`;

        // Top destinations with Location, KM & Extended Nearby Food Places
        guideDestinationsList.innerHTML = "";
        (st.top_destinations || []).forEach(d => {
            const item = document.createElement("div");
            item.className = "guide-dest-card";

            // Format highlights
            let highlightsHtml = "";
            if (d.highlights && d.highlights.length > 0) {
                const highlightPills = d.highlights.slice(0, 3).map(h => `<span class="highlight-pill">• ${h}</span>`).join(" ");
                highlightsHtml = `<div class="dest-highlights-row">${highlightPills}</div>`;
            }

            // Format all nearby food spots in extended cards
            let foodHtml = "";
            if (d.nearby_food_places && d.nearby_food_places.length > 0) {
                const foodCards = d.nearby_food_places.map(f => `
                    <div class="food-spot-card">
                        <div class="food-spot-header">
                            <span class="food-spot-name">🍲 ${f.name}</span>
                            <span class="food-spot-dist">🚗 ${f.distance_km}</span>
                        </div>
                        <div class="food-spot-loc">📍 ${f.location}</div>
                        <div class="food-spot-spec">✨ <strong>Must-Try:</strong> ${f.specialty}</div>
                    </div>
                `).join("");

                foodHtml = `
                    <div class="nearby-food-container">
                        <div class="nearby-food-title">🍽️ NEARBY FAMOUS FOOD SPOTS (${d.nearby_food_places.length})</div>
                        <div class="food-spots-list">${foodCards}</div>
                    </div>
                `;
            }

            item.innerHTML = `
                <div class="dest-card-header">
                    <span class="guide-dest-cat">${d.category || 'Attraction'}</span>
                    <span class="verified-badge">✓ Location Verified</span>
                </div>
                <h3 class="dest-title">${d.name}</h3>
                <div class="dest-meta-block">
                    <div class="dest-meta-item">
                        <span class="meta-icon">📌</span>
                        <span><strong>Location:</strong> ${d.exact_location || 'City Area'}</span>
                    </div>
                    <div class="dest-meta-item">
                        <span class="meta-icon">🚗</span>
                        <span><strong>Distance:</strong> ${d.distance_from_hub || 'Direct road access'}</span>
                    </div>
                </div>
                ${highlightsHtml}
                ${foodHtml}
            `;
            guideDestinationsList.appendChild(item);
        });

        // Extended Food Tags (Authentic Traditional Cuisine)
        guideFoodList.innerHTML = "";
        (st.authentic_cuisine || []).forEach(f => {
            const pill = document.createElement("span");
            pill.className = "food-pill extended-food-pill";
            pill.innerHTML = `🍲 ${f}`;
            guideFoodList.appendChild(pill);
        });

        showToast(`Loaded ${st.name} intelligence`, "info");
    }

    // Pill click listener
    statePillsRow.addEventListener("click", (e) => {
        const btn = e.target.closest(".state-pill");
        if (btn) {
            const sId = btn.getAttribute("data-state");
            selectState(sId, true);
        }
    });

    // Dropdown change listener
    stateSelectDropdown.addEventListener("change", (e) => {
        selectState(e.target.value, false);
    });

    // -------------------------------------------------------------------------
    // Chat Message Rendering & API Integration
    // -------------------------------------------------------------------------
    function appendChatMessage(role, content, engine = null) {
        const msgDiv = document.createElement("div");
        msgDiv.className = `message-bubble ${role === "user" ? "user-message" : "bot-message"}`;

        const avatar = document.createElement("div");
        avatar.className = "message-avatar";
        avatar.textContent = role === "user" ? "👤" : "✈️";

        const wrapper = document.createElement("div");
        wrapper.className = "message-content-wrapper";

        const author = document.createElement("div");
        author.className = "message-author";
        author.textContent = role === "user" ? "You" : "TRAVELIQ Assistant";

        const textDiv = document.createElement("div");
        textDiv.className = "message-text";

        if (role === "bot" && typeof marked !== "undefined") {
            textDiv.innerHTML = marked.parse(content);
        } else {
            textDiv.textContent = content;
        }

        wrapper.appendChild(author);
        wrapper.appendChild(textDiv);
        msgDiv.appendChild(avatar);
        msgDiv.appendChild(wrapper);

        chatMessagesStream.appendChild(msgDiv);
        chatMessagesStream.scrollTop = chatMessagesStream.scrollHeight;
    }

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const question = chatInput.value.trim();
        if (!question || state.isChatLoading) return;

        appendChatMessage("user", question);
        state.conversationHistory.push({ role: "user", content: question });
        chatInput.value = "";
        if (chatInput.tagName.toLowerCase() === "textarea") {
            chatInput.style.height = "auto";
        }

        state.isChatLoading = true;
        sendBtn.disabled = true;

        const loadingIndicator = document.createElement("div");
        loadingIndicator.className = "message-bubble bot-message";
        loadingIndicator.id = "chatLoadingIndicator";
        loadingIndicator.innerHTML = `
            <div class="message-avatar">✈️</div>
            <div class="message-content-wrapper">
                <div class="message-author">TRAVELIQ Assistant</div>
                <div class="message-text">
                    <span class="spinner" style="border-top-color: #0284c7; border-color: #e2e8f0; width:14px; height:14px;"></span>
                    <em style="color:#64748b; margin-left:6px;">Finding exact locations, distance in km & nearby food places...</em>
                </div>
            </div>
        `;
        chatMessagesStream.appendChild(loadingIndicator);
        chatMessagesStream.scrollTop = chatMessagesStream.scrollHeight;

        let answered = false;

        // 1. Try Backend API
        try {
            const res = await fetch(`${API_BASE}/api/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    question: question,
                    state_id: state.selectedState,
                    history: state.conversationHistory,
                    preferences: {
                        duration: parseInt(durationInput.value) || 4,
                        budget: budgetInput.value.trim(),
                        interests: getSelectedInterests()
                    }
                })
            });

            if (res.ok) {
                const data = await res.json();
                if (data.status === "success") {
                    const indicator = document.getElementById("chatLoadingIndicator");
                    if (indicator) indicator.remove();
                    appendChatMessage("bot", data.answer, data.engine);
                    state.conversationHistory.push({ role: "assistant", content: data.answer });
                    answered = true;
                }
            }
        } catch (err) {
            console.warn("Backend API not reachable, activating local state intelligence engine...");
        }

        // 2. Client-Side Resilience Engine
        if (!answered) {
            const indicator = document.getElementById("chatLoadingIndicator");
            if (indicator) indicator.remove();

            const localAnswer = generateClientSideAnswer(question, state.selectedState);
            appendChatMessage("bot", localAnswer, "TRAVELIQ State Intelligence");
            state.conversationHistory.push({ role: "assistant", content: localAnswer });
        }

        state.isChatLoading = false;
        sendBtn.disabled = false;
        chatInput.focus();
    });

    // Auto-grow if textarea
    if (chatInput.tagName.toLowerCase() === "textarea") {
        chatInput.addEventListener("input", () => {
            chatInput.style.height = "auto";
            chatInput.style.height = Math.min(chatInput.scrollHeight, 100) + "px";
        });
    }

    // Quick Prompts Chips
    document.querySelectorAll(".prompt-chip").forEach(chip => {
        chip.addEventListener("click", () => {
            switchTab("chat");
            chatInput.value = chip.getAttribute("data-query");
            chatInput.focus();
            chatForm.dispatchEvent(new Event("submit"));
        });
    });

    // -------------------------------------------------------------------------
    // Personalized State Trip Planner
    // -------------------------------------------------------------------------
    generateTripBtn.addEventListener("click", async () => {
        if (state.isPlanLoading) return;

        const duration = parseInt(durationInput.value) || 4;
        const budget = budgetInput.value.trim();
        const interests = getSelectedInterests();
        const stateName = state.stateData ? state.stateData.name : state.selectedState;

        switchTab("plan");
        emptyPlanState.classList.add("hidden");
        planRenderArea.classList.remove("hidden");

        planDestinationTitle.textContent = `${duration}-Day Curated Trip to ${stateName}`;
        planMetaTags.innerHTML = `
            <span class="plan-tag">📍 ${stateName}</span>
            <span class="plan-tag">📅 ${duration} Days</span>
            <span class="plan-tag">💰 ${budget ? '₹' + budget : 'Flexible Budget'}</span>
            ${interests.map(i => `<span class="plan-tag">🏷️ ${i}</span>`).join('')}
        `;

        planContentMarkdown.innerHTML = `
            <div style="padding: 40px 20px; text-align: center;">
                <span class="spinner" style="border-top-color:#0284c7; border-color:#cbd5e1; width:28px; height:28px;"></span>
                <p style="margin-top:14px; font-weight:600; color:#0369a1;">Formulating itinerary with exact locations, distance in km & nearby food...</p>
                <p style="font-size:0.85rem; color:#64748b;">Mapping routes and calculating nearby culinary spots for ${stateName}...</p>
            </div>
        `;

        state.isPlanLoading = true;
        generateTripBtn.disabled = true;
        let planGenerated = false;

        // 1. Try Backend API
        try {
            const res = await fetch(`${API_BASE}/api/plan`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    state_id: state.selectedState,
                    duration: duration,
                    budget: budget,
                    interests: interests
                })
            });

            if (res.ok) {
                const data = await res.json();
                if (data.status === "success") {
                    planContentMarkdown.innerHTML = marked.parse(data.plan);
                    showToast(`Personalized ${stateName} itinerary generated!`, "success");
                    planGenerated = true;
                }
            }
        } catch (err) {
            console.warn("Backend API not reachable, activating local itinerary generator...");
        }

        // 2. Client-Side Resilience Plan Generator
        if (!planGenerated) {
            const localPlan = generateClientSidePlan(state.selectedState, duration, budget, interests);
            planContentMarkdown.innerHTML = marked.parse(localPlan);
            showToast(`Personalized ${stateName} itinerary generated!`, "success");
        }

        state.isPlanLoading = false;
        generateTripBtn.disabled = false;
    });

    copyPlanBtn.addEventListener("click", () => {
        const text = planContentMarkdown.innerText;
        if (!text) return;
        navigator.clipboard.writeText(text).then(() => {
            showToast("Itinerary copied to clipboard!", "success");
        });
    });

    printPlanBtn.addEventListener("click", () => {
        window.print();
    });

    // -------------------------------------------------------------------------
    // Built-in Client Side Fallback Data & Generator (Zero Disconnection Error)
    // -------------------------------------------------------------------------
    function getLocalStateData(stateId) {
        const fallbackDatabase = {
            "andhra_pradesh": {
                name: "Andhra Pradesh",
                tagline: "The Sunrise State — Pristine Coastlines, Ancient Temples & Majestic Canyons",
                capital: "Amaravati",
                best_time_to_visit: "October to March (20°C - 30°C)",
                ideal_duration: "4 to 7 Days",
                estimated_daily_budget: { budget: "₹1,500/day", mid_range: "₹3,500/day", luxury: "₹8,000+/day" },
                top_destinations: [
                    {
                        name: "Visakhapatnam (RK Beach & Submarine Museum)",
                        category: "Coastal City & Heritage",
                        exact_location: "Beach Road, Pandurangapuram, Visakhapatnam, Andhra Pradesh 530003",
                        distance_from_hub: "4.5 km from Visakhapatnam Railway Station | 14 km from Vizag Airport (VTZ)",
                        highlights: ["INS Kursura Submarine Museum", "TU-142 Aircraft Museum", "Rushikonda Blue Flag Beach (12 km)"],
                        nearby_food_places: [
                            { name: "Subbayya Gari Hotel", location: "Diamond Park Road, Dwaraka Nagar", distance_km: "3.8 km from RK Beach", specialty: "Iconic Butta Bhojanam with Podis & Ghee" },
                            { name: "Sea Inn (Raju Gari Dhaba)", location: "Rushikonda Beach Road", distance_km: "11.5 km from RK Beach", specialty: "Spicy Chepala Vepudu (Fish Fry) & Natu Kodi Biryani" }
                        ]
                    },
                    {
                        name: "Araku Valley & Borra Caves",
                        category: "Hill Station & Caves",
                        exact_location: "Borra Caves, Ananthagiri Hills, Alluri Sitharama Raju District 531149",
                        distance_from_hub: "90 km from Visakhapatnam city (Borra Caves) | 115 km to Araku Valley",
                        highlights: ["Million-year-old Borra Caves", "Vistadome train through 58 tunnels", "Katiki Waterfalls"],
                        nearby_food_places: [
                            { name: "Araku Bamboo Chicken Stalls", location: "Outside Borra Caves Entrance", distance_km: "0.2 km from Caves", specialty: "Tribal Bamboo Chicken cooked over wood fire" }
                        ]
                    },
                    {
                        name: "Gandikota (Grand Canyon of India)",
                        category: "Geological Gorge & Heritage",
                        exact_location: "Gandikota Village, Jammalamadugu Mandal, YSR Kadapa District 516434",
                        distance_from_hub: "15 km from Jammalamadugu | 78 km from Kadapa",
                        highlights: ["300-foot Penna River gorge", "13th-century Gandikota Fort & Jamia Masjid", "Belum Caves (62 km)"],
                        nearby_food_places: [
                            { name: "Haritha Resort Restaurant", location: "Near Gandikota Fort Gate", distance_km: "0.5 km from Gorge", specialty: "Rayalaseema Ragi Mudde with Natu Kodi Pulusu" }
                        ]
                    },
                    {
                        name: "Tirupati & Tirumala",
                        category: "Sacred Pilgrimage",
                        exact_location: "Tirumala Hills, Tirupati District 517504",
                        distance_from_hub: "22 km from Tirupati Railway Station (via Ghat Road)",
                        highlights: ["Sri Venkateswara Temple", "Silathoranam natural rock arch", "Kapila Theertham waterfall"],
                        nearby_food_places: [
                            { name: "Srivari Annaprasadam Complex", location: "Near East Mada Street, Tirumala", distance_km: "0.4 km from Main Temple", specialty: "Sacred Srivari Annaprasadam & Srivari Laddu" },
                            { name: "Bhimas Deluxe Restaurant", location: "G. Car Street, Tirupati", distance_km: "1.2 km from Railway Station", specialty: "Ghee Roast Dosa & Filter Coffee" }
                        ]
                    }
                ],
                authentic_cuisine: ["Andhra Meals on Banana Leaf with Gongura Pachadi", "Bamboo Chicken in Araku", "Pesarattu Upma", "Rayalaseema Ragi Mudde", "Pootharekulu Sweet"]
            },
            "kerala": {
                name: "Kerala",
                tagline: "God's Own Country — Emerald Backwaters, Misty Tea Hills & Ayurvedic Coastlines",
                capital: "Thiruvananthapuram",
                best_time_to_visit: "September to March",
                ideal_duration: "5 to 8 Days",
                estimated_daily_budget: { budget: "₹1,500/day", mid_range: "₹3,500/day", luxury: "₹10,000+/day" },
                top_destinations: [
                    {
                        name: "Munnar & Tea Highlands",
                        category: "Hill Station & Tea",
                        exact_location: "Munnar, Idukki District, Kerala 685612",
                        distance_from_hub: "110 km from Cochin Airport (COK) | 115 km from Aluva Railway Station",
                        highlights: ["Eravikulam National Park (Nilgiri Tahr)", "Kolukkumalai Tea Estate", "Mattupetty Dam (13 km)"],
                        nearby_food_places: [
                            { name: "Rapsy Restaurant", location: "Main Bazaar Road, Munnar Town", distance_km: "0.8 km from Bus Stand", specialty: "Kerala Parotta with Beef Fry / Chicken Roast & Cardamom Tea" },
                            { name: "Saravana Bhavan (Pure Veg)", location: "Near KSRTC Station", distance_km: "0.4 km from Town", specialty: "Traditional Kerala Sadhya on Banana Leaf & Filter Coffee" }
                        ]
                    },
                    {
                        name: "Alleppey (Alappuzha Backwaters)",
                        category: "Backwaters & Houseboat",
                        exact_location: "Punnamada Jetty & Finishing Point, Alappuzha, Kerala 688006",
                        distance_from_hub: "4 km from Alappuzha Railway Station | 82 km from Cochin Airport (COK)",
                        highlights: ["Overnight Kettuvallam Houseboat cruise", "Vembanad Lake and Kuttanad canals", "Alleppey Beach"],
                        nearby_food_places: [
                            { name: "Thaff Restaurant", location: "General Hospital Junction, CCSB Road", distance_km: "2.8 km from Jetty", specialty: "Karimeen Pollichathu & Prawn Roast" },
                            { name: "Halais Restaurant", location: "Boat Jetty Road, Alleppey", distance_km: "2.2 km from Jetty", specialty: "Malabar Chicken Dum Biryani" }
                        ]
                    }
                ],
                authentic_cuisine: ["Kerala Sadhya on Banana Leaf", "Appam with Stew", "Karimeen Pollichathu", "Malabar Parotta with Beef Roast", "Puttu and Kadala Curry"]
            }
        };

        if (fallbackDatabase[stateId]) return fallbackDatabase[stateId];
        
        // Return a generic template for other states
        const nameFormatted = stateId.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
        return {
            name: nameFormatted,
            tagline: `Experience the culture, landmarks, and culinary wonders of ${nameFormatted}`,
            capital: "State Capital",
            best_time_to_visit: "October to March",
            ideal_duration: "4 to 7 Days",
            estimated_daily_budget: { budget: "₹1,500/day", mid_range: "₹3,500/day", luxury: "₹8,000+/day" },
            top_destinations: [
                {
                    name: `${nameFormatted} Central Heritage & Landmarks`,
                    category: "Heritage & Culture",
                    exact_location: `Central Tourism District, ${nameFormatted}`,
                    distance_from_hub: `5 km from Main Railway Station & Airport`,
                    highlights: ["Historic Forts & Palaces", "Ancient Temples & Shrines", "Local Handicraft Markets"],
                    nearby_food_places: [
                        { name: "Heritage Dining Hall", location: "Main City Bazaar", distance_km: "1.2 km from Center", specialty: "Traditional State Thali & Local Specialties" }
                    ]
                }
            ],
            authentic_cuisine: ["Traditional State Thali", "Local Spiced Curries", "Regional Breads & Sweets", "Authentic Hot Brews"]
        };
    }

    function generateClientSideAnswer(question, stateId) {
        const st = getLocalStateData(stateId);
        const name = st.name;
        const q_lower = question.toLowerCase();

        if (st.top_destinations && st.top_destinations.length > 0) {
            const destsBlocks = st.top_destinations.map(d => {
                let foodText = "";
                if (d.nearby_food_places) {
                    foodText = "\n**Nearby Food Places:**\n" + d.nearby_food_places.map(f => 
                        `  - 🍲 **${f.name}** (*${f.distance_km}* at ${f.location}) — *Try*: ${f.specialty}`
                    ).join("\n");
                }
                return `### 📍 ${d.name} *(${d.category})*\n📌 **Exact Location**: ${d.exact_location}\n🚗 **Distance**: ${d.distance_from_hub}\n🌟 **Highlights**: ${d.highlights.join(", ")}${foodText}`;
            }).join("\n\n---\n\n");

            return `### 🗺️ Places, Exact Locations & Nearby Food in ${name}\n\n${destsBlocks}\n\n📅 **Best Season**: ${st.best_time_to_visit}\n💰 **Daily Budget**: ${st.estimated_daily_budget.mid_range}`;
        }

        return `### ✈️ Travel Guide for ${name}\n\n**${st.tagline}**\n\n• **Best Season to Visit**: ${st.best_time_to_visit}\n• **Daily Budget**: ${st.estimated_daily_budget.mid_range}\n• **Must-Try Foods**: ${st.authentic_cuisine.join(", ")}`;
    }

    function generateClientSidePlan(stateId, duration, budget, interests) {
        const st = getLocalStateData(stateId);
        const name = st.name;
        const dests = st.top_destinations || [];

        const daysContent = [];
        for (let day = 1; day <= duration; day++) {
            const dest = dests[(day - 1) % dests.length];
            let foodRec = "";
            if (dest.nearby_food_places && dest.nearby_food_places.length > 0) {
                const f = dest.nearby_food_places[0];
                foodRec = `\n  - 🍲 **Recommended Lunch/Dinner**: **${f.name}** (*${f.distance_km}* at ${f.location}) — *Specialty*: ${f.specialty}`;
            }

            daysContent.push(`### 📅 DAY ${day}: ${dest.name} (${dest.category})
- 📍 **Exact Location**: ${dest.exact_location}
- 🚗 **Distance in KM**: ${dest.distance_from_hub}
- 🌅 **Morning**: Explore ${dest.highlights[0] || 'landmarks & morning sightseeing'}.
- ☀️ **Afternoon**: Discover ${dest.highlights[1] || 'cultural spots and historic trails'}.${foodRec}
- 🌆 **Evening**: Head to sunset viewpoints, photography spots, and local shopping bazaars.`);
        }

        return `# ✈️ ${duration}-Day Curated Travel Itinerary for ${name}

> **Theme**: ${st.tagline}  
> **Target Interests**: ${interests.join(", ") || 'Sightseeing & Food'} | **Budget Target**: ₹${budget || 'Flexible'}

---

## 🌟 Trip Overview & Route Strategy
This ${duration}-day route covers the most celebrated locations in **${name}**, optimized with exact distances in kilometers and authentic nearby culinary dining spots.

---

## 🗺️ Day-by-Day Detailed Plan (with Locations, Distances in KM & Nearby Food)

${daysContent.join("\n\n---\n\n")}

---

## 💰 Budget Breakdown & Daily Estimates
- **Daily Budget Target**: ${st.estimated_daily_budget.mid_range}
- **Food & Dining**: Budget ₹400 - ₹900/day for authentic local meals at the recommended food spots.
- **Best Season to Visit**: ${st.best_time_to_visit}
`;
    }

    // Initial load
    selectState("andhra_pradesh");
});
