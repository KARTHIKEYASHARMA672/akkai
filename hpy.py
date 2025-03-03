import streamlit as st
import random
import time
from datetime import datetime, date

def birthday_wish():
    decorations = ["✨", "🎂", "🎉", "🎁", "❤️", "🥳", "🎈", "💖"]
    border = " " + "".join(random.choices(decorations, k=20))
    
    st.write(border)
    st.markdown("# 🎊🎂 Happy Birthday Bhavya Akkaii! 🎂🎊")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/happy-birthday-greeting-flyer-poster-template-design-a71245c36f740aef073cffc87d7086b2_screen.jpg?ts=1693368143.png", caption="A Special Day for a Special Sister! 💖")
    st.write(border)
    st.write("")

    st.markdown("## 🎂 Blowing Out Candles in...")

    countdown_placeholder = st.empty()  # Placeholder for updating countdown

    for i in range(5, 0, -1):
       countdown_placeholder.markdown(f"### 🕯️ {i}...")
       time.sleep(1)

    countdown_placeholder.markdown("### 🎉 Make a Wish & Blow the Candles! 🕯️✨")

    st.balloons()  # Balloons after countdown!
    
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
        st.audio("https://screenapp.io/app/#/shared/MGssgry3gs")
    
    # Display a fun confetti animation
    st.snow()
    st.balloons()
    
    # Add an animated GIF
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHd6NnJya3NoMmQ2NDJybTljbDE3NHF1dzI1bWx1OXl5cTJpMDYwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cJoJXuKkiQthQjymBi/giphy.gif", caption="Party Time! 🎉")
    
    # Add a special teddy bear section
    st.markdown("## 🧸 Akka your  Teddy Bear Corner 🧸")
    st.image("https://i.pinimg.com/474x/39/54/6d/39546daa4ba02e152fa8f98ad363e86b.jpg", caption="A Cute Teddy Just for You! 🧸💖")
    st.success("Since you love teddy bears, here's a virtual one just for you! 🎁")
    
    # Interactive greeting input
    st.markdown("## 💌  A Special Birthday Message for you Akkaii!")
    user_greeting = st.text_area("Write your heartfelt message:")

    # Button to generate a random birthday wish
    if st.button("💡 Need help? Generate a Random Wish!"):
        random_wishes = [
            "Happy Birthday, Akka! 🎉 Wishing you a day filled with love, joy, and all your favorite things! ❤️",
            "You're the best sister ever! 💖 May this year bring you endless happiness and success! 🥳",
            "Sending you warm hugs and lots of love on your special day! 🎁 Stay blessed always! 💕",
            "To my amazing Akka, may your dreams come true and your heart always be filled with joy! 🎈",
        ]
        user_greeting = random.choice(random_wishes)
        st.text_area("Here's a message for you!", user_greeting)

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
        st.success("🎉 Surprise! Wishing you a year full of happiness and success for u Akkaiii! 💖🎊")
        st.image("https://media.istockphoto.com/id/187782138/photo/opened-christmas-gift-box-with-glow-and-sparkling-stars.jpg?s=612x612&w=0&k=20&c=9TLMmznOxZbkHchDD5DrXT-HmEvKG_SPXf9spaaTAX4=", caption="A Special Surprise for You which is filled with my heart! 🎁")
    
    # Add a virtual birthday gift selection
    st.markdown("## 🎁 Choose a Virtual Gift for you Akka 🎁")
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
    st.markdown("## 📸 Share a Favorite Memory with you Akka 📸")
    memory = st.text_area("Write hi in this :")
    if memory:
        st.markdown(f"### 🌟 Memory Shared: {memory} 🌟")
        st.success("Your special memory has been saved! 💖")
        st.markdown("## ✨ A Special Poem for you Akka ✨")
        poem = (
            "Roses are red, violets are blue,"
            "On your birthday, we celebrate you!🎉,"
            "A sister so kind, loving, and bright,"
            "You make our world shine with pure delight💖,"
            "Through every laugh and every tear,"
            "You've always been so near and dear,"
            "So on this day, we wish you cheer,"
            "A year of joy and dreams so clear! 🥳💐"
        )
        st.markdown(f"### 💕 {poem} 💕")

    
    # Extra Festive Elements
    st.markdown("## 🎊 Let's Celebrate! 🎊")
    st.video("https://www.youtube.com/watch?v=ho08YLYDM88")
    st.success("Hope you enjoy this special day! 💖🎂🥳")

st.title("🎂 Bhavya Akka's Birthday Celebration 🎂")
st.subheader("A Special Gift Just for You! 💖")
birthday_wish()
