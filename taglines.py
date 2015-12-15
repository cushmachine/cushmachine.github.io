
import random

#Pulls in text-formatted list of taglines
with open ("tagline-list.txt","r") as myfile:
	tagline_list=myfile.readlines()

#Captures the length of the list of taglines, to be used later in the random number generator
tagline_list_len = len(tagline_list) - 1

#Pulls and saves a random tagline from the list of taglines.
random_tagline = tagline_list[random.randint(0,tagline_list_len)]

#Prints random tagline (testing only)
print random_tagline