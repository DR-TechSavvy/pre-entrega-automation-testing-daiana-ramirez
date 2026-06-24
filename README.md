# Pre-Entrega Automation Testing

## Propósito del Proyecto
Este proyecto es la pre-entrega del curso de automatización de QA. El objetivo principal es demostrar la capacidad para automatizar flujos básicos de navegación web interactuando con elementos, utilizando estrategias de localización, validando estados y aplicando esperas explícitas en el sitio de pruebas [Saucedemo](https://www.saucedemo.com/).

## Tecnologías Utilizadas
* **Python**: Lenguaje principal.
* **Selenium WebDriver**: Herramienta de automatización y control del navegador.
* **Pytest**: Framework para la estructura y ejecución de las pruebas.
* **pytest-html**: Plugin para la generación de reportes de ejecución.

## Instalación de Dependencias
Para ejecutar este proyecto, es necesario clonar el repositorio e instalar las dependencias requeridas. Ejecutar el siguiente comando en la terminal:

```bash
pip install -r requirements.txt

## Cómo ejecutar las pruebas
Para correr todos los casos de prueba y generar automáticamente el reporte de resultados, ejecutar el siguiente comando desde la raíz del proyecto:

```bash
pytest test/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html