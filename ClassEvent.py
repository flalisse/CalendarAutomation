# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

import re

class Event():


  def __init__(self,):

    self.TupleOfTask = ["Rien a ajouter", "Sport", "Informatique", 'Loisirs']
    self.TaskSelected = ""
    self.Index = [0,1,2,3]
    self.DateStart = ""
    self.Location = "Tbd"
    self.Description =""
    self.color =""
    self.occurencefixed=""
    self.Repeat=''



  def SetTask(self,):
    self.Index = input("choissisez entre les loisirs : 1 : Sport , 2 : Informatique , 3 : Loisirs")
    self.Index = int(self.Index)

    while self.Index != 0 and self.Index != 1 and self.Index != 2 and self.Index != 3:
      self.Index = input("choissisez entre les loisirs : 1 : Sport , 2 : Informatique , 3 : Loisirs")
      self.Index = int(self.Index)

    self.TaskSelected = self.TupleOfTask[self.Index]
    return self.TaskSelected



  def SetDate(self,):
    # format de date : 2019-05-28T09:00:00-07:00

    print("+9h de décallage still working on it")

    starttime_regex = "([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2})"

    while re.search(starttime_regex, self.DateStart) is None:
      self.DateStart = input("Entrez une date pour votre tâche sous ce format (année-mois-jourT-heure:minutes:seconde-)")




  def SetDescription(self,):

    self.Description = input("Entrez une Description pour votre event {}".format(self.TaskSelected))
    return self.Description

  def SetColor(self,):

    if self.Index == 1:
      #color = green
      self.color = '#d06b64'
      self.colorID = '2'
    elif self.Index == 2 :
      self.color = '#f83a22'
      self.colorID = '3'


    elif self.Index == 3:
      self.color = '#fa573c'
      self.colorID = '4'

    return self.color
    return self.colorID

  def SetRepeat(self,):

    occurence = 'RRULE:FREQ=DAILY;COUNT='
    self.Repeat = input("comblien de fois par semaine ? ")

    while self.Repeat != "1" and self.Repeat != "2" and self.Repeat != "3" and self.Repeat != "4" and self.Repeat != "5" and self.Repeat != "6 "and self.Repeat != "7":
      self.Repeat = input("comblien de fois par semaine ? ")

    self.occurencefixed = occurence + self.Repeat
    print(self.occurencefixed)








