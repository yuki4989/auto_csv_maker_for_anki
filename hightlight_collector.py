from time import sleep

import csv
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd

#put chromedriver in the same place with this file
chrome_path = '/Users/your user name/Desktop/practice/chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

# kindle memo and hightlight url
url = 'https://read.amazon.co.jp/kp/notebook'

driver.get(url)

sleep(3)
# enter your id and password of kindle memo and hightlight
login_id = ''
login_pass = ''

# login
fill_email = driver.find_element_by_id('ap_email')
fill_email.send_keys(login_id)
sleep(2)

fill_password = driver.find_element_by_id('ap_password')
fill_password.send_keys(login_pass)
sleep(2)

login_btn = driver.find_element_by_class_name('a-button-input')
login_btn.click()
sleep(6)

# find the area of each books in left side that can be clicked to choose.
book_ttls = driver.find_elements_by_class_name('kp-notebook-library-each-book')

d_list_1 = []
i = 0
pattern = re.compile(r'^[a-zA-Z(),<>:;-]')
while book_ttls[i] != book_ttls[-1]:
        book_ttls[i].click()
        # This has to be more than 3 or 4 seconds otherwise book title doesn't emerge and can't get the title.
        sleep(8)
        book_ttl = driver.find_element_by_css_selector('h3.a-spacing-top-small').text
        result = pattern.search(book_ttl) is not None
        if result == True:
                # This also takes few second to load the latest hightlights at the bottom.
                sleep(6)
                hightlights = driver.find_elements_by_css_selector('.kp-notebook-highlight-yellow > span')
                sleep(1)
                for hightlight in hightlights:
                        d = hightlight.text.strip(',' + '“' + '.”' + '.' + '’' + '‘' + ':')
                        sleep(1)
                        d_list_1.append(d)                     
                i += 1
        else:
                i += 1
if book_ttls[i] == book_ttls[-1]: 
        book_ttls[i].click()
        sleep(8)
        book_ttl = driver.find_element_by_css_selector('h3.a-spacing-top-small').text
        result = pattern.search(book_ttl) is not None
        if result == True:
                sleep(6)
                hightlights = driver.find_elements_by_css_selector('.kp-notebook-highlight-yellow > span')
                sleep(1)
                for hightlight in hightlights:
                        d = hightlight.text.strip(',' + '“' + '.”' + '.' + '’' + '‘' + ':' + '’s')
                        sleep(1)
                        d_list_1.append(d)
                print('im done')
                driver.close()
                driver.quit()
        else:
                print('im done')
                driver.close()
                driver.quit()

# extract only a word not a sentence.
pattern2 =  re.compile(r'[ ]')
d_list = []
for d_list_ns in d_list_1:
        result = pattern2.search(d_list_ns) is None
        if result == True:
                d_list.append(d_list_ns)

print('only word:', d_list)
print(len(d_list))

done_words = []
with open('/Users/your user name here/Desktop/practice/done_words.csv', 'r') as f:
        # load csv data
        reader = csv.reader(f)
        # skip label data
        header = next(reader)
        for r in reader:
                done_words.append(r[0])
        f.close()
        # delete duplicate
        d_and_done = set(d_list) ^ set(done_words)
        d_and_done.remove('')
        print(d_and_done)

if len(d_and_done) == 0:
        print('no new word')
        exit()

data = pd.DataFrame(d_and_done)
data.to_csv('/Users/your user name here/Desktop/practice/new_words.csv', index=False, header=False)
import meaning_collector
