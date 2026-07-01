from typing import List


def sort_words(words: List[str]) -> List[str]:
    t=[]
    for i in words:
        L=len(i)
        largest=len(words[0])
        if len(i)>largest:
            largest=i
            words.remove(largest)
            t.append(largest)
        return t
    


def sort_numbers(numbers: List[int]) -> List[int]:
    t=[]

    for i in numbers:
        t.append(abs(i))
        l=sorted(t)
    return l
    


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
