"""
Strings are anything enclosed within quotes
"""

message = "Hello World"
print(message)

# Multi line strings can be made using triple quotes
multi_line = """Hello there,
my name is om"""

print(multi_line)

# we can access a particular index of a string, we can use []
print(message[6])

# we can even specify a range of index, this is called string slicing
print(message[3:8])

# there are many methods that are available too

print(message.upper())
print(message.count("l"))
print(message.find("l")) # returns the index of the first match element

print(message.replace("l", "i")) # .replace(old, new)

# Formatted string
formatted_string = "I can add this -> {}, and also this -> {}".format(message, multi_line)
print(formatted_string)

# F strings, easier way to format strings
f_string = f"I can do this instead -> {message}"
print(f_string)

# if you want to see all the methods that are available for a variable, use the dir method
# print(dir(message))

# using the help functions, it gives us the detailed description
# print(help(str))