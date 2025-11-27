def get_num_words(text):
    count = text.split()
    return len(count)


def characters_counter(text):
    data = {}
    for s in text:
        lower_s = s.lower()
        if lower_s not in data:
            data[lower_s] = 1
        else:
            data[lower_s] += 1
    return data


def sort_on(items):
    return items["num"]
