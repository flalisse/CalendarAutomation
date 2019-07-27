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
    self.DateStartCompleted = ""
    self.Location = "Tbd"
    self.Description =""
    self.color =""
    self.occurencefixed=""
    self.Repeat=''
    self.DateEndCompleted = ""



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

    starttime_regex = "([0-9]{4})-([0-9]{2})-([0-9]{2})-([0-9]{2}):([0-9]{2})"
    DateNoComplete = ""

    while re.search(starttime_regex,DateNoComplete) is None:
        DateNoComplete = input("Entrez une date pour votre tâche sous ce format (année-mois-jour-heure:minute)")

    DateNoComplete_tomodify = list(DateNoComplete)
    Time_Zone = DateNoComplete[11:13]
    Int_Good_Time_Zone = int(Time_Zone)+9

    if Int_Good_Time_Zone > 24 :
      Int_Good_Time_Zone_error_handle = Int_Good_Time_Zone-24
      Int_Good_Time_Zone_error_handle_string = str(Int_Good_Time_Zone_error_handle)
      DateNoComplete_tomodify[11]="0"
      DateNoComplete_tomodify[12]=Int_Good_Time_Zone_error_handle_string
      DateNoComplete_tomodify_string="".join(DateNoComplete_tomodify)
      print(DateNoComplete_tomodify_string)

    else:
      Int_Good_Time_Zone_string = str(Int_Good_Time_Zone)
      DateNoComplete_tomodify[11:13]=Int_Good_Time_Zone_string
      DateNoComplete_tomodify_string = "".join(DateNoComplete_tomodify)
      print(DateNoComplete_tomodify_string)


    DateToGoodFormat = DateNoComplete_tomodify_string[:11]+'T'+DateNoComplete_tomodify_string[11:]
    Additionnal_date = ':00-00:00'

    self.DateStartCompleted = DateToGoodFormat + Additionnal_date
    print(self.DateStartCompleted)


    TimeForEvent = input("combien de temps pour cet event ? en heure ")
    TimeForEvent_Int = int(TimeForEvent)

    Timetoadd = DateNoComplete_tomodify_string[11:13]


    real_time_to_end = int(Timetoadd) + TimeForEvent_Int
    print(real_time_to_end)
    real_time_to_end_string = str(real_time_to_end)


    Date_To_End_List = list(DateNoComplete_tomodify_string)

    if real_time_to_end < 11:
      Date_To_End_List[11]="0"
      Date_To_End_List[12]=real_time_to_end_string
      Date_To_End_List_in_string = "".join(Date_To_End_List)

    else :

      Date_To_End_List[11:13] = real_time_to_end_string
      Date_To_End_List_in_string = "".join(Date_To_End_List)

    print(Date_To_End_List_in_string)
    DateToEndGoodFormat = Date_To_End_List_in_string[:11]+'T'+Date_To_End_List_in_string[11:]
    self.DateEndCompleted=DateToGoodFormat+Additionnal_date
    print(self.DateEndCompleted)




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









Event = Event()

Event.SetDate()
