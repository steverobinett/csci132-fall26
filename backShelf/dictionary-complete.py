#1.1 Create and Read a Dictionary
# Create a dictionary
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",  
    "Carmen": "555-8765"
    }
print(contacts)
print(type(contacts))

#1.2 Access Dictionary Values
print(contacts["Alice"])
print(contacts["Bob"])
print(contacts["Carmen"])

#1.3 Key Error
# Uncomment the following line to see a KeyError
# print(contacts["David"])  # This will raise a KeyError since "David" is not a key in the dictionary

#1.4 check using in operator
if "David" in contacts:
    print(contacts["David"])    
else:
    print("David is not in contacts.")
    
#1.5 Safe access using get() method
print(contacts.get("David", "David is not in contacts."))  

#2.1 Add new keyvalue pair
contacts["David"] = "555-4321"
print(contacts)

#2.2 Update existing keyvalue pair
contacts["Alice"] = "555-0000"
print(contacts)

#2.3 Remove keyvalue pair using del
del contacts["Bob"]
print(contacts)

#2.4 Remove keyvalue pair using pop()
removed_number = contacts.pop("Carmen", "Carmen is not in contacts.")
print(removed_number)
print(contacts)

#2.5 Getting all keys and values
print(contacts.keys())
print(contacts.values())
print(contacts.items())

# 2.6 Iterate through the dictionary
for name, number in contacts.items():
    print(f"{name}: {number}")  
    
    
