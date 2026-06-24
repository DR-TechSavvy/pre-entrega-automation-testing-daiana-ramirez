from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def hacer_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Configuramos una espera explícita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)
    
    # Esperamos a que el campo de usuario sea visible antes de interactuar
    username_field = wait.until(EC.visibility_of_element_by_id("user-name") if hasattr(EC, 'visibility_of_element_by_id') else EC.visibility_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Validamos con una espera explícita que la URL cambie a la página de inventario
    wait.until(EC.url_contains("/inventory.html"))