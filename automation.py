# automation.py
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd


def run_automation(data):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized") 
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)


    try:
        driver.get("https://tnreginet.gov.in/portal/webHP?requestType=ApplicationRH&actionVal=homePage&screenId=114&UserLocaleID=en&_csrf=8a0e006a-0b81-4e3f-976e-9a8ee485b2ec")
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[contains(@title, 'E-Services')]").click()
        driver.find_element(By.LINK_TEXT, "Encumbrance Certificate").click()
        driver.find_element(By.LINK_TEXT, "View EC").click()

        time.sleep(4)

        # Fill form with data from FastAPI
        Select(driver.find_element(By.ID, "cmb_Zone")).select_by_value(data.zone)
        Select(driver.find_element(By.ID, "cmb_District")).select_by_value(data.district)
        Select(driver.find_element(By.ID, "cmb_SroName")).select_by_value(data.sro)
        driver.find_element(By.ID, "txt_PeriodStartDt").clear()
        driver.find_element(By.ID, "txt_PeriodStartDt").send_keys(data.ec_start_date)
        driver.find_element(By.ID, "txt_PeriodEndDt").clear()
        driver.find_element(By.ID, "txt_PeriodEndDt").send_keys(data.ec_end_date)
        Select(driver.find_element(By.ID, "cmb_Village")).select_by_value(data.village)
        driver.find_element(By.ID, "txt_SurveyNo").send_keys(data.survey_number)
        driver.find_element(By.ID, "txt_SubDivisionNo").send_keys(data.subdivision_number)
        driver.find_element(By.ID, "btn_AddSurvey").click()


        time.sleep(25)  
        driver.find_element(By.XPATH, "//a[contains(@href, 'webHP')]").click()
        time.sleep(3)  
        
    finally:
        driver.quit()
