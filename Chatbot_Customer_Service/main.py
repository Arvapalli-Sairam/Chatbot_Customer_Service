"""
Chatbot for Customer Service
----------------------------
A simple rule-based chatbot that answers basic customer queries.
"""

import re

# Predefined responses
faq = {
    "hi|hello|hey": "Hello! How can I help you today?",
    "what.*name": "I am your Customer Service Bot 🤖",
    "how.*refund": "To request a refund, please visit your orders page and click 'Request Refund'.",
    "how.*track.*order": "You can track your order in the 'My Orders' section with your tracking ID.",
    "what.*payment.*method": "We support Credit Card, Debit Card, UPI, and Net Banking.",
    "how.*contact.*support": "You can contact support at support@example.com.",
    "bye|exit|quit": "Goodbye! Have a great day!"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, response in faq.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand that. Could you rephrase?"

if __name__ == "__main__":
    print("Customer Service Chatbot 🤖 (type 'quit' to exit)")
    while True:
        query = input("You: ")
        if query.lower() in ["quit", "exit", "bye"]:
            print("Bot:", faq["bye|exit|quit"])
            break
        print("Bot:", chatbot_response(query))
