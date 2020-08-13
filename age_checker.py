def age_check():
    age_str = input( 'How old are you?: ')
    try:
        y = int(age_str)
    except:
        print ("provide your age in numbers")
        return age_check()

    else:
        return y

run_var = "Y"
while run_var == "Y":
    print ('Welcome')
    print ("Please provide your name and age")
    print ("Let's get started")

    first_name = input("Provide your first name")
    last_name = input("Provide your last name")
    age = age_check()
    year = 2020
    year_of_birth = 2020 - age

    print (f"Hello {first_name}{last_name}", f"you were born in the year {year_of_birth}")
    run_varun_var = input('Do you want to try again')
