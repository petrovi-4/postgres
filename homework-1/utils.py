import csv
import pprint


def read_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # пропуск заголовка
        return list(reader)


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(read_csv('north_data/employees_data.csv'))
