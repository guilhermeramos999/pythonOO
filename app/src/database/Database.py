import mysql.connector


class Database():
    @staticmethod
    def connection():
        return mysql.connector.connect(
            host="localhost",
            user="admin",
            database="pythonproject"
        )

    @staticmethod
    def findOneBy(model, where):
        connection = Database.connection()
        cursor = connection.cursor()

        sql = "SELECT * FROM " + model + " WHERE " + " AND ".join(where)
        print(sql)

        cursor.execute(sql)
        return cursor.fetchone()

    @staticmethod
    def findAll(model):
        connection = Database.connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM " + model)
        return cursor.fetchall()

    @staticmethod
    def create(model, data):
        connection = Database.connection()
        cursor = connection.cursor()

        columns = Database.getColumns(model)

        fields = []

        for column in columns:
            fields.append('%s')

        sql = "INSERT INTO " + model + \
            "(" + ",".join(columns) + ") VALUES ("+",".join(fields)+");"

        cursor.execute(sql, data)
        connection.commit()

    @staticmethod
    def update(model, dataChanges, where):
        connection = Database.connection()
        cursor = connection.cursor()

        sql = "UPDATE " + model + " SET " +\
            ",".join(dataChanges) + " WHERE " + " AND ".join(where)
        print(sql)

        cursor.execute(sql)

        connection.commit()

    @staticmethod
    def remove(model, where):
        connection = Database.connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM " + model +
                       " WHERE " + " AND ".join(where))
        connection.commit()

    @staticmethod
    def getColumns(model):
        connection = Database.connection()
        cursor = connection.cursor()
        cursor.execute("SHOW COLUMNS FROM " + model)

        columns = cursor.fetchall()

        dtoColumn = []

        for column in columns:
            if (column[0] != 'id'):
                dtoColumn.append(column[0])

        return dtoColumn
