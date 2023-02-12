from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStBurgers:
    def test_personal_account_to_constructor_by_constructor_button(self,driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Конструктор')]"))).click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[@class='text text_type_main-large mb-5 mt-10']"))).text
        assert a == 'Соберите бургер'


    def test_personal_account_to_constructor_by_logo(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "// div[ @class ='AppHeader_header__logo__2D0X2'] / a[@ href='/']"))).click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']"))).text
        assert a == 'Соберите бургер'
