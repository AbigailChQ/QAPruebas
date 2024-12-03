import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestCliente:
    
    def setup_method(self):
        # Configurar el WebDriver (por ejemplo, Chrome)
        self.driver = webdriver.Chrome()  # Asegúrate de poner la ruta correcta
        # Abre una página web
        self.driver.get("http://127.0.0.1:8000/dash/login")
        time.sleep(3)  # Espera a que cargue la página
        # Realiza el inicio de sesión con el correo y la contraseña
        self.driver.find_element("xpath", "//input[@id='data.email']").send_keys("qjosue091@gmail.com")
        self.driver.find_element("xpath", "//input[@id='data.password']").send_keys("Josue2905")
        self.driver.find_element("xpath", "//button[@type='submit']").click()
        # Espera unos segundos para que la página cargue completamente
        time.sleep(30)
        self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/clients']").click()
        time.sleep(40)

    def teardown_method(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()
        print("Prueba de interfaz finalizada")
    
    def test_Redireccion_Cliente(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        Guardado = self.driver.find_element("xpath", "//h1").text
        
        # Valor esperado
        GuardarEsperado = "Clientes"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    
    def test_Crear_Cliente(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        Guardado = self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/clients/create']").click()
        time.sleep(140)
        Guardado = self.driver.find_element("xpath", "//h1").text
        # Valor esperado
        GuardarEsperado = "Create Cliente"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    
    def test_Crear_Cliente(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        Guardado = self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/clients/create']").click()
        time.sleep(20)
        self.driver.find_element("xpath", "//input[@id='data.ci']").send_keys("70685423")
        self.driver.find_element("xpath", "//input[@id='data.client_cellphone_number']").send_keys("65560100")
        self.driver.find_element("xpath", "//input[@id='data.client_name']").send_keys("Ana")
        self.driver.find_element("xpath", "//input[@id='data.client_last_name']").send_keys("Choque")
        self.driver.find_element("xpath", "//input[@id='data.client_email']").send_keys("anach@gmail.com")
        self.driver.find_element("xpath", "//input[@id='data.pass']").send_keys("98ASUD$asqw")
        self.driver.find_element("xpath", "//button[@type='submit' and @id]").click()
        time.sleep(20)
        Guardado = self.driver.find_element("xpath", "//h1").text
        # Valor esperado
        GuardarEsperado = "Clientes"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    
