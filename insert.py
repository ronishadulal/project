from estd_connection import estd_connection


def create():
    cursor = estd_connection()
    id = input("Enter the id of student ")
    name = input("Enter name of the student ")
    dept = input("Enter the department ")
    sql = f"""
        INSERT INTO STUDENT(ID, NAME, DEPARTMENT)
        VALUES ('{id}', '{name}', '{dept}')
        """
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    cursor.execute(sql)
    return cont.lower() == 'y'




