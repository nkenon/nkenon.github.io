
import random


articles = ["The", "A", "El", "La"]
names = {"Vicious", "Mold", "Dragon", "Tiger", "Fate", "Dancer", "Metal","Light", "Baby", "Orc", "Orchestra", "Atlas", "Apollo", "Moon" , "Haze", "Nomad", "Zero", "Ghost", "Indigo", "Bloom", "Paradox",}  

pick_two = 3                         
list_of_band_names = random.sample(names, pick_two)
articles_length = len(articles)
random_item_in_list = random.randint(0, articles_length-1)
first_random_item = list_of_band_names[0]
second_random_item = list_of_band_names[1] 

print(articles[random_item_in_list], first_random_item , second_random_item)