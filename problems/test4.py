# Create a function that takes a list of football clubs with properties: name, wins,
# loss, draws, scored, conceded, and returns the team name with the highest
# number of points. If two teams have the same number of points, return the
# team with the largest goal difference.
# How to Calculate Points and Goal Difference
# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
# "conceded": 20 }
# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68

def test(t1,t2,t3):
  
  llist=[t1,t2,t3]
  llist2=[]
  llist3=[]
  
  for i in llist:
    Total_Points = 3 * i['wins'] + 1 * i['draws']
    Goal_Difference = i['scored'] - i['conceded']
    llist2.append(Total_Points)
    llist3.append(Goal_Difference)
  largest=max(llist2)
  biggest=max(llist3)
  if llist2.count(largest)>1:
    for i in range(0,len(llist)):
      if llist3[i]==biggest:
        return (llist[i])['name']
  else:
    for i in range(0,len(llist)):
      if llist2[i]==largest:
        return (llist[i])['name']


  
#test
a1={ "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,"conceded": 20 }
a2={ "name": "rajasthan royal", "wins": 27, "loss": 0, "draws": 14, "scored": 76,"conceded": 6 }
a3={ "name": "kkr", "wins": 26, "loss": 2, "draws": 2, "scored": 75,"conceded": 14 }
print(test(a1,a2,a3))


