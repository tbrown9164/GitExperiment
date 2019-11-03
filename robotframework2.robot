*** Settings ***
Documentation  free text documentation here displayed in console at runtime
Library   Selenium2Library
Suite Setup  GotoSite
#Suite Teardown  Close Browser      #knows to run after tcs are done

*** Variables ***
${Browser}  Chrome
${URL}  =  https:///opensource-demo.orangehrmlive.com
${HOMEPAGE}    http://www.cars.com
${LoginButton}   menuitem
${USERNAME}    tom.brown@noemail.com
@{Userlist}    User1   User2
${PASSWORD}    wrongpassword


*** Test Cases ***    USERNAME    PASSWORD
Valid Open
    [Documentation]   documentation must start intented (this is a note from me)
    [Tags]  Smoke
    Set Selenium Speed    4
    Set Browser Implicit Wait    5
    Input Text       id=txtUsername   ${Userlist}[1]
    Input Password   id=txtPassword    ${PASSWORD}
    Click Button     id=btnLogin      #no variable for this one
    page should contain element   id=spanMessage   "Invalid credentials"   #invalid credential message
    #Open Browser   http://www.thetestingworld.com/testings
    #Goto Site  works here at the tc level
    Log             Test completed

*** Keywords ***
Goto Site   Open Browser  https:///opensource-demo.orangehrmlive.com


