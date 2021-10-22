def weather_condition(temp):
    if temp > 7:
        return 'Warm'
    elif temp <= 7:
        return 'Cold'
    elif temp != int or float:
        return 'Error'
        
user_input = input("Enter ")
 
print(weather_condition(user_input))

user_input = input("Please enter name: ")
surname = input("enter surname: ")

cat = 'andrei'


message = "Hello %s " % user_input
meassage2 = "hello %s %s" % (user_input, surname)
message1 = f"Hello {user_input} {surname}. whats"
print(message)
print(message1)
print(meassage2)


print("hello", cat)

def foo(name):
    return "Hi %s" % name