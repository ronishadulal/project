from estd_connection import estd_connection


def delete(id):
    cursor = estd_connection()
    sql = f"""
    DELETE FROM STUDENT WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been deleted. Do you want to continue? (y/n)")
    return cont.lower() == 'y'
