import re
def is_palindrome(text:str) ->bool:
    text = text.lower().replace(" ","")
    return text == text[::-1]

def fibonacci(n: int) -> int:
    if(n<0):
        return None
    elif(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def count_vowels(text: str) -> int:
    text = text.lower()
    return text.count("a") +text.count("e")+text.count("i")+text.count("o")+text.count("u")+text.count("y")

def calculate_discount(price: float, discount: float) -> float:
    if(discount >1 or discount<0):
        return ValueError
    return price - price*discount
    
def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def word_frequencies(text: str) -> dict:
    words = re.findall(r"\w+", text.lower())
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True