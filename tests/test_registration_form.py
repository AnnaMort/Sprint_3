from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

faker = Faker()

class TestStBurgers:
    def test_registration_successful(self,driver):
        email = faker.email()
        print(email)
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH,"//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]").send_keys('Anya')
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]").send_keys(email)
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[@value]").send_keys('123456')
        driver.find_element(By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        a = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h2[contains(text(),'Вход')]"))).text
        assert a == 'Вход'

    def test_registration_with_incorrect_password(self, driver):
        email = faker.email()
        print(email)
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[@value]").send_keys('123')
        driver.find_element(By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'






