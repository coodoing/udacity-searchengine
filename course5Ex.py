courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

def is_offered(courses, course, hexamester):
    courses = courses_offered(courses, hexamester)
    for entry in courses:
        if course == entry:
            return True    
    return False

print(is_offered(courses, 'cs101', 'apr2012'))
print(is_offered(courses, 'cs003', 'apr2012'))


def when_offered(courses,course):
    result=[]
    for key in courses.keys():
        for v in courses[key]:
            if v==course:
                result.append(key) 
    return result

print(when_offered(courses, 'cs101'))
print(when_offered(courses, 'bio893'))


def involved(courses, person):    
    result={}
    for key in courses.keys():
        course=[]
        for v in courses[key]:
            #print(v)
            #print(courses[key])
            #print(courses[key][v])
            for m in courses[key][v].keys():
                #print(m)
                if courses[key][v][m]==person and v not in course:
                    course.append(v)
                if course !=[]:
                    result[key] = course
    return result




print(involved(courses, 'Dave'))
#=> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
print(involved(courses, 'Peter C.'))
#=> {'apr2012': ['cs262'], 'feb2012': ['cs101']}
print(involved(courses, 'Dorina'))
#=> {'jan2044': ['cs001']}





cache = {} # start cache as an empty dictionary

def cached_execution(cache,code):
    #print(code)
    for entry in cache:
        if entry==code:
            return cache[code]    
    cache[code]=eval(code)
    return cache

#Here is an example showing the desired behavior of cached_execution:
#Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

print(cached_execution(cache, 'factorial(5)'))                       
print("Second time:")
### second execution (should only print out the result)
print(cached_execution(cache, 'factorial(5)'))


#Fibonacci
def cached_fibo(cache, n):
    if n == 1 or n == 0:
        return n
    else:
        print("1")
        return cached_execution2(cache, 'cached_fibo(cache, ' + str(n - 1) + ')')+ cached_execution2(cache, 'cached_fibo(cache, ' + str(n - 2) + ')')


#Hint: you will need to use the built-in eval function similarly to how we used
#it in time_execution.  The eval function takes a string as input, and returns
#the result of evaluating that string as a Python expression.

def cached_execution2(cache,code):
    print(code)
    if code =="cached_fibo(cache, 1)" or code == "cached_fibo(cache, 0)":
        return 1
    else:
        for entry in cache:
            if entry==code:
                print("2")
                return cache[code]
        print("3")
        cache[code] = eval(code)


#print(eval('cached_fibo(cache, 3)'))
#print(cached_execution2(cache, 'cached_fibo(cache, 5)'))
    
    
    
    
    
