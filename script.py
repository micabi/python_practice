from drink import Drink
from food import Food

coffee = Drink('コーヒー', 400, 'ホット')
cola = Drink('コーラ', 500, 'アイス')
carry = Food('カレー', 700, '800cal')
pasta = Food('パスタ', 600, '600cal')

drinkItems = [coffee, cola]
foodItems = [carry, pasta]

print('まずはお飲み物からお伺いします。')

drinkCount = 0

for drinkItem in drinkItems:
  print(str(drinkCount) + ': ' + drinkItem.name + 'は' + str(drinkItem.includeTax()) + '円です。' + drinkItem.getInfo() + 'です。')
  drinkCount += 1

print('----------------------')
drink_order = int(input('飲み物を選んで下さい(番号で): '))
selected_drink = drinkItems[drink_order]
print(selected_drink.name + 'ですね。')
drinkCount = int(input('おいくつ注文しますか？(数字で): '))
drinkTotalPrice = selected_drink.getTotalPrice(drinkCount)
print(str(drinkTotalPrice) + '円です。')


print('----------------------')
print('次にお食事をお伺いします。')

foodCount = 0

for foodItem in foodItems:
  print(str(foodCount) + ': ' + foodItem.name + 'は' + str(foodItem.includeTax()) + '円です。' + foodItem.getInfo() + 'です。')
  foodCount += 1

food_order = int(input('食べ物を選んで下さい(番号で): '))
selected_food = foodItems[food_order]
print(selected_food.name + 'ですね!')
foodCount = int(input('おいくつ注文しますか？(数字で): '))
foodTotalPrice = selected_food.getTotalPrice(foodCount)
print(str(foodTotalPrice) + '円です。')


print('----------------------')
totalPrice = drinkTotalPrice + foodTotalPrice
print(selected_drink.name + 'がお' + str(drinkCount) + 'つ、')
print(selected_food.name + 'がお' + str(foodCount) + 'つ、')
print('合計' + str(totalPrice) + '円になります！')


