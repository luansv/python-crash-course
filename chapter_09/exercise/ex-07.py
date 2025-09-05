#9-10

from ex01 import Restaurant

abc = Restaurant('La cosina isla', 'Pasta')
abc.open()
abc.describe()

print("------------------------")

#9-11

from ex_05 import User, Privileges, Admin

adm = Admin("Karina", 'Kim', 'SC', 888888)
adm.describe_user()
adm.greet()

priv = Privileges('Jonas', 'Kanel', 'Italy', 77777777)
priv.describe_user()

user1 = User('ABC', 'DEF', 'FGH', 858488)
user1.describe_user()







