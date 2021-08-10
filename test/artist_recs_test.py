# How to allow the app to fail gracefully and prompt the user for another input

while True:
    mention = input("Please press 'DONE when you are finished")
    if mention == "DONE":
        break
    else:
        print("Whoops, please make sure you enter 'DONE'")

print(mention)