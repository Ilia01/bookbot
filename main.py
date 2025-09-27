import sys
from stats import get_num_words, get_num_chars, sort_on


def get_book_text(filepath):
  with open(filepath) as f:
    file_content = f.read()
    
  return file_content

  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
  path = sys.argv[1]
  
  text = get_book_text(path)
  print(get_num_words(text))
  chars = get_num_chars(text)
  chars.sort(reverse=True, key=sort_on)
  
  for item in chars:
      char, num = item.values()
      
      if not char.isalpha():
        continue
      print(f"{char}:", num)
  
main()
