from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStBurgers:
    def test_log_in_by_enter(self,driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Оформить заказ')]"))).text
        assert a == 'Оформить заказ'

    def test_log_in_by_personal_account(self,driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Оформить заказ')]"))).text
        assert a == 'Оформить заказ'

    def test_log_in_by_registration_form(self,driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Оформить заказ')]"))).text
        assert a == 'Оформить заказ'

    def test_log_in_by_reset_password(self,driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Оформить заказ')]"))).text
        assert a == 'Оформить заказ'

