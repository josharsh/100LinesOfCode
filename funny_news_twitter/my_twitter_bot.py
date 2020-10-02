import tweepy,string,time

CONSUMER_KEY = "<YOUR cunsumer key>"
CONSUMER_SECRET = "<your consumer secret>"

ACCESS_TOKEN = "<your access token>"
ACCESS_TOKEN_SECRET = "<your access token secret>"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

subsitutions = {"florida": "the alligator state","shooters": "killing retards","mistake": "chocolate cake","women": "whamen","women's": "whamen's","last": "first","first": "last","witnesses": "these dudes I know","allegedly": "kinda probably","new study": "tumblr post","rebuild": "avenge","space": "spaaace","google glass": "virtual boy","smartphone": "pokedex","senator": "elf-lord","electric": "atomic","car": "cat","election": "eating contest","congressional leaders": "river spirits","homeland security": "homestar runner","could not be reached for comment": "is guilty and everyone knows it","debate": "dance-off","self driving": "uncontrollably swering","poll": "psychic reading","candidate": "airbender","drone": "dog","vows to": "probably won't","dark web": "diagon alley","gay": "straight","straight": "gay","white": "black","black": "white","uranium": "vibranium","massive": "godzilla size","celebration": "orgy","nuclear": "pancake","at large": "very large","successfully": "suddenly","expands": "physically expands","first-degree": "friggin' awful","second-degree": "friggin' awful","third-degree": "friggin' awful","an unknown number": "like hundreds","front runner": "blade runner","global": "spherical","years": "minutes","minutes": "years","no indication": "lots of signs","urged restraint by": "drukenly egged on","horsepower": "tons of horsemeat","gaffe": "magic spell","ancient": "haunted","star-studded": "blood-soaked","remains to be seen": "will never be known","silver bullet": "way to kill werewolves","subway system": "tunnels i found","surprising": "surprising(but not to me)","war of words": "interplanetary war","tension": "sexual tension","tensions": "sexual tensions","cautiously optimistic": "delusional","doctor who": "the bigbang theory","win votes": "find pokemons","behind the headlines": "beyond the grave","email": "poem","facebook post": "poem","planes": "frisbees","people": "frogs","alabama": "sweet home alabama","plane": "frisbee","tweet": "poem","facebook ceo": "lizard guy","latest": "final","disrupt": "destroy","scientists": "channing tatum and his friends","you won't believe": "I am really sad about",
				}    


NEWS_FILE_NAME = "last_seen_news.txt"
REPLY_FILE_NAME = "last_seen_id.txt" 

def retrieve_last_seen_id(file_name):
	with open(file_name, 'r') as f_read:
		a = f_read.read().strip()
		if a=="":
			last_seen_id = -1
		else:
			last_seen_id = int(a)
	return last_seen_id	

def write_last_seen_id(file_name, last_seen_id):
	with open(file_name, 'w') as f_write:
		f_write.write(str(last_seen_id))
	return	

def tweet_for_fun():
	print("tweeting for fun")
	since_id = retrieve_last_seen_id(NEWS_FILE_NAME)
	try:
		if since_id == -1:
			cnn_tweets = list(api.user_timeline("@cnnbrk", tweet_mode = "extended"))
		else:
			cnn_tweets = list(api.user_timeline("@cnnbrk", since_id, tweet_mode = "extended"))	
	except tweepy.error.TweepError:
		pass
	else:
		for tweet in reversed(cnn_tweets):
			write_last_seen_id(NEWS_FILE_NAME, tweet.id)
			subse = 0
			t = tweet.full_text
			out = ""
			if "islam" in t or "rape" in t:   # don't wanna poke my nose there
				continue
			x = t.split()
			for i in x:
				k = i.lower()
				punch = string.punctuation.replace("-","")
				for j in punch:
					if j in k:
						k.replace("j","")
				res = subsitutions.get(k,'aaaaa')
				if res != 'aaaaa':
					subse+=1
					out = out + res + " "
				else:
					out = out + i + " "
			if subse>0:			
				# print(out)
				api.update_status(out+ "#xkcdNewsSubstitutions")

def reply_to_tweets():
	print('retrieving and replying to tweets...', flush=True)
	last_seen_id = retrieve_last_seen_id(REPLY_FILE_NAME)

	try:
		if last_seen_id == -1:
			mentions = api.mentions_timeline(tweet_mode='extended')
		else:	
			mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
	except:
		pass
	else:
		for mention in reversed(mentions):
			# print(mention)
			last_seen_id = mention.id
			write_last_seen_id(REPLY_FILE_NAME, str(last_seen_id))
			if '#hellozigzag' in mention.full_text.lower():
				print('found #hellozigzag!', flush=True)
				print('responding back...', flush=True)
				api.update_status("Hello "+'@' + mention.user.screen_name +
	            	' Nice to meet you #youAreBreathtaking', mention.id)

while True:
	tweet_for_fun()
	time.sleep(2)
	reply_to_tweets()
	time.sleep(2)