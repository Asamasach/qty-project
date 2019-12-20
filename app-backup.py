#!/usr/bin/python3
#======================================================================================
#---------------

from flask import Flask
from flask import render_template
from datetime import datetime, timedelta

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

a=0

app = Flask(__name__)

@app.route('/tot')
def qty(result_total=0):
    connection = mysql.connector.connect(host='172.20.0.55', database='khoytotal', user='root', password='')
    if connection.is_connected():
        for i in range(30):
            cursor=connection.cursor()
            my_sql_select_total = """ SELECT max(total) FROM khoytotal WHERE date_stamp LIKE %s;"""
            t1=str(datetime.now()-timedelta(days=i))[0:10]
            records_to_get = [(t1+'%')]
  
            cursor.execute(my_sql_select_total, records_to_get)
            result=cursor.fetchall()
            if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
                result_day=0
            else:
                result_day=int((str(result).split('(')[1]).split(',')[0])//6
            result_total=result_total+result_day
    return render_template('index.html', qty_total=result_total)


@app.route('/mon')
def result_day(qty_day=None):

    connection = mysql.connector.connect(host='172.20.0.55', database='khoytotal', user='root', password='')
    if connection.is_connected():
        cursor=connection.cursor()
        my_sql_select_query_other = """ SELECT max(total) FROM khoytotal WHERE date_stamp LIKE %s;"""
        my_sql_select_query = """ SELECT max(quantity) FROM khoytotal WHERE date_stamp LIKE %s ;"""
        t1=str(datetime.now())[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_day=0
        else:
            result_day=int((str(result).split('(')[1]).split(',')[0])

        print(datetime.now())

        t1=str(datetime.now()-timedelta(days=1))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_yesterday=0
        else:
            result_yesterday=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=2))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_theotherday=0
        else:
            result_theotherday=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=3))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_3ago=0
        else:
            result_3ago=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=4))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_4ago=0
        else:
            result_4ago=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=5))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_5ago=0
        else:
            result_5ago=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=6))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_6ago=0
        else:
            result_6ago=int((str(result).split('(')[1]).split(',')[0])



#        t1=str(datetime.now())[0:8]
#        records_to_get = [(t1+'%')]
#        print(records_to_get)
#        cursor.execute(my_sql_select_query_other, records_to_get)
#        result=cursor.fetchall()
#        result_month=(str(result).split('(')[1]).split(',')[0]

#        t1 = str(datetime.now())[0:5]
#        records_to_get = [(t1+'%')]
#        print(records_to_get)
#        cursor.execute(my_sql_select_query_other, records_to_get)
#        result=cursor.fetchall()
#        result_year=(str(result).split('(')[1]).split(',')[0]
#
    return render_template('index1.html', qty_day=result_day ,qty_yesterday=result_yesterday,qty_theotherday=result_theotherday, qty_3ago=result_3ago, qty_4ago=result_4ago, qty_5ago=result_5ago, qty_6ago=result_6ago)

@app.route('/day')
def result_today(qty_today=None):

    connection = mysql.connector.connect(host='172.20.0.55', database='khoytotal', user='root', password='')
    if connection.is_connected():
        cursor=connection.cursor()
        my_sql_select_query = """ SELECT max(quantity) FROM khoytotal WHERE date_stamp LIKE %s ;"""

        t1=str(datetime.now())[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if ((str(result).split('(')[1]).split(',')[0])=="None":
            result_today="0"
        else:
            result_today=str(int((str(result).split('(')[1]).split(',')[0])//6)

        t1=str(datetime.now()-timedelta(days=1))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query, records_to_get)
        result=cursor.fetchall()
        if ((str(result).split('(')[1]).split(',')[0])=="None":
            result_yesterday="0"
        else:
            result_yesterday=str(int((str(result).split('(')[1]).split(',')[0])//6)


    return render_template('index2.html', qty_today=result_today,qty_yesterday=result_yesterday)



if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
