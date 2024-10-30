import streamlit as st

# Title and Hook
st.title("RippleXp - Your Gateway to Reputation Management")
st.write("""
    ### The Irrefutable and Inevitable Nature of Social Media Risk
    Social media has transformed into a high-stakes landscape where brands can thrive or be damaged in an instant. 
    With countless narratives unfolding daily, **RippleXp** offers a top-of-the-funnel, pre-sales approach 
    that primes brands for the proactive reputation management solutions of **RippleXn**.
    """)
st.write("---")

# Navigation
section = st.sidebar.radio("Course Navigation", [
    "Dashboard Overview", 
    "Introduction", 
    "I Need an Audience", 
    "I Have an Audience", 
    "Lost Audience (Crisis Management)", 
    "Other Voices Speaking", 
    "Entry-Level Products", 
    "Advanced Options", 
    "Commercialization & Off-the-Shelf Products", 
    "Crisis Identification Stages", 
    "Course Assessment"
])

# Dashboard Overview
if section == "Dashboard Overview":
    st.header("Dashboard Overview: RippleXp’s Pre-Sales Strategy")
    st.write("""
    RippleXp is strategically designed as the top-of-the-funnel for RippleXn’s deeper, ongoing reputation management services.
    By guiding clients through reputation-building and crisis-avoidance techniques, RippleXp is the educational primer that primes
    brands to appreciate the value of RippleXn's full social listening suite.
    """)
    st.image("https://example.com/path-to-roadmap-image.jpg", caption="RippleXp to RippleXn Journey")
    st.write("---")

# Introduction with Strong Hook
elif section == "Introduction":
    st.header("Problem Identification - The RippleXp Foundation")
    st.write("""
    In today's digital age, reputation is a mosaic composed of individual stories, like a honeycomb. **RippleXp** leverages 
    storytelling to prepare brands for RippleXn’s social video listening solutions, ensuring they are proactive, not reactive, 
    to potential reputation threats.
    """)
    st.subheader("Why Choose RippleXp as Your Pre-Sales Strategy?")
    st.write("""
    RippleXp's storytelling approach addresses common reputational risks through top-of-the-funnel courses. Each course teaches 
    brands to shape their own narratives, priming them for RippleXn’s continuous monitoring.
    """)
    st.write("---")

# I Need an Audience
elif section == "I Need an Audience":
    st.header("Understanding Your Audience - I Need an Audience")
    st.write("""
    Focus on finding listeners to understand trends and stay relevant in the market. 
    For brands that need to build an audience, the goal is to capture trends and leverage insights 
    to engage potential listeners. RippleXp helps by identifying what's resonating across channels and emerging topics.
    """)

# I Have an Audience
elif section == "I Have an Audience":
    st.header("Leveraging Your Audience - I Have an Audience")
    st.write("""
    For brands with an established audience, RippleXp helps identify what else that audience is paying attention to. 
    Our storytelling approach helps capture competitive insights that keep your brand ahead in the market.
    """)

# Lost Audience (Crisis Management)
elif section == "Lost Audience (Crisis Management)":
    st.header("Crisis Management - Lost Audience")
    st.write("""
    Brands like Pepsi and others with high exposure need real-time recovery tactics. RippleXp’s approach to crisis storytelling 
    trains brands to respond effectively in moments of brand vulnerability, ensuring minimal reputation damage.
    """)

# Other Voices Speaking
elif section == "Other Voices Speaking":
    st.header("Influencer & Advocate Management - Other Voices Speaking")
    st.write("""
    RippleXp equips brands with the training to ensure influencers and advocates represent them effectively, minimizing miscommunication 
    and enhancing brand consistency across multiple voices.
    """)

# Entry-Level Products for Customer Acquisition
elif section == "Entry-Level Products":
    st.header("Entry-Level Products for Customer Acquisition")
    st.write("""
    These products are designed to lower the barrier to entry and provide value to new customers.
    """)
    st.write("""
    - **$49 FTC/SEC Disclosure Training**: Ensures influencers meet regulatory standards.
    - **$75 Trend Analysis Report**: 100 hours of curated video insights on trends.
    - **$199 Risk & Strategy Support**: Choose between influencer background checks or a listening strategy.
    """)
    st.write("---")

# Advanced Options for Sophisticated Buyer Engagement
elif section == "Advanced Options":
    st.header("Advanced Options for Sophisticated Buyers")
    st.write("""
    For brands ready to invest further, we offer comprehensive solutions to engage with RippleXn.
    """)
    st.write("""
    - **Storytelling Courses**: Develop crisis response insights.
    - **Social Video Alerts**: Real-time monitoring of risks like greenwashing or crypto-related promotions.
    """)

# Commercialization & Off-the-Shelf Products
elif section == "Commercialization & Off-the-Shelf Products":
    st.header("Commercialization Strategy and Off-the-Shelf Products")
    st.write("""
    RippleXp’s off-the-shelf products act as direct revenue generators while educating clients on the value of advanced monitoring.
    These products serve as easy entry points for clients to access RippleXp’s resources, priming them for RippleXn’s full services.
    """)
    st.write("""
    - **Compliance Training**: Easy-to-access compliance training to avoid backlash.
    - **Keyword-Based Monitoring**: Customized social media audits.
    - **Influencer Verification Tools**: Ensure influencer alignment with brand safety standards.
    """)

# Crisis Identification Stages
elif section == "Crisis Identification Stages":
    st.header("Crisis Identification Stages - When Clients Realize the Problem")
    st.write("""
    RippleXp addresses the stages where clients realize the need for social listening and storytelling:
    """)
    st.write("""
    - **Stage 1**: Emerging crisis awareness, where the brand recognizes potential reputation risks.
    - **Stage 2**: Early crisis signs, where RippleXp helps brands react with storytelling and crisis navigation.
    - **Stage 3**: Full-blown crisis, where RippleXn’s active monitoring plays a crucial role.
    """)

# Course Assessment and Funnel Effect
elif section == "Course Assessment":
    st.header("Course Assessment - Ensuring RippleXp’s Impact")
    st.write("""
    RippleXp doesn’t just provide courses; it primes clients for a full reputation management journey. Our courses work as 
    a pre-sales strategy, bringing clients into the RippleXn ecosystem.
    """)
    st.subheader("Assessing Readiness for RippleXn")
    st.write("""
    Each course in RippleXp is designed to gauge a brand’s current understanding and identify their next steps with RippleXn, 
    creating a seamless funnel effect that prepares clients for ongoing reputation management.
    """)

st.write("---")
st.write("For more information or to discuss course customization, please contact us.")
