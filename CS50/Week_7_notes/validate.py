# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#library - re (regular expressions) - for working with patterns

import re
email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):  #.+ == ..* , r = raw expression, \ for interpreting . as .for .edu, \w = word characters and _ = [a-zA-Z0-9_]
    print("Valid")
else:
    print("Invalid")