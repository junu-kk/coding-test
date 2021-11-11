import pprint


def rotate_mtrx(mtrx):
    rn = len(mtrx)
    cn = len(mtrx[0])

    '''
    abcd
    efgh
    
    ea
    fb
    gc
    hd
    
    row와 column의 역할이 바뀌고
    row -> 역순칼럼
    column -> 정순로우
    '''
    new_mtrx = [[0] * rn for _ in range(cn)]
    for r in range(rn):
        for c in range(cn):
            new_mtrx[c][rn - 1 - r] = mtrx[r][c]

    return new_mtrx


pprint.pprint(rotate_mtrx([['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]))
