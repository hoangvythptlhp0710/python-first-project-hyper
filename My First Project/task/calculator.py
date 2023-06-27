# Write your code here
print("Earned amount:\nBubblegum: $202\nToffee: $118\nIce cream: $2250\nMilk chocolate: $1680\nDoughnut: "
      "$1075\nPancake: $80\n")
bubblegum = 202
toffee = 118
icecream = 2250
milkchocolate = 1680
doughnut = 1075
pancake = 80
result = bubblegum + toffee + icecream + milkchocolate + doughnut + pancake
print("Income: $" + str(result))

print("Staff expenses: ")
staffExpenses = int(input())
print("Other expenses: ")
otherExpenses = int(input())
finalIncome = result - staffExpenses - otherExpenses
print("Net Income: $" +str(finalIncome))