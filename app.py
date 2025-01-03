import streamlit as st
import requests

#API URL
API_URL_CHAT = "http://localhost:5000/response"  


st.set_page_config(
    page_title="MediTrain AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .css-1v3fvcr {
        text-align: center;
        font-size: 36px; 
        color: #008000; /* Green */
    }

    .stTextInput>div>input,
    .stTextArea>div>textarea {
        background-color: #f0f8ff; /* Light Blue */
        border: 2px solid #ff69b4; /* Dark Pink */
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        color: #333;
    }

    /* Buttons for Dashboard */
    .stButton>button {
        background-color: white; 
        color: #008080; 
        font-weight: bold;
        font-size: 20px; 
        padding: 14px 28px;
        margin-bottom: 10px;
        cursor: pointer;
        width: 100%;
        text-align: left; 
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); 
    }

    /* Hover effect */
    .stButton>button:hover {
        background-color: #008080; 
        color: white; 
        border: 2px solid #008080; 
        font-size: 22px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2); 
    }

    /* Chat Container */
    .chat-container {
        font-family: 'Arial', sans-serif;
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f0f8ff; 
        border: 2px solid #ff69b4; 
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 20px;
    }

    /* Chat Header */
    .chat-header {
        font-size: 28px; 
        font-weight: bold;
        color: #008000; 
        text-align: center;
        margin-bottom: 20px;
    }

    /* Response Boxes */
    .response-box {
        background-color: #e6f7ff; 
        border-left: 5px solid #ff69b4; 
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        font-size: 16px;
        color: #333;
    }

    /* Labels */
    label {
        font-size: 18px;
        color: #008000;
        font-weight: bold;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: #f0f8ff; 
        color: #008000; 
        border: none;
        border-radius: 10px;
        padding: 20px;
    }

    /* Footer Links */
    a {
        color: #ff69b4; 
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }

    .small-button {
        font-size: 14px; 
        padding: 8px 16px;
        background-color: #008080; 
        color: white;
        border: none; 
        border-radius: 8px; 
        cursor: pointer; 
    }
    .small-button:hover {
        background-color: #005757;

    }

    .home-background {
        background: linear-gradient(135deg, #ffe4e1 0%, #e0f7fa 50%, #e8f5e9 100%);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    .home-header {
        text-align: center;
        color: #004d40;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .home-subheader {
        text-align: center;
        color: #005f73;
        font-size: 28px;
        font-style: italic;
        margin-bottom: 30px;
    }
    .home-content {
        color: #333;
        font-size: 20px;
        line-height: 1.8;
        text-align: justify;
        margin-bottom: 20px;
    }

    .feedback-section {
            margin-bottom: 40px;
        }
        .stSlider>div>div>input {
            width: 60% !important;
            height: 10px !important;
        }
        .button-container {
            margin-top: 20px;
        }
        hr {
            border: 1px solid #00a1a1;  /* Teal color */
            margin-top: 20px;
            margin-bottom: 20px;
        }
    
    </style>
    """, unsafe_allow_html=True
)


# Chat Page

def chat():
    # Initialize the conversation history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Chat header
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown('<div class="chat-header" style="color: #00a1a1; font-size: 28px;">Chat with MediTrain AI</div>', unsafe_allow_html=True)

    for message in st.session_state.history:
        st.markdown(f"<div class='response-box'><strong>{message['sender']}:</strong> {message['text']}</div>", unsafe_allow_html=True)

    user_query = st.text_input("", key="chat_input", label_visibility="collapsed", placeholder="Type your message here")

    if st.button("Send", help="Click to get response"):
        if user_query.strip():
            st.session_state.history.append({"sender": "You", "text": user_query})

            with st.spinner("Thinking... 🤔"):
                try:
                    response = requests.post(API_URL_CHAT, json={"query": user_query})
                    if response.status_code == 200:
                        chatbot_response = response.json().get("response", "No response.")
                        st.session_state.history.append({"sender": "MediTrain", "text": chatbot_response})
                        st.markdown("<div class='response-box'>", unsafe_allow_html=True)
                        st.markdown(f"<strong>MediTrain : </strong> {chatbot_response}", unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please type something to ask MediTrain!")

    st.markdown('</div>', unsafe_allow_html=True)

def home():
    
    st.markdown("""
    <div class="home-background">
        <div class="home-header">
            Welcome to <span style="color: #008080;">Meditrain AI</span>
        </div>
        <div class="home-subheader">
            Your Ultimate Partner in <span style="color: #000; font-weight: bold;">Mastering Medical Knowledge</span> and Revolutionizing Patient Care 🤖💡
        </div>
        <div class="home-content">
            <strong>Meditrain AI</strong> empowers <span style="color: #008080; font-weight: bold;">medical students</span>, 
            <span style="color: #008080; font-weight: bold;">healthcare professionals</span>, and 
            <span style="color: #d81b60; font-weight: bold;">patients</span> by combining <span style="color: #005f73;">advanced AI technology</span> 
            with practical medical scenarios. Whether you’re learning or enhancing your skills, Meditrain AI provides personalized insights and recommendations 
            to help you grow in your medical journey.
        </div>
        <div class="home-content">
            Experience realistic case simulations, improve patient care knowledge, and stay updated with the latest medical trends. Meditrain AI is designed 
            to make learning interactive, engaging, and most importantly, practical. Ready to take your medical knowledge to the next level?
        </div>
    </div>
    """, unsafe_allow_html=True)

# About Page
def about():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    st.markdown('<div class="chat-header" style="color: #00a1a1; font-size: 36px; font-weight: bold;">About MediTrain AI</div>', unsafe_allow_html=True)

    st.markdown("""
    <div>
        <p>MediTrain AI is an advanced conversational assistant redefining how healthcare education and communication are experienced. 
        Built to empower medical students, professionals, and health-conscious individuals, MediTrain bridges the gap between knowledge and practice 
        through interactive simulations and insightful guidance.</p>
    </div>
    <hr style="border: 1px solid #ff69b4; margin: 20px 0;">

    <div>
        <h2 style="color: #008080; font-weight: bold;">Our Vision:</h2>
        <p>We aim to make healthcare education accessible, engaging, and impactful. By offering a platform where users can learn, practice, 
        and grow, MediTrain AI fosters a deeper understanding of healthcare concepts and promotes informed decision-making.</p>
    </div>
    <hr style="border: 1px solid #ff69b4; margin: 20px 0;">

    <div>
        <h2 style="color: #008080; font-weight: bold;">Key Features:</h2>
        <ul style="font-size: 16px; line-height: 1.6;">
            <li><strong style="color: #004d40;">Patient Interaction Simulations:</strong> Engage in realistic scenarios to enhance diagnostic skills and patient communication. MediTrain’s diverse simulations help users tackle complex cases with confidence.</li>
            <li><strong style="color: #004d40;">Medical Education and Insights:</strong> Receive concise and clear explanations of medical concepts tailored to your knowledge level. Whether you're a student or a seasoned professional, MediTrain ensures learning remains relevant and straightforward.</li>
            <li><strong style="color: #004d40;">Health Awareness and Preventive Care:</strong> Explore actionable wellness advice and health tips designed to promote healthy habits. While we avoid personalized medical recommendations, MediTrain AI encourages users to consult qualified professionals for specific concerns.</li>
        </ul>
    </div>
    <hr style="border: 1px solid #ff69b4; margin: 20px 0;">

    <div>
        <h2 style="color: #008080; font-weight: bold;">How We Engage:</h2>
        <ul style="font-size: 16px; line-height: 1.6;">
            <li><strong style="color: #004d40;">Empathy and Encouragement:</strong> Our assistant communicates with warmth and positivity, making users feel valued.</li>
            <li><strong style="color: #004d40;">Simplified Communication:</strong> Avoiding unnecessary jargon, MediTrain explains terms and concepts in a user-friendly manner.</li>
            <li><strong style="color: #004d40;">Proactive Assistance:</strong> Whether clarifying concepts or expanding on queries, MediTrain provides thoughtful and helpful guidance.</li>
        </ul>
    </div>
    <hr style="border: 1px solid #ff69b4; margin: 20px 0;">

    <div>
        <h2 style="color: #008080; font-weight: bold;">Why Choose MediTrain AI?</h2>
        <p><strong>Realistic Learning:</strong> Practice medical scenarios that mimic real-world challenges.</p>
        <p><strong>Customized Experience:</strong> Tailored interactions adapt to your expertise, making learning more effective.</p>
        <p><strong>Health Literacy Promotion:</strong> Empowering users with accurate, understandable, and actionable information to make informed health decisions.</p>
        <p>MediTrain AI is more than just a tool; it’s your partner in mastering healthcare concepts, improving patient interactions, and fostering a proactive approach to health and wellness. Together, we can build a healthier, more informed world.</p>
    </div>
    <hr style="border: 1px solid #ff69b4; margin: 20px 0;">
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def how_to_use():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    st.markdown('<div class="chat-header" style="color: #00a1a1; font-size: 36px; font-weight: bold;">How to Use MediTrain AI</div>', unsafe_allow_html=True)

    st.markdown("""
    <div>
        <p>MediTrain AI helps you practice diagnosing medical conditions and learn about healthcare concepts through interactive simulations. Follow the steps below to get started:</p>
    </div>

    <div>
        <h2 style="color: #008080; font-weight: bold;">Steps to Use:</h2>
        <ul style="font-size: 16px; line-height: 1.6;">
            <li style="color: #004d40;"><strong>Go to the Chat page.</strong></li>
            <li style="color: #004d40;"><strong>Ask questions or describe your symptoms.</strong></li>
            <li style="color: #004d40;"><strong>MediTrain AI will provide recommendations based on your inputs.</strong></li>
            <li style="color: #004d40;"><strong>Use the feedback button to provide us with suggestions or ask for further assistance.</strong></li>
        </ul>
    </div>

    <div>
        <h2 style="color: #008080; font-weight: bold;">Tips:</h2>
        <ul style="font-size: 16px; line-height: 1.6;">
            <li style="color: #004d40;"><strong>Be as specific as possible with your queries.</strong></li>
            <li style="color: #004d40;"><strong>MediTrain AI continuously learns and improves, so your feedback helps us serve you better.</strong></li>
        </ul>
    </div>

   <div class="response-box">
        <h2 style="color: #008080; font-weight: bold;">Use Case Scenario</h2>
        <h3 style="color: #004d40; font-weight: bold;">Scenario: Medical Student Diagnosing a Patient’s Condition</h3>
        <ol style="font-size: 16px; line-height: 1.6;">
            <li><strong style="color: #004d40;">User Opens Chat:</strong> Alex opens the Meditrain AI app and navigates to the Chat page to start a patient diagnosis simulation.</li>
            <li><strong style="color: #004d40;">Initiating the Chat:</strong> MediTrain AI: *“Hello, Alex! I’m here to help you practice diagnosing medical cases. Are you ready for a simulation?”* <br> Alex: *“Yes, let’s start.”*</li>
            <li><strong style="color: #004d40;">Presenting a Case:</strong> MediTrain AI: *“A 45-year-old male presents with fever, sore throat, body aches, and a persistent cough. What condition do you suspect?”* <br> Alex: *“It sounds like the flu.”*</li>
            <li><strong style="color: #004d40;">Asking Probing Questions:</strong> MediTrain AI: *“Does the patient have any difficulty breathing or chest pain?”* <br> Alex: *“No, there’s no chest pain or shortness of breath.”*</li>
            <li><strong style="color: #004d40;">Confirming Diagnosis:</strong> MediTrain AI: *“The flu seems likely, but always watch for complications. Would you like to explore more about flu management?”* <br> Alex: *“Yes.”*</li>
            <li><strong style="color: #004d40;">Educational Insights:</strong> MediTrain AI: *“Flu is caused by influenza viruses and resolves in 1-2 weeks. Rest, fluids, and over-the-counter medications are key.”* <br> Alex: *“Thanks for the details!”*</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)



def feedback():
   
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    st.markdown('<div class="chat-header" style="color: #00a1a1; font-size: 36px; font-weight: bold;">Feedback for MediTrain AI</div>', unsafe_allow_html=True)

    
    st.markdown('<div class="feedback-section">', unsafe_allow_html=True)
    st.markdown("""
    <h2 style="color: #008080; font-weight: bold; font-size: 24px;">Rate Your Experience ⭐️</h2>
    <p style="font-size: 16px;">How would you rate your experience with MediTrain AI? Please select a rating below:</p>
    """, unsafe_allow_html=True)
    
    rating = st.slider("Rate your experience:", 1, 5)
    st.markdown(f"<p style='font-size: 24px; color: #008080;'>Rating: {'⭐️' * rating}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<hr>', unsafe_allow_html=True)

    
    st.markdown('<div class="feedback-section">', unsafe_allow_html=True)
    st.markdown("""
    <h2 style="color: #008080; font-weight: bold; font-size: 24px;">Your Feedback 💬</h2>
    <p style="font-size: 16px;">Please share any comments, suggestions, or issues you encountered:</p>
    """, unsafe_allow_html=True)
    user_feedback = st.text_area("", height=150)
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<hr>', unsafe_allow_html=True)

    
    st.markdown('<div class="feedback-section">', unsafe_allow_html=True)
    st.markdown("""
    <h2 style="color: #008080; font-weight: bold; font-size: 24px;">Contact Information (Optional) 📧</h2>
    <p style="font-size: 16px;">Your email (optional):</p>
    """, unsafe_allow_html=True)
    user_email = st.text_input("Email (optional)")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    submit_button = st.button("Submit Feedback")

    if submit_button:
        if user_feedback:
            st.success("Thank you for your feedback! 😊")
            
            with open("feedback.txt", "a") as file:
                file.write(f"Rating: {rating}\nFeedback: {user_feedback}\nEmail: {user_email if user_email else 'N/A'}\n\n")
        else:
            st.warning("Please provide feedback before submitting. ⚠️")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<hr>', unsafe_allow_html=True)

    
    st.markdown("""
    <div class="response-box">
        <h2 style="color: #008080; font-weight: bold; font-size: 24px;">Get in Touch 📱</h2>
        <p>If you'd like to connect with me, feel free to reach out on LinkedIn or send an email!</p>
        <ul>
            <li><a href="https://www.linkedin.com/in/anushri-soni" style="color: #008080;">LinkedIn</a>🔗</li>
            <li><a href="mailto:anushriisoni@gmail.com" style="color: #008080;">anushriisoni@gmail.com</a> 📧</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Main function to navigate between pages
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Sidebar with navigation buttons
    st.sidebar.title("DASH-BOARD")
    if st.sidebar.button("HOME"):
        st.session_state.page = "home"
    if st.sidebar.button("CHAT"):
        st.session_state.page = "chat"    
    if st.sidebar.button("ABOUT"):
        st.session_state.page = "about"
    if st.sidebar.button("EXPLORE"):
        st.session_state.page = "how_to_use"
    
    if st.sidebar.button("FEEDBACK"):
        st.session_state.page = "feedback"
        
    
    # Display the selected page
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "chat":
        chat()
    elif st.session_state.page == "about":
        about()
    elif st.session_state.page == "how_to_use":
        how_to_use()
    
    elif st.session_state.page == "feedback":
        feedback()

if __name__ == "__main__":
    main()
