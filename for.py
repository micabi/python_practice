money = 1000
items = {
  'apple':100,
  'orange':200,
  'grape':400
}

for item_name in items:
  print('----------------------------------')
  print('財布には' + str(money) + '円入っています')
  print(item_name + 'は1つ' + str(items[item_name]) + '円です')

  input_count = input(item_name + 'をいくつ買いますか？：')
  print(item_name + 'を' + input_count + '個買います!')
  count = int(input_count)
  total_price = int(items[item_name]) * count
  print('代金は' + str(total_price) + '円になります')

  if money >= total_price:
    money = money - total_price
    print('財布の中身は' + str(money) + '円になりました')
    if money == 0:
      print('財布の中身がなくなりました')
      print('買い物はそこまでです')
      break
  else:
    print('お金が足りません')
    print('買い物はそこまでです')

