from estd_connection import estd_connection


def update(id, to_change, value):
    cursor = estd_connection()
    sql = f"""
    UPDATE STUDENT SET {to_change.upper()}='{value}' WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been updated. Do you want to continue? (y/n)")
    return cont.lower() == 'y'
