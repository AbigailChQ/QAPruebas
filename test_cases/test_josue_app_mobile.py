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

def test_verify_nombre(driver):

    correito = "qjosue091@gmail.com"
    contrasenita = "Josue2905"
    esperado = "Bienvenido, Josue Giovanny"
   
    email_input = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/emailEditText"]')
    email_input.send_keys(correito)
    time.sleep(2)
    
    contrasenita_input = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.example.vision:id/passwordEditText"]')
    contrasenita_input.send_keys(contrasenita)
    time.sleep(2)

    entrar_button = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/loginButton"]')
    entrar_button.click()
    time.sleep(5)
    
    actual = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.example.vision:id/userNameTextView"]').text
    print("++++++++++++++++++ Nombre de usuario: ", actual)
    assert actual == esperado
    
    fin_button = driver.find_element(By.XPATH, '(//android.widget.Button[@resource-id="com.example.vision:id/buttonFinalizeAppointment"])')
    fin_button.click()
    time.sleep(3)

    salir_button = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.example.vision:id/buttonS"]')
    salir_button.click()
    time.sleep(3)
    
