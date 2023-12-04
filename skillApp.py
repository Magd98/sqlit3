import sqlite3


db=sqlite3.connect("Skills.db")
cr=db.cursor()


def AddUser():
    userAdded=input("Enter the name: ")
    ageAdded=int(input("Enter his age:"))
    skillAdded=input("Enter the skill you want to add: ")
    cr.execute(f"INSERT into Users(name,age,skill) VALUES ('{userAdded}',{ageAdded},'{skillAdded}')")
    print("Record Added Sucessfully !!")

def ShowAllUsers():
  cr.execute("SELECT name,age,skill From Users")
  userData=cr.fetchall()
  print(userData)

def DeleteUser():
  userName=input("Enter the name of the user you want to delete: ")
  cr.execute(f"DELETE from Users where name ='{userName}'")
  print("Record Deleted Sucessfully !!")


def UpdateUser():
  userUpdate=input("Enter the name of the user you want to Update his info.")
  dataUpdate=input("What do you want to change name, age or skill ? ")
  if dataUpdate=="name":
    dataName=input("Change name to : ")
    cr.execute(f"UPDATE Users set name ='{dataName}' where name='{userUpdate}' ")
  elif dataUpdate=="age":
    dataAge=int(input("Change age to: "))
    cr.execute(f"UPDATE Users set age = {dataAge} where name='{userUpdate}'")
  elif dataUpdate =="skill":
    dataSkill=input("Change Skill to: ")
    cr.execute(f"UPDATE Users set skill='{dataSkill}'where name='{userUpdate}'")
  print("Record Updated Sucessfully !!")




cr.execute("CREATE TABLE if not exists Users(Name string, Age integer , Skill string)")
while True:
  print("____  Skill Applicatiion ____")
  print("Please choose an option from below as follows: ")

  introChoice=input("""
  'a' >>> Add New User.
  's' >>> Show All Users.                
  'd' >>> Delete a User or a specific entry in a User.
  'u' >>> Update User Info.
  'q' >>> Quit Application.
  Your Choice is : """)

  if introChoice =="a":
    AddUser()

  elif introChoice == "s":
    ShowAllUsers()

  elif introChoice == "d":
    DeleteUser()

  elif introChoice == "u":
    UpdateUser()


  db.commit()

  if introChoice == "q":
    break

