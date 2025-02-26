import streamlit as st
import random
import time
from datetime import datetime, date

def birthday_wish():
    decorations = ["✨", "🎂", "🎉", "🎁", "❤️", "🥳", "🎈", "💖"]
    border = " " + "".join(random.choices(decorations, k=30))
    
    st.write(border)
    st.markdown("# 🎊🎂 Happy Birthday Bhavya Akka! 🎂🎊")
    st.write(border)
    st.write("")
    
    messages = [
        "### May your day be filled with love, joy, and lots of cake! 🍰🎁",
        "### You are the best sister ever, and I am so lucky to have you! ❤️💐",
        "### Enjoy your special day to the fullest! 🥳🎈🎶",
        "### With lots of love, Your Sibling! 💖💞"
    ]
    
    for message in messages:
        st.markdown(message)
        time.sleep(1)
    
    st.write(border)
    
    # Add a birthday song effect
    if st.button("🎵 Play Birthday Song 🎵"):
        st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BirthdaySong.mp3")
    
    # Display a fun confetti animation
    st.balloons()
    
    # Add an image for a personalized touch
    st.image("https://www.happybirthdayimages.com/images/birthday-cake.jpg", caption="Happy Birthday Bhavya Akka! 🎂")
    
    # Interactive greeting input
    user_greeting = st.text_area("Write a special message for Bhavya Akka:")
    if user_greeting:
        st.markdown(f"### 💌 Your Message: {user_greeting} 💌")
        st.success("Your message has been shared! 🎊")
    
    # Add a countdown to her next birthday
    st.markdown("## ⏳ Countdown to Next Birthday ⏳")
    today = date.today()
    next_birthday = date(today.year + 1, 2, 27) if today > date(today.year, 2, 27) else date(today.year, 2, 27)
    countdown = (next_birthday - today).days
    st.metric(label="Days Until Bhavya Akka's Next Birthday", value=countdown)
    
    # Add a fun random birthday quote
    quotes = [
        "Birthdays are nature’s way of telling us to eat more cake! 🎂",
        "Age is merely the number of years the world has been enjoying you! 😊",
        "The more you praise and celebrate your life, the more there is in life to celebrate! 🎉",
        "Count your age by friends, not years. Count your life by smiles, not tears! ❤️"
    ]
    st.markdown(f"## 💬 Birthday Quote of the Day: {random.choice(quotes)}")
    
    # Add a surprise button for an extra greeting
    if st.button("🎁 Click for a Surprise!"):
        st.success("🎉 Surprise! Wishing you a year full of happiness and success, Bhavya Akka! 💖🎊")
        st.image("https://www.happybirthdayimages.com/images/birthday-surprise.jpg", caption="A Special Surprise for You! 🎁")

st.title("🎂 Birthday Celebration App 🎂")
st.subheader("Let's make this day extra special!")
birthday_wish()
