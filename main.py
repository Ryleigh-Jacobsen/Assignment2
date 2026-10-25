"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthly_cost = annual_cost / MONTHS_PER_YEAR
    return monthly_cost

def cost_per_day(semester_cost):
    """Give back what one class day costs."""
    daily_cost = semester_cost / CLASS_DAYS_PER_SEMESTER
    return daily_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost / credits
    return credit_cost


def cost_per_class(credit_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = credit_cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total cost for one year: "))
    credits = int(input("How many credits are you taking? "))
    while True:
        # Show your menu here.
        print( "THE COST OF COLLEGE \n 1. Per semester \n 2. Per month \n Per class day \n Per credit \n Per CS 1430 class \n cost of skipped classes")
        choice = input("Choose an option: ")

        if choice == "Q":
            print ("Thanks for running the numbers!")
            break
        elif choice == "1":
            semester = cost_per_semester(annual_cost)
            print (f"One semester costs: {semester:,.2f}")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
