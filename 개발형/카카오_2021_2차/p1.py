'''
일단 시나리오 1부터 해결해보자.
hotplace가 없으므로, 사실 암것도 안해도 알아서 균형이 맞춰질 것으로 예상이 된다.

다만 활용하지 않는것보단 활용하는 편이 나을 것 같으므로, 다음을 일단 생각할 수 있겠다.
- 트럭은 (2, 2)에서 항시 대기한다
- 6 이상인 곳을 발견했을 때 트럭은 그곳으로 움직인다
    - 그 때 트럭의 기준으로 가까운 곳이 우선이다.
- 4가 될때까지 or 트럭이 찰때까지 싣는다
- 2 이하인 곳을 찾아 트럭은 그곳으로 움직인다
    - 그 때 트럭의 기준으로 가까운 곳이 우선이다.
- 4가 될때까지 or 트럭이 빌때까지 내린다.
- 6 이상인 곳이 없을 경우 (2,2)로 복귀한다.

궁금증
- 요청은 시작할때마다 계속 변하나?

일단 문제 1번부터 제대로 풀자.
'''

from requests import get, post, put, patch, delete
from pprint import pprint

url = 'https://example.com'
token = 'abc123'
mtrx = [[4] * 5 for _ in range(5)]
truck_loc_lbs = [[0, 0, 0] for _ in range(5)]
# truck cmds (URDL 90도 뒤집었으므로 RDLU)
NONE, R, D, L, U, LOAD, UNLOAD = 0, 1, 2, 3, 4, 5, 6

# 트럭 상태 (한 싸이클(10회) 당 하나의 상태를 가지도록 함.)
WAITING, UNLOADING, FINISHED_UNLOADING = 10, 11, 12
truck_stats = [WAITING] * 5


def inspect_overbike(t):
    overbike_locs = []
    gijun = 6 if t > 60 else 5
    for r in range(5):
        for c in range(5):
            if mtrx[r][c] >= gijun:
                overbike_locs.append((r, c))

    return overbike_locs


def inspect_underbike():
    underbike_locs = []
    for r in range(5):
        for c in range(5):
            if mtrx[r][c] <= 2:
                underbike_locs.append((r, c))

    return underbike_locs


def get_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# auth_key, problem, time
def start(pnum: int):
    uri = f'{url}/start'
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    body = {'problem': pnum}
    result = post(uri, headers=headers, json=body)
    return result.json()


# locations[(id, located_bikes_count)]
def get_bike_locs(auth_key: str):
    uri = f'{url}/locations'
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    result = get(uri, headers=headers)
    return result.json()


# trucks[(id, location_id, loaded_bikes_count)]
def get_truck_loc_lbs(auth_key: str):
    uri = f'{url}/trucks'
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    result = get(uri, headers=headers)
    return result.json()


# cmds[(truck_id, command[]]
# status, time, failed_requests_count, distance
def simulate(auth_key: str, cmds: list):
    uri = f'{url}/simulate'
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'commands': cmds
    }
    result = put(uri, headers=headers, json=body)
    return result.json()


# score
def get_score(auth_key: str):
    uri = f'{url}/score'
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    result = get(uri, headers=headers)
    return result.json()


def save_loc(d):
    id_lbcs = d['locations']
    for each in id_lbcs:
        loc, lbc = each['id'], each['located_bikes_count']
        r, c = divmod(loc, 5)
        mtrx[r][c] = lbc


def update_truck_loc_lbs(d):
    id_lid_lbcs = d['trucks']
    for each in id_lid_lbcs:
        tid, loc, lbc = each['id'], each['location_id'], each['loaded_bikes_count']
        tr, tc = divmod(loc, 5)
        truck_loc_lbs[tid] = [tr, tc, lbc]

def generate_cmd_l(tcmds):
    cmd_l = []
    for i in range(5):
        cmd = tcmds[i]
        d = {
            'truck_id': i,
            'command': cmd
        }
        cmd_l.append(d)
    return cmd_l


