# Auto join Telegram channels

# import libraries
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import *
import re

# This section parses the hash from the link

def parse_tg_hash(link):
	regex = re.compile("[^/]+$")
	hash_value = regex.findall(link)
	string_hash_value = ""
	for character in hash_value:
		string_hash_value += character
	return join_telegram(string_hash_value)

#input login values
api_id = 'API ID GOES HERE AS INT'
api_hash = 'API HASH GOES HERE AS STRING'

# creat client and connect

def join_telegram(string_hash_value):
	with TelegramClient('anon', api_id, api_hash) as client:
		try:
			result = client.loop.run_until_complete(client(ImportChatInviteRequest(
				hash=string_hash_value
				)))
			print("Hooray! I joined the group!")
		except InviteHashInvalidError:
			print("Sorry, this hash is not valid. You may try to join this channel manually.")
		except ChannelsTooMuchError:
			print("Sorry! I have joined too many channels/supergroups! Please spin up a new Telegram instance for me.")
		except InviteHashEmptyError:
			print("There is no invite hash here.")
		except InviteHashExpiredError:
			print('This invite link has expired.')
		except SessionPasswordNeededError:
			print('Looks like this channel requires a password.')
		except UsersTooMuchError:
			print('This channel is maxed out with members.')
		except UserAlreadyParticipantError:
			print('I\'m already in this channel.')


