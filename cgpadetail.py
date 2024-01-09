import requests

from html_table_parser.parser import HTMLTableParser

from prettytable import PrettyTable

def getCgpaDetails(session:requests.Session, cgpa_id:str):

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

    response = session.get(
        f'https://webkiosk.thapar.edu/StudentFiles/Exam/AcademicDetSem.jsp?ExamCode={cgpa_id}',
        headers=headers,
    )

    table = HTMLTableParser()

    table.feed(response.text)

    cgpaDetTable = PrettyTable(table.tables[0][0])

    finalTableList = []

    finalTableList.extend(table.tables[0][:-1])

    tot_row = ['', '', 'TOTAL']

    tot_row.extend(table.tables[0][-1][1:])

    finalTableList.append(['' for i in range(len(tot_row))])

    finalTableList.append(tot_row)

    for x in finalTableList[1:]:
        cgpaDetTable.add_row(x)

    finalTableList.extend(table.tables[1])

    print(cgpaDetTable)

    return finalTableList