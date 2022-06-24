import hashlib as hs
hashinput= input("Enter the input string to get hash 256 :\n")
salt= input("Enter the additional phrase which will be used as a salt:")
saltedinput = hashinput + salt

hashvalue= hs.sha256(hashinput.encode('utf-8')).hexdigest()
print("The sha256 of {} is {}".format(hashinput,hashvalue))

saltedhashvalue= hs.sha256(saltedinput.encode('utf-8')).hexdigest()
print("The sha256 of saltedinput {} is {}".format(saltedinput,saltedhashvalue))




print('You can store or write down the first 3 to 5 characters of the {} and {} for confirmation later.'.format(hashvalue,saltedhashvalue))

