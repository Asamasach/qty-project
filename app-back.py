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
            my_sql_select_total = """ SELECT max(total) FROM khoytotal WHERE date_stamp LIKE %s AND CID=18;"""
            t1=str(datetime.now()-timedelta(days=i))[0:10]
            records_to_get = [(t1+'%')]
            cursor.execute(my_sql_select_total, records_to_get)
            result=cursor.fetchall()
            if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
                result_day_out=0
            else:
                result_day_out=int((str(result).split('(')[1]).split(',')[0])//6
            result_total=result_total+result_day_out
    return render_template('index.html', qty_total=result_total)


@app.route('/mon')
def result_day_out(qty_day=None):

    connection = mysql.connector.connect(host='172.20.0.55', database='khoytotal', user='root', password='')
    if connection.is_connected():
        cursor=connection.cursor()
        my_sql_select_query_other = """ SELECT max(total) FROM khoytotal WHERE date_stamp LIKE %s AND CID=18;"""
        my_sql_select_query_out = """ SELECT max(quantity) FROM khoytotal WHERE date_stamp LIKE %s AND CID=18 ;"""
        my_sql_select_query_in = """ SELECT max(quantity) FROM khoytotal WHERE date_stamp LIKE %s AND CID=60 ;"""
        t1=str(datetime.now())[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_day_out=0
        else:
            result_day_out=int((str(result).split('(')[1]).split(',')[0])

        print(datetime.now())

        t1=str(datetime.now()-timedelta(days=1))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_yesterday_out=0
        else:
            result_yesterday_out=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=2))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_theotherday_out=0
        else:
            result_theotherday_out=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=3))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_3ago_out=0
        else:
            result_3ago_out=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=4))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_4ago_out=0
        else:
            result_4ago_out=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=5))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_5ago_out=0
        else:
            result_5ago_out=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=6))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_6ago_out=0
        else:
            result_6ago_out=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now())[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_day_in=0
        else:
            result_day_in=int((str(result).split('(')[1]).split(',')[0])

        print(datetime.now())

        t1=str(datetime.now()-timedelta(days=1))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_yesterday_in=0
        else:
            result_yesterday_in=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=2))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_theotherday_in=0
        else:
            result_theotherday_in=int((str(result).split('(')[1]).split(',')[0])

        t1=str(datetime.now()-timedelta(days=3))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_3ago_in=0
        else:
            result_3ago_in=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=4))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_4ago_in=0
        else:
            result_4ago_in=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=5))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_5ago_in=0
        else:
            result_5ago_in=int((str(result).split('(')[1]).split(',')[0])
    
        t1=str(datetime.now()-timedelta(days=6))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_in, records_to_get)
        result=cursor.fetchall()
        if (((str(result).split('(')[1]).split(',')[0])=="None" or  ((str(result).split('(')[1]).split(',')[0])==""):
            result_6ago_in=0
        else:
            result_6ago_in=int((str(result).split('(')[1]).split(',')[0])




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
    return render_template('index1.html', qty_day_out=result_day_out ,qty_yesterday_out=result_yesterday_out,qty_theotherday_out=result_theotherday_out, qty_3ago_out=result_3ago_out, qty_4ago_out=result_4ago_out, qty_5ago_out=result_5ago_out, qty_6ago_out=result_6ago_out, qty_day_in=result_day_in ,qty_yesterday_in=result_yesterday_in,qty_theotherday_in=result_theotherday_in, qty_3ago_in=result_3ago_in, qty_4ago_in=result_4ago_in, qty_5ago_in=result_5ago_in, qty_6ago_in=result_6ago_in)

@app.route('/day')
def result_today(qty_today=None):

    connection = mysql.connector.connect(host='172.20.0.55', database='khoytotal', user='root', password='')
    if connection.is_connected():
        cursor=connection.cursor()
        my_sql_select_query_out = """ SELECT max(quantity) FROM khoytotal WHERE date_stamp LIKE %s AND CID=18;"""

        t1=str(datetime.now())[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if ((str(result).split('(')[1]).split(',')[0])=="None":
            result_today="0"
        else:
            result_today=str(int((str(result).split('(')[1]).split(',')[0])//6)

        t1=str(datetime.now()-timedelta(days=1))[0:10]
        records_to_get = [(t1+'%')]
        print(records_to_get)
        cursor.execute(my_sql_select_query_out, records_to_get)
        result=cursor.fetchall()
        if ((str(result).split('(')[1]).split(',')[0])=="None":
            result_yesterday="0"
        else:
            result_yesterday=str(int((str(result).split('(')[1]).split(',')[0])//6)


    return render_template('index2.html', qty_today=result_today,qty_yesterday=result_yesterday)



if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
