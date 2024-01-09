import requests

def loginAction(enrolNum, passwd, session:requests.Session) -> requests.Session:

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://webkiosk.thapar.edu',
        'Referer': 'https://webkiosk.thapar.edu/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'txtuType': 'Member Type',
        'UserType': 'S',
        'txtCode': 'Enrollment No',
        'MemberCode': enrolNum,
        'txtPin': 'Password/Pin',
        'Password': passwd,
        'BTNSubmit': 'Submit',
    }

    res = session.post('https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp', headers=headers, data=data)

    if "For assistance, please contact Computer Centre" in res.text:
        if "Invalid Password" in res.text:
            return session,0
        else:
            return session,2
    else:
        return session,1