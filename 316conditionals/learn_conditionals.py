# learning about conditional statements

# ------part 1, one way conditional------
print("\n------part 1, one way conditional------")
num1 = 13
num2 = 42
if num1 == num2:
    print("hello")
    print("world")
print("moving on now...")




# ------part 2, two way conditional------
print("\n------part 2, two way conditional------")
num = 100
if num>10:
    print("that's greater than 10")
    print("who knows, maybe even greater than 100")
else:
    print("that's not greater than 10")
    print("maybe really small")
print("moving on now...")



# ------part 3, multi-way conditional------

print("\n------part 3, multi-way conditional------")
grade = 78
if grade > 89.5:
    print("that's an A")
elif grade > 79.5:
    print("that's a B")
elif grade > 69.5:
    print("that's a C")
elif grade > 59.5:
    print("that's a D")
else:
    print("that's not a passing grade")
print("moving on now...")




# ------ part 4, a logical error ------

print("\n------ part 4, a logical error ------")
grade = 78
if grade > 89.5:
    print("that's an A")
if grade > 79.5:
    print("that's a B")
if grade > 69.5:
    print("that's a C")
if grade > 59.5:
    print("that's a D")
else:
    print("that's not a passing grade")


print("\n\n\n\n\n")

# ------ part 5, boolean operators ------

print("one friend only likes certain movies")
funny = True
action_packed = False
if funny and action_packed:
    print("they would like this")
else:
    print("they would not like this")



print("\n\n\n\n\n\n")


print("another friend likes more movies")
funny = True
action_packed = False
if funny or action_packed:
    print("they would like this")




print("\n\n\n\n\n\n")

we_are_finished = False
if not we_are_finished:
    print("there's more!")
else:
    print("all finished")


print("\n\n\n\n\n")


num = 25
if num < 20 and num > 12:
    print("this number is in the teens")
else:
    print("this number is not in the teens")


print("\n\n\n\n\n")


age = 25
if age < 3 or age > 80:
    print("this person probably has no teeth")
else:
    print("this person probably has teeth")


print("\n\n\n\n\n")


# ans = input("What color is the sky on a gloomy day?").lower()
# if ans == "grey" or ans == "gray":
#   print("Yep...")



print("\n\n\n\n\n")
print("\n\n\n\n\n")

finished = False
while not finished:
    ans = input("tell me about yourself:")
    if ans == 'q':
        finished = True

    
print("\n\n\n\n\n")


ans = ''
while ans != 'q':
    ans = input("tell me about yourself:")
    print("...interesting...")
  





