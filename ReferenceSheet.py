def _string_module():
    '''
    name = input('Whats your name \n')
    age = input('Whats your age \n')
    new_patient = bool(input('Are you a new patient \n'))
    print('Your name is '+ name + ' your age is ' + age + ' years old and your new patient status is ' + str(new_patient) + '.')    
    '''
    
    print('*',' ' * 76,'*')

    '''
    birth_year = input(" Year: ")
    age = 2019 - int(birth_year)
    print(age)
    print(type(age))
    '''

    
    
    #course = ''' 
    #Hi John,
    #
    #Here  is our first email to you.
    #
    #Thank you,
    #The support team
    #
    #
    #print(course)


def _indexing_module():
    '''
    #indexing a string
    course = 'Python for Beginners'
    print(course)
    #searches from left to right
    print(course[0])
    #searches from end to left
    print(course[-7])
    #get the work python back checking the first 7 characters
    print(course[0:7])
    #get the same thing as above but with out 0 assumes up to 7
    print(course[:7])
    #Get 2 character to just before the last character
    print(course[1:-1])
    '''


def _string_manupulation():
    '''
    #formated strings
    fname = 'John'
    lname = 'Smith'
    message = fname + '[' + lname + '] is a coder'
    msg= f'{fname} [{lname}] is a coder'
    #print(message)
    print(msg)
    '''

    '''
    #counts length of string
    course =  'Python for Beginners'
    print(len(course))
    #these are methods does not modify original variable
    print(course.upper())
    #finds the index of the letter in string
    print(course.find('Beginners'))
    print(course.replace('Beginners', 'Absolute Beginners'))
    #above does not change varible
    print(course)
    #check to see if string contains a set/words (Boolean) True of False
    print('Python' in course)
    '''


def _math_module():
    '''
    #division results in decimal float
    print(10/3)
    #division results with no remainder 
    print(10//3)
    #division displays the remainder only symbol call modules
    print(10%3)
    #to the power
    print(10 ** 4)
    # counter
    x = 10
    x = x + 1
    #  or 
    x += 3
    print(x)
    #PEMDAS applies to math in programming
    x=0
    x = 10 + 3 * 2 **2
    print(x)
    x=0
    x = (10 + 3) * 2 **2
    print(x)

    #rounding function
    x = 2.9
    print(round(x), ' ' * 75, ' *')

    #absolute value abs() returns always a positive number
    x = -2.9
    print(abs(-x))

    #for advance mathetics calculation
    import math
    print(math.ceil(2.9)) #ceiling of 2.9)
    print(math.floor(2.9)) #floor of 2.9)
    #Google Python3 math module explaination of functions
    '''


def _conditional_module():
        
    '''
    #Basic IF elif else block
    is_hot = False
    is_cold = False
    if is_hot:
        print('Its a hot day')
        print('Drink Water')
    elif is_cold:
        print('Its a cool day')
        print("Enjoy your Day")
    else:
        print('Its a lovely day')
    
    house_price = 1000000
    credit = False

    if credit:
        down = house_price * float(.10) 
    else:
        down = house_price * float(.20)
    print(f'Down Paymen: ${down}')
    '''


def _logical_Operators():
    pass
    # Also Comparison Operators
    # and both have to be true / or either one can be true / 
    # not does the inverse of variable set to true will be false and vice /
    #  == / != / >= / <= / < / > /  
    '''   
    high_income = False
    good_credit = True
    has_criminal_record = False
    if high_income and good_credit:
        print('Eligiable for loan.')
    else:
        print('NOT Eligiable for loan.')

    high_income = False
    good_credit = True
    if high_income or good_credit:
        print('Eligiable for loan.')
    else:
        print('NOT Eligiable for loan.')

    high_income = False
    good_credit = True
    has_criminal_record = False
    if good_credit and not has_criminal_record:
        print('Eligiable for loan.')
    else:
        print('NOT Eligiable for loan.')
    
    temp = int(input('What is the temp outside? \n'))
    if temp >= 85:
        print("It's a hot day")
    elif temp <= 65:
        print("It's a cold day today")
    else:
        print("It's a perfect day today")
    
    name = input("What's your name? \n")
    if len(name) < 3:
        print(f"{name} Your name must be 3 or more characters.")
    elif len(name) > 50:
        print(f"{name} Please shorten your name. The allowed max is 50")
    else:
        print(f"{name} Your name looks good!")
    

    weight = int(input('Whats is your weight? \n'))
    unit = input('Would you like to you in (L)bs: or (K)g:')
    
    if unit.upper() == 'L':
        converted = weight * 0.45
        print(f'You are {converted}  in kilos')
    else:  
        converted = weight / 0.45
        print(f'You are {converted} in lbs')
    '''


