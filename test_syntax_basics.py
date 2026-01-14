#basic syntax checks

import this

#test variables edition

print("Test")

testMessage = "Soy un test"

print(testMessage)

testerFeedback = "De acuerdo. Que tipo de Test?"

print(testerFeedback)

testMessage = "Smoke"

print(testMessage)

testerFeedback = "Como te llamas?"

print(testerFeedback)

testMessage = (" Smoke Test' ")
testMessageCheckSpace = testMessage.rstrip()

print (testMessage.title())

print (testMessageCheckSpace.upper())

testMessageCheckSpace = testMessageCheckSpace.strip()

print (testMessageCheckSpace.lower())

#test calc and num operation

TEST_COUNT, testerThank = 3 ** 3, "merci, "

#test string format

final = f"{testerThank}{testMessageCheckSpace} {TEST_COUNT}'s"

print(f"\tMuy bien, {final.title()}, \n\tnext!")

#test list creation

tests = []

#test list fullfil

tests = ["login", "registration", "auth", "view profile", "edit profile", 
    "delete account", "send message", "read message", "skip message", "attach media", 
    "view contact", "edit contact", "delete contact", 
    "checkin", "checkout", "jump", "like", "dislike", 
    "set status", "delete status", "view status", 
    "view checkins", "delete checkin", "reset status history", "search locations", 
    "mark locations", "view settings"]

print(tests)

#test list insert
    
tests.insert(2, "email recovery")

print(tests)

print(tests[2])

#test list delete

del tests[2]

print(tests[2])
print(tests[2].title())
print(tests[-1])

testerFeedback = f"Quiuero ejecutar {tests[0].title()}"

print (testerFeedback)

#test list pop

done = tests.pop(0)

testerFeedback = f"Se ha ejecutado {done.title()}"

print (testerFeedback)

tests[0]= 1

#test list append

tests.append("view chats")

testerFeedback = f"Quiuero ejecutar {tests[26]}"

done = tests.pop(26)

testerFeedback = f"Se ha ejecutado {done.title()}"

print (testerFeedback)

print(tests)

processTest = tests.pop()

print(processTest)

print(tests)

processTest = tests.pop(0)

print(processTest)

print(tests)

#test list sort

print(sorted(tests))

print(sorted(tests, reverse = True))

tests.reverse()

print(tests)

tests.reverse()

print(tests)

# test list size

print(len(tests))
