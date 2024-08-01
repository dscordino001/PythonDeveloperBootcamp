# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': 1 #changing this will either run or not run the message_friends function.
}

def authenticated(functionAccepted):
    def wrapper(*args, **kwargs):
        if args[0]["valid"] == True:
            functionAccepted(*args, **kwargs)
        else:
            print("invalid user")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)