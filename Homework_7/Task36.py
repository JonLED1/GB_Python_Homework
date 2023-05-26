def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        line = []
        for y in range(1, num_columns + 1):
            line.append(operation(x, y))
        print(*[str(x) for x in line])


print_operation_table(lambda x, y: x * y)
