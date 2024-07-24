import random
import threading
import time

number_of_threads = int(input("Informe o número de threads: \n"))
vector_size = int(input("Informe o tamanho do vetor: \n"))

results = [0] * number_of_threads 
vector = [random.randint(0, 1000) for _ in range(vector_size)]

def sum_partition(start_index, end_index, index, results):
    partition_sum = sum(vector[start_index:end_index])
    results[index] = partition_sum

threads_list = []

number_of_elements_to_distribute_equally = vector_size // number_of_threads
left_elements = vector_size % number_of_threads

start_index = 0

# Cria as partições e associa a threads
for i in range(number_of_threads):
    end_index = start_index + number_of_elements_to_distribute_equally
    
    if i < left_elements:
        end_index += 1
    
    thread = threading.Thread(target=sum_partition, args=(start_index, end_index, i, results))
    threads_list.append(thread)
    
    start_index = end_index

start_time = time.time()
for thread in threads_list:
    thread.start()

for thread in threads_list:
    thread.join()

total_sum = sum(results)

end_time = time.time()

execution_time = end_time - start_time

print(f"Soma total do vetor: {total_sum}")
print(f"tempo de execução: {execution_time}")