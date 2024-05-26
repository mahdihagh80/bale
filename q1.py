from collections import Counter

def is_repeated(arr: list):
    m = len(arr)//2
    counter = Counter(arr)
    number, num_of_repeats = counter.most_common(1)[0]

    if num_of_repeats > m:
        return number
    return False


print(is_repeated([1, 1, 1, 2, 2, 3, 4]))

