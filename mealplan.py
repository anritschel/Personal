import random
import smtplib
from email.message import EmailMessage


"""
Project ToDo
1) modify to use RDB for users
    MySQL
2) add logic to tally ingredients
3) add logic to sort ingredients by type







SQL Tables

User
____________________________________________________________________________
ID                |Name       |Email      |MealList                        |
int auto increment|varchar(50)|varchar(50)|int(linked to MealList Table ID)|

MealList
_______________________________________________________
ID                |MealName    |Ingredient List       |
int auto increment|varchar(50) |varchar(20000)        |

Ingredients
_________________________________________________________
ID                |IngredientName    |IngredientType    |
int auto increment|varchar(50)       |varchar(50)       |


Ingredient types:
Fresh Produce
Frozen Produce
Fresh Meat
Frozen Meat
Dairy
Dry
Baked Goods
"""



def sendMeals(meals,sides):
    emailBody = """<html>
                                <head>
                                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"></head>
                                <body>
                            	<style>
                            		table {
                            			width:100%;
                            			border:1px solid #000;
                            			border-collapse:collapse;
                            		}

                            		th, td {
                            			border:1px solid #000;
                            		}
                            	</style>
                            	<p>Here are the meals for this week:</p>"""

    mealTable = """<table><tr><td> Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td><td>Friday</td><td>Saturday</td><td>Sunday</td></tr><tr>"""
    groceryTable = """<p> Here are the groceries needed:</p>"""
    sideTable = """<p> Here are the sides for the week:</p><table><tr>"""
    
    for meal in meals:
        mealTable += "<td>" + str(meal) + "</td>"
        groceryTable += "<P>" + str(ingredientLists[meal]) + "</p>"
        
    
    for side in sides:
        sideTable += "<td>" + str(side) + "</td>"
        groceryTable += "<P>" + str(sideIngredients[side]) + "</p>"

    mealTable += "</tr></table>" 
    sideTable += "</tr></table>"     
    emailBody += mealTable + sideTable + groceryTable +  "</body></html>"
    message = EmailMessage()
    message['Subject'] = "Weekly Meals & Grocery List"
    message['From'] = "Andrew.ritschel@gmail.com"
    message['To'] = "andrew.ritschel@gmail.com", "ashleeamcintire@yahoo.com"
    message.set_content('data')
    message.add_alternative(emailBody, subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('Andrew.Ritschel@gmail.com', 'Th3s0r00!')
        smtp.send_message(message)
    
    return 0


mealOptions = [ 'Lemon Pepper chicken and Rice', 'Pan Seared Chicken', 'Burgers', 'Tatertot Casserole', 'Nachos', 'Roast',
                'Porkchops', 'tacos', 'Italian Beef', 'Redbeans and Rice', 'hamburger helper', 'Steak', 'Fajitas', 'Carbonara', 
                'Vodka Noodles', 'Lasagna', 'Spaghetti', 'chilli', 'stuffed chicken breast', 'stuffed pork chops']

ingredientLists = { 'Lemon Pepper chicken and Rice' : 'Lemon Pepper, Cream of chicken soup, rice, chicken', 
                    'Pan Seared Chicken': 'chicken, italian dressing', 
                    'Burgers' : 'Ground beef, buns', 
                    'Tatertot Casserole' : 'ground beef, cream of mushroom soup, frenchfried onions, sour cream, shredded cheese', 
                    'Nachos' : 'ground beef, tortilla chips, jalapenos, onion, queso', 
                    'Roast' : 'Roast',
                    'Porkchops' : 'Pork chops, mac and cheese', 
                    'tacos' : 'ground beef, onions, shredded cheese, sour cream, tortillas', 
                    'Spaghetti' : 'Spaghetti, ground beef, pasta sauce', 
                    'Italian Beef': 'Roast, dry italian dressing, french onion soup mix, hoagies, cheese', 
                    'Redbeans and Rice' : '2 cans red beans, vegetable stock, onion, celery, garlic, rice', 
                    'hamburger helper' : 'hamburger helper, ground beef', 
                    'Steak' : 'steak', 
                    'Fajitas' : 'Steak, red onion, 3 bell peppers, cilantro, lime', 
                    'Carbonara' : 'bacon, parmesan, eggs, spaghetting noodles, cream', 
                    'Vodka Noodles' : 'tomato paste, penne, cream, parmesean, butter, garlic, onion, vodka, spicy italian sausage', 
                    'Lasagna' : 'ricotta cheese, lasagna noodles, italian sausage, ground beef, pasta sauce, paremesan, motzarella', 
                    'chilli' : 'red beans, black beans, bell peppers, jalapeno, ground beef, sausage, tomato sauce, onion, garlic',
                    'stuffed chicken breast' : 'chicken breasts, cream cheese, mozzarella, parmesan, celery, onion, garlic',
                    'stuffed pork chops' : 'pork chops, cream cheese, mozzarella, celery, onion, mushroom',
                    }

sidesNeeded = {     'Lemon Pepper chicken and Rice' : 1, 
                    'Pan Seared Chicken': 1, 
                    'Burgers' : 1, 
                    'Tatertot Casserole' : 0, 
                    'Nachos' : 0, 
                    'Roast' : 1,
                    'Porkchops' : 1, 
                    'tacos' : 1, 
                    'Spaghetti' : 1, 
                    'Italian Beef': 1, 
                    'Redbeans and Rice' : 1, 
                    'hamburger helper' : 1, 
                    'Steak' : 1, 
                    'Fajitas' : 1, 
                    'Carbonara' : 1, 
                    'Vodka Noodles' : 0, 
                    'Lasagna' : 0, 
                    'chilli' : 0,
                    'stuffed chicken breast' : 1,
                    'stuffed pork chops' : 1,
                    }


sides = [   'stuffed mushrooms', 'rice & mushrooms', 'mashed potatoes', 'twice baked potatoes', 'mac & cheese', 'asparagus', 'steamed brocolli', 'creamed spinach', 
            'garlic bread', 'potatoes au gratin', 'scallopped potatoes', 'cornbread', ]

sideIngredients = { 'stuffed mushrooms' : "whole mushrooms, cream cheese, onions, garlic",
                    'rice & mushrooms' : "rice, cream, sliced mushrooms", 
                    'mashed potatoes' : "Potatoes, cream, butter",
                    'twice baked potatoes' : "potatoes, cream, butter, green onion, cheddar cheese", 
                    'mac & cheese' : "Kraft :(",
                    'asparagus' : "asparagus, provalone", 
                    'steamed brocolli' : "brocolli, cheddar cheese, cream", 
                    'creamed spinach' : "spinach, shallot, cream",
                    'garlic bread' : "5 cheese garlic bread", 
                    'potatoes au gratin' : "Potatoes, cream, onion, garlic, cheddar cheese", 
                    'scallopped potatoes' : "Potatoes, cream, onion, parmesean cheese", 
                    'cornbread' : "cornmeal, flour, vegetable oil, egg"
}

def getSides(mealPlan):
    counter =0
    for meal in mealPlan:
        counter += sidesNeeded[meal]
    
    return counter

def generateSides(count):
    sideDishes = []
    while count > 0:
        side = sides[random.randint(0, (len(sides)-1))]
        
        while side in sideDishes:
            side = sides[random.randint(0, (len(sides)-1))]
        
        sideDishes.append(side)
        count -= 1
    
    return sideDishes
    
mealPlan = []

groceryList = {}

counter = 0

while counter < 7:
    meal = mealOptions[random.randint(0, (len(mealOptions)-1))]

    while meal in mealPlan:
        meal = mealOptions[random.randint(0, (len(mealOptions)-1))]

    mealPlan.append(meal)

    counter += 1


sidecount = getSides(mealPlan)
sidePlan = generateSides(sidecount)


sendMeals(mealPlan,sidePlan)






