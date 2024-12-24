from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://nvrc.perfectmind.com/23734/Clients/BookMe4LandingPages/CoursesLandingPage?widgetId=a28b2c65-61af-407f-80d1-eaa58f30a94a&redirectedFromEmbededMode=False&courseId=2b0a99c4-45d7-46af-a691-82dbb7624a8e"

def book_badminton(url):
    # Basic Chrome options without profile
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    
    print("Starting new Chrome session...")
    driver = webdriver.Chrome(options=options)
    
    try:
        print("Opening URL...")
        driver.get(url)
        
        # Wait for manual login
        print("Please log in manually in the browser window...")
        input("Press Enter after you've logged in to start monitoring spots...")
        
        while True:
            try:
                # Wait for spots label to be visible
                spots_label = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "spots"))
                )
                
                # Get and print the current availability
                print(f"Current status: {spots_label.text}")
                
                # Check if spots are available
                if "Full" not in spots_label.text:
                    # Find and click book button
                    book_button = driver.find_element(By.ID, "bookEventButton")
                    book_button.click()
                    print("Successfully clicked book button!")
                    time.sleep(30)  # Keep browser open for 30 seconds after success
                    break
                
                print("Spot is full, refreshing...")
                time.sleep(1)  # Wait 1 second before refresh
                driver.refresh()

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)
                driver.refresh()
                
    except Exception as e:
        print(f"Critical error: {e}")
    finally:
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == "__main__":
    book_badminton(URL)