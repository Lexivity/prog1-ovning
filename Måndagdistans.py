def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print ('Greetings welcome to your personal calculator')
print ('Please pick what calculation you want to be performed from the list going from 1 to 5')
print ('[1] addition +')
print ('[2] subtraction -')
print ('[3] multiplication *')
print ('[4] division %')
print ('[5] exit')
##Finns säkert ett mycket effektivare sätt att skriva detta åvanför på.
##Jag började med att skriva en grund med det mesta jag kunde.
##Sedan kollade jag upp på internet för att försöka förstå hur jag skulle göra uppgiften genom att hitta en färdig kod och läsa igenom den.
##Sedan vissade det sig att jag inte hade gjort ett bra jobb till början... Så jag gjorde om det och följde hjälpen have koden jag hittade...
##Lesson learned, mixa inte andras kod med din egna eftersom att ni kan ha tänkt olika och det kan försöra din kod...
##Okej nu har jag nog fått det att fungera och när man läser koden så kan man ganska bra förstå hur den fungerar.
while True:

    choice = input("Enter your choice now (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print('You have selected option [1] addition +')
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print('You have selected option [2] subtraction -')
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print('You have selected option [3] multiplication *')
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print('You have selected option [4] division %')
            print(num1, "/", num2, "=", divide(num1, num2))
        
    elif choice == '5':
        print('You have selected option [5] exit')
        print('Farewell...') 
        break

    else:
        print("Invalid input, please try again...

##Hoppas allting verkar fungera, och jag har lärt mig någonting.