'''
input
3 : 드래곤 커브는 3개
3 3 0 1 : 시작점 (3,3), 오른방향, 1세대
4 2 1 3 : 시작점 (4,2), 위방향, 3세대
4 2 2 1 : 시작점 (4,2), 왼방향, 1세대

output
4 정사각형이 드래곤 커브의 일부인 것의 개수는 4개

strategy
끝 점을 기준으로 90도 회전한다..
이걸 함수로 만들면 될 것 같은데

풀이 참조 : https://chldkato.tistory.com/150

'''


def get_score(edges):
    pass


def rotate(edges):
    # 끝점이 edges[-1], 돌릴 점들은 edges[:-1]
    pass


def get_points(x, y, dir, gen):
    # 일단 x, y, dir 신경쓰지 말고 0 0 오른방향으로 구현해보자.
    points = [(0, 0), (1, 0)]
    for i in range(gen-1):
        new_points = rotate(points)
        points = points + new_points

    return points


n = int(input())
curves = []
curves.append(list(map(int, input().split())))
for curve in curves:
    get_points(curve)
