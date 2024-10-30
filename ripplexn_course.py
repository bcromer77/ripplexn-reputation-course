import streamlit as st

# Powerful Intro - "Why Now" and Calling Card Message
st.title("RippleXp - Transforming Brand Reputation Management")
st.write("""
    ### Why Now?
    In a world where brands are constantly under the lens, the fear of reputational damage has never been more palpable. 
    **RippleXp** serves as a calling card, capitalizing on this urgency by empowering brands to understand and manage the 
    multiple narratives surrounding them online. By leveraging the fear of reputational damage, RippleXp offers a gateway 
    to RippleXn’s deeper social listening and reputation management services.
    
    Our approach is simple but powerful: use storytelling to uncover hidden risks and opportunities, allowing brands to 
    engage in self-reflection and proactive management. Through dedicated, hands-on courses, RippleXp equips teams with 
    the insights and skills they need to navigate today’s high-stakes media landscape. **The Trojan horse?** RippleXp 
    positions brands to embrace RippleXn’s full suite of social listening tools for ongoing protection.
""")
st.write("---")

# Sidebar Navigation
section = st.sidebar.radio("Course Navigation", [
    "Overview", 
    "The RippleXp Approach", 
    "Target Audiences", 
    "Entry-Level Products", 
    "Advanced Options", 
    "Commercialization & Off-the-Shelf Products", 
    "Crisis Identification Stages", 
    "Course Assessment"
])

# Overview
if section == "Overview":
    st.header("Overview: RippleXp as a Top-of-Funnel Approach")
    st.write("""
    RippleXp acts as a strategic top-of-funnel entry point for RippleXn’s core offerings. By engaging clients through storytelling 
    and reputation management courses, we position RippleXn’s deeper social listening services as the logical next step.
    """)
    st.subheader("Key Objectives:")
    st.write("""
    - **Leverage Fear of Reputational Damage**: RippleXp addresses brand vulnerability head-on, sparking interest through actionable insights.
    - **Drive Discovery through Storytelling**: Courses are structured to teach clients the art of storytelling while subtly preparing them for RippleXn.
    - **Facilitate Smooth Transitions**: Graduates of RippleXp’s courses are primed for more advanced reputation management services.
    """)

# The RippleXp Approach
elif section == "The RippleXp Approach":
    st.header("The RippleXp Approach to Reputation Management")
    st.write("""
    Reputation is a mosaic, composed of hundreds of individual stories that, together, create a brand’s narrative. RippleXp’s courses guide 
    clients through the storytelling process, uncovering hidden risks and opportunities that align with RippleXn’s proactive listening 
    tools.
    """)
    st.subheader("Why Storytelling?")
    st.write("""
    Storytelling is not just a creative exercise; it’s a strategic tool that allows brands to manage their narratives with intention.
    RippleXp helps brands develop the storytelling skills to navigate and control their reputation, leading naturally to the need 
    for RippleXn’s advanced social listening solutions.
    """)

# Target Audiences
elif section == "Target Audiences":
    st.header("Target Audiences - Four Key Areas of Focus")
    st.write("""
    RippleXp courses are tailored to address the different stages of brand audience engagement:
    
    - **No Audience Yet**: Brands looking to attract listeners and engage emerging trends.
    - **Existing Audience**: Brands with a current audience but lacking insight into competitive influences.
    - **Lost Audience (Crisis Management)**: Brands needing real-time recovery tactics.
    - **Other Voices Speaking**: Brands with influencers or advocates requiring training in brand representation.
    """)
    st.write("---")

# Entry-Level Products
elif section == "Entry-Level Products":
    st.header("Entry-Level Products for Customer Acquisition")
    st.write("""
    These offerings serve as introductory tools to bring clients into the RippleXp ecosystem while priming them for RippleXn:
    
    - **$49 FTC/SEC Disclosure Training**: Ensures influencers meet regulatory standards, reducing risk.
    - **$75 Trend Analysis**: 100 hours of curated insights, highlighting key trends.
    - **$199 Risk & Strategy Support**: Choose between an influencer background check or a custom listening strategy.
    """)
    st.subheader("Course Delivery Options")
    st.write("""
    - **Half-Day Workshop**: Brief training sessions focused on immediate insights and regulatory basics.
    """)

# Advanced Options
elif section == "Advanced Options":
    st.header("Advanced Options for Engaging Sophisticated Buyers")
    st.write("""
    For brands prepared to take the next step, RippleXp offers advanced courses that lead into RippleXn’s ongoing monitoring services:
    
    - **Storytelling Courses**: Develop narrative skills for brand control.
    - **Social Video Alerts**: Real-time insights identifying emerging risks like greenwashing.
    """)
    st.subheader("Course Delivery Options")
    st.write("""
    - **Full-Day Workshop**: Intensive storytelling and brand reputation sessions.
    - **3-Day Immersive**: In-depth courses with hands-on application and strategy development.
    """)

# Commercialization & Off-the-Shelf Products
elif section == "Commercialization & Off-the-Shelf Products":
    st.header("Commercialization & Off-the-Shelf Products")
    st.write("""
    RippleXp offers modular, off-the-shelf products that cater to brands at various stages of crisis management and 
    audience engagement:
    
    - **Crisis Identification Products**: Scalable solutions that highlight brand vulnerabilities.
    - **Audience Insight Tools**: Pre-packaged courses that guide brands through common pitfalls.
    - **Advanced Monitoring Solutions**: RippleXn’s full-service offerings for real-time brand listening.
    """)

# Crisis Identification Stages
elif section == "Crisis Identification Stages":
    st.header("Crisis Identification Stages - From Fear to Proactivity")
    st.write("""
    Each RippleXp course addresses a critical stage in crisis management, from early detection to response. 
    We position RippleXp courses as essential tools for understanding where and how reputational threats emerge.
    
    - **Stage 1**: Identify reputation risks.
    - **Stage 2**: Address complications and educate through storytelling.
    - **Stage 3**: Engage ongoing RippleXn monitoring services for continued reputation management.
    """)

# Course Assessment
elif section == "Course Assessment":
    st.header("Course Assessment - Customized Recommendations")
    st.write("""
    Our assessment tool helps clients identify the most relevant RippleXp courses based on their brand’s unique needs, 
    guiding them seamlessly into the RippleXn ecosystem.
    """)
    st.subheader("Choose Your Path:")
    st.write("""
    - **Introductory Assessment**: Determine your starting point.
    - **Advanced Analysis**: For brands needing immediate intervention.
    """)

# Footer CTA
st.write("---")
st.write("Ready to secure your brand’s reputation? Start your RippleXp journey and prepare for RippleXn’s comprehensive monitoring services.")
st.button("Contact Us for a Free Consultation")
