from classes.practice_classes import *

cat = Cat("murzik", "white", 5)
cat.set_breed("syamskaya")
print(cat.about_cat())
cat.sit()
cat.roll_over()

cat1 = Cat("murzilka", "black", 10)
print(cat.about_cat())
cat.sit()
cat.roll_over()

print("--------------------------- 9 - 1 -------------------------------")
res1 = Restaurant("Afsona", "Uzbek")
print(f"restaurant called: {res1.restaurant_name}")
print(f"cuisine: {res1.cuisine_type}")
res1.desc_res()
res1.open_res()

res2 = Restaurant("Butcher", "Stake House")
res3 = Restaurant("Dushanbe", "tajik")
res4 = Restaurant("Tatiana", "russian")
res2.desc_res()
res3.desc_res()
res4.desc_res()

print("----------------------------- 9 - 3 ----------------------------")
user1 = User("cristiano", "ronaldo")
user1.set_email("@gmail")
user1.set_age(35)
user1.greet_user()
user1.desc_user()
print()
user2 = User("khabib", "nurmagomedov")
user2.set_email("@yahoo")
user2.set_age(33)
user2.greet_user()
user2.desc_user()
print()
user2 = User("Barak", "obama")
user2.set_email("@usa")
user2.set_age(60)
user2.greet_user()
user2.desc_user()

print("------------------------- 9 - 4 ----------------------------------")
res10 = Restaurant("Baltazar", "italian")
res10.desc_res()

res10.set_served(12)
res10.desc_res()

res10.set_served(100)
res10.desc_res()