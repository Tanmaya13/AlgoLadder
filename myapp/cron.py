from django.core.mail import send_mail
from .models import *
from datetime import datetime, timedelta,date,timezone
from io import StringIO
from django.conf import settings
from django.core.mail import EmailMessage
from .views import *
import sys
import requests as req
dsa = ['Introduction to Array and Pointers in Arrays','Arrray Operations','Multi-Dimension Array','Arrays and Functions','Introduction to Linked List and Types of Linked Lists','Linked List Operations','Comparison with other data structures','Introduction to Stack and Implementation of Stack','Expression Notifications using Stack','Introduction to Queue and Operations on Queue','Queue Implementation','Introduction to Binary Tree and Binary Tree and its Types','Tree Traversal','Implementation of Binary Tree','Introduction to Binary Search Tree and Binary Search Tree Operations','Identify whether BST','Min Max of BST','Height of BST','Introduction to Strings and String Manipulation Functions','Introduction to Graph andTypes of Graphs','BFS & DFS','Introduction to Hash Table','Collision and Chaining','Open Addressing','Vectors','Sets','Pairs','Maps','Introduction to Searching and Linear Search','Binary Search','Jump Search','Introduction to Sorting , Bubble Sort and Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Counting Sort','Wave Sort','Introduction to Mathematical Logics and Euler Totient Function','Fermat Little Theorem','Sieve of Eratosthenes','Introduction to Greedy Approach and Activity Selection Problem','Job Sequencing Problem','Fractional Knapsack','Bin Packing','Introduction to Dynamic Programming','Longest Increasing Subsequence','House Robber','Edit Distance','Introduction to Divide and Conquer and Square Root','Search element in a rotated sorted array','Tiling Problem','Modular Exponentiation','Introduction to Backtracking','N QUEEN Problem','Knights Tour Problem','Introduction to Graph Algorithms','Floyd Warshall','Dijkstra’s Algorithm','Introduction to Pattern Matching and KMP Algorithm','Rabin Karp Algorithm' ]
webdev = ['Introduction to Python Data Types','Text and Numeric','Sequence and Mapping','Set, Boolean and Binary','Introduction to Python Operators','Arithmetic Operators','Bitwise Operators','Assignment Operators','Comparison Operators','Identity Operators','Logical Operators','Membership Operators','Introduction to Python Conditions','Nested & Short-Hand','Introduction to Python Loops','WHILE loop','FOR loop','NESTED loop','LOOP CONTROL SYSTEM','Introduction to Python Functions','Syntax and Examples','Introduction to Flask Basics','Creating Basic Flask App','Introduction to Flask Routing','Routes with Parameters','Introduction to Flask Methods','Methods in Route','Introduction to Flask Templates','Jinja2 Template','Introduction to Flask Deployment','Flask Web App on Heroku','Introduction to Django Basics','Creating a Project','Creating An App','Running Your First Project','Introduction to Django Views and Url','Url Mapping','Introduction to Django Models','Connecting Models','CRUD','Introduction to Django Redirection and Forms','Forms','Introduction to Django Deployment','Git and Heroku']


def whatsapp_msg():
  try:
    req.get("https://algoladder.com/eg/29")
  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    message = ("error: %s ", e)
    message = str(message)
    sample(message)
  return 1

def whatsapp_msg1():
  return 1
# def whatsapp_msg():
#   try:
#     course_id=1
#     list_students = Courses.objects.get(id=course_id).enrolledusers.all()
#     sample("algoladder message send")
#     sample(str(len(list_students)))
#     for i in list_students:
#       name = i.fullname
#       day = i.counter
#       sp = day.split(",")
#       sp1= sp[0].split("-")
#       wtdy = int(sp1[1])
#       sample(str(name))
#       if wtdy<60:
#         url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
#         headers = {
#           "Content-Type": "application/json",
#           "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
#           }
#         body ={
#           #  "to_number": "91"+i.phone,
#           "to_number": "917906334045",
#           "type":"text",
#           "message": "Hello " + name + ", Greetings from AlgoLadder, Your Today's Topic is "+dsa[wtdy] + " and your course link is http://algoladder.com/onotes_list/1"
#           }
#         res = requests.post(url1,json=body,headers = headers)
#         print("message sent")
#         sample("line 40s")
#         change = sp1[1].replace(sp1[1],str(int(sp1[1])+1))
#         sample("line 42")
#         new = sp1[0]+'-'+change +','+sp[1]+','+sp[2]
#         sample("before save")
#         print("value of new is ",new)
#         # i.counter = new
#         i.save()
#         sample("after save")
#       sample("first phase complete") 
#       today = (datetime.now(timezone.utc) +  timedelta(hours=5.5)).strftime("%A")
#       sample(str(today)) 
#       if(today == "Saturday" or today == "Sunday"):
#         url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"

#         headers = {
#           "Content-Type": "application/json",
#           "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
#         }
#         body ={
#           "to_number": "917906334045",
#           "type":"text",
#           "message": "Hello "+name+" This message is just a reminder that classes will be held today of Course Speed Up with DS and algo , Greetings from Algoladder."
#         }
#         res = requests.post(url1,json=body,headers = headers)
#         print("message sent")
#   except Exception as e:
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     message = ("error: %s ", e)
#     message = str(message)
#     sample(message)
#   return 1
    
# def whatsapp_msg1():
#   course_id=2
#   list_students = Courses.objects.get(id=course_id).enrolledusers.all()
#   for i in list_students:
#     name = i.fullname
#     day = i.counter
#     sp = day.split(",")
#     sp1= sp[1].split("-")
#     wtdy = int(sp1[1])
#     if wtdy<44:
#       url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
#       headers = {
#         "Content-Type": "application/json",
#         "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
#       }
#       body ={
#         "to_number": "917906334045",
#         # "to_number": "91"+i.phone,
#         "type":"text",
#         "message": "Hello " + name + ", Greetings from AlgoLadder, Your Today's Topic is "+webdev[wtdy] + " and your course link is http://algoladder.com/onotes_list/2"
#       }
#       res = requests.post(url1,json=body,headers = headers)
#       print("message sent")
#       change = sp1[1].replace(sp1[1],str(int(sp1[1])+1))
#       new = sp[0]+','+sp1[0]+'-'+change+','+sp[2]
#       # i.counter = new
#       i.save()
#     today = (datetime.now(timezone.utc) +  timedelta(hours=5.5)).strftime("%A")
#     if(today == "Saturday" or today == "Sunday"):
#       url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"

#       headers = {
#         "Content-Type": "application/json",
#         "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
#       }
#       body ={
#         "to_number": "91"+i.phone,
#         "type":"text",
#         "message": "Hello "+name+" This message is just a reminder that classes will be held today of Course Web Development With python + Django , Greetings from Algoladder."
#       }
#       res = requests.post(url1,json=body,headers = headers)
#       print("message sent")
#   return 1


def sample(message):
  url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
  headers = {
    "Content-Type": "application/json",
    "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
  }
  body ={
    "to_number": "917906334045",
    "type":"text",
    "message": message
  }
  res = requests.post(url1,json=body,headers = headers)

  return 1
