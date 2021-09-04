def solution(routes:list):
    routes.sort(key=lambda x:x[1])
    cam_in = -30000
    answer = 0

    for car_in, car_out in routes:
        if cam_in < car_in:
            answer += 1
            cam_in = car_out


    return answer
