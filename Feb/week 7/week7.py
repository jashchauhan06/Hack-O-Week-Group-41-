# Week 7: Context Handling for Follow-ups
# Enhance the chatbot to support short multi-turn conversations

class ContextHandler:
    def __init__(self):
        self.context = {
            'last_topic': None,
            'last_entity': None,
            'conversation_history': []
        }
    
    def process_query(self, query):
        """Process query with context awareness"""
        query_lower = query.lower()
        
        # Store in history
        self.context['conversation_history'].append(query)
        
        # Detect if this is a follow-up question
        follow_up_indicators = ['for', 'what about', 'and', 'also', 'how about']
        is_follow_up = any(indicator in query_lower for indicator in follow_up_indicators)
        
        # Extract entities
        entities = self._extract_entities(query)
        
        # If follow-up and no new topic, use previous context
        if is_follow_up and self.context['last_topic']:
            response = f"Following up on {self.context['last_topic']}"
            if entities:
                response += f" with additional context: {entities}"
            else:
                response += f" using previous context: {self.context['last_entity']}"
        else:
            # New topic
            if 'exam' in query_lower:
                self.context['last_topic'] = 'exam'
            elif 'fee' in query_lower:
                self.context['last_topic'] = 'fees'
            elif 'admission' in query_lower:
                self.context['last_topic'] = 'admission'
            
            self.context['last_entity'] = entities
            response = f"New query about {self.context['last_topic']}: {entities}"
        
        return response
    
    def _extract_entities(self, query):
        """Extract entities like year, semester, course"""
        import re
        entities = {}
        
        # Extract year
        year_match = re.search(r'(first|second|third|fourth|1st|2nd|3rd|4th)\s*year', query, re.IGNORECASE)
        if year_match:
            entities['year'] = year_match.group(1)
        
        # Extract semester
        sem_match = re.search(r'sem(?:ester)?\s*(\d+)', query, re.IGNORECASE)
        if sem_match:
            entities['semester'] = sem_match.group(1)
        
        # Extract course
        course_match = re.search(r'\b(CS|IT|MECH|EE|ECE)\b', query, re.IGNORECASE)
        if course_match:
            entities['course'] = course_match.group(1).upper()
        
        return entities if entities else None
    
    def reset_context(self):
        """Reset conversation context"""
        self.context = {
            'last_topic': None,
            'last_entity': None,
            'conversation_history': []
        }

def handle_context():
    """Interactive context handling"""
    handler = ContextHandler()
    
    print("=" * 60)
    print("Context Handling for Follow-ups - Week 7")
    print("=" * 60)
    print("\nThis bot maintains conversation context for follow-up questions.")
    print("Type 'exit' or 'quit' to stop.")
    print("Type 'reset' to start a new conversation.\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ['exit', 'quit']:
            print("\nThank you for using the Context Handler bot!")
            break
        
        if query.lower() == 'reset':
            handler.reset_context()
            print("\n[Context reset - Starting new conversation]\n")
            continue
        
        if not query:
            continue
        
        response = handler.process_query(query)
        print(f"Bot: {response}")
        print(f"Context: Topic={handler.context['last_topic']}, Entity={handler.context['last_entity']}\n")

if __name__ == "__main__":
    handle_context()
