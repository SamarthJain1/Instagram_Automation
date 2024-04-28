import time


def fresh_login(username, password, driver, By, Keys, NoSuchElementException):
    driver.get("https://www.instagram.com/")
    time.sleep(4)
    input_field = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
    )

    input_field.send_keys(username)

    password_field = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(4)
    print("Logged In SuccessFully")
    time.sleep(3)
    try:
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div",
        ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        ).click()
        time.sleep(2)

    except NoSuchElementException:
        print()
    driver.refresh()
    time.sleep(4)
