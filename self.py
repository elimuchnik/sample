'''
firs_var = 8
second_var = 10


print("Print number 1: the result is:" , firs_var + second_var)

is_it_true = True

print("Print number 2: is it true?" , is_it_true)

print("Print number 3: is it true?" , 6 > 9)

print("Print number 4: is it true?" , 6 > 9 or is_it_true)

print("Print number 5: is it true?" , 6 > 9 and is_it_true)

str1 = "bla1bla2bla3"
***
str2 = "bla2"

print("Print number 6:" , str2 in str1)

print("Print number 7:" , str2 not in str1)

input_val = input("Print number 8: Please enter a string:")

print("Print number 9: The input val is:", input_val )

input_val = input("Print number 10: Please enter a number:")

print("Print number 11: The input val is:", int(input_val) + 1 )

val1 , val2 = "MAle" , "Female"

print("Print number 12: " , val1 + " " + val2)

val1 , val2 = val2 , val1

print("Print number 13: " ,val1 + " " + val2)

print("Print number 14: He said: \"How you doing\"")

str3 = "Hello"
str4 = "world"

print("Print number 15:", str3 +" "+str4)
print("Print number 16:", (str3 + " ") * 3)



str5 = "Round Winner \n\nRound 1 Avi \nRound 2 Ben \nRound 3 Eli"
str6 = "Round\t\tWinner\n\nRound 1\t\tAvi\nRound 2\t\tBen\nRound 3\t\tEli"

print(str5)

print("*********************************************************")

print(str6)


work_string = "Joker"

print(work_string[1:-1])


my_list = [1,2,6,8]

number = 5

def check_in_list(number_to_check):    
    if number_to_check in my_list:
        print ("matched")
    else:
        print("not matched")

check_in_list(5)



my_word = "out_of_func"

def print_func():
    global my_word
    my_word = "in_func"
    print(my_word)

print_func()
print(my_word)


def funfunc(param1 , param2 , param3=3):
    return param1 + 1,param2 + 1, param3 +1

print(funfunc(1,2))
print(type(funfunc(1,2)))


cool_trick = ["a","b","c"]
a, b, c = cool_trick

print(a + " " + b + " " + c)

cool_trick2 = ["a","b","c"]

print(cool_trick + cool_trick2)

print(len(cool_trick))


x = 0
while x != 10:
    print(x)
    x+=1

cool_trick2 = "shalom"


for x in cool_trick2:
    print(x)



str_a = "apple"
str_b = "grape"

print("I love %s and %s and number %d" % (str_a,str_b,3))

'''

user_input_file, user_input_string, input_number = input("Please enter a file path and the input string: ").split()

try:
    input_number = float(input_number)
except ValueError:
    print("input_number cannot be converted to float")
    exit()

print("inputs are: %s and %s and %d: " % (user_input_file , user_input_string, input_number))
try:
    with open(user_input_file,'w') as file_obj:
        file_obj.write(user_input_string)
except OSError:
    print("user_input_file is not a valid file path")
    exit()





