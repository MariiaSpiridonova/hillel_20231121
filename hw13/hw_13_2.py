def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    max_len = max(len(word) for word in words)
    longest_word = [word for word in words if len(word) == max_len]

    return longest_word


file = "article.txt"
result = longest_words(file)
print("Word(-s) of maximum length:", result)
