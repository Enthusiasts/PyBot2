# -*- coding: utf-8 -*-
__author__ = 'vlad'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import re
logpas = open('login','r+')

driver = webdriver.Firefox()
# логинимся на инстаком
driver.get('https://instagram.com/accounts/login/')
driver.implicitly_wait(10)

# ввод логина
login = driver.find_element_by_id('lfFieldInputUsername')
login.send_keys(logpas.readline())

# ввод пароля
password = driver.find_element_by_id('lfFieldInputPassword')
password.send_keys(logpas.readline())
logpas.close()

# сабмит
button = driver.find_element_by_class_name('-cx-PRIVATE-LoginForm__loginButton')
button.click()
driver.implicitly_wait(10)

tags = ['#me', '#surf', '#longboard', '#skate', '#skateboard']

for tag in tags:
    # поиск по хештегам
    find = driver.find_element_by_class_name('-cx-PRIVATE-SearchBox__input')
    find.send_keys(tag)
    # переход по хештегу
    driver.implicitly_wait(10)
    human = driver.find_element_by_class_name('-cx-PRIVATE-Search__resultLink')
    human.click()
    driver.implicitly_wait(10)

    #открытие лайк и закрытие 5-15 фото
    link = driver.find_elements_by_class_name('-cx-PRIVATE-PostsGrid__item')
    i=0
    while i<(random.randint(5,15)):
        link[i].click()
        i += 1
        # если хотите лайки раскоменьте следующие 3 строки
        # like = driver.find_element_by_class_name('-cx-PRIVATE-PostInfo__likeButton')
        # like.click()
        # hash = driver.find_element_by_class_name('-cx-PRIVATE-PostInfo__comment')

        try:
            h1 = driver.find_element_by_class_name('-cx-PRIVATE-PostInfo__comment').text
            hashTags = re.findall(r'[#]\w+', h1)
            k=0
            while (k<len(hashTags)):
                print(hashTags[k])
                if ((hashTags[k] not in tags)):
                    tags.append(hashTags[k])
                    print(tags)
                k += 1
        except:
            pass
        closeButton = driver.find_element_by_class_name('-cx-PRIVATE-Modal__closeButton')
        closeButton.click()

    driver.get('https://instagram.com/')
    time.sleep(random.randint(60,100))


"""#link = driver.
link = driver.find_element_by_class_name('-cx-PRIVATE-PostsGrid__item')
link.click()

like = driver.find_element_by_class_name('-cx-PRIVATE-PostInfo__likeButton')
like.click()

closeButton = driver.find_element_by_class_name('-cx-PRIVATE-Modal__closeButton')
closeButton.click()
""""""human = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__header')
human1 = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__authorInfo')
human2 = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__usernameAndFollow')
span = driver.find_element_by_tag_name('span')
submit = driver.find_element_by_tag_name('button')"""
#submit.click()"""