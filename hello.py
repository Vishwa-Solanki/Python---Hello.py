
# #  ctrl + / is how you do comments 

# # This is a string example
# print("hello world")
# print("First day of Python")
# #  This is number example
# print(3)
# print(3+3)

# learner = "Abc"
# print(learner)
# ideal_number_of_pets =3
# print(ideal_number_of_pets)
# how_much_of_a_banana = 3.1
# print(how_much_of_a_banana)

# is_our_pet_vaccinated = True
# print(is_our_pet_vaccinated)

# print(type(how_much_of_a_banana))
# print(type(is_our_pet_vaccinated))
# print(type(learner))
# print(type(ideal_number_of_pets))

# # Power of example
# print(3**3)

# # Modulo
# print(10%5)
# print(10%3)

# # area of ractangle
# # l x w
# length = 342
# width = 20

# area = length * width
# print(area)

# # find text amount 
# price = 10
# tax = price * 0.08
# print(tax)

# # Find the average
# avg = (10+10+10)/3
# print(avg)

# Input Function
# length1= float(input("Enter Length: "))
# width1 = 20
# area1= length1 * width1
# print(area1)

# fav_color = input("Your Favourite coloir is?")

# print(f"Your Favoriye Color Is {fav_color}")

#Create a Receipt
# customer name
# print("Reciept")
# print("-------------------------------")
# customerName = "Vishwa"  
# print(f"Customer Name: {customerName}")
# # what they purchased
# itemPrice = 7.95
# print(f"Item Price: {itemPrice}")
# # quantity they purchased
# quantity = 42
# print(f"Quantity of Item: {quantity}")
# # Total cost
# totalCost = round(itemPrice * quantity, 2)
# # another way to round
# roundCost = round(totalCost, 2)
# print(f"Total Cost: {totalCost}")
# print(f"Total Cost: {roundCost}")


#Create a Receipt Using Input
# customer name
print("Reciept")
print("-------------------------------")
customerName = input("enter customer name: ")  
print(f"Customer Name: {customerName}")
# what they purchased
itemPrice = float(input("enter item price: "))
print(f"Item Price: {itemPrice}")
# quantity they purchased
quantity = int(input("enter quantity: "))  
print(f"Quantity of Item: {quantity}")
# Total cost
totalCost = round(itemPrice * quantity, 2)
# another way to round
roundCost = round(totalCost, 2)
print(f"Total Cost: {totalCost}")
print(f"Total Cost: {roundCost}")


# Adding this to Github
print("Now we have created a Git repo and then adding this additional line of command to try git push and add this to git")