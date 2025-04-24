import heapq

def a_star(start, goal, neighbors_fn, heuristic_fn):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic_fn(start, goal), 0, start, []))

    visited = set()

    while open_set:
        est_total, cost_so_far, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        new_path = path + [current]
        if current == goal:
            return new_path

        for neighbor, cost in neighbors_fn(current):
            if neighbor not in visited:
                heapq.heappush(open_set, (
                    cost_so_far + cost + heuristic_fn(neighbor, goal),
                    cost_so_far + cost,
                    neighbor,
                    new_path
                ))

    return None
