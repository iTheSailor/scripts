import os
def generator():
    current_directory = os.getcwd()
    def basics(location):
        my_location = os.getcwd()
        print(my_location)
        app_folders =  ['static/','config/','controllers/','models/','templates/']
        location_app = location +"/flask_app/"
        os.makedirs(location_app)
        for i in app_folders: 
            path = os.path.join(location_app, i)
            os.makedirs(path)
            if i == "static/":
                style = path + "css/"
                os.makedirs(style)
                styler = open(f"{style}style.css", "w")
                styler.write("")
                styler.close
            if i == "config/":
                config=open(f"{path}/mysqlconnection.py", "w")
                config.write("import pymysql.cursors # this is the connector we're using to connect to our db\nclass MySQLConnection:\n    def __init__(self, db):\n        # change the user and password as needed\n        connection = pymysql.connect(host = 'localhost',\n                                    user = 'root', \n                                    password = 'root', \n                                    db = db,\n                                    charset = 'utf8mb4',\n                                    cursorclass = pymysql.cursors.DictCursor,\n                                    autocommit = False)\n        # establish the connection to the database\n        self.connection = connection\n    # the method to query the database\n    def query_db(self, query:str, data:dict=None):\n        with self.connection.cursor() as cursor:\n            try:\n                query = cursor.mogrify(query, data)\n                print('Running Query:', query)\n                cursor.execute(query)\n                if query.lower().find('insert') >= 0:\n                    # INSERT queries will return the ID NUMBER of the row inserted\n                    self.connection.commit()\n                    return cursor.lastrowid\n                elif query.lower().find('select') >= 0:\n                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES\n                    result = cursor.fetchall()\n                    return result\n                else:\n                    # UPDATE and DELETE queries will return nothing\n                    self.connection.commit()\n            except Exception as e:\n                # if the query fails the method will return FALSE\n                print('!!!!!!!!!!!!!!!!!!!!!!!!!!')\n                print('Something went wrong', e)\n                print('!!!!!!!!!!!!!!!!!!!!!!!!!!')\n                return False\n            finally:\n                # close the connection\n                self.connection.close() \n# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection\ndef connectToMySQL(db):\n    return MySQLConnection(db)")
                config.close
            if i == "controllers/":
                controller=open(f"{path}/defaultcontroller.py","w")
                controller.write("from flask_app import app")
                controller.close
            if i == "models/":
                model=open(f"{path}/defaultmodel.py", "w")
                model.write("from flask_app.config.mysqlconnection import connectToMySQL")
                model.close
            if i == 'templates/':
                writer=open(f"{path}/index.html", "w")
                writer.write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>Bootstrap demo</title>\n<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">\n<link rel="stylesheet" href="/{/{ url_for("static", filename="css/style.css") /}/}"> \n</head>\n<body>\n<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous">\n</script>\n</body>\n</html>')
                writer.close
        init=open(f"{location_app}/__init__.py", "w")
        init.write("from flask import Flask\napp = Flask(__name__)\napp.secret_key = 'shhhhhh'")
        init.close
        server=open(f"{location}/server.py", "w")
        server.write("from flask_app import app\nif __name__ == '__main__':\n    app.run(debug=True)")
        server.close
        return exit_cue()
    def folder_locator():
        print(current_directory)
        directory = input("Desired flask folder name: ")
        parent_directory = input("Desired root directory (Leave blank to create in current directory): ")
        if len(parent_directory) ==  0:
            parent_directory = current_directory
        else:
            os.chdir(parent_directory)
        return user_folder_generator(directory, parent_directory)
    def exit_cue():
        print()
        input("Press enter to close this window...")
    def user_folder_generator(directory,parent_directory):
        try:
            path = os.path.join(parent_directory, directory)
            os.makedirs(path)
            print(f"{directory} was created in {parent_directory}")
            basics(directory)
            return
        except:
            print("something went wrong")
            exit_cue()
    folder_locator()
    os.chdir(current_directory)

generator()
