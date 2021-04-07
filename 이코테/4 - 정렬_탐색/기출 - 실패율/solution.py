

def solution(n, stages):
    stage_dodal_makhim_l = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        stage_dodal_makhim_l[i][0] = i
    for stage in stages:
        for s in range(1, stage):
            stage_dodal_makhim_l[s][1] += 1
        if stage <= n:
            stage_dodal_makhim_l[stage][1] += 1
            stage_dodal_makhim_l[stage][2] += 1

    for i in range(1, n+1):
        if stage_dodal_makhim_l[i][1] == 0:
            stage_dodal_makhim_l[i].append(0)
        else:
            stage_dodal_makhim_l[i].append(
                stage_dodal_makhim_l[i][2]/stage_dodal_makhim_l[i][1])
    answer = sorted(stage_dodal_makhim_l[1:],
                    key=lambda x: (-x[3], x[0]))
    return [row[0] for row in answer]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
