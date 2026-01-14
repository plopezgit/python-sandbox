#basic syntax checks

import this
from testRepo import testRepo

#test variables edition

test = "LOGIN " 

print(test)

testCheckSpace = test.rstrip()

testCheckSpaceAndCaption = testCheckSpace.lower()

#test list creation

tests = []

#test list fullfil

tests = [testCheckSpaceAndCaption, "registration", "auth", "view profile", "edit profile", 
    "delete account", "send message", "read message", "skip message", "attach media", 
    "view contact", "edit contact", "delete contact", 
    "checkin", "checkout", "jump", "like", "dislike", 
    "set status", "delete status", "view status", 
    "view checkins", "delete checkin", "reset status history", "search locations", 
    "mark locations", "view settings"]

print(tests)

#test list insert
    
tests.insert(2, "email recovery")

print(tests[2])
print(tests)

#test list delete

del tests[2]
print(tests)

#test list sort

print(sorted(tests, reverse = True))

# using list in a class method

testRepo = testRepo()
testRepo.addTest(testCheckSpaceAndCaption).addTest("registration").addTest("pass recovery")

for test in testRepo.tests:
    print(f"{test.title()} Test")
    
print(len(testRepo.tests))
print(sorted(testRepo.tests))

testRepo.tests.reverse()

for test in testRepo.tests:
    print(f"{test.title()} Test")
    
#test = testRepo.tests.pop(0)

#print(test)

#numeric list

numbers = []

for number in range (1, 11):
    numbers.append(number)

print(numbers)

numbers2 = list(range(1, 11))
print(numbers2)

squares = []

for value in numbers2[:3]:
    squares.append(value ** 2)

print(min(squares))
print(max(squares))
print(sum(squares))


halfs = [value / 2 for value in range(2,11)]
print(halfs)

# if else

nextExecution = []

for test in testRepo.tests:
    if test != "login":
        print(f"{test.title()} function is covered")    
    else:
        nextExecution.append(test)
        print(f"{test.title()} will be executed")
    
print(nextExecution)
    
