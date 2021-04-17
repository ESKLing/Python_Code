def checkMagazine(magazine, note):
    d = {}
    for word in magazine.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    for word in note.split():
        if word in d:
            d[word] -= 1
            if d[word] < 0:
                return False
        else:
            return False

    return True
