class FirstPa:
  def __init__(self):
    print("FirstPa enter")
    super().__init__()
    print("FirstPa exit")

class SecondPa:
  def __init__(self):
    print("SecondPa enter")
    super().__init__()
    print("SecondPa exit")

class YayPa:
  def __init__(self):
    print("YayPa enter")
    super().__init__()
    print("YayPa exit")

class First(FirstPa):
  def __init__(self):
    print ("First(): entering")
    super().__init__()
    print ("First(): exiting")

class Second(SecondPa):
  def __init__(self):
    print ("Second(): entering")
    super().__init__()
    print ("Second(): exiting")

class Yay(YayPa):
  def __init__(self):
    print ("Yay(): entering")
    super().__init__()
    print ("Yay(): exiting")

class Third(Second, First, Yay):
  def __init__(self):
    print ("Third(): entering")
    super().__init__()
    print ("Third(): exiting")

third = Third()
print(Third.mro())

# '''
# third enter
# second enter
# first enter
# yay enter
# yp enter
# yp exit
# yay exit
# fp enter
# fp exit
# first exit
# sp enter
# sp exit
# sec exit
# third exit
# '''