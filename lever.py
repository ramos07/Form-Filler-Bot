from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import yaml
import os


def open_file():
    try:
        print("Getting application content ready")
        # Parse YAML file with Lever application details and return those details
        with open("lever.yaml") as lever_file:
            lever_app_details = yaml.load(lever_file, Loader=yaml.FullLoader)
            return lever_app_details
        print("Finished getting application details.")
        pass
    except Exception as e:
        print("Something went wrong with opening the YAML file: ", (e))
        pass

def fill_application(application_details):
    try:
        print("Filling out application")

        # Keep the browser window open
        custom_options = Options()
        custom_options.add_experimental_option("detach", True)

        browser = webdriver.Chrome(options=custom_options)


        browser.get((LEVER_APPLICATION_URL))

        # Find the resume upload input element and attach the resume 
        resume_input = browser.find_element_by_name("resume")
        resume_input.send_keys(os.getcwd()+"/"+application_details["resume_file_name"])

        # Find the name input element and send in the fullname
        fullname_input = browser.find_element_by_name("name")
        fullname_input.send_keys(application_details["fullname"])

        # Find the email input element and send in the email
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys(application_details["email"])

        # Find the name input element and send in the phone
        phone_input = browser.find_element_by_name("phone")
        phone_input.send_keys(application_details["phone"])

        # Find the current company input element and send in the current company
        current_company_input = browser.find_element_by_name("org")
        current_company_input.send_keys(application_details["current_company"])

        # Find the LinkedIn input element and send in the LinkedIn URL
        linkedin_input = browser.find_element_by_name("urls[LinkedIn]")
        linkedin_input.send_keys(application_details["linkedin_url"])

        # Find the Twitter input element and send in the Twitter URL
        linkedin_input = browser.find_element_by_name("urls[Twitter]")
        linkedin_input.send_keys(application_details["twitter_url"])

        # Find the GitHub input and send in GitHub URL
        github_input = browser.find_element_by_name("urls[GitHub]")
        github_input.send_keys(application_details["github_url"])

        # Find portfolio input and send in portfolio URL
        portfolio_input = browser.find_element_by_name("urls[Portfolio]")
        portfolio_input.send_keys(application_details["portfolio_url"])

        # Find the Others input element and send in other URL
        linkedin_input = browser.find_element_by_name("urls[Other]")
        linkedin_input.send_keys(application_details["other_url"])

        # Confirm process is done
        print("Filled out application.")
        # pass
    except Exception as e:
        print("There was an error filling out the application: ",(e))
        pass

LEVER_APPLICATION_URL = input("Enter url of Lever job application: ")
app_details = open_file()
fill_application(app_details)