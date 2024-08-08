import win32com.client
import speech_recognition as sp
import os
import datetime
import webbrowser
import time
# import google.generativeai as genai


# Initialize the speaker object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# List all available voices
voices = speaker.GetVoices()

# Display all available voices and their attributes
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.GetDescription()}")

# Set the speaker voice to a female voice
# Assuming that the second voice (index 1) is a female voice for demonstration
# You can select the appropriate index based on the output of the above loop
female_voice_index = 0
speaker.Voice = voices.Item(female_voice_index)
def aia(mem):
    # Configure Google Generative AI with your actual API key
    genai.configure(api_key="AIzaSyAVsZ-Fy0stKCUnCzApHbS5wJR9HVqy0WE")

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(mem)

    # Extract the text from the response
    te = response.text
    speaker.Speak(te)
    print(te)

def ai(message):
    # Configure Google Generative AI with your actual API key
    genai.configure(api_key="AIzaSyBkcG0Dl1qLAWhQ4dCXZE2Jed2-kmWfYD8")

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(message)

    # Extract the text from the response
    tex = response.text

    if not os.path.exists("SaarthiAI"):
        os.mkdir("SaarthiAI")

    # Generate a unique file name using a timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_name = ''.join(message.split('intelligence')[1:]).strip()
    file_name = file_name.replace(" ", "  ").replace("/", "_") + f"_{timestamp}.txt"
    file_path = os.path.join("SaarthiAI", file_name)

    # Save the response text to the file
    with open(file_path, "w") as f:
        f.write(tex)
    speaker.Speak(tex)
    print(tex)
    # Use the speaker to read the text


def take():
    t = sp.Recognizer()
    with sp.Microphone() as source:
        t.pause_threshold = 1
        audio = t.listen(source)
        try:
            print("recognizing")
            suno = t.recognize_google(audio, language="en-in")
            print(f"You Said: {suno}")
            return suno
        except sp.UnknownValueError:
            speaker.Speak("Saarthi, couldn't understand what you said.")
            return ""
        except sp.RequestError:
            speaker.Speak("Sorry, my speech service is currently down.")
            return ""

