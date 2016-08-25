

title="\nthe_catcher_in_the_raichu\n"
dia1= "Do you want Charmander or Bulbasaur?"
dia2= "yell at pikachu or ignore?"
start = '''You open your eyes, picking out the crust from the corners. The sun way too bright and you spend a couple minutes getting angry at it. Then you realize "TODAY IS WHEN I GET MY FIRST POKEMON" 'Do you take your time getting ready or rush to the lab?'''
print(title)
print(start)

print("Type 'slow' to take your time and 'rush' to run to the lab")
user_input = input()
if user_input == "rush":
     print("You run over to the lab and get to choose between Bulbasaur and Charmander")  
     print(dia1)
	 
     user_input = input()
     if user_input == "Charmander":
        print("Sorry we only have pikachu")
     if user_input == "Bulbasaur":
        print("Sorry we only have pikachu")

	 
	 
elif user_input == "slow":
    print("You run over to the lab and get to choose your pokemon..You came too late and there's only pikachu....Pikachu is acting up and won't listen to your commands ")
    print(dia2)
	
user_input = input()
if user_input == "yell":
       print("Pikachu kills you")
if user_input == "ignore":
	print("He follows you on the path anyway")
	print("You come across a swarm of Spearows.... type walk to walk past and around to go around")
	   
	user_input = input()
	if user_input == "around":
			print("You make it to Viridian City, THE END")
	   
	user_input = input()
	if user_input == "walk":
				print("Pikachu gets hit and you must go to the pokemon center....you come across a girl and her bike, type steal to steal the bike and run to run to the center")
        
	user_input = input()
	if user_input =="steal":
						print("You make it to the Pokemon Center and Pikachu is healed but the girl will always remember that you are a theif. Be careful next time...THE END")		 
if user_input == "run": 
						print("You don't make it in time and Pikachu dies....you murderer.")       