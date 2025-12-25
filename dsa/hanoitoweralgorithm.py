def hanoi_solver(total_disks: int):
    def mover(start, end):
        disk = rods[start].pop()
        rods[end].append(disk)
        states.append(f"{rods['A']} {rods['B']} {rods['C']}")
    def solver(n, start, end, spare):
        if n == 1:
            mover(start, end)
            return
        else:
            solver(n-1, start, spare, end)
            mover(start, end)
            solver(n-1, spare, end, start)
            
    if total_disks < 1:
        raise ValueError("n must be greater then or equal to 1")
    rods = {
        "A" : list(range(total_disks,0, -1)),
        "B" : [],
        "C" : []        
    }
    states = []
    states.append(f"{rods['A']} {rods['B']} {rods['C']}")

    solver(total_disks, "A", "C", "B")
    return "\n".join(states)

print(hanoi_solver(4))