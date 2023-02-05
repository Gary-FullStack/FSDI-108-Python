#lists

colors = ["red", "white", "blue"]

# add
colors.append("black")
print (colors)


print (colors[0])

#travel list

for color in colors:
	print (color)


#dictionary

me = {
	"first_name": "John",
	"last_name": "Wick",
	"age":42
}

print (me)

#get a value from the dictionary

print (me["first_name"])

#to modify
me["age"] = 45

#add to the dictionary
me["color"] = "green"

print (me) 
