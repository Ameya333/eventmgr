
import pymysql

from prettytable import from_db_cursor

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

#sql = "ALTER TABLE EventInfo MODIFY COLUMN indexNo INT auto_increment"
#db.commit()



mycursor.execute("SELECT EventName,Budget,DateAndTime,Description FROM EventInfo")
mytable = from_db_cursor(mycursor)
htmlCode = mytable.get_html_string(attributes={"name":"mytable", "class":"table"}, border=False, padding_width=5, format=True)

#def budgetcalculator():




from flask import Flask, request, url_for, redirect, render_template


app = Flask(__name__)



@app.route('/')
def main():
    htmlHead=""" 
    <LINK REL=StyleSheet HREF="main.css" TITLE="Contemporary"> 
    <script>
        //const submit = document.querySelector(".submit");
        function moove (){
            window.location.href = '/create';
        }
        function mve (){
            window.location.href = '/delet';
        }
    </script>                                        
    <h1 class= "home">Home</h1>                                
    <button class = "delete" onclick="mve()" >Delete</button>
    <button class = "create" onclick="moove()" >Create</button> 
    <br><br><br><br>
    <style>
        body {
          background-color: #D1ECF7;
        }
        .home{
            text-align: center;
           font-family: Gill Sans, serif;
        }
        .delete {
        	box-shadow:inset 0px 34px 0px -15px #366b73;
        	background:linear-gradient(to bottom, #366b73 5%, #68a4ad 100%);
        	background-color:#366b73;
        	border:1px solid #29668f;
        	display:inline-block;
        	cursor:pointer;
        	color:#ffffff;
        	font-family:Arial;
        	font-size:15px;
        	font-weight:bold;
        	padding:9px 23px;
        	text-decoration:none;
        	text-shadow:0px -1px 0px #3d768a;
        	margin-left: 80%;
        }
        .delete:hover {
        	background:linear-gradient(to bottom, #68a4ad 5%, #366b73 100%);
        	background-color:#68a4ad;
        }
        .delete:active {
        	position:relative;
        	top:1px;
        }
        .create {
        	box-shadow:inset 0px 34px 0px -15px #366b73;
        	background:linear-gradient(to bottom, #366b73 5%, #68a4ad 100%);
        	background-color:#366b73;
        	border:1px solid #29668f;
        	display:inline-block;
        	cursor:pointer;
        	color:#ffffff;
        	font-family:Arial;
        	font-size:15px;
        	font-weight:bold;
        	padding:9px 23px;
        	text-decoration:none;
        	text-shadow:0px -1px 0px #3d768a;
        }
        .create:hover {
        	background:linear-gradient(to bottom, #68a4ad 5%, #366b73 100%);
        	background-color:#68a4ad;
        }
        .create:active {
        	position:relative;
        	top:1px;
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
        
        
        
    </style>
    """
    return htmlHead+htmlCode

#<button class = "modify">Modify</button>


@app.route('/create', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        date_time = request.form.get("datetime")
        desc = request.form.get("desc")
        budget = request.form.get("budget")
        event_name = request.form.get("ename")
        val = (date_time, desc, budget, event_name)
        mycursor.execute(sql, val)
        db.commit()

    return render_template("create.html")

@app.route('/success')
def success():
    return render_template("sucess.html")

sql = "DELETE FROM EventInfo WHERE EventName = %s"
@app.route('/delet',methods = ['POST', 'GET'])
def delete():
    if request.method == "POST":
        delet = request.form.get("eventname")
        print(delet)
        sql = "INSERT INTO EventInfo (DateAndTime, Descri, Budget, EventName) VALUES (%s,%s,%s,%s)"
        mycursor.execute(sql, delet)
        mycursor.execute(sql, delet)
        db.commit()



    return render_template("delete.html")





if __name__ == "__main__":
    app.run()

