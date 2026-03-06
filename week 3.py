# Week 3: Synonym-Aware FAQ Bot
# Extend the FAQ bot so that semantically similar queries map to the same answer using a synonym dictionary or keyword groups

faq_database = {
    "tuition_fees": {
        "answer": "Tuition fees vary by program. Please contact the admissions office for specific information.",
        "keywords": ["tuition", "fees", "cost", "price", "payment", "charges", "expenses"]
    },
    "application": {
        "answer": "You can apply online through our admissions portal at www.university.edu/apply",
        "keywords": ["apply", "application", "register", "enroll", "admission", "join"]
    },
    "deadline": {
        "answer": "Application deadlines: Fall - June 1, Spring - November 1, Summer - March 1",
        "keywords": ["deadline", "due", "date", "when", "timeline", "cutoff"]
    },
    "scholarships": {
        "answer": "Yes, we offer merit-based and need-based scholarships. Visit our financial aid office for details.",
        "keywords": ["scholarship", "financial", "aid", "grant", "funding", "assistance"]
    },
    "programs": {
        "answer": "We offer undergraduate and graduate programs in Arts, Sciences, Engineering, Business, and Medicine.",
        "keywords": ["program", "course", "major", "degree", "study", "field"]
    },
    "contact": {
        "answer": "Email: admissions@university.edu, Phone: (555) 123-4567",
        "keywords": ["contact", "reach", "call", "email", "phone", "communicate"]
    },
    "housing": {
        "answer": "Yes, on-campus housing is available. Apply through the housing portal.",
        "keywords": ["housing", "dorm", "residence", "accommodation", "living", "room"]
    },
    "location": {
        "answer": "Our main campus is located at 123 University Ave, City, State 12345",
        "keywords": ["location", "address", "where", "campus", "place", "situated"]
    }
}

def find_matching_faq(query):
    """Find FAQ entry by matching keywords"""
    query_lower = query.lower()
    query_words = query_lower.split()
    
    best_match = None
    max_matches = 0
    
    for faq_key, faq_data in faq_database.items():
        matches = sum(1 for keyword in faq_data["keywords"] if keyword in query_lower)
        
        if matches > max_matches:
            max_matches = matches
            best_match = faq_key
    
    if best_match and max_matches > 0:
        return faq_database[best_match]["answer"]
    else:
        return "I'm sorry, I couldn't find an answer to your question. Please rephrase or contact support."

def main():
    print("=== Synonym-Aware FAQ Bot ===")
    print("Ask questions using different words (type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye!")
            break
        
        if not user_input:
            continue
            
        response = find_matching_faq(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
