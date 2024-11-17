pet = "dog"
age = 3

if pet == "dog":
    if age < 2:
        print("puppy food")
    else:
        print("dog food")
elif pet == "cat":
    if age > 5:
        print("senior cat food")
    else:
        print("cat food")
else:
    print("No info available yet")