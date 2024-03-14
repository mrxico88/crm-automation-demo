*** Settings ***
Library  BuiltIn
Library    ../page_objects/Login.py
Library    ../page_objects/Navigation.py
Library    ../page_objects/Account.py
Library    Browser
*** Variables ***

*** Test Cases ***
Test Create A New Account
    Login To Microsoft Dynamic 365
    Open Accounts
    Create New Account
    Assert Created Account Has Correct Name

