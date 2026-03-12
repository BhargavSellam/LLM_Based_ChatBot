import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Use your new Groq Key
# Paste your key here
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def get_groq_response(user_input):
    try:
        # Llama 3.3 70B is a high-quality model available for free on Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"❌ Groq API Error: {e}")
        return "I'm processing things too fast! Please try again in a moment."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    bot_response = get_groq_response(user_message)
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

#In local for debug use below code
# if __name__ == '__main__': 
#     app.run(debug=True)

# import os
# from flask import Flask, render_template, request, jsonify
# from google import genai
# from dotenv import load_dotenv

# # Load the .env file
# load_dotenv()

# app = Flask(__name__)
# api_key = "AIzaSyAgOyf23BwM_VNyfuUNxC-UAO6Xyor0eYo"

# # Verify API Key is loaded
# # api_key = os.getenv("GEMINI_API_KEY")
# # if not api_key:
# #     print("❌ ERROR: GEMINI_API_KEY not found in environment. Check your .env file!")

# # Initialize Client
# client = genai.Client(api_key=api_key)

# def get_gemini_response(user_input):
#     try:
#         # Use the plain model name 'gemini-1.5-flash'
#         # The SDK handles the versioning (v1beta vs v1) automatically
#         response = client.models.generate_content(
#             model='gemini-2.0-flash', 
#             contents=user_input
#         )
#         return response.text
#     except Exception as e:
#         print(f"❌ Error calling Gemini API: {e}")
#         return "I'm having trouble connecting to the AI. Check the terminal for details."

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get('message')
    
#     if not user_message:
#         return jsonify({"response": "No message received."}), 400
    
#     bot_response = get_gemini_response(user_message)
#     return jsonify({"response": bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
#-----------------------------------------------------------------------------------


# import os
# from flask import Flask, render_template, request, jsonify
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# app = Flask(__name__)

# # Initialize the NEW Google Gen AI Client
# # It will automatically look for 'GEMINI_API_KEY' in your .env file
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def get_gemini_response(user_input):
#     try:
#         # The new syntax for Gemini 1.5 Flash
#         response = client.models.generate_content(
#             model='gemini-1.5-flash',
#             contents=user_input
#         )
#         return response.text
#     except Exception as e:
#         print(f"Error calling Gemini API: {e}")
#         return "I'm having trouble connecting to the AI. Please try again."

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get('message')
    
#     if not user_message:
#         return jsonify({"response": "No message received."}), 400
    
#     bot_response = get_gemini_response(user_message)
#     return jsonify({"response": bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)


# ---------------------------------------------------------------



# import os
# import google.generativeai as genai
# from flask import Flask, render_template, request, jsonify
# from dotenv import load_dotenv

# # 1. Setup & Configuration
# load_dotenv()
# app = Flask(__name__)

# # Configure the Gemini API
# # Get your key from: https://aistudio.google.com/app/apikey
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GEMINI_API_KEY)

# # Initialize the model
# model = genai.GenerativeModel('gemini-1.5-flash')

# def get_gemini_response(user_input):
#     try:
#         # We use a chat session for a continuous conversation feel
#         chat = model.start_chat(history=[])
#         response = chat.send_message(user_input, stream=False)
#         return response.text
#     except Exception as e:
#         print(f"Error calling Gemini API: {e}")
#         return "Sorry, I'm having trouble connecting to the AI service right now."

# # 2. Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get('message')
    
#     if not user_message:
#         return jsonify({"response": "I didn't receive a message."}), 400
    
#     # Get the actual AI response
#     bot_response = get_gemini_response(user_message)
    
#     return jsonify({"response": bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)

#---------------------------------------------------

# import os
# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from dotenv import load_dotenv

# # Load variables from .env file
# load_dotenv()

# app = Flask(__name__)
# CORS(app)  # Enables Cross-Origin Resource Sharing if needed

# # --- CONFIGURATION ---
# # Access your API key using os.getenv after you add it to your .env file
# # API_KEY = os.getenv("MY_AI_API_KEY")

# def get_ai_response(user_input):
#     """
#     This is the core logic function. 
#     Integrate your specific API library here.
#     """
#     try:
#         # -------------------------------------------------------
#         # PLACE YOUR API INTEGRATION BELOW
#         # Example for a generic API call:
#         response = MyAIClient.generate(prompt=user_input, key=API_KEY)
#         return response.text
#         # -------------------------------------------------------
        
#         # Temporary Mock Logic for testing
#         if not user_input:
#             return "I didn't catch that. Could you say it again?"
        
#         return f"Backend received: '{user_input}'. Integration pending!"

#     except Exception as e:
#         print(f"Error processing AI response: {e}")
#         return "I'm having trouble connecting to my brain right now. Please try again later."

# # --- ROUTES ---

# @app.route('/')
# def index():
#     """Serves the frontend HTML."""
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     """
#     The main API endpoint for the frontend.
#     Expects JSON: {"message": "Hello"}
#     """
#     data = request.get_json()
    
#     if not data or 'message' not in data:
#         return jsonify({"error": "Missing message content"}), 400
    
#     user_message = data.get('message')
    
#     # Get the processed response from our logic function
#     bot_response = get_ai_response(user_message)
    
#     return jsonify({
#         "status": "success",
#         "response": bot_response
#     })

# if __name__ == '__main__':
#     # Run the server
#     # debug=True allows for automatic restarts during development
#     app.run(host='0.0.0.0', port=5000, debug=True)