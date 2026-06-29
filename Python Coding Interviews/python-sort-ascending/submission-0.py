from typing import List


def sort_words(words: List[str]) -> List[str]:
    s=[]
    n=len(words)
    smallest=words[0]
    while len(s)<n:
        for letter in words:
            if letter<smallest:
                s.append(letter)
                s.remove(letter)
        return s

        
        

def sort_numbers(numbers: List[int]) -> List[int]:
    s=[]
    smallest=numbers[0]
    for integer in numbers:
        if integer<smallest:
            smallest=integer
            s.append(smallest)
            numbers.remove(smallest)
    return s
            
def sort_decimals(numbers: List[float]) -> List[float]:
    s=[]
    smallest=numbers[0]
    for integer in numbers:
        if integer<smallest:
            smallest=integer
            s.append(smallest)
            numbers.remove(smallest)
    return s
    



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
