"""
Generate a realistic sample travel PDF for TRAVELIQ testing and hackathon demo.
Creates 'uploads/Goa_Tourism_Guide.pdf' and 'sample_data/Goa_Tourism_Guide.pdf'.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak

def build_sample_pdf():
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("sample_data", exist_ok=True)
    
    target_paths = ["uploads/Goa_Tourism_Guide.pdf", "sample_data/Goa_Tourism_Guide.pdf"]
    
    for target_path in target_paths:
        doc = SimpleDocTemplate(
            target_path,
            pagesize=letter,
            rightMargin=54,
            leftMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'DocTitle',
            parent=styles['Heading1'],
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#0f3460"),
            spaceAfter=12
        )
        heading_style = ParagraphStyle(
            'SectionHeading',
            parent=styles['Heading2'],
            fontSize=15,
            leading=18,
            textColor=colors.HexColor("#e94560"),
            spaceBefore=12,
            spaceAfter=8
        )
        body_style = ParagraphStyle(
            'Body',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#1a1a2e"),
            spaceAfter=8
        )
        callout_style = ParagraphStyle(
            'Callout',
            parent=styles['Normal'],
            fontSize=9.5,
            leading=13,
            textColor=colors.HexColor("#333333"),
            backColor=colors.HexColor("#f0f4f8"),
            borderColor=colors.HexColor("#d0dbe5"),
            borderWidth=1,
            borderPadding=6,
            spaceAfter=10
        )
        
        story = []
        
        # PAGE 1: Welcome & North Goa Beaches
        story.append(Paragraph("GOA OFFICIAL TOURISM & TRAVEL GUIDE", title_style))
        story.append(Paragraph("Destination Overview & Coastal Exploration Guide", styles['Italic']))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0f3460"), spaceAfter=15))
        
        story.append(Paragraph("1. Introduction to Goa", heading_style))
        story.append(Paragraph(
            "Goa, located on the southwestern coast of India within the Konkan region, is famous for its sun-drenched beaches, Portuguese colonial architecture, rich biodiversity, and distinct Indo-Portuguese culinary heritage. The state is divided into two main administrative districts: North Goa, renowned for vibrant nightlife, lively beach shacks, and water sports, and South Goa, known for tranquil coastlines, luxury resorts, and secluded heritage villages.",
            body_style
        ))
        
        story.append(Paragraph("2. Top Beaches in North Goa", heading_style))
        story.append(Paragraph(
            "<b>Calangute Beach:</b> Often called the 'Queen of Beaches', Calangute is the largest beach in North Goa. It offers expansive golden sands and a bustling commercial center with souvenir shops, handicraft stalls, and beachside restaurants. Ideal for parasailing, banana boat rides, and jet skiing.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Baga Beach:</b> Located immediately north of Calangute, Baga is famous for its electrifying nightlife along Tito's Lane and lively seaside shacks serving fresh Goan fish curry. Activities include dolphin watching boat tours, windsurfing, and evening beachfront dining.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Anjuna & Vagator Beaches:</b> Famous for dramatic red laterite cliffs and rocky shores. Anjuna is celebrated for its historic Wednesday Flea Market and beachfront cafe culture, while Vagator offers scenic views from Chapora Fort overlooking the Arabian Sea.",
            body_style
        ))
        
        story.append(Paragraph("Key Advisory: Swimming is strictly prohibited during monsoon season (June to September) due to high rip tides.", callout_style))
        story.append(PageBreak())
        
        # PAGE 2: South Goa Beaches & Heritage
        story.append(Paragraph("3. Peaceful Coastlines of South Goa", heading_style))
        story.append(Paragraph(
            "<b>Palolem Beach:</b> A crescent-shaped bay fringed by coconut palms and colorful wooden beach huts. Palolem features gentle waters safe for swimming, sea kayaking, and boat trips to Butterfly Beach and Honeymoon Island.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Agonda Beach:</b> A wide, quiet beach stretching 3 kilometers, designated as a protected nesting ground for Olive Ridley sea turtles. Agonda enforces quiet hours after 10:00 PM and is popular for meditation retreats, yoga centers, and peaceful reading.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Colva & Benaulim:</b> White sand stretches offering traditional fishing experiences, water scooters, and beachfront dining with fresh crab and prawn recheado.",
            body_style
        ))
        
        story.append(Paragraph("4. Historical Forts and Military Architecture", heading_style))
        story.append(Paragraph(
            "<b>Aguada Fort:</b> Built in 1612 by the Portuguese at the mouth of the Mandovi River to protect against Dutch invaders. It features a historic 4-storey lighthouse (constructed in 1864) and a vast freshwater cistern capable of storing 2,376,000 gallons of drinking water. Entry fee is ₹25 for Indian nationals and ₹300 for foreign visitors. Visiting hours: 9:30 AM to 5:30 PM daily.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Chapora Fort:</b> Built by the Adil Shahi rulers of Bijapur and later rebuilt by the Portuguese in 1717. Located above the Chapora River, it offers 360-degree panoramic views of Vagator Beach and Morjim. Free admission. Best visited during sunset.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Cabo de Rama Fort:</b> Situated in Canacona, South Goa. One of the oldest forts in Goa, named after Lord Rama who is believed to have stayed here with Sita during their 14-year exile.",
            body_style
        ))
        story.append(PageBreak())
        
        # PAGE 3: Churches, Old Goa & Culture
        story.append(Paragraph("5. Old Goa (Velha Goa) & UNESCO World Heritage Sites", heading_style))
        story.append(Paragraph(
            "<b>Basilica of Bom Jesus:</b> Built in 1605, this UNESCO World Heritage monument is a masterpiece of Baroque architecture. It holds the sacred mortal remains of St. Francis Xavier within an ornate silver casket. Open Monday to Saturday: 9:00 AM to 6:30 PM; Sunday: 10:30 AM to 6:30 PM. Modest attire covering shoulders and knees is mandatory. Photography with flash is strictly prohibited inside the chapel.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Se Cathedral (Sé Catedral de Santa Catarina):</b> Dedicated to St. Catherine of Alexandria, it is one of the largest churches in Asia. It features the famous 'Golden Bell' (Sino de Ouro), known for its rich acoustic tone. Located directly opposite the Basilica of Bom Jesus.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Church of Our Lady of the Immaculate Conception (Panaji):</b> Built in 1541, featuring iconic zigzag baroque staircases and a brilliant white facade towering over the historic Church Square in the capital city of Panaji.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Fontainhas (Latin Quarter):</b> The preserved historic Latin Quarter of Panaji featuring narrow cobblestone alleyways, vibrant yellow and Portuguese-blue heritage houses, ornate wrought-iron balconies, and quaint cafes serving freshly baked Bebinca and Poi bread.",
            body_style
        ))
        story.append(PageBreak())
        
        # PAGE 4: Cuisine, Adventure & Nature
        story.append(Paragraph("6. Authentic Goan Cuisine & Food Guide", heading_style))
        story.append(Paragraph(
            "Goan cuisine is defined by coconut milk, kokum, tamarind, fiery red Kashmiri chillies, and aromatic vinegar. Essential dishes include:",
            body_style
        ))
        story.append(Paragraph(
            "• <b>Goan Fish Curry (Xitt Codi):</b> Fresh Kingfish or Pomfret simmered in grated coconut paste, ground spices, and sour kokum, served with steamed Goan red rice.<br/>"
            "• <b>Pork/Chicken Vindaloo:</b> Traditional curry marinated in palm vinegar, garlic, ginger, and red chillies.<br/>"
            "• <b>Prawn Balchão:</b> Fiery, tangy pickled prawn relish made with vinegar and spices.<br/>"
            "• <b>Chicken Xacuti:</b> Complex curry prepared with roasted poppy seeds, desiccated coconut, and toasted whole spices.<br/>"
            "• <b>Bebinca:</b> The traditional 7-layer Goan dessert made with coconut milk, egg yolks, flour, sugar, and ghee.<br/>"
            "• <b>Feni:</b> Traditional indigenous liquor distilled from cashew apples or fermented coconut toddy.",
            body_style
        ))
        
        story.append(Paragraph("7. Nature, Waterfalls & Spice Plantations", heading_style))
        story.append(Paragraph(
            "<b>Dudhsagar Waterfalls:</b> A magnificent four-tiered cascade located on the Mandovi River in the Bhagwan Mahaveer Sanctuary near Mollem. Rising to 310 meters (1,017 feet), it resembles a sea of milk pouring down the Western Ghats. Accessible via official forest jeep safari from Kulem. Forest entry and life jacket rental fee is approximately ₹500 to ₹800 per person.",
            body_style
        ))
        story.append(Paragraph(
            "<b>Sahakari Spice Farm (Ponda):</b> Guided tours through aromatic plantations of cardamom, black pepper, cinnamon, nutmeg, and vanilla, concluding with a traditional Goan buffet lunch served on banana leaves. Entry ticket: ₹400 per person including lunch.",
            body_style
        ))
        story.append(PageBreak())
        
        # PAGE 5: Travel Guidelines, Budget & Transport
        story.append(Paragraph("8. Transportation, Estimated Costs & Budgeting", heading_style))
        story.append(Paragraph(
            "<b>Local Transport:</b><br/>"
            "• <i>Scooter / Bike Rental:</i> ₹350 to ₹600 per day (valid driving license and mandatory helmet required).<br/>"
            "• <i>Self-drive Car:</i> ₹1,200 to ₹2,500 per day depending on model and season.<br/>"
            "• <i>Goa Taxi App (GoaMiles):</i> Government-approved app-based taxi service for fixed and transparent pricing.<br/>"
            "• <i>Kadamba AC State Buses:</i> Economical connectivity between Panaji, Mapusa, Margao, and Vasco da Gama (₹20 to ₹60 per ride).",
            body_style
        ))
        story.append(Paragraph(
            "<b>Daily Budget Estimations (Per Person):</b><br/>"
            "• <i>Budget Traveler:</i> ₹1,500 - ₹2,500 per day (hostels/guesthouses, beach shacks, scooter rental).<br/>"
            "• <i>Mid-Range Traveler:</i> ₹3,500 - ₹6,500 per day (3-star boutique hotels, beach dining, guided tours).<br/>"
            "• <i>Luxury Traveler:</i> ₹10,000+ per day (5-star beachfront resorts, fine dining, private charters).",
            body_style
        ))
        
        story.append(Paragraph("9. Key Travel Rules & Safety Regulations", heading_style))
        story.append(Paragraph(
            "• <b>Beach Drinking:</b> Drinking alcohol in public places, open beaches, and unauthorized areas is illegal and subject to a fine of up to ₹2,000 to ₹10,000.<br/>"
            "• <b>Littering:</b> Discarding plastic bottles, waste, or glass on beaches carries strict spot fines.<br/>"
            "• <b>Water Sports Safety:</b> Always use registered operators licensed by the Goa Tourism Department; wearing life jackets is mandatory.<br/>"
            "• <b>Emergency Helpline:</b> Police: 112 / 100, Tourist Police: +91 832 2428800, Ambulance: 108.",
            body_style
        ))
        
        doc.build(story)
        print(f"Generated sample travel PDF at: {target_path}")

if __name__ == "__main__":
    build_sample_pdf()
