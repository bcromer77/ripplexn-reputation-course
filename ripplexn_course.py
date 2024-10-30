import streamlit as st

# Page configuration
st.set_page_config(page_title="RippleXp - Storytelling & Social Listening", layout="wide")

# Sidebar Navigation
st.sidebar.title("RippleXp: Protecting Your Brand")
section = st.sidebar.radio("Navigate to:", [
    "Overview",
    "Why Storytelling Matters",
    "RippleXp Courses",
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

elif section == "RippleXp + RippleXn Integration":
    st.title("Seamlessly Transition from Storytelling to Social Listening with RippleXn")
    st.write("""
    RippleXp’s storytelling framework is just the beginning. After empowering brands with narrative control, 
    RippleXn takes it a step further by actively listening to social video channels, spotting potential issues, 
    and keeping you ahead of any threats. Here’s how RippleXp leads into RippleXn:
    """)
    
    st.subheader("1. Detecting Brand Risk Early")
    st.write("Use storytelling as a proactive approach, then leverage RippleXn’s listening tools to continuously monitor for signs of emerging risks.")
    
    st.subheader("2. Consistent Compliance Monitoring")
    st.write("FTC/SEC compliance training prepares influencers; RippleXn’s platform verifies that they adhere to guidelines in real-time.")
    
    st.subheader("3. Crisis Prevention and Management")
    st.write("RippleXp preps your team for crises. RippleXn helps you detect the warning signs early and respond before a small issue becomes a public scandal.")
    
    st.subheader("4. Enhancing Brand Engagement through Listening")
    st.write("RippleXp equips your brand to tell compelling stories; RippleXn ensures those stories reach the right audience and receive the right response.")
    
elif section == "Contact Us":
    st.title("Contact RippleXp to Safeguard Your Brand")
    st.write("Reach out to discuss your brand’s needs, set up a free consultation, or request a customized storytelling and social listening strategy.")
    st.write("Visit our [RippleXn website](https://ripplexn.com) to learn more about our social video listening platform.")

# Footer for context
st.write("---")
st.write("Learn how RippleXp can protect and amplify your brand’s reputation through the power of storytelling.")
