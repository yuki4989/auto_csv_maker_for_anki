# Name（リポジトリ/プロジェクト/OSSなどの名前）

auto_csv_maker_for_anki

This is a program that collects English word, which is hightlighted in kindle, and obtains meanings and phonetics automatically to csv file.
So that you can easily add them to Anki app.
キンドルのハイライト（英語）を取得して、日本語の意味と音声記号をWeblioから取得するプログラムです。Ankiにアップロードしやすいようにcsv形式で出力されます。

# Requirement

Python Libraries

* sleep
* csv
* selenium webdriver
* selenium Options
* selenium ActionChains
* selenium Keys
* pandas

 
# Usage
 
First, put your user name in 'your user name here', and put x-path of chromedriver in here chrome_path = ''.
Then type your Kindle memo and hightlight ID and password onto login_id = '' and login_pass = ''.
Finally, run the code. I call it a session.

 
# Note
 
 There would be three csv file outputs. 
 One is named 'done_words.csv'. This is kind of a repository of vocabularies that were obtained in each sessions.
 The 'new_words.csv' is a temporary repository of new vocaburaries that were obtained in the session.
 The 'new_words_anki.csv' is a csv file that will be imported to Anki app. 
 This will be rewritten after each session. So that I recommend to import the csv file to Anki after each session. 
 

# Author
 
* yuki4989
 
