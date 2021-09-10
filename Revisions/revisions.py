double = lambda x : x * 2
double.__doc__="""
    - Input: x: int
    - Output: x * 2 
    >>> double(5)
    10
"""
# print(double(5))

def repetition(word, n):
    """
    Inputs: word: str, n: int
    Output: None

    Print the word n times

    >>> repetition("kayak", 2)
    kayak
    kayak
    """
    for _ in range(n):
        print(word)

print(repetition("bonjour", 3))

def mention(note):
    """
    Input: note: int
    Output: int

    Checks if the graed mark has a mention or not.

    >>> mention(10)
    'Pas de mention'
    >>> mention(9)
    'Echec'
    >>> mention(15)
    'Mention'
    """
    if note < 10:
        return "Echec"
    elif note >= 10 and note <= 12:
        return "Pas de mention"
    elif note >= 13:
        return "Mention"
    

print(mention(11))

def somme(array):
    """
    Intput: int[]
    Output: int

    Sums all the numbers in the list 

    >>> somme([0, 1, 2, 3, 4, 5])
    15
    """
    sum = 0
    if isinstance(array, list):
        for number in array:
            if isinstance(number, int):
                sum += number

    return sum

print(somme([2, 5, 6, 4,5]))


def maxi(array):
    """
    Input: int[]
    Output: int

    Gets the highest number in the list.

    >>> maxi([2, 6, 5, 4, 5, 8, 6])
    8
    """
    highest = 0
    for number in array:
        if highest < number:
            highest = number

    return highest


print(maxi([2, 6,5, 4, 5, 8, 6]))


def min(array):
    """
    Input: int[]
    Output: int

    Gets the lowest number in the list

    >>> min([1, 5, 4, 8, -2])
    -2
    """
    lowest = 0
    for number in array:
        if lowest > number:
            lowest = number

    return lowest


print(min([5, 6,5, 4, 5,8 ,7, -2]))

puissance = lambda x, n : x**n
puissance.__doc__ = """

Input: x: number, y: number
Output: number

>>> puissance(2, 2)
4
"""

print(puissance(5, 6))

def reverse(word):
    """

    Input: word: str
    Output: str

    Reverses the word.

    >>> reverse("kayak")
    'kayak'
    >>> reverse("bonjour")
    'ruojnob'
    """

    result = ""
    length = len(word)

    while length != 0:
        result += word[length - 1]
        length -= 1

    return result

print(reverse("hello"))



def palindrome(word):
    """
    Input: word: str
    Output: str

    Checks if the word is a palindrome 

    >>> palindrome("kayak")
    True
    >>> palindrome("bonjour")
    False
    """
    return word == reverse(word)

print(palindrome("kayak"))
print(palindrome("bonjour"))




def fibonacci(n):
    """
    Input: n: int
    Output: int

    Gets number with fibonacci algorithm depending on n

    >>> fibonacci(2)
    2
    >>> fibonacci(1)
    1
    """
    if n == 0 or n == 1:
        return 1
    else:
        a = 1
        b = 1
        for _ in range(2, n + 1):
            c = a+b
            a = b
            b = c

    return c 

"bonjour"

print(fibonacci(10))


def tri_insertion(array):
    """
    Input: array: int[]
    Output: int[]

    Sorts the array

    >>> tri_insertion([5, 6, 44, 5, 9, -5, 6])
    [-5, 5, 5, 6, 6, 9, 44]
    """
    n = len(array)
    for k in range(1, n):
        j = k
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]

            j -= 1

    return array

print(tri_insertion([5, 6, 44, 5, 9, -5, 6]))

"""
Fonction maxi(L)
DEBUT
highest <- 0
POUR k allant de 0 à taille de la liste L <-
    SI highest < L[k]
        highest <- L[k]
    FINSI
FINPOUR

Retourner highest
FIN
"""

"""
Fonction inverse(mot)
DEBUT
result <- ""
length <- taille de la liste mot
TANT QUE length != 0 <-
    result <- result + mot[length - 1]
    length <- length - 1
FINTANTQUE

Retourner result
FIN
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()