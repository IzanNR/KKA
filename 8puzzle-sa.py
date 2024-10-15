import random
import math

# Fungsi untuk menghitung nilai heuristic (jumlah ubin yang tidak berada di posisi yang benar)
def heuristic(state, goal):
    mismatch = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                mismatch += 1
    return mismatch

# Fungsi untuk menemukan posisi kosong (0) di puzzle
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Fungsi untuk membuat tetangga dengan memindahkan ubin di sekitar posisi kosong
def get_neighbors(state):
    neighbors = []
    blank_row, blank_col = find_blank(state)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # atas, bawah, kiri, kanan
    for move in moves:
        new_row, new_col = blank_row + move[0], blank_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)
    
    return neighbors

# Fungsi untuk algoritma Simulated Annealing
def simulated_annealing(initial_state, goal_state, temperature=1000, cooling_rate=0.95, min_temperature=0.01):
    current_state = initial_state
    current_heuristic = heuristic(current_state, goal_state)
    iteration = 0
    
    while temperature > min_temperature and current_heuristic > 0:
        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_heuristic = heuristic(next_state, goal_state)
        
        delta = next_heuristic - current_heuristic
        
        # Jika next_state lebih baik atau diterima dengan probabilitas yang sesuai
        if delta < 0:
            current_state = next_state
            current_heuristic = next_heuristic
            iteration += 1
            print(f"Iteration {iteration}:")
            for row in current_state:
                print(row)
            print(f"Heuristic   : {current_heuristic}")
            print(f"Temperature : {temperature}\n")

        elif math.exp(-delta / temperature) > random.uniform(0, 1):
            current_state = next_state
            current_heuristic = next_heuristic
            iteration += 1
            print(f"Iteration {iteration}:")
            for row in current_state:
                print(row)
            print(f"Heuristic   : {current_heuristic}")
            print(f"Temperature : {temperature}\n")
        
        temperature *= cooling_rate
        
        
    print(f"Simulated Annealing selesai dalam {iteration} iterasi terpilih untuk mencapai goal state.")

# Main program
def main():
    # State awal
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    # State goal
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    # Jalankan algoritma simulated annealing
    simulated_annealing(initial_state, goal_state)

main()
