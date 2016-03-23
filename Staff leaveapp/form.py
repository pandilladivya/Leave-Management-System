import cgi
import sqlite3
import datetime
import os
from http.cookies import *
from datetime import timedelta, date
#http://localhost:8080/test/cgi-bin/form.py
try:
    global con
    global cur
    con=sqlite3.connect("F:\Tom\staffapp.db")
    cur=con.cursor()
    global ht1
    global ht3
    global id
    global id1
    global type
    global dt
    global fd
    global td
    global approv
    global reason
    fd=''
    td=''

    if 'HTTP_COOKIE' in os.environ:
         cookie_string=os.environ.get('HTTP_COOKIE')
         ck=SimpleCookie()
         ck.load(cookie_string)
         if 'username' in cookie_string:
            id=ck['username'].value
         else:
            id="Nil"
    else:
        id="None"

    form=cgi.FieldStorage()
    print("Content-Type:text/html\n\n")

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def insert():
        global dis
        cur.execute('select role from staff_det where id='+str(id))
        role=cur.fetchone()[0]
        approv=0
        if role=="co-ord":
            approv=1
        cur.execute('insert into leave_tab values(?,?,?,?,?,?,?,?,?,?)',(id,dt,type,fd,td,approv,reason,0,0,0))
        #cur.execute('delete from storage')
        con.commit()
        ht='''
                <html>
                    <body onload="window.location='http://localhost:8080/test/cgi-bin/form2.py'"></body>
                </html>
            '''
        print(ht)

    ht1='''
                    <html>
                     <head>
            <link rel="icon" href="../favicon.ico" type="image/x-icon">
                        <link rel="stylesheet" type="text/css" href="../style.css" />
                        <title>Leave Form</title>
                        <table width="100%" bgcolor="black">
                         <tr>
                            <td width="10%"><img src="../logo.jpg" alt="img" height="130" width="148" ></td>
                            <td width="90%"><img src="../clg4.jpg" alt="img" height="130" width="1170" ></td>
                        </tr>
                     </table>
                     </head>
                     <body>
                     <table width="100%" bgcolor="lightyellow">
           <tr>
           <td align="left" width="25%" style="font-size:16px;font-family:verdana;font-weight:bold;"><a href="notify2.py" style="text-decoration:none">Get my leave details&emsp;</a></td>
           <td align="right" width="35%" ><a href="stafflogin.py" style="text-decoration:none">
           <input type="submit" name="logout" style="font-size:16px;font-family:verdana;font-weight:bold;color:green;border-color:green;background-color:lightyellow;" value="Logout"/></a></td>
           </tr>
                     </table>
                     <form method="POST">
                     <br><br>
                     <table  align="Center" class="lf1">
                     <tr>
                       <td><b>&nbsp;Id:</b></td>
                       <td>{id}</td>
                     </tr>
                     <tr>
                       <td><b>&nbsp;Date:</b></td>
                        <td>From:&nbsp;<input type="date" name="fromdt"  name="fromdt" required name="fromdt" placeholder="From date" /></td>
                     </tr>
                         <td></td>
                         <td>To:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="date" name="todt" required name="todt" name="todt" placeholder="To date" /></td>
                     <tr>
                       <td><b>&nbsp;Type of Leave:</b></td>
                       <td><input type="radio" name="type" required name="type" value="sick" />Sick
                       <input type="radio" name="type" reqired name="type" value="normal" />Normal</td>
                     </tr>
                     <tr>
            <td><b>&nbsp;Reason:</b></td>
            <td><pre><textarea maxlength="100" name="r"   name="r" rows="3" cols="35" placeholder="Enter reason (max. characters = 100)"></textarea>&emsp;</pre></td>
        </tr>
        <tr><td>&nbsp;
        I confirm the details&nbsp;</td><td><input type="checkbox" name="agree" required name="agree">Yes
        </td></tr>
        <tr><td></td><td>&nbsp;<input style="font-size:15px;" type="submit" name="submit" value="Get Substitution Form" /></td></tr>
    </table>
        </form>
        </body>
        <table height="15%">
            <tr height="15%"></tr>
        </table>
      <footer>
            <table style="width:100%;" align="center">
                <tr>
                    <td style="width:33%;text-align:center;font-size:18px;">3-5-1026, Narayanguda, Hyderabad, Telangana -500029</td>
                    <td style="width:33%;text-align:center;font-size:18px;">&emsp;&emsp;&emsp;Copyright &#169; KMIT</td>
                    <td style="width:33%;text-align:center;font-size:18px;">&emsp;&emsp;&emsp;Website:    <a href="http://www.kmit.in/" style="text-decoration:none"/>kmit.in</td>
                </tr>
            </table>
        </footer>
    </html>
    '''
    
    print(ht1.format(**locals()))
    
    if "submit" in form:
         #id1=int(form.getvalue('id',0))
         dt=str(datetime.date.today())
         type=form.getvalue('type')
         fd=form.getvalue('fromdt')
         td=form.getvalue('todt')
         reason=str(form.getvalue('r'))
         approv=0
         insert()

except Exception as e:
     print(e)

