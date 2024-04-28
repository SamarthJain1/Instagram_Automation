import time


def search_user(username, driver, By, Keys):
    time.sleep(2)

    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div",
    ).click()
    time.sleep(4)
    search = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input",
    )
    search.send_keys(username)
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    outer_div = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div",
    )
    span_tags = outer_div.find_elements(
        By.XPATH, ".//span[contains(@class, 'x1lliihq x1plvlek xryxfnj x1n2onr6')]"
    )
    for tag in span_tags:
        if tag.text.strip() == username:
            tag.click()
            break
