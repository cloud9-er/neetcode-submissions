from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word:len(word))
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    smallest=numbers[0]
    t=[]
    for num in numbers:
        if abs(num)==min(numbers):
            t.append(num)
            number.remove(num)
    return t


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
