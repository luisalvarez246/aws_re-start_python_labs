user_reply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ");

if user_reply == "stamps":
    print("We have many stamp designs to choose from.");
elif user_reply == "envelope":
    print("We have many envelope sizes to choose from.");
elif user_reply == "copy":
    copies = input("How many copies would you like? (Enter a number) ");
    print("Here are {} copies.".format(copies));
else:
    print("Please come back when you need to ship a package. Thank you.");