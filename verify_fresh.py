# Import required libraries

from datetime import date
import time
import re
import csv


# Iterate through links(and parse them from posts) to make sure they are new

def verify_fresh():
	time.sleep(2)
	print("Now I'm just making sure that these links aren't spammy or old before I show them to you.\n\n")
	count = 0
	with open("input_file.txt") as file_1:
		posts = file_1.read().splitlines()
		for post in posts:
			regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
			linklist = regex.findall(post)
			with open('processed.txt', 'r+') as file_2:
				day_collected = date.today()
				fields = ['link', 'day_collected']
				output_writer = csv.DictWriter(file_2, fieldnames=fields)
				output_writer.writeheader()
				for item in linklist:
					if item in file_2.read():
						break
					else:
						log = {
						'link':item,
						'day_collected':day_collected 
						}
						output_writer.writerow(log)
						with open('verify_fresh_output.txt', 'a') as file_3:
							file_3.write(post + "\n")
						count += 1
	time.sleep(2)
	print("There were {count} unique Telegram or Discord links.\n".format(count=count))

if __name__=="__main__":
	verify_fresh()




