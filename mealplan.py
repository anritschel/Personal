import random
import smtplib
from email.message import EmailMessage


def sendMeals(meals):
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
    for meal in meals:
        mealTable += "<td>" + str(meal) + "</td>"
        groceryTable += "<P>" + str(ingredientLists[meal]) + "</P>"
    mealTable += "</tr></table>"

    
    for meal in meals:
        

    emailBody += mealTable + groceryTable +  "</body></html>"
    message = EmailMessage()
    message['Subject'] = "Weekly Meals & Grocery List"
    message['From'] = ""
    message['To'] = ""
    message.set_content('data')
    message.add_alternative(emailBody, subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('email@gmail.com', 'yourpassword')
        smtp.send_message(message)
    
    return 0


mealOptions = [ 'MealName']

ingredientLists = { 'MealName' : 'Meal ingredients',
                    }



mealPlan = []

groceryList = {}

counter = 0

while counter < 7:
    meal = mealOptions[random.randint(0, (len(mealOptions)-1))]

    while meal in mealPlan:
        meal = mealOptions[random.randint(0, (len(mealOptions)-1))]

    mealPlan.append(meal)

    counter += 1

sendMeals(mealPlan)