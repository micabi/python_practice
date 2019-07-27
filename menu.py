class Menu:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def getTax(self):
    return self.price * 1.08




