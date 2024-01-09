import requests

from html_table_parser.parser import HTMLTableParser

from prettytable import PrettyTable

def getSeatingPlan(session:requests.Session):

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

    response = session.get('https://webkiosk.thapar.edu/StudentFiles/Exam/StudViewSeatPlan.jsp', headers=headers)

    table = HTMLTableParser()

    table.feed(response.text)

    seatingPlan = PrettyTable(['Course', 'Date', 'Time', 'Centre Name', 'Room Name'])

    seatTable = table.tables[2]

    while len(seatTable) != 0:
        seatingPlan.add_row([
            seatTable[0][0].split(':')[1].strip(),
            seatTable[0][1].split('At')[0].strip('Date : ').strip(),
            seatTable[0][1].split('At')[1].strip(),
            seatTable[2][0],
            seatTable[2][2]
        ])
        seatTable.pop(0)
        seatTable.pop(0)
        seatTable.pop(0)


    print(seatingPlan)