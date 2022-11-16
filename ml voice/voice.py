#Check if two files are similar/same in python

import hashlib 
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(),h2.hexdigest()

msg1,msg2 = hash_file("C:\\Users\\adhis\\OneDrive\\Documents\\Sound Recordings\\Recording (9).m4a","C:\\Users\\adhis\\OneDrive\\Documents\\Sound Recordings\\Recording (9).m4a")
print(msg1+"\t"+msg2)
print((SequenceMatcher(None,msg1,msg2).ratio())*100)


