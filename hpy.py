import streamlit as st
import random
import time
from datetime import datetime, date

def birthday_wish():
    decorations = ["✨", "🎂", "🎉", "🎁", "❤️", "🥳", "🎈", "💖"]
    border = " " + "".join(random.choices(decorations, k=30))
    
    st.write(border)
    st.markdown("# 🎊🎂 Happy Birthday Bhavya Akka! 🎂🎊")
    st.image("https://i.imgur.com/4M34hi2.png", caption="A Special Day for a Special Sister! 💖")
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
    st.image("https://i.imgur.com/8xO5F5X.jpg", caption="Happy Birthday Bhavya Akka! 🎂")
    
    # Interactive greeting input
    user_greeting = st.text_area("Write a special message for Bhavya Akka:")
    if user_greeting:
        st.markdown(f"### 💌 Your Message: {user_greeting} 💌")
        st.success("Your message has been shared! 🎊")
    
    # Add a countdown to her next birthday
    st.markdown("## ⏳ Countdown to Next Birthday ⏳")
    today = date.today()
    this_year_birthday = date(today.year, 2, 27)
    if today > this_year_birthday:
        next_birthday = date(today.year + 1, 2, 27)
    else:
        next_birthday = this_year_birthday
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
        st.image("https://i.imgur.com/rzX6CgE.jpg", caption="A Special Surprise for You! 🎁")
    
    # Add a virtual birthday gift selection
    st.markdown("## 🎁 Choose a Virtual Gift for Bhavya Akka 🎁")
    gifts = {
        "🌹 A Beautiful Rose": "https://i.imgur.com/VzJL2vB.jpg",
        "🍫 A Box of Chocolates": "https://i.imgur.com/9N1FFRH.jpg",
        "💍 A Sparkling Ring": "https://i.imgur.com/5QK7rUJ.jpg",
        "🧸 A Cute Teddy Bear": "https://i.imgur.com/YHbPiYy.jpg"
    }
    selected_gift = st.selectbox("Pick a gift to send:", list(gifts.keys()))
    if selected_gift:
        st.image(gifts[selected_gift], caption=selected_gift)
        st.success(f"You have gifted {selected_gift} to Bhavya Akka! 🎁💖")
    
    # Birthday Memory Sharing Section
    st.markdown("## 📸 Share Your Favorite Memory with Bhavya Akka 📸")
    memory = st.text_area("Write a cherished memory you have with her:")
    if memory:
        st.markdown(f"### 🌟 Memory Shared: {memory} 🌟")
        st.success("Your special memory has been saved! 💖")

st.title("🎂 Bhavya Akka's Birthday Celebration 🎂")
st.subheader("A Special Gift Just for You! 💖")
birthday_wish()
