import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Aseguramos que Python encuentre la carpeta utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.funciones_auxiliares import hacer_login

# ==========================================
# CASO 01: AUTOMATIZACIÓN DE LOGIN
# ==========================================
def test_caso_01_login_exitoso(driver):
    """Navegar, loguearse y validar redirección a inventario"""
    hacer_login(driver)
    
    wait = WebDriverWait(driver, 10)
    
    # Criterio mínimo: Validación de /inventory.html
    assert "/inventory.html" in driver.current_url
    
    # Criterio mínimo: Validación de “Products/Swag Labs”
    header_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert "Products" in header_title.text
    assert "Swag Labs" in driver.title
    
    print("¡Login exitoso y página de inventario verificada!")

# ==========================================
# CASO 02: NAVEGACIÓN Y VERIFICACIÓN DEL CATÁLOGO
# ==========================================
def test_caso_02_verificacion_catalogo(driver):
    """Validar título, presencia de productos y listar nombre/precio del primero"""
    hacer_login(driver)
    wait = WebDriverWait(driver, 10)
    
    # Validar título
    assert "Swag Labs" in driver.title
    
    # Validar que elementos importantes de la interfaz estén presentes
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))).is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    
    # Validar presencia de productos y obtener el primero
    primer_producto_nombre = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text
    primer_producto_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    assert len(primer_producto_nombre) > 0
    assert len(primer_producto_precio) > 0
    print(f"\n[PRODUCTO ENCONTRADO] Nombre: {primer_producto_nombre} | Precio: {primer_producto_precio}")

# ==========================================
# CASO 03: INTERACCIÓN CON EL CARRITO
# ==========================================
def test_caso_03_verificar_carrito(driver):
    """Añadir producto, verificar contador, ir al carrito y comprobar que esté ahí"""
    hacer_login(driver)
    wait = WebDriverWait(driver, 10)
    
    # Capturamos el nombre del producto antes de hacer clic para compararlo después
    producto_a_agregar = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text
    
    # 1. Añadir el primer producto al carrito
    boton_agregar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_inventory")))
    boton_agregar.click()
    
    # 2. Verificar que el contador del carrito se incremente correctamente a "1"
    contador_carrito = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert contador_carrito.text == "1", "El contador del carrito no se incrementó a 1"
    
    # 3. Navegar al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 4. Comprobar que el producto añadido aparezca correctamente en el carrito
    producto_en_carrito = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    assert producto_en_carrito.is_displayed()
    assert producto_en_carrito.text == producto_a_agregar, "El ítem en el carrito no coincide con el que agregamos"
    
    print("¡Validación de ítem dentro del carrito exitosa!")