def cheese_and_crackers(cheese_count,boxs_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxs_of_crackers
	print "Man that's enouch for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)

print "We can call the function in a loop,calling it 10 times"
for i in range(10):
	cheese_and_crackers(20,30)

print "We can now ask the user for the number of cheese and crackers"
cheese_and_crackers(int(raw_input("how many cheese?")),int(raw_input("how many crackers?")))