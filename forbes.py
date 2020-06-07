#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

result = """
    <p>You do not have permission to access this page.</p>
    <br>
    <a class = "start" href="register.py">Register</a>
    <a class = "start" href="login.py">Login</a>"""
   
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                connection = db.connect('cs1.ucc.ie', 'ncm1', 'oosha', 'cs1021_cs5021_ncm1')
                cursor = connection.cursor(db.cursors.DictCursor)
                cursor.execute("""INSERT INTO forbes VALUES (%s, %s) """,  (session_store.get('username'),cookie['prize'])



                cursor.close()
    


                cursor = connection.cursor(db.cursors.DictCursor)
                cursor.execute("""SELECT username, prize
                      FROM forbes
                      ORDER BY prize ASC""")

                result = '<table><tr><th>Username</th><th>Total Prize</th></tr>'
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%i</td></tr>' % (row['candidate_name'], row['total_votes'])
                    result += '</table>'
                        
                cursor.close()
                connection.close()
                        
                <a class = "start" href="logout.py">Logout</a>
            
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Forbes</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            %s
        </body>
    </html>""" % (result))