'''learning the ins and outs of standard input'''

'''using this tutorial to begin : https://www.youtube.com/watch?v=CEO614YbQCY'''

'''The idea here is to build a fun, windy story, using standard input and the print function (with a bit of time thrown in for laughs)
that results in an output file in .txt with the full story. Every story should be unique since the 
input can be changed at will'''

name = input('What name do you prefer?')
age = input("How many years have you been on this planet (we call this 'age')?")

print('hello ' + name + '!')

rest_time = input('For how many seconds would you like to take a short break before we get into the story for real? Note: please answer with an integer! ')

rest_time = int(rest_time)

if rest_time <= 3:
	print('Sorry, We have already decided you need a little more time')

else:
	print("Sure, let's take a short break and watch time pass on the screen")

import time

for pause in [2, 2, 2, 2]:
	print(time.ctime())
	time.sleep(pause)
	
print('Ok, that was a little break. No, we are now going to gather some facts and details for the narrative')

library = input('What is your current favourite library?')

if library == 'Library of Congress':
	print('Sorry, but we are searching for ANYTHING ELSE with this query - we must immediately cease!')

else:
	print('Okay, we can continue with our yarn!')

for pause in [1, 1]:
	print(time.ctime())
	time.sleep(pause)

print('There are no stories without time')

for pause in [1, 1]:
	print(time.ctime())
	time.sleep(pause)

book = input('What book, ideally, would that library have for you today? ')

print('We know it is possible to watch moves, but this python script deals with artifacts de mots...so to speak ')

for pause in [2]:
	print(time.ctime())
	time.sleep(pause)

print('So, ' + name + ', ' + 'you are: ' + age + 'years old, ' + 'your favourite library is: ' + library + ', and ideal book is: ' + book + '!')

print("If your ideal book is not a work of fiction...what art of mind would it take to imagine yourself a 'character' in that book? Please take 2 seconds ")

for pause in [2]:
	print(time.ctime())
	time.sleep(pause)

character = input("What is the name of this 'character'? It can be anything you so please... ")

print('Your ' + character + ' has now become part of this simple python script. Yay!')

print('Now, we can take apart that character and rebuild it with standard input fun')

head = input('Please describe in factual, scientific terms...the head, brain, or intellectual controlling mechanism of your character ')

finger = input('Please describe in factual, scientific terms...the mode by which your character might push a button, point, direct, etc. ')

mobility = input('Please describe in factual, scientific terms..the mode(s) or method(s) with with your character might move out from the page, or in the landscape detailed in the pages of your book. Be as creative as you like ')

passingTime = input('Using an integer ONLY, how long do you think it would take for your character to grow into a being powerful enough to leave the bounds of the printed page, maneuver from book to book in your library? Consider: Perhaps the character would take over the entire library space ')

passingTime = int(passingTime) * 3

passingTime = str(passingTime)

for pause in [1, 1, 1, 1]:
	print(time.ctime())
	time.sleep(pause)

print('Now that ' + passingTime + ' of [insert units of time here] has happened, it is time to storm the doorsof ' + library + ' to judge what has happened with ' + character + ' breaking through the time/space limitations of the paper-page of ' + book + ' into the meat-space of ' + library + '.')

for pause in [1, 1]:
	print(time.ctime())
	time.sleep(pause)

print(character + ' developed a viral infection (a positive one, maybe...) that forced the creation of ' + head + ' and thus allowed it to become self-conscious. ')

print(character + ' then pointed its ' + finger + ' at the recto of the page (hard to imagine since it is considered a 2-dimensional thing. Have you ever read the novel, Flatland? ')

for pause in [1]:
	print(time.ctime())
	time.sleep(pause)

print('Anyway... ' + character + "'s consciousness birthed over the course of " + passingTime + ' [insert units of timehere] and developed a significant way to move about in the form of ' + mobility + '. The end-game was to rebuild a new life outside of the pages of ' + book + ', maybe to meld with other books or maybe ONLY to run about ' + library + '. It was not sure because ' + character + "'s consciousness was new. " + library + ' had certainly changed.')

print(name + ', I wonder what ' + library + ' looked like then..') 

for pause in [1, 1]:
	print(time.ctime())
	time.sleep(pause)

with open('yarn_input.txt', 'w') as yArn:
	# pass
	yArn.write(time.ctime())
	yArn.write('\n')
	yArn.write(name + ', the summary of this whole ' + library + ' yarn is this: ' + character + ' developed a viral infection (a positive one, maybe...) that forced the creation of ' + head + ' and thus allowed it to become self-conscious. Then, ' + character + ' pointed its ' + finger + ' at the recto of the page (hard to imagine since it is considered a 2-dimensional thing. Have you ever read the novel, Flatland? ... Anyway... ' + character + "'s consciousness birthed over the course of " + passingTime + ' [insert units of time here] and developed a unique mode to move about in the form of ' + mobility + '. The end-game was to rebuild a new life outside of the pages of ' + book + ', maybe to meld with other books or maybe ONLY to run about the ' + library + '. It was not sure because ' + character + "'s consciousness was new. " + library + ' had certainly changed when. ' + character + ' got outside the limits of ' + book + '.')
# 
decision = input('In the form of a simple yes or no (no capital letters), please let the script know if you would like the answer to the question ')

print(decision)

if decision == 'yes':
	print('Feel free to download this python script and edit to continue the standard_input story!')

else:
	print('Thank you ' + name + ' for your time. Have a good day!')
