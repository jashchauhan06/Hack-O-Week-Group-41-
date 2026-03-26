# Week 5: Intent Classification for Queries
# Define 3-7 intents and build a simple classifier to route student queries to the correct category

import re

# Define intents and their patterns
INTENTS = {
    "admissions": {
        "patterns": ["apply", "application", "admission", "enroll", "join", "requirements", "deadline"],
        "response": "This is an admissions-related query. Routing to admissions department."
    },
    "financial": {
        "patterns": ["tuition", "fees", "cost", "scholarship", "financial", "aid", "payment", "refund"],
        "response": "This is a financial query. Routing to financial aid office."
    },
    "academic": {
        "patterns": ["program", "course", "major", "degree", "class", "register", "schedule"],
        "response": "This is an academic query. Routing to academic advising."
    },
    "housing": {
        "patterns": ["housing", "dorm", "residence", "accommodation", "room", "living"],
        "response": "This is a housing query. Routing to housing services."
    },
    "technical": {
        "patterns": ["password", "login", "portal", "account", "access", "system", "website"],
        "response": "This is a technical support query. Routing to IT help desk."
    },
    "campus_services": {
        "patterns": ["library", "hours", "location", "campus", "facilities", "services"],
        "response": "This is a campus services query. Routing to student services."
    },
    "general": {
        "patterns": ["contact", "email", "phone", "help", "information"],
        "response": "This is a general inquiry. Routing to main information desk."
    }
}

def classify_intent(query):
    """Classify the intent of a user query"""
    query_lower = query.lower()
    
    intent_scores = {}
    
    for intent_name, intent_data in INTENTS.items():
        score = sum(1 for pattern in intent_data["patterns"] if pattern in query_lower)
        intent_scores[intent_name] = score
    
    # Get intent with highest score
    best_intent = max(intent_scores, key=intent_scores.get)
    
    if intent_scores[best_intent] > 0:
        return best_intent, INTENTS[best_intent]["response"]
    else:
        return "unknown", "I couldn't determine the intent of your query. Please rephrase or contact general support."

def main():
    print("=== Intent Classification System ===")
    print("Available intents: admissions, financial, academic, housing, technical, campus_services, general\n")
    
    test_queries = [
        "How do I apply for admission?",
        "What are the tuition fees?",
        "What programs do you offer?",
        "Is housing available?",
        "I forgot my password",
        "What are the library hours?",
        "How can I contact you?"
    ]
    
    print("Demo with test queries:\n")
    for query in test_queries:
        intent, response = classify_intent(query)
        print(f"Query: {query}")
        print(f"Intent: {intent}")
        print(f"Response: {response}\n")
    
    print("\nTry your own queries (type 'quit' to exit):\n")
    
    while True:
        user_query = input("You: ").strip()
        
        if user_query.lower() in ['quit', 'exit', 'bye']:
            print("System: Goodbye!")
            break
        
        if not user_query:
            continue
        
        intent, response = classify_intent(user_query)
        print(f"Intent: {intent}")
        print(f"System: {response}\n")

if __name__ == "__main__":
    main()
