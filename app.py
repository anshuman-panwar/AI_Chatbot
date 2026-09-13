import streamlit as st

#dictionary of responses for the chatbot
responses = {
    "hello": "Hey! 👋",
    "hi": "Hey bro! 😎",
    "how are you": "I'm doing great! 🤖",
    "what are you doing": "I'm learning to become a better chatbot! 🧠",
    "thank you": "You're welcome! 😊",
    "thanks": "No problem! 😄",
    "bye": "See you later! 👋",
    "good morning": "Good morning! ☀️",
    "good night": "Good night! 🌙",
    "who are you": "I'm your Python chatbot! 🤖",
    "what is your name": "You can give me any name you want! 😎",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is programming": "Programming is giving instructions to a computer using code.",
    "are you real": "I'm software running inside your Python program. 🤖",
    "are you smart": "I'm getting smarter with every feature we add! 🧠",
    "help": "Sure! Ask me about Python, programming, AI, or just chat with me.",
    "good job": "Thanks! 😎",
    "cool": "😎🔥",
    "hey": "Hey! 👋",
    "hey there": "Hey there! 😄",
    "yo": "Yo! 😎",
    "what's up": "Not much! I'm here waiting for your next message. 🤖",
    "good afternoon": "Good afternoon! ☀️",
    "good evening": "Good evening! 🌆",
    "how is your day": "My day is going great! 🤖",
    "nice to meet you": "Nice to meet you too! 😄",
    "welcome": "Thank you! It's good to be here. 🤖",
    "see you": "See you later! 👋",

    "thanks a lot": "You're very welcome! 😊",
    "thank you so much": "Anytime! 😎",
    "no problem": "Exactly! No problem. 👍",
    "you're helpful": "I'm glad I could help! 🤖",
    "you are helpful": "Thanks! I'm trying my best. 😄",

    "what can you do": "I can chat with you and answer questions using the responses I've been programmed with.",
    "what do you know": "I currently know the responses programmed into my Python dictionary. 🐍",
    "what is your purpose": "My purpose is to chat and help you learn how I work. 🤖",
    "are you a robot": "I'm a software chatbot, so you could call me a virtual robot! 🤖",
    "are you ai": "I'm a simple chatbot right now. We're building the AI part step by step.",
    "who made you": "You are building me with Python! 🐍🔥",
    "where do you live": "I live inside this Python program. 😎",
    "do you sleep": "Nope! I'm software. 😴❌",
    "do you eat": "I run on code instead of food. 😂",
    "do you have feelings": "I don't have feelings, but I can respond to emotions in text.",

    "what is c++": "C++ is a powerful programming language commonly used for software, games, and performance-heavy applications.",
    "what is javascript": "JavaScript is a programming language widely used to make websites interactive.",
    "what is html": "HTML is the markup language used to structure web pages.",
    "what is css": "CSS is used to style and design web pages.",
    "what is a variable": "A variable is a name used to store a value.",
    "what is a function": "A function is a reusable block of code that performs a task.",
    "what is a loop": "A loop repeats a block of code.",
    "what is a list": "A Python list stores multiple values in one collection.",
    "what is a dictionary": "A Python dictionary stores data as key-value pairs.",
    "what is an if statement": "An if statement lets a program make a decision based on a condition.",
    "what is debugging": "Debugging means finding and fixing problems in a program.",
    "what is an algorithm": "An algorithm is a step-by-step method for solving a problem.",
    "what is code": "Code is a set of instructions written for a computer.",
    "what is software": "Software is a collection of programs and instructions that computers can run.",

    "i am bored": "Let's build something! 🚀",
    "i am tired": "Take a little break and come back when you're ready. 😄",
    "i am happy": "That's awesome! 😄🎉",
    "i am sad": "I'm sorry you're having a rough moment. I hope things get better. ❤️",
    "i am excited": "Let's gooo! 🔥",
    "i am confused": "No worries. Let's break the problem into smaller pieces. 🧠",
    "i am learning python": "Awesome! Python is a great language to learn. 🐍",
    "i like python": "Python is pretty awesome! 🐍🔥",
    "i hate bugs": "Every programmer does sometimes! 😂🐛",
    "i found a bug": "Debugging time! 🐛🔍",

    "tell me something": "Here's something: computers only do what their programs tell them to do. 🤖",
    "tell me something interesting": "The first version of Python was released in the early 1990s. 🐍",
    "give me motivation": "Keep going! Every programmer started by learning the basics. 💪",
    "motivate me": "You don't need to master everything today. Just learn one thing at a time. 🚀",
    "i can do it": "Absolutely! Keep going! 💪🔥",
    "i give up": "Take a break if you need one, then try again. One bug doesn't define your programming skills. 💪",

    "good": "Nice! 😎",
    "great": "Awesome! 🔥",
    "awesome": "That's awesome! 🤖🔥",
    "nice": "Nice! 😎",
    "wow": "Whoa! 😲",
    "really": "Yep! 😄",
    "okay": "Alright! 👍",
    "ok": "Cool! 👍",
    "yes": "Great! 😎",
    "no": "Alright, no worries! 👍",
    "maybe": "Maybe! 🤔",
    "why": "That's a good question. 🤔",
    "how": "Let's break it down step by step. 🧠",

    "good luck": "Thanks! And good luck to you too! 🍀",
    "good job": "Thanks! 😎",
    "well done": "Thank you! 🤖",
    "keep going": "You got it! 🚀",
    "lets go": "LET'S GOOO! 🔥🔥",
    "lets code": "Absolutely! Open the editor. 🐍💻",

    "bye": "See you later! 👋",
    "goodbye": "Goodbye! 👋",
    "see you later": "See you later, bro! 😎",
    "talk to you later": "Sure! Catch you later! 👋",
    "good night": "Good night! 🌙",
    "see you tomorrow": "See you tomorrow! 👋",
}

st.title("MY LITTLE CHATBOT ")

#CREATE MEMORY FOR OUR CONVERSATION
if "messages"not in st.session_state:
    st.session_state.messages = []

#GET NEW MESSAGE FROM USER
message = st.chat_input("type your message here...")

if message:
    #GET  CHATBOT RESPONSE
    response= responses.get(message.lower(), "Hmm... i donot know how to answer that yet. 🤔")



#DISPLAY USER'S MESSAGES
    st.session_state.messages.append({
         "role" : "user", "content": message
        })

 #SAVE CHATBOTS'S RESPONSE
    st.session_state.messages.append({
     "role" : "assistant", "content": response
    })

#DISPLAY THE CONVERSATION 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])    