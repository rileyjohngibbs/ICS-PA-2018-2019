def greetings(name):
	greeting = f"Hello {name}"
	return greeting


# Test for function
name = "Riley"
greeting = greetings(name)
assert greeting == f"Hello {name}"


# Program
my_cat = "Ike"
names = ["Richard", "Linda", "Keegan", "Katelin", "Danielle", "Kiran", "Riley", "Lou", my_cat]
for name in names:
	print(f"Right now, the variable `name` is {name}")
	print(greetings(name))
print("Welcome everyone to Thanksgiving, my favorite holiday!")