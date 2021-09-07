def solution(genres: list, plays: list):
    genre_power = dict()
    for genre, play in zip(genres, plays):
        if genre in genre_power:
            genre_power[genre] += play
        else:
            genre_power[genre] = play
    put_dict = dict()
    for key in genre_power.values():
        put_dict[key] = 2
    to_sort = []
    answer = []
    for idx, play in enumerate(plays):
        idx_play_gen = (idx, play, genre_power[genres[idx]])
        to_sort.append(idx_play_gen)
    for idx, _, key in sorted(to_sort, key=lambda x: (-x[2], -x[1], x[0])):
        if put_dict[key] > 0:
            answer.append(idx)
            put_dict[key] -= 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
