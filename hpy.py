import streamlit as st
import random
import time
from datetime import datetime, date

def birthday_wish():
    decorations = ["✨", "🎂", "🎉", "🎁", "❤️", "🥳", "🎈", "💖"]
    border = " " + "".join(random.choices(decorations, k=30))
    
    st.write(border)
    st.markdown("# 🎊🎂 Happy Birthday Bhavya Akka! 🎂🎊")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/happy-birthday-greeting-flyer-poster-template-design-a71245c36f740aef073cffc87d7086b2_screen.jpg?ts=1693368143.png", caption="A Special Day for a Special Sister! 💖")
    st.write(border)
    st.write("")
    
    messages = [
        "### May your day be filled with love, joy, and lots of cake! 🍰🎁",
        "### You are the best sister ever, and I am so lucky to have you! ❤️💐",
        "### Enjoy your special day to the fullest! 🥳🎈🎶",
        "### With lots of love, Your brother! 💖💞"
    ]
    
    for message in messages:
        st.markdown(message)
        time.sleep(1)
    
    st.write(border)
    
    # Add a birthday song effect
    if st.button("🎵 Play Birthday Song 🎵"):
        st.audio("https://drive.google.com/uc?export=download&id=18AGzDkx1hYelX6sZpelonA-MwdgOg6Md")
    
    # Display a fun confetti animation
    st.snow()
    st.balloons()
    
    # Add an animated GIF
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHd6NnJya3NoMmQ2NDJybTljbDE3NHF1dzI1bWx1OXl5cTJpMDYwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cJoJXuKkiQthQjymBi/giphy.gif", caption="Party Time! 🎉")
    
    # Add a special teddy bear section
    st.markdown("## 🧸 Bhavya Akka's Teddy Bear Corner 🧸")
    st.image("https://i.pinimg.com/474x/39/54/6d/39546daa4ba02e152fa8f98ad363e86b.jpg", caption="A Cute Teddy Just for You! 🧸💖")
    st.success("Since you love teddy bears, here's a virtual one just for you! 🎁")
    
    # Interactive greeting input
    user_greeting = st.text_area("Write a special message for Bhavya Akka:")
    if user_greeting:
        st.markdown(f"### 💌 Your Message: {user_greeting} 💌")
        st.success("Your message has been shared! 🎊")
    
    # Add a countdown to her next birthday
    st.markdown("## ⏳ Countdown to Next Birthday ⏳")
    today = date.today()
    birthday = date(today.year, 2, 27)
    
    if today > birthday:
        birthday = date(today.year + 1, 2, 27)
    
    days_left = (birthday - today).days
    
    st.metric(label="Days Until Bhavya Akka's Next Birthday 🎂", value=days_left)
    
    # Add a fun random birthday quote
    quotes = [
        "Birthdays are nature’s way of telling us to eat more cake! 🎂",
        "Age is merely the number of years the world has been enjoying you! 😊",
        "The more you praise and celebrate your life, the more there is in life to celebrate! 🎉",
        "Count your age by friends, not years. Count your life by smiles, not tears! ❤️"
    ]
    st.markdown(f"## 💬 Birthday Quote of the Day: {random.choice(quotes)}")
    
    # Add a surprise button for an extra greeting
    if st.button("🎁 Click for a Surprise! 🎁"):
        st.success("🎉 Surprise! Wishing you a year full of happiness and success, Bhavya Akka! 💖🎊")
        st.image("https://i.imgur.com/rzX6CgE.jpg", caption="A Special Surprise for You! 🎁")
    
    # Add a virtual birthday gift selection
    st.markdown("## 🎁 Choose a Virtual Gift for Bhavya Akka 🎁")
    gifts = {
        "🌹 A Beautiful Rose": "https://i.pinimg.com/736x/65/a6/50/65a6508ecd6bd85b2c5b2eb57a4482dc.jpg",
        "🍫 A Box of Chocolates": "https://luvflowercake.com/wp-content/uploads/2022/10/23.1.webp",
        "💍 A Sparkling Ring": "https://cdn.shopify.com/s/files/1/0081/7496/0736/t/5/assets/pf-2b3777ef-2ff8-442e-be4d-7cdf4e124d90--saltandpepperdiamondclawprongs.jpg?v=1576239493",
        "🧸 A Cute Teddy Bear": "https://m.media-amazon.com/images/I/61JDO9ItiXL.jpg",
        "🎈 A Colorful Balloon Set": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsLPXwkLSO0OuUD2LYnsqrga9BltnyrRwRxA&s",
        "🎨 A Personalized Artwork": "https://m.media-amazon.com/images/I/81LTw1+JAOL._UF350,350_QL50_.jpg"
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

    
    # Extra Festive Elements
    st.markdown("## 🎊 Let's Celebrate! 🎊")
    st.video("https://www.youtube.com/watch?v=ho08YLYDM88")
    st.success("Hope you enjoy this special day! 💖🎂🥳")

st.title("🎂 Bhavya Akka's Birthday Celebration 🎂")
st.subheader("A Special Gift Just for You! 💖")
birthday_wish()
