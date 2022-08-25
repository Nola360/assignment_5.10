#Akinola Daramola Jr
#Programming Exercise 5.10
#Due Date: 07/20/2022


"""
Feet to Inches
One foot equals 12 inches.
Write a function named feet_to_inches that accepts a number of feet
as an argument and returns the number of inches in that many feet.
Use the function in a program that prompts the user to
enter a number of feet then displays the number of inches in that many feet.

"""



#Call main function
def main():
    #Prompting user to enter number
    number_of_feet = float(input("Enter number of feet: "))
    
    #Declaring functiton as variable to print function with argument
    convert_to_inches = feet_to_inches(number_of_feet)

    """
   #feet_to_inches(userInput())
    """

    #Displays feet and inches
    print(f"Number of Feet: {number_of_feet:,.2f}ft")
    print(f"Number of Inches: {convert_to_inches:,.2f}in")

#Define function that takes one parameter
def feet_to_inches(number_of_feet):
    
    #Declare value of inches variable
    inches = 12

    #Return number of feet times inches
    return number_of_feet * inches
    

"""
def userInput():
    number_of_feet = float(input("Enter number of feet: "))
    return number_of_feet
    pass
"""



#Calling main function to invoke return statement function
main()
