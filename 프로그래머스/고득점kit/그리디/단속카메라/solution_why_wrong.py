def cam_available(road_in, road_out, cam_in, cam_out):
    if road_out <= cam_in or road_in <= cam_out:
        return True
    return False


def solution(routes: list):
    cams = [[-30000, 30000]]
    for road_in, road_out in routes:
        for i in range(len(cams)):
            cam_in, cam_out = cams[i]
            if cam_available(road_in, road_out, cam_in, cam_out):  # 있는 카메라 사용 가능한경우
                cams[i][0] = max(cam_in, road_in)
                cams[i][1] = min(cam_out, road_out)
                break
        else:  # 있는 카메라로 감당이 안될 경우
            cams.append([road_in, road_out])

    # print(cams)
    return len(cams)


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[1, 2], [1, 2], [1, 2], [4, 5]]))
