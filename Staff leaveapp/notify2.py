import cgi
import datetime
import os
from http.cookies import *
import sqlite3
try:
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
    print("Content-Type:text/html\n\n")
    form=cgi.FieldStorage()
    con=sqlite3.connect("F:\Tom\staffapp.db")
    cur=con.cursor()
    cur.execute('select * from leave_tab where id='+str(id)+' and approv=3')
    data=cur.fetchall()
    cur.execute('select name from staff_det where id='+str(id))
    name=cur.fetchone()
    hh='''
       <html>
       <head>
            <link rel="icon" href="../favicon.ico" type="image/x-icon">
       <table bgcolor="black" width="100%">
           <tr>
             <td><img src="../logo.jpg" width="148" height="130"/></td>
             <td><img src="../clg4.jpg" width="1187" height="130"/></td>
           </tr>
        </table>
        <link rel="stylesheet" type="text/css" href="../style.css"/>
       <title>Notifications</title>
       </head>
       <body>
       <form>
        <table width="100%" bgcolor="lightyellow">
           <tr>
           <td align="left" style="font-size:16px;font-family:verdana;font-weight:bold;color:red;"><i><b>Welcome, '''+str(name[0])+'''</b></i></td>
           <td align="right"><a href="stafflogin.py" style="text-decoration:none;">
           <input type="button" name="logout" style="font-size:16px;font-family:verdana;font-weight:bold;color:green;border-color:green;background-color:lightyellow;" value="Logout"/></a></td>
           </td></tr>
</table><br>
       </form>
       <form>
       <table bgcolor="f7f5fe" align="center" border="0" width="80%">
         <caption><h3>NOTIFICATIONS</h3></caption>
         <tr><b>
           <td align="center" class="zero"><h4>Appplied Date</h4></td>
           <td align="center" class="zero"><h4>Type</h4></td>
           <td align="center" class="zero"><h4>From Date</h4></td>
           <td align="center" class="zero"><h4>To Date</h4></td>
           <td align="center" class="zero"><h4>No. of days</h4></td>
           <td align="center" class="zero"><h4>Reason</h4></td>
           </b>
           </tr>       
'''
    for i in data:
        h=i[3].split('-')
        g=i[4].split('-')
        a=datetime.date(int(h[0]),int(h[1]),int(h[2]))
        b=datetime.date(int(g[0]),int(g[1]),int(g[2]))
        c=b-a
        day=int(c.days)+1
        h1='''
        <tr>
           <td align="center" class="one">'''+str(i[1])+'''</td>
           <td align="center" class="two">'''+str(i[2])+'''</td>
           <td align="center" class="one">'''+str(i[3])+'''</td>
           <td align="center" class="two">'''+str(i[4])+'''</td>
           <td align="center" class="one">'''+str(day)+'''</td>
           <td align="center" class="two">'''+str(i[6])+'''</td>
        </tr>
'''
        hh=hh+h1
    cur.execute('select ldays from staff_det where id='+str(id))
    f=cur.fetchall()
    f1=f[0]
    ht='''
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td align="center" style="font-size:16px;font-family:verdana;font-weight:bold;"><b>Total leaves taken:</b></td>
        <td align="center" style="font-size:16px;font-family:verdana;font-weight:bold;"><b>'''+str(f1[0])+'''</b></td>
    </tr>'''
    if f1[0]>15:
        ht7='''
          <tr></b>
             <td><b>You have already taken   '''+str(f1[0]-15)+''' unpaid leaves</b></td>
          </tr>'''
        ht=ht+ht7
        
    hy='''</table>
    </form>
    </body>
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
    hf=hh+ht+hy
    print(hf.format(**locals()))

except Exception as e:
    print(e)

