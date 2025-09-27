def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words" 

def get_num_chars(text):
    result = []
    for ch in text:
        found = False
        for item in result:
            if item["char"] == ch.lower():
                item["num"] += 1
                found = True
                break
        if not found:
            result.append({"char": ch.lower(), "num": 1})
    return result

def sort_on(chars):
  return chars["num"]
    
    