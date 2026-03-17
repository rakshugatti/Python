from abc import ABC, abstractmethod

# Abstract class
class DatabaseConnector(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def fetch_results(self):
        pass

    @abstractmethod
    def close(self):
        pass

    # Template Method
    def run_query(self, query):
        self.connect()
        self.execute_query(query)
        results = self.fetch_results()
        self.close()
        return results


# MySQL implementation
class MySQLConnector(DatabaseConnector):

    def connect(self):
        print("Connected to MySQL Database")

    def execute_query(self, query):
        print(f"Executing MySQL Query: {query}")

    def fetch_results(self):
        return ["MySQL Result 1", "MySQL Result 2"]

    def close(self):
        print("MySQL Connection Closed")


# MongoDB implementation
class MongoConnector(DatabaseConnector):

    def connect(self):
        print("Connected to MongoDB")

    def execute_query(self, query):
        print(f"Executing MongoDB Query: {query}")

    def fetch_results(self):
        return ["MongoDB Document 1", "MongoDB Document 2"]

    def close(self):
        print("MongoDB Connection Closed")


# Usage
mysql = MySQLConnector()
result1 = mysql.run_query("SELECT * FROM users")
print("MySQL Results:", result1)

print("----------------------")

mongo = MongoConnector()
result2 = mongo.run_query("db.users.find()")
print("MongoDB Results:", result2)