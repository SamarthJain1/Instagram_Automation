from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(
    service=Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
)


def login(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(5)
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
    time.sleep(2)
    print("Logged In SuccessFully")


def search_user(username):
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div",
    ).click()
    time.sleep(3)
    search = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input",
    )
    search.send_keys(username)
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]",
    ).click()
    print("User Searched SuccessFully")
    time.sleep(2)


def single_user_detail():
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


def fetch_user_detail(users):

    if isinstance(users, str):
        search_user(users)
        return single_user_detail()
    else:
        user_details = {}
        for user in users:
            time.sleep(1)
            search_user(user)
            time.sleep(1)
            data = single_user_detail()
            user_details[user] = data
            print(data)


def like_n_post(allpost=0):
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


def follow_user(username):
    search_user(username)
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


def unfollow_user(username):
    search_user(username)
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


def is_he_a_follower(From_which_account, Account_to_check):
    search_user(From_which_account)
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


def is_public_account(Account_to_check, scratch=True):
    if scratch:
        search_user(Account_to_check)
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


def home_page():
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a/div",
    ).click()
    time.sleep(3)
