from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

app = Flask(__name__)

# FAQ Responses
faq = {
    "hi": "Hello 👋 Welcome!",
    "hello": "Hi there 😊",
    "price": "Our pricing starts from $10.",
    "services": "We provide AI & Automation services.",
    "bye": "Goodbye 👋",
    "help": "Available commands:\n1. price\n2. services\n3. hello"
}

# HOME ROUTE
@app.route("/")
def home():
    return "WhatsApp Bot Running Successfully!"

# WHATSAPP BOT ROUTE
@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():

    # User message
    incoming_msg = request.values.get("Body", "").lower()

    # Bot reply
    reply = faq.get(
        incoming_msg,
        "Sorry 😔 I didn't understand that."
    )

    # Save chat logs
    with open("chatlogs.txt", "a", encoding="utf-8") as file:
        file.write(
            f"""
Time: {datetime.now()}
User: {incoming_msg}
Bot: {reply}
-----------------------------------
"""
        )

    # Send response
    response = MessagingResponse()
    response.message(reply)

    return str(response)

# RUN APP
if __name__ == "__main__":
    app.run(debug=True)