def send(To_whom, Message, n, driver, By, time, Keys):
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div",
    ).click()
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div",
    ).click()
    time.sleep(3)
    input = driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input",
    )
    input.send_keys(To_whom)
    input.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div",
    ).click()
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div",
    ).click()
    time.sleep(4)
    for i in range(n):
        div_element = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p",
        )
        div_element.send_keys(Message)
        time.sleep(1)
        div_element.send_keys(Keys.RETURN)
        time.sleep(4)
        print((i + 1), "th", "Message send SuccessFully")
