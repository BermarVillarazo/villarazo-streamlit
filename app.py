import streamlit as st

st.set_page_config(layout="wide")

# Add custom CSS for tab headers
st.markdown(
    """
    <style>
    /* Style for tab headers */
    .css-1l02z0e { /* Adjust this selector based on the class names Streamlit generates */
        font-size: 2rem; /* 32px */
        line-height: 2.5rem; /* 40px */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a tab for each section
tabs = st.tabs([
    "Introduction", 
    "Curiosity", 
    "First Website", 
    "Challenges", 
    "React", 
    "Next.js", 
    "Ongoing Journey"
])

# Tab content
with tabs[0]:
    st.markdown("""
        <div style="
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        ">
            <div><h1>My Portfolio! 🚀</h1></div>
            <div><h3>Bermar Villarazo</h3></div>
        </div>
        """, unsafe_allow_html=True
    )

with tabs[1]:
    st.write("I started off as a self-taught full stack web developer since I was really curious about the process of making websites.")
    st.write("From a young age, technology fascinated me, and the idea of creating something on the web sparked my interest. I wanted to understand how the websites I visited were built, what made them function, and how I could create something similar.")

with tabs[2]:
    st.write("My first website was a straightforward design made with only HTML, CSS, and a small amount of JavaScript, which I utilized somewhat.")
    st.write("While it wasn't very impressive, it was my first attempt into the world of web development. Even when it was simply a straightforward static website, I can still feel the excitement of watching my code come to life. It gave me a great sense of satisfaction to see what I made online.")

with tabs[3]:
    st.write("My excitement kept me going despite the early challenges as I explored increasingly advanced technologies.")
    st.write("There were times when I was frustrated, particularly when things didn't go as planned. But each challenge presented a chance to learn. I spent many hours debugging and experimenting, where I learned not only programming skills but also problem-solving and logical thinking.")

with tabs[4]:
    st.write("I jumped right into React, but I was disappointed with the tutorials since I found the routing concepts to be a little overwhelming.")
    st.write("Building dynamic and interactive applications with React opened up new possibilities, but at first it felt difficult to understand state management and routing. I watched a lot of lessons, but I still couldn't seem to put everything together properly.")

with tabs[5]:
    st.write("But when I came across Next.js, a full stack framework that made web programming more understandable and simplified routing, everything fell into place.")
    st.write("Next.js was like a breath of fresh air. The development process was significantly more straightforward because of the full stack capabilities and built-in routing. I was able to focus more on developing and less on configuring, which improved my understanding of modern web development methodologies.")

with tabs[6]:
    st.write("I'm still pursuing this interesting educational path now, continuously gaining new knowledge and skills.")
    st.write("There are new challenges to be faced every day, and I'm determined to never stop learning. My journey as a developer is one of continuous growth and change, whether it's learning new frameworks, being up to date with web development trends, or diving further into backend technologies.")
