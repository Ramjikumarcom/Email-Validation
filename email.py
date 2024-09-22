# email validation code in python
k, j, d = 0, 0, 0
email = input("Enter email:")
if len(email) >= 8 and len(email) <= 30:  # check for length
    if email[0].isalpha():  # check for alpha character is it starts  with or not
        if (
            ("@" in email)
            and (email.count("@") == 1)
            and ("." in email)
            and (email.count(".") == 1)
        ):  # check for @ ,.
            if (email[-4] == ".") ^ (email[-3] == "."):  # check for place of . from end
                if email.endswith("@gmail.com") ^ email.endswith(
                    ".in"
                ):  # check for endswith gmai.com or .in
                    for item in email:  # executin loop
                        if item == item.isspace():  # check for space
                            k = 1
                        elif item.isalpha():  # check for alpha
                            if item == item.upper():
                                j = 1  # check for is it upper letter or not if yes return false
                        elif item.isdigit():
                            continue  # check for digit
                        elif item == "." or item == "_" or item == "@":
                            continue  # check for .,_,@
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        print("invalid email")
                    else:
                        print("right email")
                else:
                    print("invalid email")
            else:
                print("invalid email")
        else:
            print("invalid Email")
    else:
        print("please Enter valid email ")
else:
    print("invalid email")
# print(email)
