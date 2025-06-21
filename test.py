import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Setup
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask app
app = Flask(__name__)
##============================================================================================================================

@app.route("/", methods=["GET", "POST"]) # when the user visit the webpage , our function will run
def make_summary():
    summary = "" # store the AI responde
    if request.method == "POST": # we are taking the news from the user as input when he click Submit button
        news = request.form["news_input"] # taking the news from textarea tag in html page
        prompt = f"Write Summary of the following article in bullet-point form: {news}"
        try:
            response = model.generate_content(prompt) # here we are sending the prompt to the AI model
            summary = response.text.strip()
        except Exception as e:
            summary = f"[Gemini AI Summarization failed: {str(e)}]"
            
    return render_template("index.html", summary=summary) # pass the AI generated summary in the HTML page
##============================================================================================================================
# call the function 
if __name__ == "__main__":
    app.run(debug=True) # here we started running Flask server and start listening for web requests
