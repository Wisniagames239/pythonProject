def count_solutions(total_sum, num_variables, current_sum, current_index):
    if num_variables == current_index:
        return 1 if current_sum == total_sum else 0

    count = 0
    for i in range(-total_sum, total_sum + 1):
        count += count_solutions(total_sum, num_variables, current_sum + abs(i), current_index + 1)
    return count

total_solutions = count_solutions(20, 5, 0, 0) * 2  # Mnożymy przez 2, aby uwzględnić również rozwiązania ujemne
print("Liczba rozwiązań:", total_solutions)