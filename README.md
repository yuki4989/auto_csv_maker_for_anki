# Name

auto_csv_maker_for_anki

This is a program that collects English word, which is hightlighted in kindle, and obtains meanings and phonetics of Japanese automatically to csv file.
So that you can easily add them to Anki app.<br>
キンドルのハイライト（英語単語）を取得して、日本語の意味と音声記号をWeblioから取得するプログラムです。Ankiにアップロードしやすいようにcsv形式で出力されます。

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
 There would be three csv file outputs. <br>
 One is named 'done_words.csv'. This is kind of a repository of vocabularies that were obtained in each sessions. From next session, a redundant word will be detected by refering to this file. <br>
 The 'new_words.csv' is a temporary repository of new vocaburaries that were obtained in the session.<br>
 The 'new_words_anki.csv' is a csv file that will be imported to Anki app. <br>
 This will be rewritten after each session. So that I recommend to import this file to Anki after each session. 
 <br>
 <br>
First, put your user name in 'your user name here', and put x-path of chromedriver in here chrome_path = '' in the code.<br>
Then type your Kindle memo and hightlight ID and password in login_id = '' and login_pass = '' in the code.<br>
Finally, run the code. I call it a session.

# Note
You can change the output place of the csv files by changing the x-path wherever you'd like to.

 

# Author
 
* yuki4989
 

