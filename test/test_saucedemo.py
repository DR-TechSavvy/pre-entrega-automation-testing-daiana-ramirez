import sys
import os
import time
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.funciones_auxiliares import hacer_login

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# CASO 01: AUTOMATIZACIÓN DE LOGIN
# ==========================================
def test_caso_01_login_exitoso(driver):
    """Navegar, loguearse y validar redirección a inventario"""
    hacer_login(driver)
    time.sleep(1) 
    
    assert "/inventory.html" in driver.current_url
    header_page = driver.find_element(By.CLASS_NAME, "header_secondary_container")
    assert "Products" in header_page.text
    print("¡Login exitoso y página de inventario verificada!")

# ==========================================
# CASO 02: NAVEGACIÓN Y VERIFICACIÓN DEL CATÁLOGO
# ==========================================
def test_caso_02_verificacion_catalogo(driver):
    """Validar título, presencia de productos y listar nombre/precio del primero"""
    hacer_login(driver)
    
    assert "Swag Labs" in driver.title
    
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    
    primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    assert len(primer_producto_nombre) > 0
    print(f"\n[PRODUCTO ENCONTRADO] Nombre: {primer_producto_nombre} | Precio: {primer_producto_precio}")

# ==========================================
# CASO 03: INTERACCIÓN CON EL CARRITO
# ==========================================

def test_caso_03_verificar_carrito(driver):
    """Añadir producto, verificar contador, ir al carrito y comprobar que esté ahí"""
    hacer_login(driver)
    
    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
    
    wait = WebDriverWait(driver, 10)
    contador_carrito = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    
    # 3. Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    producto_en_carrito = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    
    assert producto_en_carrito.is_displayed()
    print("¡Validación de ítem dentro del carrito exitosa!")