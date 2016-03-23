import cgi
import sqlite3
import datetime
import os
from http.cookies import *
from datetime import timedelta
#http://localhost:8080/test/cgi-bin/form2.py
try:
    global con
    global cur
    global td
    global fd
    global dep
    global dt
    global ht4
    global ht3
    global ht2
    global ht1
    global hsel
    global cse
    global ece
    global eie
    global it
    con=sqlite3.connect("F:\Tom\staffapp.db")
    cur=con.cursor()
    

    form=cgi.FieldStorage()
    print('Content-Type:text/html\n\n')
    
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
    
    cur.execute('select * from leave_tab where id='+str(id))
    data=cur.fetchall()
    ex=data[-1]

    s=str(ex[3]).split('-')
    fd=datetime.date(int(s[0]),int(s[1]),int(s[2]))
    s=str(ex[4]).split('-')
    td=datetime.date(int(s[0]),int(s[1]),int(s[2]))
    
    dt=str(fd.strftime("%d-%m-%Y"))
    htf=''

    cse='''
        <option selected>CSE</option>
        <option>IT</option>
        <option>ECE</option>
        <option>EIE</option></select></td>
    '''
    ece='''
        <option>CSE</option>
        <option>IT</option>
        <option selected>ECE</option>
        <option>EIE</option></select></td>
    '''
    it='''
        <option>CSE</option>
        <option selected>IT</option>
        <option>ECE</option>
        <option>EIE</option></select></td>
    '''
    eie='''
        <option>CSE</option>
        <option>IT</option>
        <option>ECE</option>
        <option selected>EIE</option></select></td>
    '''
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def fill_d():
        global ht4
        ht4='''
        <td>
            <select name="dropdown">
            <option>Date</option>
        '''
        for single_date in daterange(fd,td+timedelta(1)):
            ht4=ht4+'''<option>'''+single_date.strftime("%d-%m-%Y")+'''</option>'''
        ht4=ht4+'''</select></td>'''
        return ht4

    ht1='''
    <html>
        <head>
            <link rel="icon" href="../favicon.ico" type="image/x-icon">
            <link rel="stylesheet" type="text/css" href="../style.css" />
            <title>Substitution Form</title>
            <table width="100%" bgcolor="black" width="100%">
                <tr>
                    <td width="10%"><img src="../logo.jpg" alt="img" height="130" width="148" ></td>
                    <td width="90%"><img src="../clg4.jpg" alt="img" height="130" width="1187" ></td>
                </tr>
            </table>
        </head>
            <body>
            <table width="100%" bgcolor="lightyellow">
            <tr>
                <td>&emsp;<a href="notify.py" style="text-decoration:none">Get my leave details</td>
                <td align="right"><a href="form.py"><button>Done</button></a>&emsp;</td>
            </tr>
            </table>
            <form method="POST">
                     <br><br>
                     <table  align="Center" class="lf1" bgcolor="black">
                    <tr>
                        <td><b>&nbsp;Id:</b></td>
                        <td>'''+str(id)+'''</td>
                    </tr>
                    <tr>
                        <td><b>&nbsp;Date:</b></td>
                        <td>From:&nbsp;'''+str(fd.strftime("%d-%m-%Y"))+'''</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>To:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(td.strftime("%d-%m-%Y"))+'''</td>
                    </tr>
                    <tr>
                        <td><b>&nbsp;Type of Leave:</b></td>
                        <td>'''+str(ex[2]).capitalize()+'''</td>
                        <td></td>
                    </tr>
                </table>
                <br><br>
                <table height="10%" align="center">
                    <tr height="10%">
                        <td style="font-family:tahoma;font-size:20px;">Substitution Form</td>
                    </tr>
                </table>
        <table align="center" border="0" class="lf1">
            <tr>
                <td><b>Substitutee's</td>
                <td><b>Department&nbsp;</td>
            </tr>
            <tr>
                <td><select name="ddep">
        '''
    hsel='''
    <td><input type="submit" name="sub" value="Select" /></td>
    '''
    def check():
        global ht1
        global cse
        global ece
        global eie
        global it
        global hsel
        #print(ht1.format(**locals()))
        dep=str(form.getvalue('ddep'))
        #print(dep)
        if dep!='ECE' and dep!='EIE' and dep!='IT':
            ht1=ht1+cse+hsel
        if dep=='EIE':
            ht1=ht1+eie+hsel
        if dep=='ECE':
            ht1=ht1+ece+hsel
        if dep=='IT':
            ht1=ht1+it+hsel

    def fill():
        global ht2
        cur.execute('select name from staff_det where dept="'+dep+'"')
        d=cur.fetchall()
        ht2='''
        <td><select name="dropdown">
        <option>Name</option>
        '''
        for i in d:
            a=i[0]
            ht2=ht2+'''<option>'''+str(a)+'''</option>'''
        ht2=ht2+'''</select></td>'''
        #return ht

    def gen():
        global ht3
        ht3='''
                <td><select name="dropdown">
                    <option>Year</option>
                    <option>I</option>
                    <option>II</option>
                    <option>III</option>
                    <option>IV</option>
                </select></td>
                <td><select name="dropdown">
                    <option>Branch</option>
                    <option>CSE</option>
                    <option>ECE</option>
                    <option>EIE</option>
                    <option>IT</option>
                </select></td>
                <td><select name="dropdown">
                    <option>Section</option>
                    <option>A</option>
                    <option>B</option>
                    <option>C</option>
                    <option>D</option>
                    <option>E</option>
                    <option>F</option>
                    <option>G</option>
                </select></td>
                <td><select name="dropdown">
                    <option>Period</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>
                    <option>6</option>
                    <option>7</option>
                </select></td>
                <td><input type="submit" name="sub1" value="Submit" /></td>
            </tr>
            </table>
            </form>
            </body>
            </html>
        '''
        #ht3=fill()+ht3
        #print(ht4.format(**locals()))

    if "sub" in form:
        dep=str(form.getvalue('ddep'))
        gen()
        fill()
        fill_d()
        htf=ht4+ht2+ht3
    
    if "sub1" in form:
        data=form.getvalue('dropdown')
        #print(data,data[0])
        cur.execute('insert into leave_sub values(?,?,?,?,?,?)',(str(id),data[0],data[1],(data[2]+'-'+data[3]+'-'+data[4]),data[5],0))
        con.commit()

    counter=1
    check()
    print(ht1.format(**locals()))
    print(htf.format(**locals()))

except Exception as err:
    print(err)