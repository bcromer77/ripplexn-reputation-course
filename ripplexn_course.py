import streamlit as st

# Page configuration
st.set_page_config(page_title="RippleXp - Storytelling & Social Listening", layout="wide")

# Sidebar Navigation
st.sidebar.title("RippleXp: Protecting Your Brand")
section = st.sidebar.radio("Navigate to:", [
    "Overview",
    "Why Storytelling Matters",
    "RippleXp Courses",
    "Commercialization - Off-the-Shelf Products",
    "Course Structure",
    "RippleXp + RippleXn Integration",
    "Contact Us"
])

# Main Content Area
if section == "Overview":
    st.title("RippleXp - The Art of Storytelling to Shield Your Reputation")
    st.write("""
    RippleXp empowers brands to proactively safeguard their reputation through storytelling and listening.
    In today’s social media landscape, every misstep is a potential risk to brand reputation. By equipping brands 
    with the tools to shape and monitor their narrative, RippleXp ensures brands stay protected.
    """)

elif section == "Why Storytelling Matters":
    st.title("Why Storytelling Matters for Your Brand’s Safety")
    st.write("""
    Brands today face unprecedented scrutiny. Social media makes it easy for narratives to spiral out of control,
    potentially harming brand reputation. RippleXp’s storytelling framework is designed to help you:
    - **Control Your Narrative:** Avoid reputation-damaging incidents by mastering proactive storytelling.
    - **Identify Potential Risks:** Understand what audiences care about to predict risks before they escalate.
    - **Engage Authentically:** Build trust by telling real, compelling stories that resonate with your audience.
    
    **Bottom Line:** A brand’s reputation is too valuable to leave unprotected. RippleXp is your defense.
    """)

elif section == "RippleXp Courses":
    st.title("RippleXp Courses: Empower Your Team to Protect Your Reputation")
    st.write("""
    Each course is designed to build a foundation for recognizing and mitigating potential reputation threats:
    """)
    st.subheader("1. Reputation Story")
    st.write("Focus: Helping your team understand how audiences perceive your brand.")
    st.markdown("**Outcome:** Equip your brand to proactively shape perceptions and mitigate misunderstandings.")

    st.subheader("2. Reputation Rhetoric")
    st.write("Focus: Balancing persuasion with authenticity to prevent backlash.")
    st.markdown("**Outcome:** Train your influencers to represent your brand without triggering regulatory issues.")

    st.subheader("3. Comeback Story (Crisis Navigation)")
    st.write("Focus: Using storytelling to navigate and recover from potential crises.")
    st.markdown("**Outcome:** Strengthen your brand's resilience by planning your response in advance.")

    st.subheader("4. Evolution Story")
    st.write("Focus: Evolving your narrative as your brand grows.")
    st.markdown("**Outcome:** Keep your brand’s story fresh and aligned with current market trends.")

elif section == "Commercialization - Off-the-Shelf Products":
    st.title("Commercialization: Off-the-Shelf Products to Get You Started")
    st.write("""
    RippleXp offers entry-level products to provide immediate value, allowing you to start safeguarding your brand today:
    """)
    st.subheader("1. $49 FTC/SEC Disclosure Training")
    st.write("""
    Essential training to ensure influencers and key brand representatives meet regulatory standards for disclosure.
    **Benefit:** Avoid costly compliance issues by equipping your team with the basics.
    """)

    st.subheader("2. $75 Trend Analysis Report")
    st.write("""
    A 100-hour curated video insights report on key trends.
    **Benefit:** Gain instant insights into what’s resonating in the market and identify opportunities.
    """)

    st.subheader("3. $199 Risk & Strategy Support")
    st.write("""
    Choose from either an influencer background check ("risk torch") or a customized listening strategy for small brands or campaigns.
    **Benefit:** Immediate risk assessment and actionable strategies to safeguard brand integrity.
    """)

elif section == "Course Structure":
    st.title("Course Structure: RippleXp’s Unique Approach to Storytelling")
    st.write("""
    All RippleXp courses are founded on three core tenets:
    
    - **Principle (The Art of Story):** Understand
