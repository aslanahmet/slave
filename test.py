import datetime
import os
import sys
import time
import string
import random
import codecs
import MySQLdb
import xlrd
import unittest
import traceback
import ConfigParser
import re
import requests
import pytz
import editdistance
from jenkinsapi.jenkins import Jenkins
from pytz import timezone
from raven import Client
from functools import wraps
from selenium import webdriver
from datetime import timedelta
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from Levenshtein import distance
from selenium.webdriver.supportd.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from argparse import Namespace
import json
import httplib2
import paramiko
import selenium


driver = webdriver.Remote(
            command_executor='http://52.31.209.74:5550/wd/hub',
            desired_capabilities={'browserName': 'chrome'})
driver.get('https:www.google.com')