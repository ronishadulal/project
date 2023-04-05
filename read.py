from estd_connection import estd_connection


def read(id):
    cursor = estd_connection()
    sql = f"""
    SELECT * FROM STUDENT WHERE ID='{id}'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cont = input("Do you want to continue? (y/n)")
    return cont.lower() == 'y'


