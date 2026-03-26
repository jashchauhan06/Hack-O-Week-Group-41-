# Week 6: Entity Extraction for Dates & Courses
# Extract semester numbers and course codes from questions

import re

# Sample exam schedule data for demo/testing purposes.
# Key format: (semester_number, course_code)
SAMPLE_EXAM_DATES = {
    (6, 'CS'): '12-May-2026',
    (6, 'IT'): '14-May-2026',
    (5, 'CS'): '20-Apr-2026',
    (4, 'ECE'): '25-Mar-2026',
    (3, 'MECH'): '18-Feb-2026',
}

def extract_entities(query):
    """
    Entity recognition to extract dates, course codes, and semester numbers
    from questions (e.g., "What is SEM 6 CS exam?") and use them in responses.
    """
    entities = {
        'semester': None,
        'course_code': None,
        'dates': []
    }
    
    # Extract semester numbers (e.g., SEM 6, semester 3, 5th sem)
    sem_patterns = [
        r'sem(?:ester)?\s*(\d+)',
        r'(\d+)(?:st|nd|rd|th)?\s*sem',
    ]
    for pattern in sem_patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            entities['semester'] = int(match.group(1))
            break
    
    # Extract course codes (e.g., CS, IT, MECH, EE, etc.)
    course_patterns = [
        r'\b(CS|IT|MECH|EE|ECE|CE|ME|EEE|CSE|ISE)\b',
        r'\b([A-Z]{2,4}\d{3,4})\b'  # Course codes like CS101, MATH2001
    ]
    for pattern in course_patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            entities['course_code'] = match.group(1).upper()
            break
    
    # Extract dates (e.g., 15th March, March 15, 2024-03-15)
    date_patterns = [
        r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)',
        r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}(?:st|nd|rd|th)?)',
        r'(\d{4}-\d{2}-\d{2})',
        r'(\d{1,2}/\d{1,2}/\d{2,4})'
    ]
    for pattern in date_patterns:
        matches = re.findall(pattern, query, re.IGNORECASE)
        entities['dates'].extend(matches)
    
    return entities

def generate_response(query, entities):
    """Generate a response using extracted entities"""
    response = f"Query: {query}\n"
    response += f"Extracted Entities:\n"
    query_lower = query.lower()
    is_exam_date_query = any(keyword in query_lower for keyword in ['when', 'date', 'exam'])

    sample_exam_date = None
    if entities['semester'] and entities['course_code'] and is_exam_date_query:
        sample_exam_date = SAMPLE_EXAM_DATES.get((entities['semester'], entities['course_code']))
    
    if entities['semester']:
        response += f"  - Semester: {entities['semester']}\n"
    if entities['course_code']:
        response += f"  - Course Code: {entities['course_code']}\n"
    if entities['dates']:
        response += f"  - Dates: {', '.join(entities['dates'])}\n"
    elif sample_exam_date:
        response += f"  - Dates: {sample_exam_date} (sample data)\n"
    elif is_exam_date_query:
        response += "  - Dates: No sample date available for this semester/course\n"
    
    # Generate contextual response
    if entities['semester'] and entities['course_code']:
        if is_exam_date_query:
            response += (
                f"\nSearching for Semester {entities['semester']} "
                f"{entities['course_code']} exam date information..."
            )
        else:
            response += f"\nSearching for Semester {entities['semester']} {entities['course_code']} information..."
    elif entities['semester']:
        response += f"\nSearching for Semester {entities['semester']} information..."
    elif entities['course_code']:
        response += f"\nSearching for {entities['course_code']} course information..."
    
    return response

if __name__ == "__main__":
    print("=" * 60)
    print("Entity Extraction for Dates & Courses - Week 6")
    print("=" * 60)
    print("\nThis bot extracts semester numbers, course codes, and dates from your queries.")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ['exit', 'quit']:
            print("\nThank you for using the Entity Extraction bot!")
            break
        
        if not query:
            continue
        
        entities = extract_entities(query)
        response = generate_response(query, entities)
        print(f"\n{response}")
        print("-" * 60 + "\n")
