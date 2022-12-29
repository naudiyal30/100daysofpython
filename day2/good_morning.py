import time

hour = time.strftime('%H:%M:%S')

if (hour > '04:59:59' and hour < '12:00:00'):
  print("Good Morning Sir")
elif (hour > '11:59:59' and hour < '18:00:00'):
  print("Good Afternoon Sir")
elif (hour > '17:59:59' and hour < '19:59:59'):
  print("Good Evening Sir")
else:
  print("Good Night Sir")