'''
다음 코드를 참조해 내 식대로 개조함.
(https://github.com/kakao-recruit/2019-blind-2nd-elevator/blob/master/example/example.py)
'''

from requests import get, post, put, patch, delete
from pprint import pprint

url = 'http://localhost:8000'

# cmds
STOP, OPEN, CLOSE, ENTER, EXIT, UP, DOWN = 'STOP', 'OPEN', 'CLOSE', 'ENTER', 'EXIT', 'UP', 'DOWN'

'''
파라미터로 요청값들을 집어넣으면
함수에서 요청을 보내고 그 결과를 json 형태로 반환하는 느낌으로 가면 되겠다.
'''


def start(problem, elev_n_to_use):
    uri = f'{url}/start/kacho/{problem}/{elev_n_to_use}'
    try:
        result = post(uri)
        return result.json()
    except:
        print(result)
        # exit()


def oncalls(token):
    uri = f'{url}/oncalls'
    try:
        result = get(
            uri,
            headers={'X-Auth-Token': token}
        )
        return result.json()
    except:
        print(result)
        # exit()


# 바디의 경우 body 대신 json으로 표현하는구나 ㅇㅇ.
def action(token, cmds):
    uri = f'{url}/action'

    try:
        result = post(
            uri,
            headers={'X-Auth-Token': token},
            json={'commands': cmds}
        )
        return result.json()
    except:
        pprint(result)
        # exit()

    return result.json()


def problem0():
    # 0번문제를 엘베 한개로 풀겠다.
    problem, elev_n = 0, 1

    token_json = start(problem, elev_n)
    token = token_json['token']
    print(f'내 토큰은 {token}')

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': STOP}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': STOP}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': OPEN}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': ENTER, 'call_ids': [5, 5, 5, 5,5,5]}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': CLOSE}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': UP}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': STOP}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': OPEN}]))

    pprint(oncalls(token))
    pprint(action(token, [{'elevator_id': 0, 'command': EXIT, 'call_ids': [5, 5, 5, 5, 5, 5]}]))


if __name__ == '__main__':
    problem0()
