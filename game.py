#!/usr/local/bin/python3

import pymysql  as db                  
from cgitb import enable
enable()
from os import environ
from http.cookies import SimpleCookie
cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')

if not http_cookie_header:
    cookie['played'] = 1
    cookie['prize'] = 50000


else:
    cookie.load(http_cookie_header)
    if 'played' not in cookie:
        cookie['played'] = 1
    if 'prize' not in cookie:
        cookie['prize'] = 50000

    else:
        cookie['played'] = int(cookie['played'].value) + 1
        cookie['prize'] = int(cookie['prize'].value) + 50000
        
        
print(cookie)

from cgi import FieldStorage

from html import escape
print('Content-Type: text/html')
print()

counter = int(cookie['played'].value)
connection = db.connect('connect to your database')
cursor = connection.cursor(db.cursors.DictCursor)
cursor.execute("""SELECT  Questions, Option_A, Option_B, Option_C, Option_D, Answer
                    FROM Game """) 

data = cursor.fetchall()[counter]

form_data = FieldStorage()

value = int(cookie['prize'].value)
prize = value - 100000
correct = data["Answer"]

result = """
            <h1>  This question is for $%s </h1>
            <br><br>
            <p> %s</p>
            <form action = 'game.py' method = 'get'>
                <fieldset>
                    <input type="radio" name="option" value = %s class='pick' />
                    <label for=%s>%s</label>
                    <input type="radio" name="option" value =%s class='pick' />
                    <label for=%s class='fick'>%s</label>
                    <input type="radio" name="option" value =%s class='pick' checked />
                    <label for=%s class='fick'>%s</label>
                    <input type="radio" name="option" value =%s class='pick'/>
                    <label for= %s class='fick'>%s</label> 
                    <input type="submit" class = "start" value="Yes!" />
                    <button type="button" class = "start">50/50</button>
                </fieldset>
            <p id = hidden> %s</p>
            """ % (value, data['Questions'],data['Option_A'],data['Option_A'],data['Option_A'], data['Option_B'], data['Option_B'],data['Option_B'], data['Option_C'], data['Option_C'] ,data['Option_C'], data['Option_D'],data['Option_D'], data['Option_D'],correct)



if len(form_data) != 0:
    try:
        connection = db.connect('cs1.ucc.ie', 'ncm1', 'oosha', 'cs1021_cs5021_ncm1')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT  Questions, Option_A, Option_B, Option_C, Option_D, Answer FROM Game """) 
    
        counter = counter -1
        data = cursor.fetchall()[counter]
        correct = data["Answer"]
        choice = form_data.getfirst("option")
        



        if counter == 20:
            prize = value - 50000
            result = """<strong> Congratulations! You won the game! You are now a digital millionaire!</strong>
            <p> Your total prize money is <b> $%s </b> </p> 
            <br>
            <p> <a  class ='start' href = 'index.py'> Play again? </a> </p>
            """ % (prize)
        
        
        elif choice in correct:
            
            connection = db.connect('cs1.ucc.ie', 'ncm1', 'oosha', 'cs1021_cs5021_ncm1')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT  Questions, Option_A, Option_B, Option_C, Option_D, Answer FROM Game """) 
            counter = counter + 1
            data = cursor.fetchall()[counter]
            correct = data["Answer"]

            result = """
            <p> That was Correct! Congratulations! Here is the Next Question: <br>
            <h1>  This question is for $%s </h1>
            <br><br>
            <p> %s</p>

            
            <form action ='game.py' method = 'get'>
                <fieldset>
                    <input type="radio" name="option" value = %s class='pick' />
                    <label for=%s class='fick'>%s</label>
                    <input type="radio" name="option" value =%s class='pick' />
                    <label for=%s class='fick'>%s</label>
                    <input type="radio" name="option" value =%s class='pick' checked />
                    <label for=%s class='fick'>%s</label>
                    <input type="radio" name="option" value =%s class='pick'/>
                    <label for= %s class='fick'>%s</label> 
                    <input type="submit" value="Yes!" class = "start" />
                    <button type="button"  class = "start">50/50 </button>
                </fieldset>
                <p id = hidden> %s</p>

            """ % (value, data['Questions'],data['Option_A'],data['Option_A'],data['Option_A'], data['Option_B'], data['Option_B'],data['Option_B'], data['Option_C'], data['Option_C'] ,data['Option_C'], data['Option_D'],data['Option_D'], data['Option_D'],correct)
            
            
        else:
            result = """
            <strong> I'm sorry that was not the answer I was expecting </strong>
            <p> The correct answer is <em> %s </em> </p>
            <p> Your total prize money is <b> $%s </b> </p> 
            <br>
            <p> <a  class = 'start' href = 'index.py'> Play again? </a> </p>

            """ % (correct, prize)
            
            

        cursor.close()
        connection.close()


    except:
        result = "Sorry we are experienching technical difficulties"


        
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Millionaire!</title>
        <link rel="stylesheet" href="styles.css"/>
        <script src = "game.js" type = "module"> </script>
    </head>
    <body>
        <h1>Who wants to be a Millionaire?</h1>
            <p>Do you have what it takes?</p>
        <Section id = 'game' >
           
            %s
                
        </Section>
    </body>
</html>

""" % (result))

