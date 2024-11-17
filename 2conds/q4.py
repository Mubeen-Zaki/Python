color = "brown"
fruit = "banana"

if fruit == "banana":
    if color == "green":
        print("unripe")
    elif color == "yellow":
        print("ripe")
    elif color == "brown":
        print("overripe")
    else:
        print("Invalid color")

else:
    print("No details available currently")