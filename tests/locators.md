#локаторы
==test_registration_form==
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице
"//a[contains(text(),'Зарегистрироваться')]" - кнопка "Зарегистрироваться" на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода имени
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода почты
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[@value]" - поле ввода пароля
"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']" - кнопка "Зарегистрироваться" на странице регистрации
"//h2[contains(text(),'Вход')]" - заголовок "Вход" на странице логина
"//p[contains(text(),'Некорректный пароль')]" - предупреждающее сообщение о неверном пароле

==test_for_log_in_via_different_pages==
"//button[contains(text(),'Войти в аккаунт')]"  - кнопка "Войти в аккаунт" на стартовой странице
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода почты на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода пароля на странице логина
"//button[contains(text(),'Войти')]" - кнопка "Вход" на странице логина
"//button[contains(text(),'Оформить заказ')]" - кнопка "Оформить заказ" на стратовой странице после авторизации пользователя
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице
"//a[contains(text(),'Зарегистрироваться')]" - кнопка "Зарегистрироваться" на странице логина
"//a[contains(text(),'Войти')]" - кнопка войти в форме регистрации
"//a[contains(text(),'Восстановить пароль')]" - кнопка "Восстановить пароль" в "Личном кабинете"
"//a[contains(text(),'Войти')]" - кнопка "Войти" в форме восстановления пароля

==test_personal_account_link==
"//button[contains(text(),'Войти в аккаунт')]"  - кнопка "Войти в аккаунт" на стартовой странице
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода почты на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода пароля на странице логина
"//button[contains(text(),'Войти')]" - кнопка "Вход" на странице логина
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице
"//p[@class='Account_text__fZAIn text text_type_main-default']" - уникальное информационное сообщение на странице личного профиля

==test_personal_account_to_constructor==
"//button[contains(text(),'Войти в аккаунт')]"  - кнопка "Войти в аккаунт" на стартовой странице
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода почты на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода пароля на странице логина
"//button[contains(text(),'Войти')]" - кнопка "Вход" на странице логина
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице
"//p[contains(text(),'Конструктор')]" - кнопка "Конструктор" на странице личного профиля
"//h1[@class='text text_type_main-large mb-5 mt-10']" - текст заголовка на странице сборки бургера
"// div[ @class ='AppHeader_header__logo__2D0X2'] / a[@ href='/']" - логотип бургерной на странице личного профиля

==test_log_out==
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода почты на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода пароля на странице логина
"//button[contains(text(),'Войти')]" - кнопка "Вход" на странице логина
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице после логина
"//button[contains(text(),'Выход')]" - кнопка "Выход" на странице личного профиля
"//h2[contains(text(),'Вход')]" - заголовок на странице логина 

==test_constructor_tabs==
"//button[contains(text(),'Войти в аккаунт')]"  - кнопка "Войти в аккаунт" на стартовой странице
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@value]" - поле ввода почты на странице логина
"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@value]" - поле ввода пароля на странице логина
"//button[contains(text(),'Войти')]" - кнопка "Вход" на странице логина
"//p[contains(text(),'Личный Кабинет')]" - кнопка "Личный кабинет" на стартовой странице после логина
"//p[contains(text(),'Конструктор')]" - кнопка "Конструктор" на странице личного профиля
"//span[contains(text(),'Начинки')]" - таба "Начинки" на странице конструктора
"//h2[contains(text(),'Начинки')]" - заголовок раздела "Начинки"  в ленте конструктора
"//span[contains(text(),'Соусы')]" - таба "Соусы" на странице конструктора
"//h2[contains(text(),'Соусы')]" - заголовок раздела "Соусы" в ленте конструктора
"//span[contains(text(),'Булки')]" - таба "Булки" на странице конструктора
"//h2[contains(text(),'Булки')]" - заголовок раздела "Булки" в ленте конструктора









