# StupidApp Predictor
A predictor for stupid app trivia game

## Before starting you need
* You need you *cse id* and your *google api key* for using google custom search api.
STEP 1 and STEP 2 of the [given answer at stackoverflow will help you with it](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search).

* You need adb installed  and [USB Debugging](http://www.kingoapp.com/root-tutorials/how-to-enable-usb-debugging-mode-on-android.htm) mode on.

* You need python 3+ installed and libraries
  * pillow
  * pytesseract
  * cv2
  * googleapiclient
  
  
 ## How to use for Windows user?

 * Open the script getAnswersStupid and replace *my_api_key* and *my_cse_id* with your key and id.
 * Copy the script to some Folder
 * Open the cmd and point to that location where you have saved the script
 * Write the command 
 ```
    chcp 65001
 ```
 * Now connect the phone with USB and recheck if your phone is in debugging mode and have adb installed.
 * Keep the screen of the phone on and type these command in cmd
```
     adb shell screencap -p /mnt/sdcard/sc.png
     adb pull /mnt/sdcard/sc.png
     python getAnswersStupid.py --image sc.png
```

 ## Contribution
 
 You all are invited to contribute to this project.
 
 
 ## Disclaimer
 
 Use of this program to win trivia games is not the intend of developing it and I hope people use it in its 
 intended way.

