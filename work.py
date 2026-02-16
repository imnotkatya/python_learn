import csv

input_file = "penguins.csv"
missing_file = "missing.csv"
m = "NA"


def freq(col_num):

    column_freq = {}
    for row in all_rows:
        if row[col_num] and row[col_num] != m:
            if row[col_num] and row[col_num] != m:
                column_freq[row[col_num]] = column_freq.get(row[col_num], 0) + 1
    return column_freq


def avg(col_num):
    sum = 0
    arr = []
    count = 0
    avg = 0
    for row in all_rows:
        if row[col_num] and row[col_num] != m:
            sum += row[col_num]
            arr.append(row[col_num])
            count += 1
    avg = sum / count
    return avg


def min_val(col_num):
    arr = []
    for row in all_rows:
        if row[col_num] and row[col_num] != m:
            arr.append(row[col_num])
    return min(arr)


def max_val(col_num):
    arr = []
    for row in all_rows:
        if row[col_num] and row[col_num] != m:
            arr.append(row[col_num])
    return max(arr)


def missing():
    print("Rows with missing")
    count = 0
    missing_rows = []
    for row in all_rows:
        if m in row:
            count += 1
            missing_rows.append(row)
            print(row)
    print("amount of missing", count)
    with open(missing_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(missing_rows)


with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    all_headers = list(header)
    print(all_headers)

    all_rows = []

    for row in reader:
        converted_row = []
        for cell in row:
            try:
                converted_row.append(float(cell))
            except ValueError:
                converted_row.append(cell)

        all_rows.append(converted_row)
        print(converted_row)

missing()

# print
print("species_freq", freq(0))
print("island_freq", freq(1))
print("year_freq", freq(7))
print("sex_freq", freq(6))
print("bill_length_avg", avg(2))
print("bill_depth_avg", avg(3))
print("flipper_length_avg", avg(4))
print("weight_avg", avg(5))
print("min_bill_length", min_val(2))
print("max_bill_length", max_val(2))
print("min_bill_depth", min_val(3))
print("max_bill_depth", max_val(3))
print("min_flipper_length", min_val(4))
print("max_flipper_length", max_val(4))
