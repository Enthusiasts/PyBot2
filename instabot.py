# -*- coding: utf-8 -*-
__author__ = 'vlad'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import re


limit = random.randint(500,800); # num of likes
smt = 10; # implicity wait
max=3; # кол-во хештегов
templikes=0;
def wait():
    driver.implicitly_wait(smt)

logpas = open('login','r+')
driver = webdriver.Firefox()
# логинимся на инстаком
driver.get('https://instagram.com/accounts/login/')
wait()

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
wait()

tags = ['#food', '#skate', '#surf', '#longboard', '#me', '#skateboard']

for tag in tags:
    # поиск по хештегам
    find = driver.find_element_by_class_name('-cx-PRIVATE-SearchBox__input')
    find.send_keys(tag)
    wait()
    # переход по хештегу
    human = driver.find_element_by_class_name('-cx-PRIVATE-Search__resultLink')
    human.click()
    wait()
    # открытие фоточки
    link = driver.find_elements_by_class_name('-cx-PRIVATE-PostsGrid__item')
    link[0].click()
    wait()
    i=0

    while i<(random.randint(5,15)):

        # открытие страницы человека
        person = driver.find_element_by_class_name('-cx-PRIVATE-Post__ownerUserLink')
        person.click()
        wait()
        time.sleep(5)

        # определение количества лайков которые будут поставлены человеку
        personPhotoLink = driver.find_elements_by_class_name('-cx-PRIVATE-Photo__root')
        maxLikes = random.randint(3,len(personPhotoLink))

        it = 0
        while (it < maxLikes):

            personPhotoLink[it].click()
            # ищем кнопку Лайк, отсеевая фото которые уже лайкнули
            try:
                if templikes < limit:
                    like = driver.find_element_by_link_text('Like')
                    like.click()
            except:
                pass
            else:
                templikes +=1
            # добавляем хештеги
            try:
                h1 = driver.find_element_by_class_name('-cx-PRIVATE-PostInfo__comment').text
                hashTags = re.findall(r'[#]\w+', h1)
                k=0
                if (max > len(hashTags)):
                    max = len(hashTags)
                while (k<max):
                    if ((hashTags[k] not in tags)):
                        tags.append(hashTags[k])
                    k += 1
            except:
                pass
            driver.back()
            it +=1
        i += 1
        driver.back()
        driver.back()

        time.sleep(3)
        link = driver.find_elements_by_class_name('-cx-PRIVATE-PostsGrid__item')
        link[i].click()

    driver.get('https://instagram.com/')
    time.sleep(random.randint(60,6000))


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