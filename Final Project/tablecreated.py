from estd_connection import estd_connection

cursor=estd_connection()


sql="""
CREATE TABLE DtaEntryForm(
    FNAME CHAR(20),
    LNAME CHAR(20),
    Title CHAR(20),
    AGE INT,
    Nationality CHAR(20),
    CC INT,
    SEM INT,
    RS CHAR(20)
)"""



cursor.execute(sql)
print("table has been made")