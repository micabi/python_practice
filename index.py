money = 1000
apple_price = 200

input_count = input("数を入力：")

count = int(input_count)

total_price = apple_price * count

print("財布の中身は" + str(money) + "円です")

if money > total_price:
  print("りんごを" + str(count) + "個買います")
  print("財布の中身は" + str(money - total_price) + "円となりました")
elif money == total_price:
  print("りんごを" + str(count) + "個買います")
  print("財布の中身は" + str(money - total_price) + "円となりました")
else:
  print("りんごを" + str(count) + "個買いたかったけど、お金が足りません")