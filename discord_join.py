# This is part 5 of the Collections Bot series. It's function is to add the analyst selected Discord Channels fed to it.


#import modules
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Run Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Login to Discord
def go_to_discord():
	driver.get("https://discordapp.com/channels/@me") 
	time.sleep(5)
	username = driver.find_element_by_name('email')
	username.send_keys('DISCORD EMAIL HERE')
	password = driver.find_element_by_name('password')
	password.send_keys('DISCORD PASSWORD HERE')
	driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/button[2]/div').click()
	time.sleep(10)
	return add_server(server)

def add_server(link):
	driver.get(link)
	time.sleep(5)
	try:
		driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/section/div/button/div').click()
		print('Added the Server!')
	except:
		return checker(link)

# verify invite link is valid if unable to add server
headers = {
	'Accept': 'application/json',
}

def checker(link):
	regex = re.compile("[^/]+$")
	hash_value = regex.findall(link)
	string_hash_value = ""
	for character in hash_value:
		string_hash_value += character
	line = "https://discordapp.com/api/invite" + string_hash_value
	response = requests.get(line, headers = headers)
	if response.status_code == 200:
		print("https://discord.gg" + str(line) + " is a valid invite link. However, I cannot join it. I may have joined too many servers.")
	elif response.status_code == 429:
		print("I'm sorry, discord has banned me from checking this link because I made too many API calls. I should be able to check again in 24 hours")
	else:
		print("Sorry! This invite link appears to be invalid.")






