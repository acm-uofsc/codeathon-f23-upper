#!/usr/local/bin/python3
import random


def generate_random_input(max_individuals):
    # Define constraints
    max_name_length = 50
    max_name_pairs = 50

    # Generate a random number of individuals and name pairs
    num_individuals = random.randint(1, max_individuals)
    num_name_pairs = random.randint(1, max_name_pairs)

    # Generate a list of unique individuals
    individuals = set()
    while len(individuals) < num_individuals:
        name = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(max_name_length))
        individuals.add(name)

    individuals = list(individuals)

    # Generate a list of edges (friendships) between individuals
    edges = []
    for _ in range(num_individuals):  # Random number of friendships
        u, v = random.sample(individuals, 2)
        edges.append((u, v))

    # Generate a list of name pairs to be checked for connectivity
    name_pairs = []
    for _ in range(num_name_pairs):
        u, v = random.sample(individuals, 2)
        name_pairs.append((u, v))

    # Print the generated data
    print(len(edges))
    for edge in edges:
        print(f"{edge[0]} {edge[1]}")
    print(num_name_pairs)
    for pair in name_pairs:
        print(f"{pair[0]} {pair[1]}")


def main():
    case_num = int(input())
    # 0 and 1 are the sample cases
    if case_num == 0:
        print(5)
        friendships = [['Alice', 'Bob'],
                       ['Bob', 'Carol'],
                       ['David', 'Alice'],
                       ['Eve', 'Frank'],
                       ['Grace', 'David']]
        for friendship in friendships:
            print(*friendship)
        print(3)
        pairs = [['Alice', 'Carol'],
                 ['Eve', 'Grace'],
                 ['Eve', 'Bob']]
        for pair in pairs:
            print(*pair)
    elif case_num < 5:
        generate_random_input(10**2)
    else:
        generate_random_input(10**4)


if __name__ == "__main__":
    main()
