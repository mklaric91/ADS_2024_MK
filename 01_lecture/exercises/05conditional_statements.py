"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
# Write your solution here
#number=int(input("Enter a number:"))
#if number % 2 == 0:
#    print(f"the number", number, "is even")
#else:
#    print(f"the number", number, "is odd")


"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# Write your solution here
#grade=int(input("Enter your exam grade"))
#if grade <=50:
#    print("Unfortunately, you failed the exam")
#elif grade >=60:
#    print("You passed the exam!")
#elif grade >=90:
#    print("Congratulations, you are excellent")
"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
# Write your solution here
sandwich_choice= none
dressing_choice= none
toasted_choice= none

choice=input("Would you like a sandwich, salad, or wrap? ").lower()
if choice == "sandwich":
    sandwich_choice = input("What kind of Sandwich do you want? Chicken, beef or veggie")
elif choice == "salad":
    dressing_choice = input("What kind of dressing would you like: vinaigrette, ranch, or caesar?")
elif choice == "wrap":
    toasted_choice = input("Do you want it toasted? yes/no ")

print("Your order:", choice)
if sandwich_choice:
    print("Sandwich choice:", sandwich_choice), 
elif dressing_choice:
    print("Dressign choice:", dressing_choice)
elif toasted_choice
print("Toasted choice:, toasted_choice)
