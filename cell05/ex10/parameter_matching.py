import sys
params = sys.argv[1:]
if len(params) != 1:
    print("none")
else:
    user_input = input("what was the parameter?: ")
    if user_input == params[0]:
        print("Good jop!")
    else:
        print("Nope, sorry...")
    
