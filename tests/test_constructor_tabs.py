from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStBurgers:
    def test_constructor_toppings(self,driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Конструктор')]"))).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Начинки')]"))).click()
        a = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Начинки')]"))).text
        assert a == driver.find_element(By.XPATH,"//h2[contains(text(),'Начинки')]").text

    def test_constructor_sauce(self,driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Конструктор')]"))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Соусы')]"))).click()
        a = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Соусы')]"))).text
        assert a == driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text

    def test_constructor_bread(self,driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('stevencummings@example.net')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Конструктор')]"))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Соусы')]"))).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Булки')]"))).click()
        a = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Булки')]"))).text
        assert a == driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text

