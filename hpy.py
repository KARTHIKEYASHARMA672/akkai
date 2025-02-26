import streamlit as st
import random
import time
from datetime import date

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
    
    # Music Selection
    st.markdown("## 🎵 Choose a Birthday Song 🎵")
    song_options = {
        "Classic Birthday Song": "https://www2.cs.uic.edu/~i101/SoundFiles/BirthdaySong.mp3",
        "Fun Remix": "https://sample-videos.com/audio/mp3/crowd-cheering.mp3"
    }
    selected_song = st.selectbox("Pick a song to play:", list(song_options.keys()))
    if st.button("🎶 Play Selected Song 🎶"):
        st.audio(song_options[selected_song])
    
    # Confetti & Celebration Button
    if st.button("🎊 Celebrate 🎊"):
        st.balloons()
        st.snow()
    
    # Teddy Bear Corner
    st.markdown("## 🧸 Bhavya Akka's Teddy Bear Corner 🧸")
    st.image("https://i.imgur.com/YHbPiYy.jpg", caption="A Cute Teddy Just for You! 🧸💖")
    st.success("Since you love teddy bears, here's a virtual one just for you! 🎁")
    
    # Personal Message Input
    user_greeting = st.text_area("Write a special message for Bhavya Akka:")
    if user_greeting:
        st.markdown(f"### 💌 Your Message: {user_greeting} 💌")
        st.success("Your message has been shared! 🎊")
    
    # Countdown Timer
    st.markdown("## ⏳ Countdown to Next Birthday ⏳")
    today = date.today()
    birthday = date(today.year, 2, 27)
    if today > birthday:
        birthday = date(today.year + 1, 2, 27)
    days_left = (birthday - today).days
    st.metric(label="Days Until Bhavya Akka's Next Birthday 🎂", value=days_left)
    
    # Birthday Trivia Question
    st.markdown("## 🤔 Birthday Trivia! 🤔")
    trivia_question = "What is Bhavya Akka's favorite childhood toy?"
    options = ["Dolls", "Teddy Bears", "Lego", "Board Games"]
    answer = st.radio(trivia_question, options)
    if answer == "Teddy Bears":
        st.success("🎉 Correct! She loves teddy bears! 🧸")
    elif answer:
        st.error("Oops! Try again! 🎈")
    
    # Virtual Gift Selection
    st.markdown("## 🎁 Choose a Virtual Gift for Bhavya Akka 🎁")
    gifts = {
        "🌹 A Beautiful Rose": "https://i.imgur.com/VzJL2vB.jpg",
        "🍫 A Box of Chocolates": "https://i.imgur.com/9N1FFRH.jpg",
        "💍 A Sparkling Ring": "https://i.imgur.com/5QK7rUJ.jpg",
        "🧸 A Cute Teddy Bear": "https://i.imgur.com/YHbPiYy.jpg",
        "🎈 A Colorful Balloon Set": "https://i.imgur.com/4yXCsPT.jpg",
        "🎨 A Personalized Artwork": "https://i.imgur.com/F9qTqDp.jpg"
    }
    selected_gift = st.selectbox("Pick a gift to send:", list(gifts.keys()))
    if selected_gift:
        st.image(gifts[selected_gift], caption=selected_gift)
        st.success(f"You have gifted {selected_gift} to Bhavya Akka! 🎁💖")
    
    # Memory Sharing with Photo Upload
    st.markdown("## 📸 Share Your Favorite Memory with Bhavya Akka 📸")
    memory = st.text_area("Write a cherished memory you have with her:")
    uploaded_photo = st.file_uploader("Upload a photo of the memory:", type=["jpg", "png", "jpeg"])
    if memory and uploaded_photo:
        st.markdown(f"### 🌟 Memory Shared: {memory} 🌟")
        st.image(uploaded_photo, caption="A Beautiful Memory! 💖")
        st.success("Your special memory has been saved! 💖")
    
    # Celebration Video
    st.markdown("## 🎊 Let's Celebrate! 🎊")
    st.video("https://www.youtube.com/watch?v=ho08YLYDM88")
    st.success("Hope you enjoy this special day! 💖🎂🥳")
    
# App Title & Header
st.title("🎂 Bhavya Akka's Birthday Celebration 🎂")
st.subheader("A Special Gift Just for You! 💖")
birthday_wish()
