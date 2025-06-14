def search_keywords_in_text(text, keywords, case_sensitive=True):
    if not case_sensitive:
        text = text.lower()
        keywords = [keyword.lower() for keyword in keywords]
    
    found_keywords = []

    for keyword in keywords:
        if keyword in text:
            found_keywords.append(keyword)

    return found_keywords