def _whileloops():
    '''
    #loops
    #while condition:
    
    i = 1
    while i <= 5:
        print(i)
        print('*' * i)
        i = i + 1
    print('Done')
    
    #Guessing game tutorial | While conditions can have else: as follows 
    secret_number = 9
    guess_count = 0
    guess_max = 3
    while guess_count < guess_max:
        guess = int(input('Guess '))
        guess_count += 1
        if guess == secret_number:
            print('You won!!')
            break
    else: #users trys the above and doesnt guess then or else gets executed
          #instead of just ending with nothing said.
        print('Sorry You lose!!')
    #_______________________________
    #Car game
    help = 'start - to start the car \nstop - to stop the car\nquit - to exit'
    car = ''
    started = False
    
    while True: # I had this before "car != 'QUIT':" it works just not writen code friendly "DRY"
                # technically i repeat myself(expression) in car == QUIT  
        car = input('># ').lower() #turns answer to lower case
        
        if car == 'start':
            print('Car Started ready to go')                     
        
        elif car == 'stop':
            print('Car Stopped')
                
        elif car == 'help':
            print(help)
            
        elif car == 'quit':
            break
        
        else:
            print("I don't understand that....")
    '''   


def _forLoops():
    '''
    #forloops
    for item in 'Python':
        print(item)
    
    for item in ['Mosh','Johnny','Sarah']:
        print(item)

    for item in range(5,10,2): #start, stop, step
        print(item)
    
    list = [10,20,30]
    total = 0
    for item in list:
        total = item + item
    print(f'Your total is ${total}')
    
    #making Coordinates
    #my way of completing execise
    for x in range(4):
        for y in range(3):
            print(f'({x},{y})')

    for x in range(2):
        print('X'*5)
        for y in range(1):
            print('X'*2)
    print('XX')
    
    #how Mosh did the exercise
    num = [5,2,5,2,2]
    for x_count in num:
        output = ''
        for count in range(x_count):
            output += 'x'
        print(output)
    '''


def _lists():
    '''
    names = ['John','Bob','James','Wayne','Genny']
    print(names)
    print(names[0])
    print(names[3])
    print(names[-3])
    print(names[2:]) # : is a range
    print(names[2:4]) # 4th is not returned
    print(names[:4])
    names[0] = 'Jon' # modifies list but only the specified index
    print(names)
    
    #find highest number in list
    high_num = 0
    num = [3,6,2,0,1,10,5]
    for i in num:
        if i > high_num:
            high_num = i
    print(high_num) 

    # 2D Lists like a matrix/array
    #[
    #    1 2 3
    #    4 5 6
    #    7 8 9
    #]
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(matrix[0][1])
    #first bracket calls first index[1,2,3,]. 
    #Second bracket calls the first index in the index[2]
    
    #changing 2 to 20 in matrix
    #matrix[0][1] = 20
    print(matrix[0][1])
    print(matrix[0][:])
    print(matrix[1][:])
    print(matrix[2][:])

    #interate through matrix
    for row in matrix:
        for item in row:
            print(item)
    
    #List Methods
    num = [5,2,1,5,7,4]
    num.append(20) #add to the end of the list
    print(num)
    num.insert(1, 10) #add in the middle where you specified first num is location index
                 #then it place the number after it.
    print(num)
    num.remove(10)
    print(num)
    #num.clear() #lears the list
    num.pop() # removes the last item
    print(num.index(7)) #looks for the first instance of 7 in the list returns index value 
    print(50 in num) #same as above looks for the first instance of 50 in the num list 
                     #returns boolean value 
     
    print(num.count(5)) #counts the times it sees 5 in num list
    print(num.sort()) #cant print 
    num.sort() #preforms the action then you can call the sorted list
    print(num)
    num.reverse() #preforms the action then you can call the reverse sorted list
    print(num)
    num2 =  num.copy() #makes copy called num2 does not affect original num
    num2.append(25)
    print(num)
    print(num2)
    
    #remove Duplicates
    num = [1,5,4,6,7,6,10]
    unique = []
    for digit in num:
        if digit not in unique:
            unique.append(digit)
       
    print(unique)
    '''