if __name__ == "__main__":
    speaker.Speak("Namaste! I am Saarthhi AI. Please say something...... Listening")
    while True:
        print("Listening...")
        text = take()
        # speaker.Speak(text)
        sites = [
            ["youtube", "https://youtube.com"],
            ["google", "https://google.com"],
            ["wikipedia", "https://wikipedia.org"],
            ["facebook", "https://facebook.com"],
            ["twitter", "https://twitter.com"],
            ["instagram", "https://instagram.com"],
            ["linkedin", "https://linkedin.com"],
            ["reddit", "https://reddit.com"],
            ["amazon India", "https://www.amazon.in"],
            ["netflix", "https://netflix.com"],
            ["gmail", "https://mail.google.com"],
            ["yahoo mail", "https://in.mail.yahoo.com"],
            ["bing", "https://www.bing.com"],
            ["spotify", "https://spotify.com"],
            ["github", "https://github.com"],
            ["stackoverflow", "https://stackoverflow.com"],
            ["flipkart", "https://flipkart.com"],
            ["paytm", "https://paytm.com"],
            ["hotstar", "https://hotstar.com"],
            ["jio", "https://www.jio.com"],
            ["Chat GPT", "https://chatgpt.com/"],
            ["quora", "https://quora.com"],
            ["pinterest", "https://pinterest.com"],
            ["tumblr", "https://tumblr.com"],
            ["snapchat", "https://snapchat.com"],
            ["ebay", "https://ebay.com"],
            ["medium", "https://medium.com"],
            ["bbc", "https://bbc.com"],
            ["cnn", "https://cnn.com"],
            ["nytimes", "https://nytimes.com"],
            ["forbes", "https://forbes.com"],
            ["guardian", "https://theguardian.com"],
            ["reuters", "https://reuters.com"],
            ["aliexpress", "https://aliexpress.com"],
            ["coursera", "https://coursera.org"],
            ["edx", "https://edx.org"],
            ["udemy", "https://udemy.com"],
            ["khan academy", "https://khanacademy.org"],
            ["twitch", "https://twitch.tv"],
            ["vimeo", "https://vimeo.com"],
            ["dailymotion", "https://dailymotion.com"],
            ["dropbox", "https://dropbox.com"],
            ["onedrive", "https://onedrive.live.com"],
            ["slack", "https://slack.com"],
            ["trello", "https://trello.com"],
            ["asana", "https://asana.com"],
            ["zoom", "https://zoom.us"],
            ["skype", "https://skype.com"],
            ["whatsapp", "https://web.whatsapp.com"],
            ["telegram", "https://telegram.org"],
            ["signal", "https://signal.org"],
            ["weebly", "https://weebly.com"],
            ["wix", "https://wix.com"],
            ["wordpress", "https://wordpress.com"]
        ]


        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                speaker.Speak(f"opening {site[0]} for you")
                webbrowser.open(site[1])
        section =[
            ["Identity", "I am known as Saarthi AI."],
            ["Title", "I am referred to as Saarthi AI."],
            ["Designation", "I go by the name Saarthi AI."],
            ["Label", "I am labeled as Saarthi AI."],
            ["Moniker", "My moniker is Saarthi AI."],
            ["Alias", "I am also known as Saarthi AI."],
            ["Appellation", "I am called Saarthi AI."],
            ["Tag", "You can call me Saarthi AI."],
            ["Reference", "I am referenced as Saarthi AI."],
            ["Nomination", "I am nominated as Saarthi AI."],
            ["Title", "I hold the title of Saarthi AI."],
            ["Nickname", "My nickname is Saarthi AI."],
            ["Brand", "I am branded as Saarthi AI."],
            ["Builder", "I am built by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Architect", "I am architected by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Student", "I am developed by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Programmer", "I am programmed by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Developer", "Sanjeev Kumar is a 1st year student at Poornima College of Engineering, Jaipur and he developed me"],
            ["Maintainer", "I am maintained by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Coder", "I am coded by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Implementer", "I am implemented by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Producer", "I am produced by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Constructor", "I am constructed by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["owner", "I am originated by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur, So the owner is Sanjeev Kumar"],
            ["Initiator", "I am initiated by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Formulator", "I am formulated by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Author", "I am authored by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Inventor", "I am invented by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Founder", "I am founded by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Name", "My name is Saarthi AI."],
            ["Brand", "I am branded as Saarthi AI."],
            ["Builder", "I am built by Sanjeev Kumar, who is a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Architect", "I am architected by Sanjeev Kumar, a 1st year student at Poornima College of Engineering, Jaipur"],
            ["Name of Creator", "My creator's name is Sanjeev Kumar."],
            ["College", "Sanjeev Kumar studies at Poornima College of Engineering, Jaipur."],
            ["Year of Study", "Sanjeev Kumar is a first-year student."],
            ["Field of Study", "Sanjeev Kumar is pursuing Computer Science Engineering (CSE)."],
            ["Nationality", "My Nationality is Indian."],
            ["City", "Sanjeev Kumar resides in Jaipur."],
            ["Origin", "I was developed in Jaipur, India"],
            ["Purpose", "I am designed to assist and interact with users."],
            ["Development Year", "I was developed in 2024."],
            ["Motivation", "Sanjeev Kumar was motivated by a passion for AI and technology."],
            ["Inspiration", "Sanjeev Kumar was inspired by the potential of AI to solve real-world problems."],
            ["Unique Feature", "I have a conversational interface designed for user assistance."],
            ["Skills", "Sanjeev Kumar is skilled in programming, particularly in Python."],
            ["Projects", "Sanjeev Kumar has worked on several projects, including Saarthi AI."],
            ["Hobbies", "Sanjeev Kumar enjoys coding, reading, and playing chess."],
            ["Ambition", "Sanjeev Kumar aims to become a leading AI expert."],
            ["Development Tools", "I was developed using various tools like Python and natural language processing libraries."],
            ["Testing", "I was thoroughly tested to ensure accuracy and reliability."],
            ["Deployment", "I am deployed to interact with users and assist them in various tasks."],
            ["Education Background", "Sanjeev Kumar has a strong background in mathematics and computer science."],
            ["Achievements", "Sanjeev Kumar has received accolades for innovative projects and academic excellence."],
            ["Future Plans", "Sanjeev Kumar plans to pursue advanced studies in AI and machine learning."],
            ["Improvement", "I am continuously improved based on user feedback and technological advancements."],
            ["Contribution", "Sanjeev Kumar has significantly contributed to my development and functionality."],
            ["Language Support", "I support interactions in English."],
            ["Learning Capability", "I am designed to learn from interactions to improve my responses."],
            ["Learning Approach", "Sanjeev Kumar adopts a hands-on approach to learning and development."],
            ["User Base", "I am designed to assist students, professionals, and enthusiasts."],
            ["Guidance", "Sanjeev Kumar was guided by professors and online resources during my development."],
            ["Maintenance", "I am regularly updated to ensure optimal performance."],
            ["Network", "Sanjeev Kumar collaborates with peers and mentors for continuous improvement."],
            ["Feedback Mechanism", "I have a built-in feedback mechanism to learn from user interactions."],
            ["Research", "Sanjeev Kumar conducts research on the latest AI trends and technologies."],
            ["Accessibility", "I am accessible to users through various platforms."],
            ["Customization", "Sanjeev Kumar customized my functionalities to suit user needs."],
            ["Community Involvement", "Sanjeev Kumar actively participates in tech communities and forums."],
            ["Technical Challenges", "Sanjeev Kumar overcame various technical challenges during my development."],
            ["Mentorship", "Sanjeev Kumar receives mentorship from experienced professionals in AI."],
            ["Ethical Considerations", "Sanjeev Kumar ensures that I adhere to ethical standards in AI."],
            ["Codebase", "My codebase is maintained by Sanjeev Kumar."],
            ["User Interaction", "I am designed to provide a seamless user interaction experience."],
            ["Feedback Integration", "Sanjeev Kumar integrates user feedback to enhance my performance."],
            ["Collaborations", "Sanjeev Kumar collaborates with other developers for continuous improvement."],
            ["Support", "I provide support to users in various tasks and queries."],
            ["Updates", "Sanjeev Kumar ensures that I receive regular updates for optimal performance."],
            ["Security", "Sanjeev Kumar has implemented security measures to protect user data."],
            ["Brand", "I am branded as Saarthi AI."]
        ]

        for sections in section:
            if f" {sections[0]}".lower() in text.lower():
                speaker.Speak(f"{sections[1]}")
        if "Artificial Intelligence".lower() in text.lower():
            ai(message=text)
        elif "Tell me".lower() in text.lower():
            aia(mem=text)
        elif "time" in text.lower():
            h = datetime.datetime.now().strftime("%H")
            m = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Sir the time now is {h} {m}")
        elif "stop yourself".lower() in text.lower():
            speaker.Speak("Stopping myself. Remember me if you want any help. bye!, Take care")
            break
        else:
            speaker.Speak("Listening")
