import random

# Enhanced Chatbot for Customer Interaction

def chatbot():
    print("ChatBot: Hello! I'm here to help you. Type 'exit' to end our chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("ChatBot: Goodbye! Take care!")
            break
        elif "products" in user_input:
            responses = [
                "We have a variety of products such as electronics, clothing, and home goods. What are you looking for today?",
                "Our products include gadgets, apparel, and home essentials. Is there anything specific you'd like to know about?",
                "We offer a wide range of products. Let me know what you're interested in, and I'll help you find it."
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "order" in user_input:
            responses = [
                "You can place an order for any product directly on our website. Would you like help with that?",
                "To place an order, please visit our online store. I can guide you through the process if you'd like!",
                "To make a purchase, simply add your desired items to the cart and proceed to checkout. Need help with that?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "discount" in user_input or "offer" in user_input:
            responses = [
                "We have special offers available on certain products. Are you looking for any specific discounts?",
                "Discounts are available on selected items. Would you like to know which products are on sale?",
                "Currently, we have great discounts on popular items. Let me know what you're interested in!"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "delivery" in user_input:
            responses = [
                "Delivery time depends on your location. Typically, it takes 3-7 business days for domestic orders.",
                "We offer both standard and express delivery options. When do you need the products to arrive?",
                "We offer fast delivery! Domestic orders usually take 3-7 days. Would you like to know more about our shipping policies?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "thank you" in user_input or "thanks" in user_input:
            responses = [
                "You're welcome! Is there anything else I can assist you with?",
                "My pleasure! If you have any more questions, feel free to ask.",
                "Glad to be of help! Let me know if you need anything else."
            ]
            print(f"ChatBot: {random.choice(responses)}")
        elif "hello" in user_input or "hi" in user_input:
            responses = [
                "Hello! How can I assist you today?",
                "Hi! What can I help you with today?",
                "Hey there! How can I be of service?"
            ]
            print(f"ChatBot: {random.choice(responses)}")
        else:
            responses = [
                "Sorry, I didn't understand that. Could you please rephrase?",
                "I'm not sure I follow. Could you clarify?",
                "Hmm, could you ask that in a different way?"
            ]
            print(f"ChatBot: {random.choice(responses)}")

# Run the chatbot
chatbot()
