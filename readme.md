# News Ticker OBS Script

![alt text](https://raw.githubusercontent.com/ARTINKEL/OBS-News-Ticker/master/ticker-example.gif)

This is a script I wrote for [BreakCorvid](https://www.twitch.tv/breakcorvid)'s stream.

It is meant to be used in conjunction with a Text Source with a Scroll filter on it.

## How To Use

1. Extract virgil-news-ticker.py into your OBS scripts folder. This is usually found somewhere like: ```C:\Program Files (x86)\obs-studio\data\obs-plugins\frontend-tools\scripts```
2. Install [Python 3.6](https://www.python.org/downloads/release/python-360/). Make sure you get the right version based on your operating system.
3. Create a new Text source in the scene you want the ticker to be in. Make sure you have "Use Custom Text Extants" turned OFF.
4. Right click on the Text source and go to "Filters". Add a "Scroll" filter. Here is an example of the settings. The "Limit Width" option is important. I've found that 3440 is a good setting for this.

![alt text](https://raw.githubusercontent.com/ARTINKEL/OBS-News-Ticker/master/ticker-filter-setup.PNG)

5. Create a text file (.txt) in the same directory as your assets for the scene. Enter each message you want to appear on the screen on a new line. I've included an example file.
5. Open OBS and go to Tools -> Scripts. Go to the "Python Settings" tab and navigate to where you installed python.exe. For me, this is in ```C:\Users\$user_name\AppData\Local\Programs\Python\Python36```. It should say ```Loaded Python Version: 3.6```.
6. Go to Tools -> Scripts and then click the plus on the bottom. Select the virgil-news-ticker.py file you put here earlier.
7. It should show this menu.

![alt text](https://raw.githubusercontent.com/ARTINKEL/OBS-News-Ticker/master/ticker-script-setup.PNG)

8. Set the "Source Name" to the Text source you created earlier.
9. Set the "Source File" to the .txt file you created earlier.
10. Set the "Spaces" to the amount of space you want in between each entry in the text file.
11. Set "Interstitial Character" if you want certain characters to appear between entries. For example, if I have Test1 and Test2 in my txt file, and I set "Interstitial Character" to "||", the output would be Test1||Test2. If "Spacing" is set to 5, it would be Test1  ||  Test2.
12. Click "Update".

***NOTE: It is important that you click the "Update" button after making changes to the .txt file or the script properties. If you do not click the "Update" button, none of your changes will show on stream.***
