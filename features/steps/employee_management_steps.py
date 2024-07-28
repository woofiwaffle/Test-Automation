from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
import csv
import os

WAIT_TIMEOUT = 10

def generate_random_string(length=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_employee_id(length=4):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))

def take_screenshot(context, step_name):
    screenshots_dir = 'features/screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    screenshot_file = os.path.join(screenshots_dir, f'{step_name}.png')
    context.driver.save_screenshot(screenshot_file)

@given('I am logged in as an admin')
def step_given_i_am_logged_in_as_admin(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username_field = WebDriverWait(context.driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    password_field = context.driver.find_element(By.NAME, 'password')
    username_field.send_keys('Admin')
    password_field.send_keys('admin123')
    login_button = context.driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

@when('I navigate to the "Add Employee" page')
def step_when_i_navigate_to_add_employee_page(context):
    pim_menu = WebDriverWait(context.driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))
    )
    pim_menu.click()

    add_employee_button = WebDriverWait(context.driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Add Employee"]'))
    )
    add_employee_button.click()
    time.sleep(2)


@when('I fill in the employee details')
def step_when_i_fill_in_employee_details(context):
    context.first_name = generate_random_string()
    context.last_name = generate_random_string()
    context.employee_id = generate_random_employee_id()

    first_name_field = WebDriverWait(context.driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.NAME, 'firstName'))
    )
    last_name_field = context.driver.find_element(By.NAME, 'lastName')
    employee_id_field = context.driver.find_element(By.XPATH,
                                                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')

    first_name_field.send_keys(context.first_name)
    last_name_field.send_keys(context.last_name)
    employee_id_field.clear()
    employee_id_field.send_keys(context.employee_id)

    save_button = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
    WebDriverWait(context.driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(save_button))
    save_button.click()
    time.sleep(10)
    take_screenshot(context, 'employee_details')