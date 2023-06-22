import re

# Matching patterns
pattern = r'abc'  # Raw string to represent the pattern

# Match: checks if the pattern matches at the beginning of the string
result = re.match(pattern, 'abcdef')
if result:
    print('Match')
else:
    print('No match')

# Search: searches the entire string for a match
result = re.search(pattern, 'defabc')
if result:
    print('Match')
else:
    print('No match')

# Find all: finds all occurrences of the pattern in the string
matches = re.findall(pattern, 'abcabcabc')
print(matches)  # Output: ['abc', 'abc', 'abc']

# Split: splits the string based on the pattern
parts = re.split(pattern, 'xyzabc123def')
print(parts)  # Output: ['xyz', '123def']

# Substitution: replaces occurrences of the pattern with a new string
new_string = re.sub(pattern, 'xyz', 'abc123abc456')
print(new_string)  # Output: 'xyz123xyz456'

# Matching groups
pattern = r'(\d+)-(\d+)'
result = re.match(pattern, '10-20')
if result:
    print(result.group(0))  # Output: '10-20' (entire match)
    print(result.group(1))  # Output: '10' (first group)
    print(result.group(2))  # Output: '20' (second group)

# Predefined character classes
pattern = r'\d'  # Matches any digit (0-9)
pattern = r'\D'  # Matches any non-digit character
pattern = r'\w'  # Matches any alphanumeric character (a-z, A-Z, 0-9, _)
pattern = r'\W'  # Matches any non-alphanumeric character
pattern = r'\s'  # Matches any whitespace character
pattern = r'\S'  # Matches any non-whitespace character

# Quantifiers
pattern = r'a+'  # Matches one or more occurrences of 'a'
pattern = r'a*'  # Matches zero or more occurrences of 'a'
pattern = r'a?'  # Matches zero or one occurrence of 'a'
pattern = r'a{3}'  # Matches exactly three occurrences of 'a'
pattern = r'a{2,4}'  # Matches two to four occurrences of 'a'
pattern = r'a{2,}'  # Matches two or more occurrences of 'a'

# Anchors
pattern = r'^abc'  # Matches 'abc' at the beginning of the string
pattern = r'abc$'  # Matches 'abc' at the end of the string

# Modifiers
pattern = r'abc'  # Matches 'abc' in a case-sensitive manner
pattern = r'abc'  # Matches 'abc' in a case-insensitive manner
pattern = r'abc(?i)'  # Equivalent to r'abc' with re.IGNORECASE flag

# Flags (can be combined with |)
pattern = r'abc(?i)'  # Case-insensitive matching
pattern = r'abc(?m)'  # Multiline matching
pattern = r'abc(?s)'  # Dot matches all characters, including newlines
pattern = r'abc(?x)'  # Verbose mode, allows comments and whitespace

# Escape special characters
pattern = re.escape('abc.def')  # Matches 'abc.def' literally

# Compiling patterns (for performance optimization)
compiled_pattern = re.compile(pattern)
