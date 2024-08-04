from _datetime import datetime
import threading
import time
def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(f'Какое-то слово № {word_count}')
        time.sleep(0.01)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
time_start1 = datetime.now()
thr_first = threading.Thread(target=wite_words(10, 'example5.txt'))
thr_second = threading.Thread(target=wite_words(30, 'example6.txt'))
thr_third = threading.Thread(target=wite_words(200, 'example7.txt'))
thr_forth = threading.Thread(target=wite_words(100, 'example8.txt'))
thr_first.start()
thr_second.start()
thr_third.start()
thr_forth.start()
thr_first.join()
thr_second.join()
thr_third.join()
thr_forth.join()
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)
