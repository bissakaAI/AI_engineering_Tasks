#this is a code that slices the email into username and domain
# f ="lead"
# q=f.rindex("m")
# print(q)
while True:
    try:
        #Gets user email address 
        user_email = (input ("Please input your email address: ").lower()).strip()

        #splits the email and unpacks it 
        username,domain= user_email.split("@")

        #now i need to be able to detect the username and domain
        #if in username there is @the words befor @ is the username while the one after the dot after @ is the domain 

        if "@" not in user_email or user_email.rfind(".")== -1:
            print("invalid email address")
        elif "." in username:
            print("invalid input before @")
        else:
            print("valid email address")
            print(f"Username: {username}\nDomain: {domain}")
            break
    except ValueError:
        print("invalid input")
    except Exception as e:
        print("Error: ", e)

