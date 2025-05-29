
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

replies = {
    "Hi": "Hey there! I am here to assist you with any of your dental queries.",
    "hi": "Hey there! I am here to assist you with any of your dental queries.",
    "what are your working hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "Why does my tooth hurt?": "It could be due to cavities, sensitivity, or even an infection. It's best to get it checked by a dentist.",
    "What can I do to relieve tooth pain at home?": "Try a saltwater rinse: mix 1/2 teaspoon of salt in a glass of warm water and rinse for 30 seconds.",
    "When should I see a dentist for a toothache?": "If the pain lasts more than a day or is severe, please visit us during working hours: 9 AM to 6 PM, Monday to Friday.",
    "Where are you located": "We are located at CIIT TBI RCOEM."
}

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = replies.get(user_msg, "Sorry, I don't know that yet.")
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
