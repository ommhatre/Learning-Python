# Lists
courses = ["math", "science", "history"]
print(courses)

# list operations
print(courses[1])
print(courses[:2])

courses.append("computer")
courses.insert(1, "commerce")

# if we want to add multiple items to our list, we can use the extend method
courses2 = ["biology", "cybersecurity"]
courses.extend(courses2)

print(courses)

# deleting items from our list

# remove method
courses.remove("biology")

# pop method: deleted the last element and returns the value
pop_element = courses.pop()

# reversing list
courses.reverse()

# Sorting list
courses.sort() # ascending order
courses.sort(reverse=True) # descending order

# Sorting list without changing the orignal list
sorted_courses = sorted(courses)

# other operations
print(min(courses))
print(max(courses))

nums = [1,2,3,4,5,6]

print(sum(nums))

# check if something exists in the list
print("Art" in courses)

# enumeration loop

for index, course in enumerate(courses):
    print(index, course)

# if we want to print out list as a string seperated by something
course_str = ", ".join(courses)
print(course_str)

# converting a string back into a list
str_to_list = course_str.split(", ")
print(str_to_list)
