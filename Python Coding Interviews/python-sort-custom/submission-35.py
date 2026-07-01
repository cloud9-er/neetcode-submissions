from typing import List


def sort_words(words: List[str]) -> List[str]:
    t=[]
    while words:
        largest=words[0]
        i=max(words,key=len)
        largest=i
        t.append(largest)
        words.remove(largest)
    return t
    


def sort_numbers(numbers: List[int]) -> List[int]:
    t=[]
    while numbers:
        largest=numbers[0]
        for i in numbers:
            if abs(i)==min(numbers):
                largest=i
        t.append(abs(i))
        l=sorted(t)
    return l
    


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
