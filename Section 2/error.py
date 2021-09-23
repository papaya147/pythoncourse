raise RuntimeError("Something went wrong :(") # throws Runtime error

try:
    # code here
    
except RuntimeError:
    print("RuntimeError was caught")