import this

#test presentation

print("Test")

testMessage = "Soy un test"

print(testMessage)

#tester feedback

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

#test count and thank words

TEST_COUNT, testerThank = 3 ** 3, "merci, "

#final words to close

final = f"{testerThank}{testMessageCheckSpace} {TEST_COUNT}'s"

print(f"\tMuy bien, {final.title()}, \n\tnext!")

