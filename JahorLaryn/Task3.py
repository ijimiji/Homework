"""File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark. 
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass"""


def get_top_performers(file_path, number_of_top_students=5):
    d = {}
    with open(file_path) as table:
        students = [item.split(",") for item in table.read().split("\n")[1:]]
        d = {name: (age, mark) for (name, age, mark) in students}
    top_performers = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
    return [
        top_performer[0] for top_performer in top_performers[:number_of_top_students]
    ]


def write_eldest_students_to_table(input_file_path, output_file_path):
    d = {}
    header = "student name,age,average mark\n"
    with open(input_file_path) as table:
        students = [item.split(",") for item in table.read().split("\n")[1:]]
        d = {name: (age, mark) for (name, age, mark) in students}
    eldest_students = sorted(d.items(), key=lambda x: x[1][0], reverse=True)
    with open(output_file_path, "a") as table:
        table.write(header)
        for student in eldest_students:
            table.write(f"{student[0]},{student[1][0]},{student[1][1]}\n")


def main():
    print(get_top_performers("data/students.csv"))
    write_eldest_students_to_table("data/students.csv", "data/eldest.csv")


if __name__ == "__main__":
    main()
