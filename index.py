#!/usr/local/bin/python3                
from cgitb import enable
enable()
from os import environ
from http.cookies import SimpleCookie
cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')

if http_cookie_header:
    cookie['played'] = 0
    cookie['prize'] = 0


else:
    cookie.load(http_cookie_header)
    if 'played'  in cookie:
        cookie['played'] = 0
    if 'prize' in cookie:
        cookie['prize'] = 0


print(cookie)

from cgi import FieldStorage

print('Content-Type: text/html')
print()

print("""
<!DOCTYPE html>
<html lang="en" id = "index">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Millions!</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>

        <figure>
            <img src= "millionaire.png" alt="A Millionaire wallpaper"/>
                
        </figure>

        <nav>
            <ul>
                <li> <a class="start" href = "game.py">Start</a> </li>
                <li> <a class="start" href = "rules.html">Rules</a></li>
                <li> <a class="start" href = "login.py">Login</a> </a></li>
                <li> <a class="start" href = "register.py">Register</a> </li>
                
            </ul>
        </nav>


        
                
        
        
    </body>
</html>""")