from menu import Menu

class Food(Menu):
  def __init__(self, name, price, calorie):
    super().__init__(name, price)
    self.calorie = calorie

  def getInfo(self):
    return self.calorie

  def includeTax(self):
    return round(self.price * 1.08)

  def getTotalPrice(self, count):
    return count * self.includeTax()
