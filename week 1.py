# Week 1: Basic FAQ Responder
# Design a rule-based chatbot that answers 10-15 fixed instance FAQ

faq_data = {
    "what are the tuition fees": "Tuition fees vary by program. Please contact the admissions office for specific information.",
    "how do i apply": "You can apply online through our admissions portal at www.university.edu/apply",
    "what is the deadline": "Application deadlines vary by semester. Fall: June 1, Spring: November 1, Summer: March 1",
    "do you offer scholarships": "Yes, we offer merit-based and need-based scholarships. Visit our financial aid office for details.",
    "what programs do you offer": "We offer undergraduate and graduate programs in Arts, Sciences, Engineering, Business, and Medicine.",
    "how do i contact admissions": "Email: admissions@university.edu, Phone: (555) 123-4567",
    "what are the admission requirements": "Requirements include transcripts, test scores, essays, and letters of recommendation.",
    "is housing available": "Yes, on-campus housing is available for students. Apply through the housing portal.",
    "what is the campus location": "Our main campus is located at 123 University Ave, City, State 12345",
    "how do i reset my password": "Visit the IT help desk or use the password reset link on the login page.",
    "what are the library hours": "Monday-Friday: 8am-10pm, Saturday-Sunday: 10am-8pm",
    "do you have online courses": "Yes, we offer fully online and hybrid courses in various programs.",
    "what is the refund policy": "Refunds are available within the first two weeks of the semester. See the bursar's office for details.",
    "how do i register for classes": "Log into the student portal and use the course registration system.",
    "what support services are available": "We offer tutoring, counseling, career services, and disability support."
}

def get_faq_response(question):
    """Return FAQ response for a given question"""
    question_lower = question.lower().strip()
    
    # First try exact match
    if question_lower in faq_data:
        return faq_data[question_lower]
    
    # Try partial matching - find if any keywords match
    for faq_question, answer in faq_data.items():
        # Check if key words from FAQ question appear in user question
        faq_words = set(faq_question.split())
        user_words = set(question_lower.split())
        
        # If at least 2 words match (or 1 significant word), return that answer
        common_words = faq_words & user_words
        significant_words = common_words - {'the', 'a', 'an', 'is', 'are', 'do', 'does', 'what', 'how', 'when', 'where'}
        
        if len(significant_words) >= 1:
            return answer
    
    return "I'm sorry, I don't have an answer to that question. Please contact our support team."

def main():
    print("=== University FAQ Chatbot ===")
    print("Ask me questions about the university (type 'quit' to exit)\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Thank you for using the FAQ system. Goodbye!")
            break
        
        if not user_input:
            continue
            
        response = get_faq_response(user_input)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()
