from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd


d_list = []
with open('/Users/your user name here/Desktop/practice/new_words.csv',) as f:
    reader = csv.reader(f)
    for i in reader:
        d_list.append(i[0])

print(d_list)

chrome_path = '/Users/your user name here/Desktop/practice/chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url_weblio = 'https://ejje.weblio.jp/'

driver.get(url_weblio)
sleep(3)

d_list_meaning = []
d_list_phonetic = []
i = 0
while d_list[i] != d_list[-1]:
        sleep(2)
        search_bar = driver.find_element_by_class_name('formBoxITxt')
        search_btn = driver.find_element_by_class_name('formButton')
        sleep(1)
        search_bar.send_keys(d_list[i])
        search_btn.click()
        # to get meaning
        try:
                meaning = driver.find_element_by_class_name('content-explanation')
                d_list_meaning.append(meaning.text)
                sleep(1)
                try:
                    phonetic = driver.find_element_by_class_name('phoneticEjjeWrp')
                    d_list_phonetic.append(phonetic.text)
                    delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                    delete_btn.click()
                    i += 1
                except:
                    d_list_phonetic.append('phonetic was not found')
                    delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                    delete_btn.click()
                    i += 1
        except:
                print('the meaning and phonetic of', d_list[i], 'was not found')
                d_list_meaning.append('definition was not found')
                d_list_phonetic.append('phonetic was not found')
                delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                delete_btn.click()
                i += 1
        sleep(2)
        if d_list[i] == d_list[-1]:
                sleep(2)
                search_bar = driver.find_element_by_class_name('formBoxITxt')
                search_btn = driver.find_element_by_class_name('formButton')
                sleep(1)
                search_bar.send_keys(d_list[i])
                search_btn.click()
                try:
                        meaning = driver.find_element_by_class_name('content-explanation')
                        d_list_meaning.append(meaning.text)
                        sleep(1)
                        try:
                            phonetic = driver.find_element_by_class_name('phoneticEjjeWrp')
                            d_list_phonetic.append(phonetic.text)
                            delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                            delete_btn.click()
                            print("i'm done in weblio")
                            driver.close()
                            driver.quit()
                            break
                        except:
                            d_list_phonetic.append('phonetic was not found')
                            delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                            delete_btn.click()
                            print("i'm done in weblio")
                            driver.close()
                            driver.quit()
                            break
                except:
                        print('the meaning and phonetic of', d_list[i], 'was not found')
                        d_list_meaning.append('definition was not found')
                        d_list_phonetic.append('phonetic was not found')
                        delete_btn = driver.find_element_by_class_name('combo_txt_clr')
                        delete_btn.click()
                        print("i'm done in weblio")
                        driver.close()
                        driver.quit()
                        break

# This is for adding words to words.csv so that from next time, in make_anki2.py, the existing words will be filtered. 
with open('/Users/your user name here/Desktop/practice/done_words.csv', 'a', encoding='utf-8-sig', newline='\n') as f:
    writer = csv.writer(f, lineterminator='\n') 

    for i in range(len(d_list_meaning)):
        w = writer.writerow([d_list[i], d_list_meaning[i], d_list_phonetic[i]])
    f.close()

# the meaning and phonetic lists are conglomerate into one list
dim2list = [[d_list_meaning[i], d_list_phonetic[i]] for i in range(len(d_list_meaning))]

df = pd.DataFrame(dim2list, columns=['definition', 'phonetic'], index=[d_list])

# export the csv file
df.to_csv('/Users/your user name here/Desktop/practice/new_words_anki.csv', encoding='utf-8-sig')
