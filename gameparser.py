import string

# List of unimportant words
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

# This functions removes all the unimportant words
def filter_words(words, skip_words):
    count = 0
    filtered = []

    for word in words:
        count = 0
        for word2 in skip_words:
            if word2 == word:
                    continue
            else:
                    count = count + 1
            if count == len(skip_words):
                filtered.append(word)                              
    return filtered

# This function removes all punctuation from a string
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct

# This function removes all punctuation from the string, converts it to lower case, removes extra spaces, splits the string into a list of words and removes the unimportant words
def normalise_input(user_input):
    remove_punctuation = remove_punct(user_input)
    split_words = remove_punctuation.lower().split()
    important_words = filter_words(split_words, skip_words)
    return important_words