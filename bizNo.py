import requests
import json

def getbiz(number):
    headers = {
        'accept': 'application/json',
        'Authorization': '2tNRx2X2iaJxyI8f7b1NDfI1zaNobxIOF7kVm4aW52G7xMLw6T4trCLd7yc10gzPHuIYXvQXgnldjcdpu30LcA==',
        'Content-Type': 'application/json',
    }

    params = (
        ('serviceKey', '2tNRx2X2iaJxyI8f7b1NDfI1zaNobxIOF7kVm4aW52G7xMLw6T4trCLd7yc10gzPHuIYXvQXgnldjcdpu30LcA=='),
    )

    data = '{ "b_no": [ "' + str(number) + '" ]}'


    response = requests.post('https://api.odcloud.kr/api/nts-businessman/v1/status', headers=headers, params=params,
                             data=data)
    res = json.loads(response.text)
    data = res['data']
    if data[0]['tax_type'] == "국세청에 등록되지 않은 사업자등록번호입니다.":
        return data[0]['tax_type']
    else:
        return "사업자등록번호 '" + data[0]['b_no'] + "'은 " + data[0]['tax_type'] + "입니다."