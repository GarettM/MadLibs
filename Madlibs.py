""" Mad Libs story.  Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story."""

print("Mad Libs has started")

name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one more adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
number = input("Enter a number: ")
hero = input("Enter a superhero name: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")


#The template for the story
STORY = "This morning I woke up and felt {} because {} was going to finally {} over the big {} {}. On the other side of the {} were many {}s protesting to keep {} in stores. The crowd began to {} to the rythym of the {}, which made all of the {}s very {}. {} tried to {} into the sewers and found {} rats. Needing help, {} quickly called {}. {} appeared and saved {} by flying to {} and dropping {} into a puddle of {}. {} then fell asleep and woke up in the year {}, in a world where {}s ruled the world."

print STORY(adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, hero, hero, name, country, name, dessert, name, year, noun4)
