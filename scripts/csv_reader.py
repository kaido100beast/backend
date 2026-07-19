import csv

def read_csv_and_sum(file_loc_csv, file_loc_txt):
    try:
        with open(file_loc_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            sum = 0
            for row in reader:
                print(row)
                sum = sum + int(row[0])
    except Exception as e:
        print(f'Error reading CSV file: {e}')
        return
    try:
        with open(file_loc_txt, 'w') as f:
            f.write(f'The sum is: {sum}\n')
    except Exception as e:
        print(f'Error writing to text file: {e}')
        return

read_csv_and_sum('scripts/example.csv', 'scripts/text.txt')