import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    # Inicializa el navegador Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Le da el control del navegador al test
    yield driver
    
    # Al terminar el test, cierra todo de forma limpia
    driver.quit()