import sys
import csv
import os

def split_csv(source_filepath, dest_folder, split_file_prefix,
                records_per_file):
    """
    Split a source csv into multiple csvs of equal numbers of records,
    except the last file.

    Includes the initial header row in each split file.

    Split files follow a zero-index sequential naming convention like so:

        `{split_file_prefix}_0.csv`
    """
    if records_per_file <= 0:
        raise Exception('records_per_file must be > 0')

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_idx = 0
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f'{split_file_prefix}_{file_idx}.csv'
            target_filepath = os.path.join(dest_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < records_per_file:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_idx += 1
if __name__ == "__main__":
	a = sys.argv[1]
	b = sys.argv[2]
	c = sys.argv[3]
	d = int(sys.argv[4])

	split_csv(a, b, c, d)
