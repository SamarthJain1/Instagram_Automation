import pandas as pd

import time
from InstaBot.Templates.Search import *


def single_user_detail(driver, By, Keys, NoSuchElementException):
    map = {}
    time.sleep(3)

    try:
        user_name = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/a/h2",
        ).text
        map["Insta Profile"] = user_name
    except NoSuchElementException:
        map["Insta Profile"] = None

    try:
        map["Posts"] = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span",
        ).text
    except NoSuchElementException:
        map["Posts"] = None

    try:
        map["Followers"] = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span",
        ).text
    except NoSuchElementException:
        map["Followers"] = 0

    try:
        map["Following"] = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span",
        ).text
    except NoSuchElementException:
        map["Following"] = 0

    try:
        map["User Name"] = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]/span",
        ).text
    except NoSuchElementException:
        map["User Name"] = map["Insta Profile"]

    try:
        map["Description"] = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1",
        ).text
    except NoSuchElementException:
        map["Description"] = None

    time.sleep(1)
    return map


def fetch_user_detail(users, driver, By, Keys, NoSuchElementException):

    if isinstance(users, str):
        search_user(users, driver, By, Keys)
        return single_user_detail(driver, By, Keys, NoSuchElementException)
    else:
        user_details = []
        for user in users:
            time.sleep(1)
            search_user(user, driver, By, Keys)
            time.sleep(1)
            data = single_user_detail(driver, By, Keys, NoSuchElementException)
            user_details.append(data)
        return user_details


def convert(data):
    df = pd.DataFrame(data)

    df.to_excel("Instagram_Data.xlsx", index=False)

    print("Excel file created successfully.")
