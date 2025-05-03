from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_prediction_form():
    try:
        # Open the webpage (adjust URL as needed)
        driver.get("http://127.0.0.1:8000")

        # Wait for the page to load
        driver.implicitly_wait(10)

        year_built = driver.find_element(By.ID, "year_built")
        year_built.send_keys("2021")

        overall_quality = driver.find_element(By.ID, "overall_quality")
        overall_quality.send_keys("9")

        total_bsmt_sf = driver.find_element(By.ID, "total_bsmt_sf")
        total_bsmt_sf.send_keys("4000")

        gr_liv_area = driver.find_element(By.ID, "gr_liv_area")
        gr_liv_area.send_keys("1000")

        full_bath = driver.find_element(By.ID, "full_bath")
        full_bath.send_keys("2")

        half_bath = driver.find_element(By.ID, "half_bath")
        half_bath.send_keys("1")

        garage_cars = driver.find_element(By.ID, "garage_cars")
        garage_cars.send_keys("2")

        garage_area = driver.find_element(By.ID, "garage_area")
        garage_area.send_keys("3")

        tot_rms_abv_grd = driver.find_element(By.ID, "tot_rms_abv_grd")
        tot_rms_abv_grd.send_keys("5000")

        fireplaces = driver.find_element(By.ID, "fireplaces")
        fireplaces.send_keys("2")

        # Find and click the 'Submit' button
        submit_button = driver.find_element(By.ID, "submit_button")  # Adjust ID as necessary
        submit_button.click()

        # Verify the result (e.g., check if result is displayed)
        result = driver.find_element(By.ID, "result")  # Adjust ID as necessary
        print(result.text)  # Output result for verification

    finally:
        driver.quit()

if __name__ == "__main__":
    test_prediction_form()