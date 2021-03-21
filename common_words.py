
def common_words(string_one, string_two):
    """
    enter 2 different strings, and return the common word(s) and
    its count of both strings

    Args:
        string_one ([str]): [one string]
        string_two ([str]): [other string]

    Returns:
        [dictionary]: [{word: count}]
    """
    unique_words = set()
    all_words = string_one + ' ' + string_two
    for word in all_words.split(' '):
        unique_words.add(word)

    common_count = {}
    for unique_word in unique_words:
        count = 0
        for word in all_words.split(' '):
            print(word, unique_word)
            if word == unique_word:
                count += 1
        if count != 0:
            common_count[unique_word] = count

    return common_count


if __name__ == "__main__":
    print(common_words('ghdsh dsjj all two one all',
          'ghdsh dsjj all two one all alll oll all'))
