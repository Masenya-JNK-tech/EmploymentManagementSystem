import psycopg2

def connect_database():
#connect to the PostgreSQL database 
 connection = psycopg2.connect(
  host= 'localhost',
  user = 'postgres',
  database =  'employee_management',
  password = "M@senyakeletso05",
  port = '2405'
 )
 return connection