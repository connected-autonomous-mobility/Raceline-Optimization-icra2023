import csv

# Open the input and output files
with open('inputs/tracks/icra2023-track.csv', 'r') as csv_file, open('inputs/tracks/icra2023-track2.csv', 'w', newline='') as out_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(out_file)

    # Iterate over rows, skipping every 10th row
    for i, row in enumerate(csv_reader, start=1):
        if i % 2 != 0:
            csv_writer.writerow(row)

