import time


def follow(username, search, By, driver, Keys):
    search(username)
    time.sleep(2)
    button = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button",
    )
    txt = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div",
    )

    if txt.text.strip() == "Follow":
        button.click()
        time.sleep(3)
        print("Account is Followed")
    else:
        print("Already following", username)


def unfollow(username, search, By, driver, Keys):
    search(username)
    time.sleep(2)
    button = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button",
    )
    # time.sleep(2)
    txt = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div",
    )
    if txt.text.strip() != "Follow":
        txt.click()
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]",
        ).click()
        time.sleep(2)
        print("Account unfollowed", username)
    else:
        print("Already unfollowed", username)


def is_he_a_follower(
    From_which_account,
    Account_to_check,
    search,
    By,
    driver,
    Keys,
    NoSuchElementException,
):
    search(From_which_account)
    time.sleep(1)
    if is_public_account(From_which_account, False):
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a",
        ).click()
        time.sleep(4)

        search = driver.find_element(
            By.XPATH,
            "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/input",
        )
        search.send_keys(Account_to_check)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            element = driver.find_element(
                By.XPATH,
                "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/span",
            )
            print("No he is not a follower.")
        except NoSuchElementException:
            print("Yes he is a follower.")
        driver.find_element(
            By.XPATH,
            "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button",
        ).click()
        time.sleep(2)
    else:
        print("Private Account cannot check")


def is_public_account(
    Account_to_check, scratch, search, driver, By, NoSuchElementException, Keys
):
    if scratch:
        search(Account_to_check)
        time.sleep(2)
    time.sleep(2)
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[1]/div/div[1]/div[2]/div/div/span",
        )
        print("This is a private Account.")
        return False
    except NoSuchElementException:
        print("This is a public Account.")
        return True
