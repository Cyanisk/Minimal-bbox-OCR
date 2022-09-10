# Minimal-bbox-OCR
Inspired by [Game2Text](https://github.com/mathewthe2/Game2Text) which I am completely unable to get running on my Linux PC :hammer::monkey: 

## Requirements
- This is being developed on a Linux machine. I hope it works on other OS as well, but I simply don't know.
- This pretty much just a front-end for Tesseract, so you need to install [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html).
- You also need training data for the language you want to scan. Download the one you need from [here](https://github.com/tesseract-ocr/tessdata_best). The default language is Japanese (jpn), if you want a different language you just need to change the value of ```lang``` in ```MinimalSelectionOCR.py```.
- Linux users might need xclip or similar to be able to copy to clipboard

## What does it do 
Select an area of the screen and press scan. Text within the selected area will appear in the textbox, ready to be used with an online dictionary (making it easy to look up words you don't know).
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-05-25.png)

Pressing ```Select new area``` opens an overlay where you can select the area to scan for text
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-06-55.png)![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-08-01.png)

### Automatic mode
Scan the selected area for new text every second instead of manually pressing ```Scan``` every time. Be aware that bogus results are likely to occur when there is no text in the selected area.

### Copy to clipboard
Combine with an online texthooker (like [this](https://learnjapanese.moe/texthooker.html)), a clipboard inserter (like [this](https://addons.mozilla.org/en-US/firefox/addon/clipboard-inserter)) and a pop-up dictionary (like [this](https://addons.mozilla.org/en-US/firefox/addon/yomichan)) to create a powerful tool that allows for instant look-ups
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-12-07.png)

### Edit result
Sadly the OCR is not always accurate, and especially content with stylized fonts can be difficult to scan correctly. For example the Pokemon BDSP games have a pretty readable font except for the fact that ```っ``` and ```つ``` are almost the same size, and ```!``` is read as ```/``` because it is so slanted.
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-19-23.png)
If the text is wrong you won't be able to translate it with a pop-up dictionary. To deal with this issue you can edit the result to fix it and then use ```Overwrite clipboard``` to copy the new result to the clipboard (which makes the fixed result appear in the texthooker)
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-19-47.png)
![image](https://raw.githubusercontent.com/Cyanisk/Minimal-bbox-OCR/main/Screenshots/Screenshot%20from%202022-09-10%2012-22-02.png)
