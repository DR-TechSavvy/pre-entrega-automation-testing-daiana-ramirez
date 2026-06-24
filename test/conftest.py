import pytest
import os
from datetime import datetime
from selenium import webdriver

# 1. Configura automáticamente la ruta del reporte
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/reporte.html'

# 2. Fixture del Driver (Usando el gestor nativo de Selenium 4)
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    # Selenium 4.6+ se encarga de buscar el driver de tu Chrome automáticamente
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

# 3. Captura de pantalla automática en caso de falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"reports/screenshot_{timestamp}.png"
            driver_fixture.save_screenshot(file_name)
            
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(f"screenshot_{timestamp}.png"))
                report.extra = extra