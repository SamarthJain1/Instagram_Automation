from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from InstaBot.Templates.Login import *
from InstaBot.Templates.Search import *
from InstaBot.Templates.User_detail import *
from InstaBot.Templates.PostLike import *
from InstaBot.Templates.Follow_Unfollow import *
from InstaBot.Templates.Message_send import *
from InstaBot.Templates.Upload_post import *


import time


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(
    service=Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
)


def login(username, password):
    fresh_login(username, password, driver, By, Keys, NoSuchElementException)


def search(username):
    search_user(username, driver, By, Keys)


def user_detail(users):
    return fetch_user_detail(users, driver, By, Keys, NoSuchElementException)


def like_n_post(username, allpost=0):
    home_page()
    search(username)
    like_post(allpost, driver, By, Keys)


def follow_user(username):
    follow(username, search, By, driver, Keys)


def unfollow_user(username):
    unfollow(username, search, By, driver, Keys)


def is_public_account(username, scratch=True):
    is_public_account(
        username, scratch, search, driver, By, NoSuchElementException, Keys
    )


def is_he_a_follower(From_which, To_check):
    is_he_a_follower(
        From_which,
        To_check,
        search(From_which),
        By,
        driver,
        Keys,
        NoSuchElementException,
    )


def home_page():
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a/div",
    ).click()
    time.sleep(3)


def send_message(username, message, n=1):
    send(username, message, n, driver, By, time, Keys)


def upload_post(Image_Url, Caption):
    post_upload(Image_Url, Caption, time, driver, By, NoSuchElementException, Keys)


def convert_excel(data):
    convert(data)