def _tuples():
    num = (1,2,3) #items can not be changed only . methods are .count and .index
    print(num[0])
    #Used in enviorments were you dont want data to be changed


def _unpacking():
    coordinates = (1,2,3)
    print(coordinates[0] * coordinates[1] * coordinates[2]) # long coding Alternatively we can do the following
    x = coordinates[0]
    y =  coordinates[1]
    z = coordinates[2]
    print(x * y * z) #this os not unpacking
    x, y, z = coordinates # short hand to achieve the same results as above
                          # Unpacking coordinates into the x,y,z
    print(x, y, z)

    #also works with lists you can change coordinate to [] and it will work the same.


def _dict():

    '''
    customer = {
        'name':'Jon Smith',
        'age':30,
        'is_verified':True
    } 
    print(type(customer)) #verify its a dict
    print(customer) 
    print(customer['age']) #calls the dict key and prints the value
    #print(customer['career']) #errors because career not in dict out use below method
    print(customer.get('career')) #will look in dict to see if career exist
                                  #returns none is does not exists instead of error
    
    #supplying a default value for non existing key:value but it does not add it
    #to the dict
    print(customer.get('birthdate','Jan 1, 1977')) 
    print(customer)

    customer['name'] = 'Jack Smith'
    print(customer['name'])
    #adding key:value to dict
    customer['birthdate'] = 'Jan 1, 1977'
    print(customer)
    print(customer['birthdate'])
    

    #number string conversion to word
    phone = input('Phone: ')
    dict_mapping = {
        '1' :'one',
        '2' :'two',
        '3' :'three',
        '4' :'four',
        '5' :'five',
        '6' :'six',
        '7' :'seven',
        '8' :'eight',
        '9' :'nine'
    }
    output = ''
    for character in phone:
        output = output + dict_mapping.get(character,'!') + " "
    print(output)
    
    #EMOJI DICT
    message = input('>_')
    words = message.split(' ') #splits using the space " " between words as a boundary - makes list
                               #very important to me for network automation
    emojis = {
        ':)'  : '😊', # windos key plus semicolon for emoji
        ':('  : '😔',
        ':E>' : '😍'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' ' 

    print(output)
    '''


#how to use functions are below this line
def _functions():# add a, b argument if you want to use the function
    #value stored in name when it was past by function in main program.
    #when the function has a parameter we are obiligated to pass a value
    #place holder
    
    print(f'Hi There {a}, {b}!')
    print('I am a functions thanks for calling me!')

    # Next 3 lines Shift back outside of function
    print('Start Here')
    #_functions('Johnny','Nieves') #passing the value of JOHNNY to the function | remove # if in use
    print('Finish Here')

    #------------------
    #passing parameters look at the comments above
    #We can also pass multiple values separated by commas
    #-----------------
    # keyword arguments are sequential intake of value suppled to function
    #_functions('Johnny','Nieves')
    #Keyword positional arguments, just means you can specify out of order
    #_function(b = 'Nieves', a = 'Johnny') it will still give  you Johnny Nieves
    #when it prints to screen.


def _function2(total,shipping,discount): # return function
    '''
    #this func goes with _functions() i just broke it up to keep examples
    newtotal = total - (total * discount) + shipping
    print(f'$ {newtotal} Dollars')
    #below would be in main or where ever your sending info from 
    #_function2(total = 50, shipping = 5, discount = 0.1) #can not mix match keyword assignment,
    # with positional keyword assigment
    '''

    ''' Shift block back trying to use this with _function2
    #returning value to function that called
    def _function3(num):
        return num * num #if return was not here you would get None printed to the screen
                        #because by default def excutes and leaves to next line of code
                        # if you need result from the def you need return statement

    print(_function3(3))
    '''
    '''
    my applied example for my thought process
    def _error_handling():
        x = 3 
        x += 1
        return x
        
    next to lines shift back if you going to use
    a = (_error_handling())
    print(a)
        '''

