class DList:  # h, t, c
    class Node:  # v, l, r
        # 이해됐지?
        def __init__(self, l, v, r):
            self.l = l
            self.v = v
            self.r = r

    def __init__(self):
        # 헤드 -> ______ -> 테일의 구조.
        # 초기생성시엔 비어있으니 바로 헤드->테일로 초기화.
        # 연결리스트가 비어있을 땐 커서를 맨 끝(테일) 에 둔다. 삽입 시 커서 왼쪽에 삽입.
        self.h = self.Node(None, None, None)
        self.t = self.Node(self.h, None, None)
        self.h.r = self.t
        self.c = self.t

    def insert(self, next_node: Node, v):
        prev_node = next_node.l
        new_node = self.Node(prev_node, v, next_node)
        prev_node.r = new_node
        next_node.l = new_node

    def delete(self, node:Node):
        prev_node, next_node = node.l, node.r
        prev_node.r, next_node.l = next_node, prev_node

    def print_list(self):
        itr_node = self.h.r
        while itr_node != self.t:
            print(itr_node.v, end='')
            itr_node = itr_node.r
        print()

s = list(input())
dl = DList()
for c in s:
    dl.insert(dl.t, c)

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L': # 왼쪽 (맨앞이면 무시)
        if dl.c == dl.h.r:
            continue
        dl.c = dl.c.l
    elif cmd[0] == 'D': # 오른쪽 (맨끝이면 무시)
        if dl.c == dl.t:
            continue
        dl.c = dl.c.r
    elif cmd[0] == 'B': # 왼쪽 삭제 (맨앞이면 무시)
        if dl.c == dl.h.r:
            continue
        dl.delete(dl.c.l)
    elif cmd[0] == 'P':
        v = cmd[1]
        dl.insert(dl.c, v)

dl.print_list()