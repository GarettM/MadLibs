""" Mad Libs story.  Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story."""

print "Mad Libs has started"

name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter another adjective: ")
adj3 = raw_input("Enter one more adjective: ")
verb1 = raw_input("Enter a verb: ")
verb2 = raw_input("Enter another verb: ")
verb3 = raw_input("Enter one more verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter a noun: ")
noun3 = raw_input("Enter a noun: ")
noun4 = raw_input("Enter a noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
hero = raw_input("Enter a superhero name: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, hero, hero, name, country, name, dessert, name, year, noun4)
