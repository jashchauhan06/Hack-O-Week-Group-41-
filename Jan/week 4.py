# Week 4: FAQ Retrieval with TF-IDF
# Build a retrieval-based chatbot that stores FAQs and uses TF-IDF similarity to select the most relevant answer for a student's query

import math
from collections import Counter

faq_corpus = [
    "Tuition fees vary by program. Contact admissions for details.",
    "Apply online through our admissions portal.",
    "Application deadlines: Fall June 1, Spring November 1.",
    "We offer merit-based and need-based scholarships.",
    "Programs include Arts, Sciences, Engineering, Business, Medicine.",
    "Contact admissions: email admissions@university.edu or call 555-123-4567.",
    "On-campus housing is available through the housing portal.",
    "Campus location: 123 University Ave, City, State.",
    "Library hours: Monday-Friday 8am-10pm, weekends 10am-8pm.",
    "Online and hybrid courses are available in various programs."
]

def tokenize(text):
    """Simple tokenization"""
    return text.lower().split()

def compute_tf(document):
    """Compute term frequency"""
    tokens = tokenize(document)
    tf_dict = Counter(tokens)
    total_terms = len(tokens)
    return {term: count / total_terms for term, count in tf_dict.items()}

def compute_idf(corpus):
    """Compute inverse document frequency"""
    num_docs = len(corpus)
    idf_dict = {}
    
    all_terms = set()
    for doc in corpus:
        all_terms.update(tokenize(doc))
    
    for term in all_terms:
        doc_count = sum(1 for doc in corpus if term in tokenize(doc))
        idf_dict[term] = math.log(num_docs / doc_count)
    
    return idf_dict

def compute_tfidf(document, idf_dict):
    """Compute TF-IDF vector for a document"""
    tf_dict = compute_tf(document)
    tfidf_dict = {}
    
    for term, tf_value in tf_dict.items():
        tfidf_dict[term] = tf_value * idf_dict.get(term, 0)
    
    return tfidf_dict

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors"""
    all_terms = set(vec1.keys()) | set(vec2.keys())
    
    dot_product = sum(vec1.get(term, 0) * vec2.get(term, 0) for term in all_terms)
    
    mag1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
    mag2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    
    return dot_product / (mag1 * mag2)

def retrieve_best_faq(query, corpus, idf_dict):
    """Retrieve the most relevant FAQ using TF-IDF"""
    query_tfidf = compute_tfidf(query, idf_dict)
    
    best_score = -1
    best_index = 0
    
    for i, doc in enumerate(corpus):
        doc_tfidf = compute_tfidf(doc, idf_dict)
        similarity = cosine_similarity(query_tfidf, doc_tfidf)
        
        if similarity > best_score:
            best_score = similarity
            best_index = i
    
    return corpus[best_index], best_score

def main():
    print("=== TF-IDF FAQ Retrieval System ===\n")
    
    # Precompute IDF
    idf_dict = compute_idf(faq_corpus)
    
    print("Ask your questions (type 'quit' to exit)\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ['quit', 'exit', 'bye']:
            print("System: Goodbye!")
            break
        
        if not query:
            continue
        
        answer, score = retrieve_best_faq(query, faq_corpus, idf_dict)
        print(f"System: {answer}")
        print(f"(Confidence: {score:.2f})\n")

if __name__ == "__main__":
    main()
