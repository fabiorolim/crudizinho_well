import sqlite3


def execute_(query):
    db_path = 'produtos.db'
    connetion = sqlite3.connect(db_path)
    cursor = connetion.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connetion.commit()
    except Exception as error:
        print(error)

    return result
