# Week 2: Preprocessing Student Queries
# Implement text preprocessing for student queries: tokenization, stopword removal, punctuation removal, and basic spelling normalization

import re
import string

# Common stopwords
STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'will', 'with'
}

# Common spelling corrections
SPELLING_CORRECTIONS = {
    'tution': 'tuition',
    'addmission': 'admission',
    'scholership': 'scholarship',
    'registeration': 'registration',
    'libary': 'library',
    'recieve': 'receive',
    'seperate': 'separate',
    'occured': 'occurred'
}

def tokenize(text):
    """Split text into tokens"""
    return text.lower().split()

def remove_punctuation(text):
    """Remove punctuation from text"""
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(tokens):
    """Remove stopwords from token list"""
    return [token for token in tokens if token not in STOPWORDS]

def correct_spelling(tokens):
    """Apply basic spelling corrections"""
    return [SPELLING_CORRECTIONS.get(token, token) for token in tokens]

def preprocess_query(query):
    """Complete preprocessing pipeline"""
    # Remove punctuation
    query = remove_punctuation(query)
    
    # Tokenize
    tokens = tokenize(query)
    
    # Correct spelling
    tokens = correct_spelling(tokens)
    
    # Remove stopwords
    tokens = remove_stopwords(tokens)
    
    return tokens

def main():
    print("=== Query Preprocessing Demo ===\n")
    
    test_queries = [
        "What are the tution fees?",
        "How do I apply for addmission?",
        "Is there a scholership available?",
        "What is the registeration deadline?"
    ]
    
    for query in test_queries:
        processed = preprocess_query(query)
        print(f"Original: {query}")
        print(f"Processed: {' '.join(processed)}\n")

if __name__ == "__main__":
    main()
