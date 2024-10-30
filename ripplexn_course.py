import streamlit as st

# Page configuration
st.set_page_config(page_title="RippleXp - Storytelling for Social Listening", layout="wide")

# Sidebar Navigation
st.sidebar.title("RippleXp Offerings")
section = st.sidebar.radio("Navigate to:", [
    "Introduction to RippleXp",
    "Focus Areas",
    "Entry-Level Products",
    "Advanced Options",
    "Additional Resources"
])

# Main Content Area
if section == "Introduction to RippleXp":
    st.title("RippleXp - Using Storytelling to Sell Social Video Listening")
    st.write("""
    RippleXp is designed to use storytelling as a tool to help brands not only ‘listen’ but also engage meaningfully with audiences.
    In the world of RippleXn, reputation is a mosaic of countless individual stories. Every brand’s narrative is shaped by these
    stories, and our goal is to empower brands to navigate this listening landscape effectively.
    """)

elif section == "Focus Areas":
    st.title("RippleXp Focus Areas")
    st.write("""
    To help brands succeed, we’ve identified four focus areas aligned with RippleXn’s core goals:
    """)
    st.subheader("1. No Audience Yet")
    st.write("**Objective**: Find listeners. We offer trend analysis to help identify emerging topics.")
    
    st.subheader("2. Existing Audience")
    st.write("**Objective**: Understand audience interests. RippleXn’s competitor insights reveal what other brands your audience follows.")
    
    st.subheader("3. Lost Audience (Crisis Management)")
    st.write("**Objective**: Crisis response. Real-time insights help brands like Pepsi implement recovery strategies.")
    
    st.subheader("4. Other Voices Speaking")
    st.write("**Objective**: Influence alignment. Equip influencers with the training needed to represent brands effectively.")

elif section == "Entry-Level Products":
    st.title("RippleXp Entry-Level Products for Customer Acquisition")
    st.write("""
    These products are designed to lower the barrier to entry, allowing new clients to experience the RippleXn ecosystem.
    """)
    st.markdown("**$49 FTC/SEC Disclosure Training** - Ensures influencers meet regulatory standards. Ideal for compliance-conscious brands.")
    st.markdown("**$75 Trend Analysis** - Provides 100 hours of curated video insights to identify emerging trends.")
    st.markdown("**$199 Risk & Strategy Support** - Choice of influencer background checks or custom listening strategies.")

elif section == "Advanced Options":
    st.title("RippleXp Advanced Offerings for Engaged Buyers")
    st.write("""
    For clients ready to go further, we offer in-depth courses and tools:
    """)
    st.markdown("**Storytelling Courses** - Enhances narrative skills and crisis response insights.")
    st.markdown("**Social Video Alerts** - Real-time monitoring for risks like greenwashing, crypto-promotions, and crisis prevention.")

elif section == "Additional Resources":
    st.title("Additional Resources and Strategy Guides")
    st.write("""
    Explore strategic resources to see how RippleXp can address key brand concerns and regulatory challenges:
    """)
    st.markdown("- **Strategy Guide**: Using reputational tools to generate leads.")
    st.markdown("- **Exposure Case Studies**: Detailed examples of how RippleXn can address specific brand vulnerabilities.")
    st.markdown("- **Verification Tools**: $49 compliance training to prevent influencer-related backlash.")

# Footer for context and contact
st.write("---")
st.write("Contact RippleXp for more details or to discuss custom solutions tailored to your brand's needs.")
