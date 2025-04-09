import sqlite3

class AbstractController:
    def __init__(self):
        self.db_path = "src/datas/neozyth.sqlite"
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establish a connection to the database."""
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_path)

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str, params: tuple = ()):
        """Execute a SQL query and return the result."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        self.close()
        return result

    def execute_insert(self, query: str, params: tuple = ()):
        """Execute an INSERT SQL query."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        inserted_id = cursor.lastrowid
        self.connection.commit()
        self.close()
        return inserted_id

    def execute_delete(self, query: str, params: tuple = ()):
        """Execute a DELETE SQL query."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        self.close()
    
    def execute_update(self, query: str, params: tuple = ()):
        """Execute an UPDATE SQL query."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        self.close()
        return cursor.rowcount