#create Class
class Employee:

    # intializing
    def __init__(self):
        print("Employ created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():

    print('Making Object...')

    obj = Employee()

    print('function end...')

    return obj

print('Calling Create_obj() function...')

obj = Create_obj()

print('Program End...')    
