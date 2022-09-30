import os
import time
import random
import argparse
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    """Main function"""

    # Arguments
    parser = argparse.ArgumentParser(description='Google hangout spammer')
    parser.add_argument('-u', '--username', required=True, help='Your Google username')
    parser.add_argument('-p', '--password', required=True, help='Your Google password')
    parser.add_argument('-t', '--target', required=True, help='The target email address')
    parser.add_argument('-m', '--message', required=True, help='The message to spam')
    parser.add_argument('-i', '--interval', required=False, default=1, type=int, help='The interval between messages')
    parser.add_argument('-c', '--count', required=False, default=1, type=int, help='The number of messages to send')
    args = parser.parse_args()

    # Start the browser
    driver = webdriver.Chrome()
    driver.get('https://hangouts.google.com/')

    # Wait for the login page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'Email')))

    # Login
    driver.find_element_by_id('Email').send_keys(args.username)
    driver.find_element_by_id('next').click()
    wait.until(EC.presence_of_element_located((By.ID, 'Passwd')))
    driver.find_element_by_id('Passwd').send_keys(args.password)
    driver.find_element_by_id('signIn').click()

    # Wait for the main page to load
    wait.until(EC.presence_of_element_located((By.ID, 'gbwa')))

    # Start a new conversation
    driver.find_element_by_id('gbwa').click()
    driver.find_element_by_id('gb23').click()
    wait.until(EC.presence_of_element_located((By.ID, 'gbqfq')))
    driver.find_element_by_id('gbqfq').send_keys(args.target)
    driver.find_element_by_id('gbqfb').click()

    # Wait for the conversation to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'vN')))

    # Spam the message
    for i in range(args.count):
        driver.find_element_by_class_name('vN').send_keys(args.message)
        driver.find_element_by_class_name('vO').click()
        time.sleep(args.interval)

    # Close the browser
    driver.close()


if __name__ == '__main__':
    main()