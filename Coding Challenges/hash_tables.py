def checkMagazine(magazine, note):
    mag_word_count = {}
    for word in magazine.split():
        if word in mag_word_count:
            mag_word_count[word] += 1
        else:
            mag_word_count[word] = 1

    for word in note.split():
        if word not in mag_word_count or mag_word_count[word] <= 0:
            return False
        mag_word_count[word] -= 1

    return True
