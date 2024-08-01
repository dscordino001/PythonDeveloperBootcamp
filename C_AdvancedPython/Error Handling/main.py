while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise Exception('Hey cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
        break
    else: # this will run if the try block runs successfully
        print('Thank you!')
    finally: # this will run no matter what
        print('ok, I am finally done')
    print('Can you hear me?')
