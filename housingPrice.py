from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xmltodict
import json


def HousingPrice(pnu, stdrYear):
    url = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr'
    serviceKey = '2tNRx2X2iaJxyI8f7b1NDfI1zaNobxIOF7kVm4aW52G7xMLw6T4trCLd7yc10gzPHuIYXvQXgnldjcdpu30LcA=='

    queryParams = '?' + urlencode({
        quote_plus('serviceKey'): serviceKey,
        quote_plus('pnu'): str(pnu),
        quote_plus('stdrYear'): str(stdrYear),
    })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    jsonString = json.loads(json.dumps(xmltodict.parse(response_body), ensure_ascii=False))
    result = jsonString['response']['fields']['field']
    return result