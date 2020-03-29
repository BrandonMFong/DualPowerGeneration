from django.http import HttpResponse
from django.shortcuts import render
import datetime
import mysql.connector

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

def index(request):
<<<<<<< Updated upstream
    test = "yes";
    context= {
        'test':test,
        }
    return render(request, 'DataCenter.html', context)
=======
    return HttpResponse("<h1>Testing</h1>")
>>>>>>> Stashed changes


def Query():
    try:
        cnx = mysql.connector.connect(user='dual', password='power', host='127.0.0.1', database='dualpower_datacenter')
        cursor = cnx.cursor()
        query = ("select * from client");

        cursor.execute(query);
        return str(cursor[0]);
                
    except Error as e:
        return str(e);
 
    finally:
        cursor.close()
        cnx.close()
