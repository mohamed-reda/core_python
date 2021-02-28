from urllib.request import urlopen


def fetch_words():
    """this is Docstring"""
    story = urlopen("http://sixty-north.com/c/t.txt")
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


# if __name__ == '__main__':
# print(fetch_words())

string = 'hello'
string = 20
print(type(string))
# print(help(fetch_words()))
help(fetch_words)
# from fun import fetch_words
