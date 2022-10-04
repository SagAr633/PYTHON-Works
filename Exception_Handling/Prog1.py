user_age=int(input('Enter Age'))
if user_age>=18:
    print("You Are Eligible For Vaccination")
else:
    raise Exception("We Are Sorry\nYou Are Not Eligble For Vaccination")