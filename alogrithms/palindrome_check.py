def check_if_palindrome(words):
    words_that_are = []
    for word in words:
       if reverseString(word) == word:
           words_that_are.append(word)

    return words_that_are

def reverseString(word):
    return word[::-1]

