import pytest
import time
from selenium.webdriver.common.by import By

def test_caso_01_login_exitoso(driver):
    """Verificar el inicio de sesión con credenciales válidas"""
    # 1. Abrir la página
    driver.get("https://www.saucedemo.com/")
    time.sleep(1) # Pausa cortita para ver el proceso
    
    # 2. Encontrar los campos e ingresar los datos
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    
    # 3. Hacer clic en el botón de Login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) # Pausa para ver que entramos a la tienda
    
    # 4. Validar que entramos (comprobando la URL o un elemento de la tienda)
    assert "inventory.html" in driver.current_url
    print("¡Login exitoso verificado!")

def test_caso_02_agregar_al_carrito(driver):
    """Verificar la adición de productos al carrito de compras"""
    driver.get("https://www.saucedemo.com/")
    # Aquí irá la lógica para agregar productos
    pass

def test_caso_03_compra_exitosa(driver):
    """Verificar el flujo completo de checkout exitoso"""
    driver.get("https://www.saucedemo.com/")
    # Aquí irá el flujo final de facturación
    pass