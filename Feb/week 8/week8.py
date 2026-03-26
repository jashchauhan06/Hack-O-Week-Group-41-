# Week 8: Fallbacks and Handover
# Design a strategy for unclear or out-of-scope questions

class FallbackHandler:
    def __init__(self):
        self.known_topics = ['exam', 'fee', 'admission', 'result', 'schedule', 'course', 'hostel']
        self.confidence_threshold = 0.5
        self.human_contact = {
            'email': 'support@university.edu',
            'phone': '+1-234-567-8900',
            'desk': 'Student Help Desk - Room 101'
        }
    
    def analyze_query(self, query):
        """Analyze query confidence and topic"""
        query_lower = query.lower()
        
        # Check if query matches known topics
        matched_topics = [topic for topic in self.known_topics if topic in query_lower]
        
        # Calculate confidence (simple heuristic)
        confidence = len(matched_topics) / max(len(query.split()), 1)
        
        # Check for unclear indicators
        unclear_indicators = ['?', 'help', 'confused', 'not sure', 'maybe']
        is_unclear = sum(1 for ind in unclear_indicators if ind in query_lower) > 1
        
        return {
            'matched_topics': matched_topics,
            'confidence': confidence,
            'is_unclear': is_unclear
        }
    
    def handle_query(self, query):
        """Handle query with fallback strategy"""
        analysis = self.analyze_query(query)
        
        # High confidence - process normally
        if analysis['confidence'] >= self.confidence_threshold and analysis['matched_topics']:
            return {
                'status': 'handled',
                'response': f"I can help you with {', '.join(analysis['matched_topics'])}. Let me find that information..."
            }
        
        # Low confidence but has some topic - ask clarification
        elif analysis['matched_topics'] and not analysis['is_unclear']:
            return {
                'status': 'clarification',
                'response': f"I found information about {', '.join(analysis['matched_topics'])}. Could you please be more specific? For example:\n"
                           f"  - What semester/year?\n"
                           f"  - Which course/department?\n"
                           f"  - What specific details do you need?"
            }
        
        # Out of scope or very unclear - handover to human
        else:
            return {
                'status': 'handover',
                'response': f"I'm not sure I can help with that query. Let me connect you with a human advisor:\n\n"
                           f"📧 Email: {self.human_contact['email']}\n"
                           f"📞 Phone: {self.human_contact['phone']}\n"
                           f"🏢 Visit: {self.human_contact['desk']}\n\n"
                           f"They'll be able to assist you better with your specific question."
            }

def handle_fallback():
    """Interactive fallback handling"""
    handler = FallbackHandler()
    
    print("=" * 60)
    print("Fallbacks and Handover - Week 8")
    print("=" * 60)
    print("\nThis bot handles unclear queries and routes to human support when needed.")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ['exit', 'quit']:
            print("\nThank you for using the Fallback Handler bot!")
            break
        
        if not query:
            continue
        
        result = handler.handle_query(query)
        
        print(f"\n[Status: {result['status'].upper()}]")
        print(f"\nBot: {result['response']}")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    handle_fallback()
