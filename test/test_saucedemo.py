import time
from selenium.webdriver.common.by import By

# ==========================================
# CASO 01: AUTOMATIZACIÓN DE LOGIN
# ==========================================
def test_caso_01_login_exitoso(driver):
    """Navegar, loguearse y validar redirección a inventario"""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    assert "/inventory.html" in driver.current_url
    header_page = driver.find_element(By.CLASS_NAME, "header_secondary_container")
    assert "Products" in header_page.text
    print("¡Login exitoso y página de inventario verificada!")

# ==========================================
# CASO 02: NAVEGACIÓN Y VERIFICACIÓN DEL CATÁLOGO
# ==========================================
def test_caso_02_verificacion_catalogo(driver):
    """Validar título, presencia de productos y listar nombre/precio del primero"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    # 1. Validar título de la pestaña
    assert "Swag Labs" in driver.title
    
    # 2. Validar presencia de elementos de la interfaz
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    
    # 3. Obtener y listar nombre y precio del primer producto (Mochila)
    primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    assert len(primer_producto_nombre) > 0
    print(f"\n[PRODUCTO ENCONTRADO] Nombre: {primer_producto_nombre} | Precio: {primer_producto_precio}")

# ==========================================
# CASO 03: INTERACCIÓN CON EL CARRITO
# ==========================================
def test_caso_03_verificar_carrito(driver):
    """Añadir producto, verificar contador, ir al carrito y comprobar que esté ahí"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    # Asegurarnos de que el carrito esté vacío usando la campera de Luz de Sauce (otra ID para evitar conflictos)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)
    
    # 2. Verificar que el contador del carrito se incremente a "1"
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_carrito.text == "1"
    
    # 3. Navegar al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    
    # 4. Comprobar que el producto añadido aparezca dentro del carrito
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_en_carrito == "Sauce Labs Bolt T-Shirt"
    print("¡Validación de ítem dentro del carrito exitosa!")