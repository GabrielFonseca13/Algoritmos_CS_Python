def study_schedule(permanence_period, target_time):
    if not target_time or not isinstance(target_time, int):
        return None

    counter = 0
    for student in permanence_period:
        if not isinstance(student[0], int) or not isinstance(student[1], int):
            return None
        if student[0] <= target_time and student[1] >= target_time:
            counter += 1
    return counter


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))

# 1.2 - Retorne None se em permanence_period houver alguma entrada inválida;

# 1.3 - Retorne None se target_time recebe um valor vazio;

# 1.4 - A função deverá, por meio de análise empírica, se comportar (no
# avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com
# complexidade assintótica linear.

# # Nos arrays temos 6 estudantes

# # estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
