import imp
from testdata import test_data
from lib.helpers import Helper
from pages.sign_in import SignIn
from pages.sign_up import SignUp
import json

def test_2_sign_in(driver):
    with open('creds.json', 'r') as f:
       content =  json.loads(f.read())

    helper =  Helper(driver)
    sign_in = SignIn(driver)
    helper.go_to_page(test_data.main_url)
    sign_in.login(content['email'], content['pass'])
