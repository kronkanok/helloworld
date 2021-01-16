x = "awesome


def myFunc():
    global x
    # x = "fantastic"
    print("Python is" + x)
    x = "fantastic"
    # x = "fantastic"


myFunc()
print("Python is" + x)
