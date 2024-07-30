# 1) Consider city 1 as the starting and ending point.
# 2) Generate all (n-1)! Permutations of cities. 
# 3) Calculate the cost of every permutation and keep track of the minimum cost permutation. 
# 4) Return the permutation with minimum cost. 

import random
import numpy as np

# generate a random solution
def generate_random_solution(num_cities):
    return random.sample(range(num_cities), num_cities)

# Calculate the total distance of a given tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities):
        total_distance += distance_matrix[tour[i-1], tour[i]]
    return total_distance

# Generate neighboring solutions by swapping tow cities
def get_neighbors(tour):
    neighbors = []
    num_cities = len(tour)
    for i in range(num_cities):
        for j in range(num_cities):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Hill climbing algorithm
def hill_climbing(distance_matrix):
    num_cities = len(distance_matrix)
    current_solution = generate_random_solution(num_cities)
    current_distance = calculate_total_distance(current_solution, distance_matrix)
    while True:
        neighbors = get_neighbors(current_solution)
        best_neighbor = min(neighbors, key=lambda tour: calculate_total_distance(tour, distance_matrix))
        best_neighbor_distance = calculate_total_distance(best_neighbor, distance_matrix)
        if best_neighbor_distance < current_distance:
            current_solution = best_neighbor
            current_distance = best_neighbor_distance
        else:
            break
    return current_solution, current_distance

def main():
    num_cities = int(input("Enter the number of cities: "))
    distance_matrix = np.zeros((num_cities, num_cities))
    print("Enter the distance matrix (each row on a new line, distance separated by spaces): ")
    for i in range(num_cities):
        row = list(map(int, input().strip().split()))
        distance_matrix[i] = row
    best_solution, best_distance = hill_climbing(distance_matrix)
    print(f"Best Solution: {best_solution}")
    print(f"Best Distance: {best_distance}")
    
if __name__ == "__main__":
    main()