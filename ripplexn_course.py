import streamlit as st

# Set up page configuration
st.set_page_config(page_title="RippleXn Reputation Course", layout="wide")

# 1. Introduction Section
st.title("RippleXn Reputation Course")
st.header("Reputation as a Mosaic")
st.write("""
In RippleXn, reputation is a mosaic—composed of hundreds of individual stories, much like a honeycomb.
Every brand’s narrative relies on these stories, and who’s listening to them matters. This course helps you
navigate the listening landscape to build a resilient brand reputation.
""")

# 2. Audience Identification Module
st.header("Understanding Your Audience")
st.write("### Four Key Audience Types:")
st.write("""
1. **No Audience Yet** - Brands need listeners to understand trends and stay relevant.
2. **Existing Audience** - Brands have listeners but need insights into what else they're paying attention to (competitors).
3. **Lost Audience (Crisis Management)** - Brands in crisis, like Pepsi, who need real-time recovery tactics.
4. **Other Voices Speaking** - Brands with influencers or advocates who need training to represent them effectively.
""")

# Interactive Selection
audience_type = st.selectbox("Select an Audience Type to Learn More:", 
                             ["No Audience Yet", "Existing Audience", "Lost Audience", "Other Voices Speaking"])

if audience_type == "No Audience Yet":
    st.write("Audience Type: **No Audience Yet** - Focus on understanding trends and staying relevant.")
elif audience_type == "Existing Audience":
    st.write("Audience Type: **Existing Audience** - Learn what else your listeners pay attention to, like competitors.")
elif audience_type == "Lost Audience":
    st.write("Audience Type: **Lost Audience (Crisis Management)** - Develop real-time recovery strategies.")
elif audience_type == "Other Voices Speaking":
    st.write("Audience Type: **Other Voices Speaking** - Train influencers and advocates to represent your brand effectively.")

# 3. Entry-Level Products Module
st.header("Entry-Level Products for Customer Acquisition")
st.write("These products are designed to lower the barrier to entry and provide value to new customers.")
st.write("**$49 FTC/SEC Disclosure Training** - Ensures influencers meet regulatory standards.")
st.write("**$75 Trend Analysis Report** - Provides 100 hours of curated insights on current trends.")
st.write("**$199 Risk & Strategy Support** - Choose between an influencer background check or a customized listening strategy.")

# Links to purchase options
st.markdown("[FTC/SEC Disclosure Training](https://example.com/training)")
st.markdown("[Trend Analysis](https://example.com/trend-analysis)")
st.markdown("[Risk & Strategy Support](https://example.com/risk-strategy)")

# 4. Advanced Options Module
st.header("Advanced Options for Sophisticated Buyers")
st.write("For clients ready to engage further, we offer advanced solutions tailored to complex needs.")
st.write("### Storytelling Courses")
st.write("Develop narrative skills and gain insights into crisis response strategies.")
st.write("### Social Video Alerts")
st.write("Receive real-time alerts to identify risks like greenwashing or crypto promotions.")

# 5. Final Quiz/Assessment
st.header("Course Assessment")
st.write("Test your understanding with a quick quiz.")

# Simple Quiz Example
score = 0

question1 = st.radio("1. What does RippleXn mean by reputation as a 'mosaic'?", 
                     ["A single brand message", "Many interconnected stories", "A perfect, unchanging image"])
if question1 == "Many interconnected stories":
    score += 1

question2 = st.radio("2. Which audience type focuses on crisis recovery?", 
                     ["No Audience Yet", "Lost Audience", "Other Voices Speaking"])
if question2 == "Lost Audience":
    score += 1

st.write(f"Your score: {score}/2")

# Completion Message
if score == 2:
    st.success("Congratulations! You've completed the RippleXn Reputation Course.")
else:
    st.info("Keep learning to improve your understanding of brand reputation with RippleXn!")

