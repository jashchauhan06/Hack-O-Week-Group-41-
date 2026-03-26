# Week 10: Analytics and Continuous Improvement
# Log all interactions, label a small sample, and propose improvements

import json
from datetime import datetime
from collections import Counter

class AnalyticsLogger:
    def __init__(self):
        self.interactions = []
        self.labeled_samples = []
    
    def log_interaction(self, query, response, intent=None, confidence=None):
        """Log a chatbot interaction"""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'response': response,
            'intent': intent,
            'confidence': confidence,
            'query_length': len(query.split())
        }
        self.interactions.append(interaction)
    
    def label_sample(self, interaction_id, correct_intent, feedback):
        """Label a sample interaction for training"""
        if interaction_id < len(self.interactions):
            labeled = {
                'interaction': self.interactions[interaction_id],
                'correct_intent': correct_intent,
                'feedback': feedback,
                'labeled_at': datetime.now().isoformat()
            }
            self.labeled_samples.append(labeled)
    
    def analyze_patterns(self):
        """Analyze interaction patterns"""
        if not self.interactions:
            return "No interactions to analyze"
        
        # Extract intents
        intents = [i['intent'] for i in self.interactions if i['intent']]
        intent_counts = Counter(intents)
        
        # Calculate average confidence
        confidences = [i['confidence'] for i in self.interactions if i['confidence']]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        
        # Find common query patterns
        all_words = []
        for interaction in self.interactions:
            all_words.extend(interaction['query'].lower().split())
        common_words = Counter(all_words).most_common(10)
        
        return {
            'total_interactions': len(self.interactions),
            'intent_distribution': dict(intent_counts),
            'average_confidence': round(avg_confidence, 2),
            'common_words': common_words,
            'labeled_samples': len(self.labeled_samples)
        }
    
    def propose_improvements(self):
        """Propose improvements based on analytics"""
        analysis = self.analyze_patterns()
        improvements = []
        
        # Check confidence levels
        if analysis['average_confidence'] < 0.7:
            improvements.append({
                'type': 'model_improvement',
                'suggestion': 'Average confidence is low. Consider retraining with more examples.'
            })
        
        # Check for new intents
        if analysis['labeled_samples'] > 0:
            new_intents = set()
            for sample in self.labeled_samples:
                if sample['correct_intent'] not in analysis['intent_distribution']:
                    new_intents.add(sample['correct_intent'])
            
            if new_intents:
                improvements.append({
                    'type': 'new_intents',
                    'suggestion': f'Add new intents: {", ".join(new_intents)}'
                })
        
        # Check for common unhandled queries
        if analysis['common_words']:
            improvements.append({
                'type': 'faq_expansion',
                'suggestion': f'Most common query terms: {", ".join([w[0] for w in analysis["common_words"][:5]])}. Consider adding FAQs for these topics.'
            })
        
        return improvements
    
    def generate_report(self):
        """Generate analytics report"""
        analysis = self.analyze_patterns()
        improvements = self.propose_improvements()
        
        report = "=" * 60 + "\n"
        report += "ANALYTICS REPORT\n"
        report += "=" * 60 + "\n\n"
        
        report += f"Total Interactions: {analysis['total_interactions']}\n"
        report += f"Labeled Samples: {analysis['labeled_samples']}\n"
        report += f"Average Confidence: {analysis['average_confidence']}\n\n"
        
        report += "Intent Distribution:\n"
        for intent, count in analysis['intent_distribution'].items():
            report += f"  - {intent}: {count}\n"
        
        report += f"\nCommon Query Terms:\n"
        for word, count in analysis['common_words'][:5]:
            report += f"  - '{word}': {count} times\n"
        
        report += "\n" + "=" * 60 + "\n"
        report += "PROPOSED IMPROVEMENTS\n"
        report += "=" * 60 + "\n"
        
        for i, improvement in enumerate(improvements, 1):
            report += f"\n{i}. {improvement['type'].upper()}\n"
            report += f"   {improvement['suggestion']}\n"
        
        return report

def analytics_logging():
    """Interactive analytics and improvement system"""
    logger = AnalyticsLogger()
    
    print("=" * 60)
    print("Analytics and Continuous Improvement - Week 10")
    print("=" * 60)
    print("\nThis bot logs interactions and provides analytics.")
    print("\nCommands:")
    print("  - Type your query to log an interaction")
    print("  - 'report' - View analytics report")
    print("  - 'label <id>' - Label an interaction (e.g., 'label 0')")
    print("  - 'exit' or 'quit' - Stop\n")
    
    intents = ['exam_query', 'fee_query', 'admission_query', 'result_query', 'hostel_query', 'other']
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("\n" + logger.generate_report())
            print("\nThank you for using the Analytics bot!")
            break
        
        if user_input.lower() == 'report':
            print("\n" + logger.generate_report())
            continue
        
        if user_input.lower().startswith('label '):
            try:
                interaction_id = int(user_input.split()[1])
                if interaction_id >= len(logger.interactions):
                    print(f"\n[Error: Interaction {interaction_id} not found]\n")
                    continue
                
                print(f"\nLabeling interaction {interaction_id}:")
                print(f"Query: {logger.interactions[interaction_id]['query']}")
                print(f"\nAvailable intents: {', '.join(intents)}")
                correct_intent = input("Correct intent: ").strip()
                feedback = input("Feedback: ").strip()
                
                logger.label_sample(interaction_id, correct_intent, feedback)
                print(f"\n[Interaction {interaction_id} labeled successfully]\n")
            except (ValueError, IndexError):
                print("\n[Error: Invalid label command. Use 'label <id>']\n")
            continue
        
        if not user_input:
            continue
        
        # Simulate bot response
        response = f"Processing your query: '{user_input}'"
        
        # Simple intent detection
        query_lower = user_input.lower()
        if 'exam' in query_lower:
            intent = 'exam_query'
            confidence = 0.85
        elif 'fee' in query_lower:
            intent = 'fee_query'
            confidence = 0.90
        elif 'admission' in query_lower:
            intent = 'admission_query'
            confidence = 0.80
        elif 'result' in query_lower:
            intent = 'result_query'
            confidence = 0.75
        else:
            intent = 'other'
            confidence = 0.50
        
        logger.log_interaction(user_input, response, intent, confidence)
        
        print(f"\nBot: {response}")
        print(f"[Logged as interaction #{len(logger.interactions)-1} | Intent: {intent} | Confidence: {confidence}]\n")

if __name__ == "__main__":
    analytics_logging()
