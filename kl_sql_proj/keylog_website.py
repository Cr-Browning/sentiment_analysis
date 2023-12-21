# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:32:38 2023

@author: Owner
"""
from selenium import webdriver
import key_logger
from sentiment_analysis import sentiment_analysis

driver = webdriver.Chrome()
driver.get("https://instagram.com")

if driver.current_url == "https://instagram.com":
    key_logger()
    
sentiment_analysis()