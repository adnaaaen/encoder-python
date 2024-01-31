#this is the sample pyhton script for encrypt and decrypt data
import string 
import random
#random.seed(1)
key = string.digits + string.ascii_letters + string.punctuation + " "

keyList = list(key)
shuffle_key = keyList.copy()

random.shuffle(shuffle_key)

def getEncode_text(text: str) -> str:
    result = ""
    for each in text:
        value = keyList.index(each)
        result += "".join(shuffle_key[value])
    return result

def getDecode_text(key: str) -> str:
    result = ""
    for each in key:
        value = shuffle_key.index(each)
        result += "".join(keyList[value])
    return result
        

while True:
    userChoice = int(input("1.Encode\n2.Decode\n3.Exit\nEnter choice: "))
    match userChoice:
        case 1:
            plane_text = input("\nEnter text to ecnode: ")
            encoded_data = getEncode_text(plane_text)
            print(encoded_data)
        case 2:
            encoded_text = input("\nEnter data to decode: ")
            decoded_data = getDecode_text(encoded_text)
            print(decoded_data)
        case 3:
            print("\nExiting..")
            break
        case _:
            print("\nEnter valid choice")




