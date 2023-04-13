from flask_app.config.mysqlconnection import connectToMySQL # assuming connection file is called mysqlconnection.py

class Dojo: # replace with name of class (table name)
    DB = "dojos_and_ninjas_schema" # replace with name of schema
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;" # change all mentions of 'dojos' to table name
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for i in results:
            dojos.append( cls(i) )
        return dojos
    # class method to save our friend to the database

    @classmethod
    def save(cls, data ): 
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        result = connectToMySQL(cls.DB).query_db( query, data )
        return result

    @classmethod
    def get_one(cls, dojo_id):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        data = {'id':dojo_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls, dojo_id):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        data = {"id": dojo_id}
        return connectToMySQL(cls.DB).query_db(query,data)