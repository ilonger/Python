my_name = 'ilonger'
my_age = 26 # not a lie
my_height = 175
my_weight = 125 
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'


print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy" % my_weight)
print ("He's got %s eyes and %s hair." % (my_eyes,my_hair))
print ("Actually that's not too heavy")
print ("His teeth are usually %s depending on the coffee." % my_teeth)

#this lin is tricky,try to get it exactly right
#print("If i add %d, %d, and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight))
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))