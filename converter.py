def id2tinyURL(id):
	map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	tinyURL = ""
	
	while(id > 0):
		tinyURL += map[id % 62]
		id //= 62

	return tinyURL[len(tinyURL): : -1]

def tinyURL2Id(tinyURL):
	id = 0
	for i in tinyURL:
		val_i = ord(i)
		if(val_i >= ord('a') and val_i <= ord('z')):
			id = id*62 + val_i - ord('a')
		elif(val_i >= ord('A') and val_i <= ord('Z')):
			id = id*62 + val_i - ord('Z') + 26
		else:
			id = id*62 + val_i - ord('0') + 52
	return id

tinyURL = "www.google.com"
print("ID from", tinyURL, "is : ", tinyURL2Id(tinyURL),end="\n\n")

print("Tiny URL from ", tinyURL2Id(tinyURL), " is : ", tinyURL)
