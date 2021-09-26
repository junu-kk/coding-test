'''

'''

from requests import get, post, put, patch, delete
from pprint import pprint, pformat
from logging import basicConfig, warning as log

# (필요시) log('텍스트')로 파일에 기록할 것!
basicConfig(filename='0.log', filemode='a', format='%(message)s')

url = 'http://localhost:8000'
user_key = 'kacho'


# (필요시) 클래스 선언
class Elevator:
    def __init__(self, bye):
        self.id = 0
        self.floor = 1
        self.passengers = []
        self.status = STOPPED

    def __str__(self):
        return f'{id} / {self.floor}층 / {self.passengers} / {self.status}'


# cmds, status 등(UPPERCASE)
STOP, UP, DOWN, OPEN, CLOSE, ENTER, EXIT = 'STOP', 'UP', 'DOWN', 'OPEN', 'CLOSE', 'ENTER', 'EXIT'
UPWARD, DOWNWARD, STOPPED, OPENED = 10, 11, 12, 13


# 그 외 필요한 리스트 등의 변수들 (lowercase)


############# 함수부 1 : 일반 ##################
def generate_cmd(eid, cmd_letter, call_ids=None):
    cmd = {
        'elevator_id': eid,
        'command': cmd_letter,
    }
    if call_ids:
        cmd['call_ids'] = call_ids
    return cmd

########################################


############# 함수부 2 : api 호출 ##################

# 뽑을거 : token
# 버릴거 : timestamp, elevators, is_end
def api_start(pnum, elev_n):
    uri = f'{url}/start/{user_key}/{pnum}/{elev_n}'
    result = post(uri)
    return result.json()


# 뽑을거 : calls[{id, timestamp, start, end}]
# 그 외 : token, timestamp, elevators, is_end
def api_get_calls(token):
    uri = f'{url}/oncalls'
    headers = {
        'X-Auth-Token': token,
    }
    result = get(uri, headers=headers)
    return result.json()


# body에 들어갈 cmds : [{elevator_id, command, (옵셔널)call_ids[]}]
# 뽑을거 : elevators: [{id, floor, passengers[{id, timestamp, start, end}], status}]
# 그 외 : token, timestamp, is_end
def api_cmd_elev(token, cmds: list):
    uri = f'{url}/action'
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    json = {
        'commands': cmds
    }
    result = post(uri, headers=headers, json=json)
    return result.json()


############################################

################# 함수부 3 : 메인 #####################
def p(n):
    start_d = api_start(n, 1)  # 일단 엘베 하나만.
    token = start_d['token']
    for i in range(10):
        print(f'{i}번째 턴')
        cmd_d = generate_cmd(0, STOP)
        api_cmd_elev(token, [cmd_d])
        calls = api_get_calls(token)['calls']
        '''
        4개의 엘리베이터를
        절반은 1층배치
        누군가 오면 태운다
        비울때까지 올라간다
        올라가며 마침 올라가는 손님이 있다면 태운다.
        비면 다시 1층으로 내려온다
        
        절반은 꼭대기 배치
        내려가는 사인이 눌려지면 태운다
        비울때까지 내려간다.
        내려가며 마침 내려가는 손님이 있다면 태운다
        비면 다시 꼭대기로 올라간다
        
        p2같은 경우엔
        원래 전략을 우선은 쓰고
        또 다른 전략은
            하나는 1층과 13층을 와리가리한다.
            하나는 13층과 25층을 와리가리한다.
            두개는 전 층을 와리가리한다.
        
        '''

    # pprint(api_get_calls(token))
    # pprint(api_get_calls(token))
    # pprint(api_get_calls(token))
    # pprint(api_get_calls(token))


################################################


###################### 실행부 ########################
if __name__ == '__main__':
    p(0)

#####################################################
