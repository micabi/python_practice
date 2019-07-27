from menu import Menu

class Drink(Menu):
  def __init__(self, name, price, type):
    super().__init__(name, price)
    self.type = type

  def getInfo(self):
    return self.type

  def includeTax(self):
    return round(self.price * 1.08)

  def getTotalPrice(self, count):
    return count * self.includeTax()


