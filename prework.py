def greeting(user_name):
    print("Hello {}".format(user_name.title()))
    print(f"Hello again {user_name.title()}") # use this one
greeting("Alex")

def hello_name(user_name):
    """greets user"""
    print("Hello_" + user_name + "!")
hello_name("USERNAME")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

numbers = range(1,202,2)
"""prints the first 100 odd numbers"""
for number in numbers:  
    print(number)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def max_num_in_list(a_list):
    """finds the max number in a list"""
    for number in a_list:
        number = max(a_list)
    return(number)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def is_leap_year(a_year):
    """lets you know if the year input is a leap year"""
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True    
    else:
        return False

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def is_consecutive(a_list):
    """lets user know if numbers in list are consecutive"""
    consecutive = a_list[0]
    if consecutive == a_list[+1]-1:
        consecutive = a_list[+1]
        return True
    else:
        return False

