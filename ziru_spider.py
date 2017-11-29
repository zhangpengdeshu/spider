import requests
import json
import time

def request_data(url,params,headers):
    try:
       resp = requests.post(url,data=json.dumps(params),headers=headers)
       return resp.json()
    except:
       return None

def parse_data(content):
    hourse_lists = json.loads(json.dumps(content,ensure_ascii=False))
    base_url = 'http://m.ziroom.com/BJ/room/'
    for item in hourse_lists['data']:
        yield {
        "house_id": item['house_id'],
        "id": item['id'],
        "district_name":item['district_name'],
        "area_name": item['area_name'],
        "bizcircle_name": item['bizcircle_name'],
        "resblock_name": item['resblock_name'],
        "room_name": item['room_name'],
        "dispose_bedroom_amount": item['dispose_bedroom_amount'],
        "house_facing": item['house_facing'],
        "compartment_face": item['compartment_face'],
        "sell_price": item['sell_price'],
        "subway_station_code_first": item['subway_station_code_first'],
        "walking_distance_dt_first": item['walking_distance_dt_first'],
        "detailUrl": base_url + item['house_id'] + '.html'
    }


def main(url,params,headers):
    with open('hourse_info.json','w',encoding="UTF-8") as f:
        for item in parse_data(request_data(url,params,headers)):
            print(f.closed)
            f.write(json.dumps(item,ensure_ascii=False)+'\n')

if __name__ == "__main__":
    url = 'http://m.ziroom.com/list/ajax-get-data'
    step = 0
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
     }

    params = {
        'district_code':'',
        'subway_station':'',
        'bizcircle_code':'',
        'subway_line_code':'',
        'recent_money':0,
        'sort':0,
        'is_whole':0,
        'room':'',
        'key_word':'',
        'is_duy':0,
        'is_duanz':0,
        'is_first':0,
        'is_wc':0,
        'step':0
    }

    while step < 500:
        step += 10
        params['step'] = step
        main(url,params,headers)
