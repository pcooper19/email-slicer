# get user e-mail address

email = input("What is your e-mail address?: ").strip()

# slice out username

user = email[:email.index("@")]

# slice out domain name

domain = email[email.index("@") + 1:]

# format output message

output = "Your username is {} and your domain name is {}".format(user,domain)

# display output message

print (output)