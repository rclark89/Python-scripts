
def plt_calculation ():
    choice_input = input("Do you wish to continue Y/N? " )
    while choice_input == "Y":

        #The three initial user inputs.
        pressure_kpa = float(input("Please input your desired pressure in kPA. "))
        plate_area = float(input("Please input your desired plate area in metres squared. "))
        plunger_area = float(input("Please input your desired plunger area in metres squared. "))

        #Calculation of the force on the plate.
        force_kn = pressure_kpa * plate_area

        #Calculation of the pressure exerted by the plunger against the kentledge.
        exerted_pressure = force_kn/plunger_area

        #Calculation of the pressure exerted against the kentledge in PSI.
        exerted_pressure_kpa = exerted_pressure * 0.145

        #Output.
        print (str(exerted_pressure_kpa) + " kPA")

        #Updating the choice_input variable to see if the user wishes to continue.
        choice_input = input("Do you wish to continue Y/N? " ) 

#Calling the function.
plt_calculation()

#Keeping the python terminal open for convenience of users.
keep_open = input("Press return to exit.")
