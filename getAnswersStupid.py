#  -*- coding: utf-8 -*-

# import the necessary packages
import pprint
#import webbrowser
from PIL import Image
from PIL import ImageGrab
import pytesseract
import argparse
import cv2
import os
import requests
#from urllib import parse


# replace it with your subscription key
subscription_key = "your subscription key"

# I am referring https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
# for optical image recognition
#im=ImageGrab.grab(bbox=(1,276,339,665))
#im.save('screen.png')
# construct the argument parse and parse the arguments
#screenshot_file="screen.png"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
   gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)






# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename),lang="eng")
os.remove(filename)
#print(text)


# taking out details from text after OCR
textArray = text.split('\n')
newText=[]
length=len(textArray)
optionArray=[]
noOfOption=0
question=''
for i in range(length):
    partOfArray=textArray[length-1-i]
    question=question.strip()
    if(partOfArray!='' and noOfOption<3):
        optionArray.append(partOfArray.strip())
        noOfOption = noOfOption+1
    elif(question!='' and partOfArray==''):
        break
    else:
        question=partOfArray+" "+question


#webbrowser.open('https://www.google.co.in/search?q=' +  parse.quote_plus(question), new=2)

print(optionArray)
print(question)
optionArray.reverse()
question=question.strip()


def bingAPI(search_term):
    """
    :param search_term: the question to be searched
    :return: array of results containing the heading of the result plus its details
    """
    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['webPages']['value']



def countWord(word, result):
    """

    :param word: contains a part of the option
    :param result: one of the result among several
    :return: number of occurences of the word in the result
    """
    return result.count(word)



def calc(wordString,result):
    """
    :param wordString: complete option string
    :param result: one of the result among several
    :return: mean of occurences of each word of wordString in the result
    """
    wordArray=wordString.split(" ")
    lengthOfWordArray=len(wordArray)
    sum=0
    for i in range(lengthOfWordArray):
        sum=sum+countWord(wordArray[i],result)

    mean=sum/lengthOfWordArray
    return mean


# results is the array of the search results
results=bingAPI(question)

# Here we are calculating the answer
# score represents the occurences of an option in google result with some twist
# highScore represent the option which have highest occurences in the google result with some twist
highScore=0
max_i=-1

for i in range(noOfOption):
    score=0
    for result in results:
        resultHeading=result['name']
        result=result['snippet']
        score=score*2+resultHeading.count(optionArray[i])
        score = score+calc(optionArray[i],result)


    if(score>highScore):
        highScore=score
        max_i=i
    print(optionArray[i], "--->", score)
if(max_i==-1):
    print("DON'T KNOW")
else:
    print("ANSWER  ",optionArray[max_i])




