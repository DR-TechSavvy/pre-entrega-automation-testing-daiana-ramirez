import pytest
import time
from selenium.webdriver.common.by import By

def test_caso_01_login_exitoso(driver):
    """Verificar el inicio de sesión con credenciales válidas"""
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) # Pausa temporal para ver que abre bien
    assert "Swag Labs" in driver.title

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