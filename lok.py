from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



   
browser = webdriver.Firefox()
browser.implicitly_wait(0)  # Set implicit wait time to 0

browser.get('https://www.instagram.com/')

    # Wait for the username input field to be visible
username_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )

    # Enter the username
username_input.send_keys('murtazo__204')

    # Wait for the password input field to be visible
password_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    )

    # Enter the password
password_input.send_keys('Murtazo$$08')

    # Wait for the login button to be clickable
login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Click the login button
login_button.click()

    # Wait for the page to load after login
WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='button']"))
    )

try:
        # Find and click the "Not Now" button if it's present
        not_now_button = browser.find_element(By.CSS_SELECTOR, "div[role='button']")
        not_now_button.click()
        sleep(3)  # Wait for the actions to be performed
except Exception as e:
        print('The "Not Now" button was not found:', e)

 


try:
    # Go to the specified tag page and find the first post to like
    browser.get(f'https://www.instagram.com/explore/tags/ufc/')
    sleep(2)

    # Find the first post to like
    first_post = browser.find_element(By.CSS_SELECTOR, "a[href$='/p/']")

    # Scroll to the parent container of the post
    container = first_post.find_element(By.XPATH, "ancestor::div[1]")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", container)

    # Perform actions on the post
    actions = ActionChains(browser)
    actions.move_to_element(first_post).click().perform()
    sleep(2)

    # Find the like button and click it
    like_button = first_post.find_element(By.CSS_SELECTOR, "button[aria-label='Like']")
    like_button.click()

    sleep(2)

    # Find the close button and click it
    close_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Close']")
    close_button.click()


    
    sleep(2)

except:
    print('error')  



# Login to Instagram


# Like a post with the specified tag


# Close the browser