# match is like switch in other lang
# match the option and execute
# run in python > 3.10

# syntax
#
# match variable:
#     case pattern1:
#         #code
#     case pattern2:
#         #code

browser_name = input("Enter browser name")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute firefox code")
    case "chrome":
        print("Execute chrome code")
    case "brave":
        print("Execute brave code")
    case  _:
        print("Invalid entry")
