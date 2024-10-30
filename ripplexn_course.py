import streamlit as st

# Set up page configuration
st.set_page_config(page_title="RippleXn Reputation Course", layout="wide")

# Sidebar for navigation
st.sidebar.title("RippleXn Navigation")
section = st.sidebar.radio("Select a section:", [
    "Introduction",
    "I Need an Audience",
    "I Have an Audience",
    "Lost Audience (Crisis Management)",
    "Other Voices Speaking",
    "Entry-Level Products",
    "Advanced Options",
    "Course Assessment"
])

# Main content based on sidebar selection
if section == "Introduction":
    st.title("RippleXn Reputation Course")
    st.header("Reputation as a Mosaic")
    st.write("""
    In RippleXn, reputation is a mosaic—composed of hundreds of individual stories, much like a honeycomb.
    Every brand’s narrative relies on these stories, and who’s listening to them matters. This course helps you
    navigate the listening landscape to build a resilient brand reputation.
    """)

elif section == "I Need an Audience":
    st.header("Understanding Your Audience - I Need an Audience")
    st.write("Focus on finding listeners to understand trends and stay relevant in the market.")
    st.write("""
    For brands that need to build an audience, the goal is to capture trends and leverage insights to engage potential listeners.
    RippleXn helps by identifying what's resonating across channels and emerging topics.
    """)

elif section == "I Have an Audience":
    st.header("Understanding Your Audience - I Have an Audience")
    st.write("You have listeners but need insights into what else they're paying attention to.")
    st.write("""
    For brands with an existing audience, RippleXn provides tools to explore competitor engagement,
    audience interests, and topics that capture attention beyond your brand's core message.
    """)

elif section == "Lost Audience (Crisis Management)":
    st.header("Understanding Your Audience - Lost Audience (Crisis Management)")
    st.write("For brands experiencing a crisis, quick recovery strategies are essential.")
    st.write("""
    Brands like Pepsi in times of crisis need real-time monitoring and recovery tactics.
    RippleXn provides immediate insights and response tools to manage and rebuild audience trust.
    """)

elif section == "Other Voices Speaking":
    st.header("Understanding Your Audience - Other Voices Speaking")
    st.write("Brands with influencers or advocates who need training to represent them effectively.")
    st.write("""
    For brands working with influencers or advocates, RippleXn offers training and monitoring tools
    to ensure brand messaging is consistent and regulations are adhered to.
    """)

elif section == "Entry-Level Products":
    st.header("Entry-Level Products for Customer Acquisition")
    st.write("These products are designed to lower the barrier to entry and provide value to new customers.")
    st.write("**$49 FTC/SEC Disclosure Training** - Ensures influencers meet regulatory standards.")
    st.write("**$75 Trend Analysis Report** - Provides 100 hours of curated insights on current trends.")
    st.write("**$199 Risk & Strategy Support** - Choose between an influencer background check or a customized listening strategy.")
    st.markdown("[FTC/SEC Disclosure Training](https://example.com/training)")
    st.markdown("[Trend Analysis](https://example.com/trend-analysis)")
    st.markdown("[Risk & Strategy Support](https://example.com/risk-strategy)")

elif section == "Advanced Options":
    st.header("Advanced Options for Sophisticated Buyers")
    st.write("For clients ready to engage further, we offer advanced solutions tailored to complex needs.")
    st.write("### Storytelling Courses")
    st.write("Develop narrative skills and gain insights into crisis response strategies.")
    st.write("### Social Video Alerts")
    st.write("Receive real-time alerts to identify risks like greenwashing or crypto promotions.")

elif section == "Course Assessment":
    st.header("Course Assessment")
    st.write("Test your understanding with a quick quiz.")

    # Simple Quiz Example
    score = 0

    question1 = st.radio("1. What does RippleXn mean by reputation as a 'mosaic'?", 
                         ["A single brand message", "Many interconnected stories", "A perfect, unchanging image"])
    if question1 == "Many interconnected stories":
        score += 1

    question2 = st.radio("2. Which audience type focuses on crisis recovery?", 
                         ["I Need an Audience", "Lost Audience (Crisis Management)", "Other Voices Speaking"])
    if question2 == "Lost Audience (Crisis Management)":
        score += 1

    st.write(f"Your score: {score}/2")

    # Completion Message
    if score == 2:
        st.success("Congratulations! You've completed the RippleXn Reputation Course.")
    else:
        st.info("Keep learning to improve your understanding of brand reputation with RippleXn!")

