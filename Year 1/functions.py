import os
os.system('clear')



# def add_two_numbers(num1, num2): # numbers in parentheses are called parameters
#     return num1 + num2

# print(add_two_numbers(1,2))
# print(add_two_numbers(4,99))
# print(add_two_numbers(333,999))

# def add_two_numbers(num1, num2=5): # can num2=5 sets the default value to 5
#     return num1 + num2

# num1 = int(input("Please enter the first side length."))
# num2 = int(input("Please enter the second side length."))

# def area_of_rectangle(num1, num2):
#     return num1 * num2

# print(area_of_rectangle(num1, num2))

# number = int(input("Please give a number: "))


def prime_num (number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime_num(5))

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverse_sentence("Hello there, welcome back"))

def number_sorter(numbers):
    return sorted(numbers)

print(number_sorter([1, 5, 3, 2, 4]))

# <------- Option to do the same as below but without a function and making each word in a seperate line  ----->

# sentence = "This is a very long sentence that I am going to use to test the function that I am going to write."

# dic = {}

# words = sentence.split()
# for word in words:
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1
#     print(f"{word} - {dic[word]}")

# <------- Option to do the same as below but without a function and making each word in a seperate line  ----->
    
def word_counter(sentence):
    dic = {}
    words = sentence.split()
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic
print(word_counter("This is a very long sentence that I am going to use to test the function that I am going to write."))
