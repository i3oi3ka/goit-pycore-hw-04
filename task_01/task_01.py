"""task 01"""


def total_salary(path: str) -> tuple[float, float]:
    """
    The total_salary function reads a file containing salary data and calculates the total and average salary.
    It accepts a single parameter - the path to the file.

    Parameters:
    path (Path): The path to the file containing salary data. The file should be in CSV format,
    where each line contains an employee's name and salary, separated by a comma.

    Returns:
    tuple: A tuple containing two values:
    The total of all salaries.
    The average salary.

    Exceptions:
    FileNotFoundError: Raised if the file is not found at the specified path. In this case, an error message is printed.
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            salary_list = [float(i.split(",")[1]) for i in file]
            total_sum = sum(salary_list)
            average_salary = total / len(salary_list)
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"File {path} not found.")
        return 0, 0


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
