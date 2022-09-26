# Create a dictionary called `person`, it has three properties, `name` which is a string, `age` which is an integer, `hobbies` which is a list of strings.
person={"name":"Yousef","age":40,
"hobbies":["reding","playing fotball"],
}

# Create a function called `change_age` which takes the `person` dictionary and a `number` as arguments, this function changes the age in the dictionary to the `number`. The return value of this function is the updated dictionary.


def change_age(person,number):
   person['age'] = number
   return person
print(change_age(person, 21))


# Create a function called `add_hobby` which takes the `person` dictionary and a `hobby` as arguments. This function adds the hobby to the list of `hobbies` inside the person dictionary. The function will return the updated dictionary.


def add_hobby(person, hobby):
    person["hobbies"].append(hobby)
    return person
print(add_hobby(person, "Table Tennis"))


# CHALLENGE

# Create a function called `add_job` which takes `person` dictionary and `job` which is a string, as arguments. This function checks, if the dictionary does not have a property called `job` then it will add it to the dictionary. The function will return the updated dictionary.


def add_job(person, job):
#    for key in person:
#     if key.find("job"):
#         print(person)
#     else:
#         person.__setitem__("job","IT")
#     return person
  if "job" not in person:
    person["job"]="eng"
  else:
    print("the key is already there")
  return person
print(add_job(person,"job"))





# 2. Create a function called `check_hobbies`, which takes a person dictionary as an argument. This function checks the number of hobbies for this person, if it's more than three hobbies, print to the user a message telling them that they're talented.



def check_hobbies(person):
    x=0
    for hobby in person["hobbies"]:
        x=+x
    if x >= 3:
        print("you are talent")
    else:
        print("add one more")
        
print(check_hobbies(person))

