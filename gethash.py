import hashlib as hs
hashinput= input("Enter the input string to get hash 265 :\n")
hashvalue= hs.sha256(hashinput.encode('utf-8')).hexdigest()
print("The sha256 of {} is {}".format(hashinput,hashvalue))
print(len(hashvalue), (hashvalue.encode('utf-8')))
print('You can store or write downthe first 3 to 5 characters of the {} for confirmation later.'.format(hashvalue))

