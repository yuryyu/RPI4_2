#import csv
import pandas as pd 

#import os
#print(os.getcwd())
# Out: /Users/shane/Documents/blog
# Display all of the files found in your current working directory
#print(os.listdir(os.getcwd())
# read csv
# with open('C:\\Users\\yuzba\\Documents\\GitHub\\RPI4_2\\data\\K544_TLV_20-05-2020_NODE_4191.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)
#         line_count += 1
#     print(f'Processed {line_count} lines.')


# save csv
# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])    


def acq_data(file_name="data/data_good.csv"):
    data = pd.read_csv(file_name)
    return data 



if __name__ == "__main__":
    data = acq_data()
    # Preview the first 5 lines of the loaded data 
    print(data.head())
