import multiprocessing
import time

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

#start_t = time.time()
#for file in files:
    #read_info(file)
#end_t = time.time()
#print(f'Линейное выполнение: {end_t - start_t} секунд')

if __name__=='__main__':
    start_t = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end_t = time.time()
    print(f'Многопроцессорное выполнение: {end_t - start_t} секунд')
