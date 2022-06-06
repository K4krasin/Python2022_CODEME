def clear_text(text):
    for char in '!,.;«':
        text = text.replace(char, '')
    text = text.replace('\n', ' ')

    return text

def find_longest_word(text):
    longest = ''
    for word in text:
        if len(word) > len(longest):
            longest = word
    return longest

def main():
    with open('text.txt', encoding="utf=8") as f:
        content = f.read()

    content = clear_text(content)
    content = content.split()
    longest_word = find_longest_word(content)
    print(longest_word,' - ', len(longest_word))

main()