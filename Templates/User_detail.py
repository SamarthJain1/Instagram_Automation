import time
from InstaBot.Templates.Search import *


def single_user_detail(driver, By, Keys):
    map = {}
    time.sleep(1)
    user_name = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/a/h2",
    ).text
    map["Insta Profile"] = user_name
    map["Posts"] = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span",
    ).text
    map["Followers"] = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span",
    ).text
    map["Following"] = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span",
    ).text
    map["User Name"] = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]/span",
    ).text
    map["Description"] = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1",
    ).text
    time.sleep(1)
    return map


def fetch_user_detail(users, driver, By, Keys):

    if isinstance(users, str):
        search_user(users, driver, By, Keys)
        return single_user_detail()
    else:
        user_details = {}
        for user in users:
            time.sleep(1)
            search_user(user, driver, By, Keys)
            time.sleep(1)
            data = single_user_detail(driver, By, Keys)
            user_details[user] = data
            print(data)
