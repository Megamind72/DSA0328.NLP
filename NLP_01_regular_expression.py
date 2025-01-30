import re

text = "The quick brown fox jumps over the lazy dog. The fox is clever."

pattern = r'fox'

matches = re.findall(pattern, text)
print(f"Found {len(matches)} occurrences: {matches}")

match = re.search(pattern, text)
if match:
    print(f"First occurrence found at index: {match.start()}")

new_text = re.sub(pattern, 'cat', text)
print("Modified text:", new_text)
