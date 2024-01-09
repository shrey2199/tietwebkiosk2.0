import requests

from html_table_parser.parser import HTMLTableParser

from prettytable import PrettyTable

def getDateSheet(session:requests.Session):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://webkiosk.thapar.edu/StudentFiles/FrameLeftStudent.jsp',
        'Sec-Fetch-Dest': 'frame',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = session.get("https://webkiosk.thapar.edu/StudentFiles/Exam/StudViewDateSheet.jsp", headers=headers)

    table = HTMLTableParser()

    table.feed(response.text)

    dateSheet = PrettyTable(table.tables[2][0])

    for x in table.tables[2][1:]:
        dateSheet.add_row([x[0], x[1], x[2], x[3].split('(')[1].strip(')'), x[3].split('(')[0]])

    print(dateSheet)