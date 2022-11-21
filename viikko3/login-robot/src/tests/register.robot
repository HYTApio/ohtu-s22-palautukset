*** Settings ***
Resource  resource.robot
Test Setup  Create User Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input Create User Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be atleast 3 characters and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Password must be atleast 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain      Password must contain letters and numbers

*** Keywords ***
Create User Command
    Input Create User Command