def p(n):
    start_d = start(n)
    auth_key = start_d['auth_key']
    cmds_waiting = [NONE] * 10
    for t in range(720):
        print(f't = {t}')
        tcmds = [cmds_waiting] * 5
        d = get_truck_loc_lbs(auth_key)
        update_truck_loc_lbs(d)
        ############ 시뮬레이트 ##############

        # pprint(simulate(auth_key, cmds))
        '''
        - 트럭은 (2, 2)에서 항시 대기한다 (희망사항)
        
        - 트럭 상태는 싣는중, 대기중, 내리는중으로 한다.
        - 내리는중 상태의 트럭에 대해 다음을 수행한다.
            - 2 이하의 곳을 발견했을 때 트럭은 그곳으로 움직인다
            - 싹 다 내린다
            - 상태를 내리기완료로 바꾼다
            
        '''
        overbike_locs = inspect_overbike(t)
        underbike_locs = inspect_underbike()
        overbike_n = len(overbike_locs)
        underbike_n = len(underbike_locs)
        oi, ui, = 0, 0

        if underbike_locs:
            for ti in range(5):
                tstat = truck_stats[ti]
                ur, uc = underbike_locs[ui]
                if tstat == UNLOADING:
                    print(f'{ti}가 내리러 간다')
                    cmd_i = 0
                    cmds = [UNLOAD] * 10
                    ## 그 ti의 cmd를 움직이고 내리는걸로 채움 ##
                    # 트럭 입장 : bloc-tloc
                    tr, tc, _ = truck_loc_lbs[ti]
                    dr, dc = ur - tr, uc - tc

                    if dr > 0:
                        for _ in range(dr):
                            cmds[cmd_i] = U
                            cmd_i += 1
                    elif dr < 0:
                        for _ in range(-dr):
                            cmds[cmd_i] = D
                            cmd_i += 1

                    if dc > 0:
                        for _ in range(dc):
                            cmds[cmd_i] = R
                            cmd_i += 1
                    elif dc < 0:
                        for _ in range(dc):
                            cmds[cmd_i] = L
                            cmd_i += 1

                    tcmds[ti] = cmds
                    truck_stats[ti] = FINISHED_UNLOADING

                    ui += 1
                    if ui == underbike_n:
                        break
        '''
        - 대기중 상태의 트럭에 대해 다음을 수행한다.
            - 6 이상인 곳을 발견했을 때 트럭은 그곳으로 움직인다
            - 싹 다 싣는다
            - 상태를 내리는중으로 바꾼다
        '''
        # print()
        # print(f'overbike locs : {overbike_locs}')
        # print()
        if overbike_locs:
            for ti in range(5):
                tstat = truck_stats[ti]
                br, bc = overbike_locs[oi]
                if tstat == WAITING:
                    print(f'{ti}가 실으러 간다')
                    cmd_i = 0
                    cmds = [LOAD] * 10
                    # 트럭 입장 : bloc-tloc
                    tr, tc, _ = truck_loc_lbs[ti]
                    dr, dc = br - tr, bc - tc

                    if dr > 0:
                        for _ in range(dr):
                            cmds[cmd_i] = U
                            cmd_i += 1
                    elif dr < 0:
                        for _ in range(-dr):
                            cmds[cmd_i] = D
                            cmd_i += 1

                    if dc > 0:
                        for _ in range(dc):
                            cmds[cmd_i] = R
                            cmd_i += 1
                    elif dc < 0:
                        for _ in range(dc):
                            cmds[cmd_i] = L
                            cmd_i += 1

                    tcmds[ti] = cmds
                    truck_stats[ti] = UNLOADING

                    oi += 1
                    if oi == overbike_n:
                        break

        for ti in range(5):
            if truck_stats[ti] == FINISHED_UNLOADING:
                truck_stats[ti] = WAITING
        cmd_l = generate_cmd_l(tcmds)
        # pprint(cmd_l)
        simulate(auth_key, cmd_l)

        ###################################

        d = get_bike_locs(auth_key)
        save_loc(d)
        # pprint(mtrx)
    pprint(get_score(auth_key))


if __name__ == '__main__':
    # p(1) 이 주석 풀지마
    p(2)

