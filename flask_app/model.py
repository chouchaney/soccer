import sqlite3
import os
from flask_app import data
from flask_app import ranking



def dictionary_factory(cursor, row):
  dictionary = {}
  for index in range(len(cursor.description)):
    column_name = cursor.description[index][0]
    dictionary[column_name] = row[index]
  return dictionary

def connect(database = "database.sqlite"):
  connection = sqlite3.connect(database)
  connection.execute("PRAGMA foreign_keys = 1")
  connection.row_factory = dictionary_factory
  return connection

def read_build_script():
  path = os.path.join(os.path.dirname(__file__), 'build.sql')
  file = open(path)
  script = file.read()
  file.close()
  return script

def create_database(connection):
  script = read_build_script()
  connection.executescript(script)
  connection.commit() 
  
def insert_team(connection , team):
 sql = 'INSERT INTO teams(id,name) VALUES (:id , :name);'
 connection.execute(sql,team)
 connection.commit()

def insert_match(connection,match):
 sql = 'INSERT INTO matches(id,team0,team1,score0,score1,date) VALUES (:id,:team0,:team1,:score0,:score1,:date);'
 connection.execute(sql,match)
 connection.commit() 


def teams(connection):
 cursor=connection.cursor()
 sql = 'SELECT * FROM teams ;'
 cursor.execute(sql)
 rows = cursor.fetchall()
 list_teams = []
 for row in rows :
  dic_row = dictionary_factory(cursor, row)
  list_teams .append(dic_row)
 cursor.close()
 return list_teams 


 ''' 
 # *************** without factory 
 for row in rows : 
  dict_row = dict(row)
  list_teams.append(dict_row)
 cursor.close() 
 return(list_teams)
'''

def matches(connection):  
 sql = 'select * from matches '  
 cursor=connection.cursor()
 cursor.execute(sql)
 rows = cursor.fetchall()
 list_matches = []
 for row in rows :
  dic_row = dictionary_factory(cursor, row)
  list_matches .append(dic_row)
 cursor.close()
 return list_matches 
 
 '''
 # *************** without factory 
 for row in rows : 
  dict_row = dict(row)
  list_matches.append(dict_row)
 cursor.close() 
 return(list_matches)
'''

# ___ TO TEST IN BASH _________________________________________ 
 #from flask_app import model
 #connection=model.connect()
 #    model.create_database(connection):
 #    model.insert_team(connexion,{'id':10,'name':'toulouse'})
 #    model.insert_match(connection,{'id': 1, 'team0': 17, 'team1': 19, 'score0': 2, 'score1': 5, 'date': '2048-08-03 00:00:00'})
 #    model.matches(connection)
 #    model.teams(connection)