# Reusing functions
#'functional functions usally do not use input and output, input, output can come from varies sources'
def emoji_converter(message):
    '''
    words = message.split(' ')
    emojis = {
        ':)'  : '😊', # windos key plus semicolon for emoji  
        ':('  : '😔',  
        ':E> ' : '😍'  
    } 
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '   
    return output

    #next 2 shift block back if want to use in emoji_converter func
    message = input('> ')
    print(emoji_converter(message))#I get and make my variable in line above then i pass the value 
    #in my print statement which calls func the returns value of func and prints it out all with in one line
    '''


#perfect try block for me
def _error_handling():
    '''
    try:
        age = (int(input('age')))
        print(age)
    except ValueError:
        print('invalid value')
        _error_handling()
    '''
    #another example multiple error handling
    try:
        age = (int(input('Age')))
        income = 75000
        risk = income / age
        print(f'your age is {age} and your risk is {risk}')
    except ZeroDivisionError:
        print('Your age is not 0 try again')
        _error_handling()
    except ValueError:
        print('invalid value')
        _error_handling()


def _commenting():
    #hows and whys
    '''
    Block comments like this explain why what program
    does. Also maybe how to run your program although 
    that should be in the read me. Maybe license of 
    program
    '''

    #Line below prints-- Dont comment obvious things like this lines ouput input
    #comment on things not so obvious calculations, classes maybe.
    print('Sky is blue')


def _classes_Section():
    '''
    class defines things that we can not fit into like shopping cart or person
    They are like models / methods we call capitalize first letter
    Numbers
    Strings
    Boolean
    Lists
    Dictionaries    
    '''
class PointClasses: #object is an instance of a class. class is a blue print for creating object
    def __init__(self, x, y): #self references itself in memory to initialize object
        self.x = x 
        self.y = y
    
    def move(self): # object is an instance of that class 
        print('move')
    
    def draw(self): #def in your class is called a method
        print('draw')
    ''' Remarked because now i am calling class which require two arguments:
    point1 = PointClasses() #this object will use our class. 
    #point1.               #Now dot method will show/option to use our def within our class
    point1.draw()  
    point1.x = 10
    point1.y = 20  # your methods can have attributes your class.attibute 
    print(point1.x)

    point2 =  PointClasses() # make point2 be this class or this template p1 and p2 are diffirent objects
    point2.x = 1
    print(point2.b) # you will get AttributeError: 'PointClasses' object has no attribute 'b'
    
    next 6 line of code shift tab to use class
    #Constructor gets created at the time you create and object. Used to construct a new object
    # with variables passed 
    #how can i pass value to the class like def
    #make def __init__(self,x,y) self must be first and in not just the __init def but all def in class

    point = PointClasses(10,20)
    print(point.x)
    '''
'''
#another example of a class
class Person:
    def __init__(self,name): #again this is the template for the object so object should have a name
        self.name = name
    
    def talk(self):
        print(f'Hi i am {self.name}')


    #next block of 5 lines Shift tab to use
    john = Person('John Smith')
    john.talk()

    bob = Person('Bob Smith')
    bob.talk()
'''
'''
#Inheritance  Dont repeat yourself (DRY) if i want to  have another class with the same content of the previous class we can just make it inherate
#the content and add additional content to the created class.
class Mammal:
    def walk(self):
        print("Walk")
        

class Dog(Mammal): #
    #pass # python does not like empty classes. Even though it is inheriting from parent the dog class block is still empty so we tell pythong pass this line 
    def bark(self):
        print('bark') 

class Cat(Mammal):
    #pass
    def meow(self):
        print('meow')


josey = Cat()
josey.walk()
josey.meow()
rover = Dog()
rover.walk()
rover.bark()
#Of course if we wanted to print the name we would have to create a __init__ def
''' #this belongs to the classes sections
#__________________________________________  
#modules section






'''
if __name__ == '__main__':
    #call the function your trying to sample
    _error_handling()
'''
