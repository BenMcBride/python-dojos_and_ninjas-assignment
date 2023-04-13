from flask_app.config.mysqlconnection import connectToMySQL # assuming connection file is called mysqlconnection.py

class Ninja: # replace with name of class (table name)
    DB = "dojos_and_ninjas_schema" # replace with name of schema
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, dojo_id):
        query = f"SELECT * FROM ninjas WHERE dojo_id = {dojo_id};"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for i in results:
            ninjas.append( cls(i) )
        return ninjas
    # class method to save our friend to the database

    @classmethod
    def save(cls, data): 
        query = "INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id ) VALUES ( %(fname)s , %(lname)s , %(age)s , NOW() , NOW(), %(dojo_id)s );"
        result = connectToMySQL(cls.DB).query_db( query, data )
        return result

    @classmethod
    def get_one(cls, ninja_id):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        data = {'id':ninja_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(fname)s,last_name=%(lname)s,age=%(age)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls, ninja_id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        return connectToMySQL(cls.DB).query_db(query,data)