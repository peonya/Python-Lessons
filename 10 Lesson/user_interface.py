import numbers
import view
import init
from fractions import Fraction

def main_menu():
    print('Please select between:\n\n 1. Complex numbers\n 2. Fraction\n')
    choice = input("Enter your choice:")
    if choice == "1":
        main_menu1()
    elif choice == "2":
        main_menu2()
    else: 
        print( "Please type 1 or 2! \n") 
        enter = input( "Press Enter to continue ...") 
        main_menu1()

        

def main_menu1(): 
    print( "\nMAIN MENU\n") 
    print( "1. Addition") 
    print( "2. Difference")
    print( "3. Multiplication")
    print( "4. Division")
    print( "5. Exit") 
    choice = input("Enter your choice: ") 
    if choice == "1": 
        view.pr_add()
        a = complex(input('Enter 1 value:'))
        b = complex(input('Enter 2 value:'))
        init.sum(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu1() 
    elif choice == "2": 
        view.pr_diff()
        a = complex(input('Enter 1 value:'))
        b = complex(input('Enter 2 value:'))
        init.diff(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu1() 
    elif choice == "3": 
        view.pr_mult()
        a = complex(input('Enter 1 value:'))
        b = complex(input('Enter 2 value:'))
        init.mult(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu1()
    elif choice == "4": 
        view.pr_div()
        a = complex(input('Enter 1 value:'))
        b = complex(input('Enter 2 value:'))
        init.div(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu1() 
    elif choice == "5": 
        print("Thank you for using Calculator!") 
    else: 
        print( "Please type the number from 1 to 5! \n") 
        enter = input( "Press Enter to continue ...") 
        main_menu1() 

def main_menu2(): 
    print( "\nMAIN MENU\n") 
    print( "1. Addition") 
    print( "2. Difference")
    print( "3. Multiplication")
    print( "4. Division")
    print( "5. Exit") 
    choice = input("Enter your choice: ") 
    if choice == "1": 
        view.pr_add()
        a = Fraction(input('Enter 1 value:'))
        b = Fraction(input('Enter 2 value:'))
        init.sum(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu2() 
    elif choice == "2": 
        view.pr_diff()
        a = Fraction(input('Enter 1 value:'))
        b = Fraction(input('Enter 2 value:'))
        init.diff(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu2() 
    elif choice == "3": 
        view.pr_mult()
        a = Fraction(input('Enter 1 value:'))
        b = Fraction(input('Enter 2 value:'))
        init.mult(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu2()
    elif choice == "4": 
        view.pr_div()
        a = Fraction(input('Enter 1 value:'))
        b = Fraction(input('Enter 2 value:'))
        init.div(a,b)
        enter = input("Press Enter to continue ...") 
        main_menu2() 
    elif choice == "5": 
        print("Thank you for using Calculator!") 
    else: 
        print( "Please type the number from 1 to 5! \n") 
        enter = input( "Press Enter to continue ...") 
        main_menu2() 
