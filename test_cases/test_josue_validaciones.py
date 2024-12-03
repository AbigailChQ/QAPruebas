import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "DI7PTSGUTG85HIPF"
    options.app_package = "com.example.vision"
    options.app_activity = ".MainActivity"
    options.new_command_timeout = 600
    options.adbExecTimeout = 120000
    options.connect_hardware_keyboard = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_login_espacios_vacios(driver):
    correito = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/emailEditText"]')
    correito.clear()
    contrasenita = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/passwordEditText"]')
    contrasenita.clear()
    botoncito = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/loginButton"]')
    botoncito.click()
    time.sleep(2)
    print("Prueba con campos vacíos realizada. Verifica manualmente el comportamiento.")

def test_login_usuario_incorrecto(driver):
    correito = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/emailEditText"]')
    correito.clear()
    correito.send_keys("usuario_falso@gmail.com")
    contrasenita = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/passwordEditText"]')
    contrasenita.clear()
    contrasenita.send_keys("clave_invalida")
    botoncito = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/loginButton"]')
    botoncito.click()
    time.sleep(2)
    print("Prueba con usuario y contraseña incorrectos realizada. Verifica manualmente el comportamiento.")

def test_login_solo_usuario(driver):
    correito = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/emailEditText"]')
    correito.clear()
    correito.send_keys("qjosue091@gmail.com")
    contrasenita = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/passwordEditText"]')
    contrasenita.clear()
    botoncito = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/loginButton"]')
    botoncito.click()
    time.sleep(2)
    print("Prueba con solo correo electrónico realizada. Verifica manualmente el comportamiento.")

def test_login_solo_contrasena(driver):
    correito = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/emailEditText"]')
    correito.clear()
    contrasenita = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/passwordEditText"]')
    contrasenita.clear()
    contrasenita.send_keys("Josue2905")
    botoncito = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/loginButton"]')
    botoncito.click()
    time.sleep(2)
    print("Prueba con solo contraseña realizada. Verifica manualmente el comportamiento.")
