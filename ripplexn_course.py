import streamlit as st

# Set up page configuration
st.set_page_config(page_title="RippleXn Storytelling Experience", layout="wide")

# Sidebar for main navigation
st.sidebar.title("Course Navigation")
course = st.sidebar.radio("Choose a course:", [
    "Free Trial: The Art of Storytelling",
    "Core Course: The Art of Story",
    "Core Course: Story Design",
    "Core Course: Story Deployment",
    "Immersive Experience: Forum Environment"
])

# Two-column layout for the main content and additional info
left_column, right_column = st.columns([2, 1])

# Main content based on selected course
with left_column:
    if course == "Free Trial: The Art of Storytelling":
        st.title("Free Trial: The Art of Storytelling")
        st.write("""
        **Experience the power of storytelling in an introductory session.**
        
        Learn the basics of storytelling and rhetoric in this free one-hour session. This is your opportunity
        to see how the art of story can transform your brand’s connection with its audience.
        """)
        st.button("Start Free Trial")
    
    elif course == "Core Course: The Art of Story":
        st.title("The Art of Story")
        st.write("""
        **Principle** - Learn the aesthetics of impactful storytelling. This course focuses on the dramatic narrative
        and how to captivate your audience right from the start.
        """)
        st.progress(25)  # Progress bar example
        st.button("Continue to Story Design")

    elif course == "Core Course: Story Design":
        st.title("Story Design")
        st.write("""
        **Model** - Dive into the poetics of storytelling. This course builds on the aesthetics by introducing
        the structural elements that make stories memorable and persuasive.
        """)
        st.progress(50)
        st.button("Continue to Story Deployment")

    elif course == "Core Course: Story Deployment":
        st.title("Story Deployment")
        st.write("""
        **Execution** - Bringing theory into practice. Learn to deploy stories as compelling content
        that shapes conversations and resonates with audiences.
        """)
        st.progress(75)
        st.button("Proceed to Forum Environment")

    elif course == "Immersive Experience: Forum Environment":
        st.title("Forum Environment")
        st.write("""
        **Immersive Experience** - Participate in a 3-day forum with your team, designed for deep learning
        and practical application. Ideal for brands ready to embed storytelling at the cultural level.
        """)
        st.progress(100)
        st.button("Contact Us to Schedule")

# Right column with commercial information
with right_column:
    st.header("Course Structure")
    st.write("""
    **Core Tenets**: Principle, Design Model, Trade Exemplar
    
    Our approach combines aesthetics, structure, and execution. Each level builds a foundation to ensure
    stories are crafted with purpose, from initial concept to audience connection.
    """)

    st.header("Pricing")
    st.write("""
    - **Free Trial**: 1 Hour Intro
    - **Single Session**: €149/hour
    - **Three-Session Bundle**: €399
    - **Full Immersion (3 Days)**: €2999 for groups up to 10
    """)

    st.header("Scheduling Options")
    st.write("Each course is available on-site, virtually, or at our Lisbon learning space.")

# Footer for testimonials
st.write("---")
st.write("**Testimonials**")
st.write("Apple, Nike, and other iconic brands have transformed through storytelling. See the change for yourself.")
