
"""
This Function calculate the total of points by the system of calcification of the races and return a list of the champion or the champions
Args, the first arg is all the results of the races y and second one the system of calification.
"""
def calculate_points(results, system_punctuation):
    points = [0] * len(results[0])
    for i in range(len(results)):
        for j in range(len(results[i])):
            if j < system_punctuation[0]:
                points[results[i][j] - 1] += system_punctuation[j + 1]
    return points


# Obtaing the number of GrandPrix and the total of runners and return two integer values
def obtain_g_and_p():
    G, P = map(int, input("Enter Grand Prix number and number of runners: ").split())
    return G, P


# Obtain the total of races and the results of each GrandPrix and return a list of the results. The first arg is the total of grandprix.
def obtain_results(G):
    results = []
    for _ in range(G):
        result_race = list(map(int, input("Enter result of the races: ").split()))
        results.append(result_race)
    return results


# Obtain the number of scoring system and the scores of each one, an return a list. The first arg is the result of the grandprix.
def obtain_scoring_system(resultados):
    S = int(input("Enter number of scoring systems: "))
    champions_by_system = []

    for _ in range(S):
        system = list(map(int, input("Enter the scoring: ").split()))
        points = calculate_points(resultados, system)
        max_points = max(points)
        campeones_sistema = [i + 1 for i, p in enumerate(points) if p == max_points]
        champions_by_system.append(campeones_sistema)
    return champions_by_system


# Print all the champions or the champions.
def print_champions(champions_by_system):
    for champion_by_system in champions_by_system:
        champion_by_system = sorted(champion_by_system)
        print(*champion_by_system)


def main():
    while True:
        G, P = obtain_g_and_p()
        if G == 0 and P == 0:
            break

        results = obtain_results(G)
        champions_by_system = obtain_scoring_system(results)
        print_champions(champions_by_system)


if __name__ == "__main__":
    main()
