# Exercises
# 1. Modify the program to count the number of unique words in the text.
# 2. Add a function to find the longest word in the text.
# 3. Implement a feature to count the occurrences of a specific word (case-insensitive).
# 4. Create a function to calculate the percentage of words that are longer than the average word length.

# SOLUTION :  

# Open and Read a Text File

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

# Count the Number of Lines

def count_lines(content):
    return len(content.split('\n'))

# Count Words

def count_words(content):
    return len(content.split())

# Count Unique Words

def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)  # Using a set to store unique words
    return len(unique_words)

# Find the Most Common Word

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Calculate Average Word Length

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Find the Longest Word

def longest_word(content):
    words = content.split()
    longest = max(words, key=len)  # Find the longest word
    return longest

# Count Occurrences of a Specific Word

def count_specific_word(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())  # Count occurrences case-insensitively

# Calculate Percentage of Words Longer Than Average Word Length

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words_count = sum(1 for word in words if len(word) > avg_length)
    return (longer_words_count / len(words)) * 100 if words else 0  # Avoid division by zero

# Combine Everything into a Main Function

def analyze_text(filename, specific_word):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    long_word = longest_word(content)
    specific_word_count = count_specific_word(content, specific_word)
    percent_longer_than_avg = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Longest word: '{long_word}'")
    print(f"Occurrences of the word '{specific_word}': {specific_word_count}")
    print(f"Percentage of words longer than average: {percent_longer_than_avg:.2f}%")

# Run the analysis
analyze_text('sample.txt', 'plagiarism')  # Here 'plagiarism' is the specific word
