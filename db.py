import mysql.connector

def data(title):
    mydb = mysql.connector.connect(
    host="Host URL",
    user="Username",
    password="Password",
    database="Database Name"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM books WHERE title REGEXP %s"
    mycursor.execute(sql,['^'+title])
    a=mycursor.fetchall()
    data=[]
    for i in a:
        author=mycursor.execute("SELECT name FROM authors WHERE author_id=%s",[str(i[6])])
        author=mycursor.fetchall()

        data.append({
            'title': i[1],
            'pages': i[2],
            'publish_date': i[3],
            'rating': i[4],
            'price': i[5],
            'author': author[0][0],
        })
    return data
