my_string = "This is a string.";
first_string = "water";
second_string = "fall";
name = input("What is your name? ");
color = input("What is your favorite color?  ");
animal = input("What is your favorite animal?  ");
# number = input("What is your favorite number? ");
number = 42;
age = 29;
print(my_string);
print(type(my_string));
print(my_string + " is of the data type " + str(type(my_string)));
print(first_string + second_string);
print(name);
print("{}, you like a {} {}!".format(name, color, animal));
print("{}, your favorite number is {}!".format(name, number));
print("My name is {}, and I am {} years old".format(name, age));