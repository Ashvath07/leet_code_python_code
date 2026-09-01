from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        sx = sy = -1
        litter_id = [[-1] * n for _ in xrange(m)]
        litter_count = 0

        for i in xrange(m):
            for j in xrange(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_id[i][j] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1

        if full_mask == 0:
            return 0
        best = [
            [
                [-1] * (1 << litter_count)
                for _ in xrange(n)
            ]
            for _ in xrange(m)
        ]

        q = deque()
        q.append((sx, sy, 0, energy, 0))
        best[sx][sy][0] = energy

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            x, y, mask, cur_energy, step = q.popleft()

            if mask == full_mask:
                return step
            if cur_energy == 0:
                continue

            next_step = step + 1

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                cell = classroom[nx][ny]

                if cell == 'X':
                    continue

                next_energy = cur_energy - 1
                next_mask = mask

                if cell == 'R':
                    next_energy = energy
                elif cell == 'L':
                    idx = litter_id[nx][ny]
                    next_mask = mask | (1 << idx)
                if best[nx][ny][next_mask] >= next_energy:
                    continue

                best[nx][ny][next_mask] = next_energy
                q.append((nx, ny, next_mask, next_energy, next_step))

        return -1