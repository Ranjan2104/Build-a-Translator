# Build a Translator
 API link = https://py-googletrans.readthedocs.io/en/latest/

Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.
Features
    
    Fast and reliable - it uses the same servers that translate.google.com uses
    Auto language detection
    Bulk translations
    Customizable service URL
    HTTP/2 support
    Installation
    To install, either use things like pip with the package “googletrans” or download the package and put the “googletrans” directory into your python path.
    $ pip install googletrans
You may wonder why this library works properly, whereas other approaches such like goslate won’t work since Google has updated its translation service recently with a ticket mechanism to prevent a lot of crawler programs.

![images](https://user-images.githubusercontent.com/60054130/118861211-df70a100-b8f9-11eb-9f09-07eec092eaca.png)


I eventually figure out a way to generate a ticket by reverse engineering on the obfuscated and minified code used by Google to generate such token, and implemented on the top of Python. However, this could be blocked at any time.
 
