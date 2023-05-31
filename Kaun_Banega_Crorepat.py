questions = [[" (01) Presentation of the first ever railway budget in India held in",
               1853, 1888,1925,23],
             ["Presentation of the first ever railway budget in India held in", 1853, 1888,1925,23],
             ["Presentation of the first ever railway budget in India held in", 1853, 1888,1925,23],
             ["Presentation of the first ever railway budget in India held in", 1853, 1888,1925,23],
             ["Presentation of the first ever railway budget in India held in", 1853, 1888,1925,23]
             ]
levels = [10000,20000,30000,40000,50000,
          60000,70000,80000,90000,100000, 100000, 100000, 100000, 120000,]
money = 0 
for i in range(0 , len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"\n {question[i]}")
    print(f"a){question[1]}   b){question[2]}")
    print(f"c){question[3]}   d){question[4]}")
    reply = int(input("Enter your answer (1 to 4) or quit the program press 0"))
    if (reply == 0):
      money = levels[i-1]
    if (reply == question[1]):
     print(f"Correct Answer you have won {levels[i]}")
     if(i == 4):
      money = 50000
    elif(i == 9):
       money = 100000
    else: 
     print("worning answer")
     break
    

print(F'your total money is {money}')


