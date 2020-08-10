import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()
print("hello ")
a = {
"malli" : "Malli2010!",
"nesh" : "1234",
"sharon": "sharon2008"
}
complete = False
user = {"malli" : "Malli2010", "nesh" : "1234" }
while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        print("Password is not valid for username.")
        continue
    elif password == user[username]:
        print("Welcome username ")
        print("Thank you for logging on. ")
        complete = True
    def table():
        c.execute('CREATE TABLE IF NOT EXISTS books(name TEXT, book TEXT)')
    table()
    def categoris():
        print("these are the categorys we have")
        print(
            '''
            a.science
            b.Gamming
            ''')
        d  = input("chose the caetegories you want:  ")
        def logic():
            if d == "a":
                print("you have chosen science")
                print("these are the books we have:")
                print('''
                1.spotlight science
                2.primary science
                ''')
                e = input("chose the book you want?:")
                c.execute("INSERT INTO books(name, book) VALUES(?,?)",(username, e))
                print("do you want to borrow another book:  ")
                s = input(" yes(y) or no(n): ")
                if s == "y":
                    categoris()
                elif s == "n":
                    print("Make shure that you return the book or books in two weeks time.")
                    print("Thank you for visiting my library. good bye")
            elif d == "b":
                print("you have chosen gamming")
                print("choose the book you want")
                print('''
                1.secrents of mincraft
                2.how to win a batle royal in fortnght
                ''')
                v = input ("chose the book you want?: ")
                c.execute("INSERT INTO books(name, book) VALUES(?,?)",(username,v ))
                z = input("do you want to borrow another book:  ")
                if z == "y":
                    categoris()
                elif z == "n":
                    print("Make shure that you return the book " )
                    print("Thankyou for visiting my library good bye")
        logic()
categoris()