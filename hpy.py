import streamlit as st
import random

def birthday_wish():
    decorations = ["✨", "🎂", "🎉", "🎁", "❤️", "🥳", "🎈", "💖"]
    border = " " + "".join(random.choices(decorations, k=30))
    
    st.write(border)
    st.markdown("## 🎊🎂 Happy Birthday Bhavya Akka! 🎂🎊")
    st.write(border)
    st.write("")
    
    st.markdown("### May your day be filled with love, joy, and lots of cake! 🍰🎁")
    st.markdown("### You are the best sister ever, and I am so lucky to have you! ❤️💐")
    st.markdown("### Enjoy your special day to the fullest! 🥳🎈🎶")
    st.markdown("### With lots of love, Your Sibling! 💖💞")
    
    st.write(border)

st.title("🎂 Birthday Celebration App 🎂")
birthday_wish()
