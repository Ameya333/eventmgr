import pymysql
from prettytable import from_db_cursor
import os
from shutil import copyfile

MYSQL_ADDON_DB = "bxfieozbungipzbksce7"
MYSQL_ADDON_HOST = "bxfieozbungipzbksce7-mysql.services.clever-cloud.com"
MYSQL_ADDON_PASSWORD = "xilnzWtvpgu38mrnlVT4"
MYSQL_ADDON_PORT="3306"
MYSQL_ADDON_URI="mysql://u3gdskoedahyixt4:xilnzWtvpgu38mrnlVT4@bxfieozbungipzbksce7-mysql.services.clever-cloud.com:3306/bxfieozbungipzbksce7"
MYSQL_ADDON_USER="u3gdskoedahyixt4"
MYSQL_ADDON_VERSION="8.0"


db = pymysql.connect(MYSQL_ADDON_HOST,MYSQL_ADDON_USER,MYSQL_ADDON_PASSWORD, MYSQL_ADDON_DB)

print (db)

mycursor = db.cursor()
mycursor.execute("SELECT sum( price ) FROM BudgetInfo")
rows = mycursor.fetchall()

print (rows[00][0])

db.commit()

def fileCopy():
    if os.path.exists("budgetcopy.html"):

        os.remove("budgetcopy.html")

        print("File deleted !")

    else:

        print("File does not exist !")

    copyfile('templates/budget.html', 'templates/budgetcopy.html')



def budge():



    if myresult > rows:
        dest1 = open("templates/budgetcopy.html", "a")
        dest1.write("<br><br><h3>You are below the budget</h3>")
        dest1.close()

    elif myresult == rows:
        dest2 = open("templates/budgetcopy.html", "a")
        dest2.write("<br><br><h3>Careful, you are right at the budget</h3>")
        dest2.close()
    
    else:
        dest3 = open("templates/budgetcopy.html", "a")
        dest3.write("<br><br><h3>You are above the budget</h3>")
        dest3.close()

#sql = "TRUNCATE TABLE BudgetInfo "
#mycursor.execute(sql)
#db.commit()
#print(totPrice)



from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


#mycursor.execute("""
		#CREATE TABLE BudgetInfo (
			#expense_name nvarchar(50),
			#price int
			#)
               #""")
#db.commit()

sql = "INSERT INTO BudgetInfo (expense_name, price) VALUES (%s,%s)"
mycursor.execute("SELECT Budget FROM EventInfo")
myresult = mycursor.fetchone()
db.commit()
print(myresult)

mycursor.execute("SELECT * FROM BudgetInfo")
budgTable = from_db_cursor(mycursor)
htmlCode = budgTable.get_html_string(attributes={"class":"table"}, format=True, border=False, padding_width=5 )

fileCopy()

f = open("templates/budgetcopy.html", "a")
f.write(htmlCode)
f.close()

css = open("templates/budgetcopy.html", "a")
css.write("""
     <style> 
     body{
        background-color: #D1ECF7;
        text-align: center;           
        font-family: Gill Sans, serif;
       }
     input {   
                 width: 50%;   
                 padding: 12px 20px;   
                 margin: 8px 0;   
                 box-sizing: border-box;   
                 border: none;   
                 border-bottom: 2px solid black;   
                 background-color: #D1ECF7; 
                 font-size: 20px;  
             }   
     }
      .table{
           font-family: Gill Sans, serif;       
                
      }     
      th{     
            font-size: 20px;     
            padding-bottom: 1.5em;     
      }     
      td{     
            font-size: 18px;     
            padding-bottom: 0.8em;     
      }     
        .move {     
                    box-shadow:inset 0px 34px 0px -15px #366b73;     
                    background:linear-gradient(to bottom, #366b73 5%, #68a4ad 100%);     
                    background-color:#366b73;     
                    border: none;     
                    display:inline-block;     
                    cursor:pointer;     
                    color:#ffffff;     
                    font-family:Arial;     
                    font-size:15px;     
                    font-weight:bold;     
                    padding:9px 23px;     
                    text-decoration:none;     
                    text-shadow:0px -1px 0px #3d768a;     
                    width:8%;     
                }     
                .move:hover {  
                    background:linear-gradient(to bottom, #68a4ad 5%, #366b73 100%);  
                    background-color:#68a4ad;  
                }  
                .move:active {  
                    position:relative;  
                    top:1px;  
                }  
             </style>""")
css.close()
budge()


@app.route('/', methods =["GET", "POST"])
def budget():
    if request.method == "POST":
        bName = request.form.get("expname")
        bNum = request.form.get("expense")
        bVal = (bName, bNum)
        mycursor.execute(sql, bVal)
        db.commit()

    return render_template("budgetcopy.html")



if __name__ == "__main__":
    app.run()



