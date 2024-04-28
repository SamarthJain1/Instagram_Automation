import time


def like_post(allpost, driver, By, Keys):
    time.sleep(5)
    post_number = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span",
    ).text

    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div/div[1]/a/div[1]/div[2]",
    ).click()

    time.sleep(3)

    # like button heart
    driver.find_element(
        By.XPATH,
        "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div/span",
    ).click()
    time.sleep(2)

    # next post button
    driver.find_element(
        By.XPATH,
        "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button",
    ).click()

    # like for remaining post and if
    if allpost > 0:
        for _ in range(min(int(post_number) - 2, allpost)):
            time.sleep(3)
            driver.find_element(
                By.XPATH,
                "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div/span",
            ).click()
            time.sleep(3)
            driver.find_element(
                By.XPATH,
                "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button",
            ).click()

        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div/span",
        ).click()

    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div").click()
    time.sleep(2)
    print("Liked All Post")
