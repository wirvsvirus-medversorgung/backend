from persistence.DBController import DBController

__author__='Marc, Hendrik'
__status__='DEV'

def testDB():
    controller = DBController("sqlite3")
    controller.test_db()


testDB()
