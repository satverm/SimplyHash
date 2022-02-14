import hashlib as hs
hashinput= input("Enter the input string to get hash 265 :\n")
hashvalue= hs.sha256(hashinput.encode('utf-8')).hexdigest()
print("The sha256 of {} is {}".format(hashinput,hashvalue))
print(len(hashvalue), (hashvalue.encode('utf-8')))

