from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

PATH = "C:\\Users\\rajag\\Desktop\\web_scraping\\chromedriver.exe"

wd = webdriver.Chrome(PATH)

# image_URL = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    url = "https://www.google.com/search?q=cats&sxsrf=APq-WBtRq3aDQ6RiInb3l8QS9-fIKh-Yzw:1643978320550&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjW4sG-iOb1AhV-3zgGHcK8B4YQ_AUoAXoECAIQAw&biw=982&bih=760&dpr=1.25#imgrc=0V922RrJgQc9SM"
    wd.get(url)

    image_urls = set()

    while len(image_urls) < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        for img in thumbnails[len(image_urls):max_images]:
            try:
                img.click()
                time.sleep(delay)

            except:
                continue

            


def dowload_image(dowload_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = dowload_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print('FAILED -', e)

# dowload_image("", image_URL, "test.jpg")
get_images_from_google(wd, 2, 10)
wd.quit()