import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestCita:
    
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
        self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/appointments']").click()
        time.sleep(40)

    def teardown_method(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()
        print("Prueba de interfaz finalizada")
    
    def test_Redireccion_Citas(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        Guardado = self.driver.find_element("xpath", "//h1").text
        
        # Valor esperado
        GuardarEsperado = "Citas"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    
    def test_Crear_Citas(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/appointments/create']").click()
        time.sleep(140)
        Guardado = self.driver.find_element("xpath", "//h1").text
        # Valor esperado
        GuardarEsperado = "Create Cita"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    
    
    def test_Crear_Cita(self):
        
        # Obtener el texto del avatar o del elemento que aparece después del inicio de sesión
        self.driver.find_element("xpath", "//a[@href='http://127.0.0.1:8000/dash/appointments/create']").click()
        time.sleep(20)
        
        #Cliente
        self.driver.find_element("xpath", "//select[@id='data.client_id']//ancestor::div[@tabindex]").click()
        time.sleep(5)
        self.driver.find_element("xpath", "//select[@id='data.client_id']//ancestor::div[@tabindex]//child::input").send_keys("70685423")
        time.sleep(5)
        self.driver.find_element("xpath", "//div[@id='choices--dataclient_id-item-choice-4']").click()
        #PropertyPrice
        time.sleep(5)
        self.driver.find_element("xpath", "//select[@id='data.propertyprice_id']//ancestor::div[@tabindex]").click()
        time.sleep(5)
        self.driver.find_element("xpath", "//select[@id='data.propertyprice_id']//ancestor::div[@tabindex]//child::input").send_keys("73")
        time.sleep(5)
        self.driver.find_element("xpath", "//div[@id='choices--datapropertyprice_id-item-choice-2']").click()
        #Horario
        
        time.sleep(5)
        self.driver.find_element("xpath", "//select[@id='data.schedule_id']//ancestor::div[@class='grid auto-cols-fr gap-y-2']").click()
        time.sleep(5)
        self.driver.find_element("xpath", "//select[@id='data.schedule_id']//ancestor::div[@class='grid auto-cols-fr gap-y-2']//child::option[@value='7']").click()
        #Fecha
        self.driver.find_element("xpath", "//input[@id='data.appointment_date']").send_keys("06/12/2024")
        
        self.driver.find_element("xpath", "//button[@type='submit' and @id]").click()
        time.sleep(10)
        Guardado = self.driver.find_element("xpath", "//h1").text
        # Valor esperado
        GuardarEsperado = "Citas"  # Aquí colocas lo que esperas ver
        
        # Asegurarse de que el valor obtenido es igual al esperado
        assert GuardarEsperado in Guardado, f"El valor {Guardado} no es igual al valor esperado {GuardarEsperado}"
    # Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
