# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# rand_letters = random.choice(letters)
list_letter = []
letter = nr_letters
for letter in range(nr_letters):
    rand_letters = random.choice(letters)
    nr_letters = rand_letters
    list_letter.append(rand_letters)

list_symbol = []
symbol = nr_symbols
for symbol in range(nr_symbols):
    rand_symbols = random.choice(symbols)
    nr_symbols = rand_symbols
    list_symbol.append(rand_symbols)

list_number = []
number = nr_numbers
for number in range(nr_numbers):
    rand_num = random.choice(numbers)
    nr_numbers = rand_num
    list_number.append(rand_num)


password_list = [list_letter, list_symbol, list_number]
# iterate through the sublist using List comprehension
flatList = [element for innerList in password_list for element in innerList]


random.shuffle(flatList)
print("Your Password is : "+(''.join(flatList)))


# print((''.join(list_letter)+''.join(list_number)+''.join(list_symbol)))
