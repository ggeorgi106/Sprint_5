from selenium.webdriver.common.by import By


class Locators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка «Личный кабинет»

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя» в форме регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле «Пароль»

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка «Некорректный пароль»

    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка «Войти»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка «Восстановить пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти» в форме входа

    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")  # Ссылка «Конструктор»
    LOGO_LINK = (By.XPATH, "//a[@href='/'][.//*[name()='svg']]")  # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход» в личном кабинете
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка «Булки» в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка «Соусы» в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка «Начинки» в конструкторе
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # Ссылка «Зарегистрироваться» на странице входа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ»
    LOGIN_FROM_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка «Войти» на странице восстановления пароля