import time

from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class LoginTest(LiveServerTestCase):

    def test_sign_up(self):
        selenium = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
        time.sleep(2)
        selenium.get('http://127.0.0.1:8000/')
        time.sleep(2)
        login = selenium.find_element(By.ID, 'login-id')
        login.click()
        time.sleep(2)
        sign_up = selenium.find_element(By.LINK_TEXT, 'sign up here')
        sign_up.click()

        form_username = selenium.find_element(By.ID, 'id_username')
        form_username.send_keys('NewUser')

        form_password1 = selenium.find_element(By.ID, 'id_password1')
        form_password1.send_keys('NoveHeslo123')

        form_password2 = selenium.find_element(By.ID, 'id_password2')
        form_password2.send_keys('NoveHeslo123')

        form_biography = selenium.find_element(By.ID, 'id_biography')
        form_biography.send_keys("Moje biografie......................"
                                 "...................................."
                                 "...................................."
                                 "....................................")

        form_submit = selenium.find_element(By.ID, 'btn-submit')
        form_submit.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Welcome in our movie database.' in selenium.page_source

    def test_login(self):
        selenium = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
        #selenium = webdriver.Firefox(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        #selenium = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        time.sleep(2)
        selenium.get('http://127.0.0.1:8000/')
        time.sleep(2)
        login = selenium.find_element(By.ID, 'login-id')
        login.click()
        time.sleep(2)

        form_username = selenium.find_element(By.ID, 'id_username')
        form_password = selenium.find_element(By.ID, 'id_password')

        form_username.send_keys('User1')
        form_password.send_keys('Heslo123')
        time.sleep(2)

        form_submit = selenium.find_element(By.ID, 'btn-submit')
        form_submit.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Welcome in our movie database.' in selenium.page_source


class CountryFormTest(LiveServerTestCase):

    def test_new_country(self):
        selenium = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")
        # selenium = webdriver.Firefox(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        # selenium = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        time.sleep(2)
        selenium.get('http://127.0.0.1:8000/')
        time.sleep(2)
        login = selenium.find_element(By.ID, 'login-id')
        login.click()
        time.sleep(2)

        form_username = selenium.find_element(By.ID, 'id_username')
        form_password = selenium.find_element(By.ID, 'id_password')

        form_username.send_keys('User1')
        form_password.send_keys('Heslo123')
        time.sleep(2)

        form_submit = selenium.find_element(By.ID, 'btn-submit')
        form_submit.send_keys(Keys.RETURN)
        time.sleep(2)

        countries_link = selenium.find_element(By.LINK_TEXT, 'Countries')
        countries_link.click()
        time.sleep(2)

        create_country_link = selenium.find_element(By.LINK_TEXT, 'Create new country')
        create_country_link.click()
        time.sleep(2)

        form_country_name = selenium.find_element(By.ID, 'id_name')
        form_country_name.send_keys('Finland')
        time.sleep(2)

        form_county_abbreviation = selenium.find_element(By.ID, 'id_abbreviation')
        form_county_abbreviation.send_keys('FI')
        time.sleep(2)

        submit = selenium.find_element(By.TAG_NAME, 'button')
        submit.send_keys(Keys.RETURN)
        time.sleep(2)

        assert 'Finland (FI)' in selenium.page_source
