import random 
import time

vector_size = int(input("Informe o tamanho do vetor\n"))

# vector = [random.randint(0, 1000) for _ in range(vector_size)]
vector = [1 for _ in range(vector_size)]

start_time = time.time()
print(f"soma total dos elementos: {sum(vector)}")
end_time = time.time()

execution_time = end_time - start_time

print(f"tempo de execução: {execution_time}")
