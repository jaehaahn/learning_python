def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)

if __name__ == "__main__":
    str1 = "파이ㅆㅓㄴ 알고리즘 정말 재미이이다"
    str2 = reversing_words_slice(str1)
    print(str2)

