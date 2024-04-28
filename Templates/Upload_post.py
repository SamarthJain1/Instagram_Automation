def post_upload(Image_Url, Caption, time, driver, By, NoSuchElementException, Keys):
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div",
    ).click()
    # time.sleep(1)
    # driver.find_element(
    #     By.XPATH,
    #     "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/div/div/div[1]/a[1]/div[1]",
    # ).click()
    time.sleep(3)
    upload_file = driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/form/input",
    )
    time.sleep(2)
    upload_file.send_keys(Image_Url)
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div",
    ).click()
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div",
    ).click()
    time.sleep(2)
    caption = driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/p",
    )
    caption.send_keys(Caption)
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div",
    ).click()
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div").click()
    time.sleep(3)

    print("Post Uploaded Succesfully")
