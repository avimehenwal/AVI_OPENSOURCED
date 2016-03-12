*** Test Cases ***
Normal Error
    Fail    This is a rather boring example...

HTML Error
    ${number} =   ${14} 
    Should Be Equal    ${number}    42    *HTML* Number is not my <b>MAGIC</b> number.
