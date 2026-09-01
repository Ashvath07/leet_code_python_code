from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start = None

        # Find start and assign IDs to litter
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        # All litter collected
        target = (1 << len(litter)) - 1

        if target == 0:
            return 0

        # BFS:
        # (row, col, energy, mask, steps)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        # best[(row, col, mask)] = maximum energy seen
        best = {
            (start[0], start[1], 0): energy
        }

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:

            r, c, e, mask, steps = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside classroom
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Wall
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = e - 1

                # Collect litter
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    new_mask |= (1 << litter[(nr, nc)])

                # If all litter collected
                if new_mask == target:
                    return steps + 1

                # Recharge
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Can't move further without energy
                if new_energy <= 0:
                    continue

                state = (nr, nc, new_mask)

                # If we've already reached this state
                # with equal or greater energy, this path
                # can never be better.
                if state in best and best[state] >= new_energy:
                    continue

                # This is a better state
                best[state] = new_energy

                q.append(
                    (nr, nc, new_energy, new_mask, steps + 1)
                )

        return -1