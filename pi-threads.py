import random
import time
import threading

def calcular_pi(index_inicio, index_fim, i, resultados):
    pontos_dentro_do_circulo = 0

    for _ in range(index_inicio, index_fim):
        x, y = random.random(), random.random()
        distancia_ao_centro = x**2 + y**2
        if distancia_ao_centro <= 1:
            pontos_dentro_do_circulo += 1
    
    resultados[i] = pontos_dentro_do_circulo
    

def dividir_pontos_entre_threads(numero_de_pontos, numero_de_threads):
    numero_de_pontos_para_distribuir_igualmente = numero_de_pontos // numero_de_threads
    pontos_restantes = numero_de_pontos % numero_de_threads
            
    resultados = [0] * numero_de_threads
    lista_de_threads = []
    start_index = 0
    
    for i in range(numero_de_threads):
        end_index = start_index + numero_de_pontos_para_distribuir_igualmente
        
        if i < pontos_restantes:
            end_index += 1
        
        thread = threading.Thread(target=calcular_pi, args=(start_index, end_index, i, resultados))
        lista_de_threads.append(thread)
        
        start_index = end_index
        
    start_time = time.time()  # Inicia a medição do tempo
    for thread in lista_de_threads:
        thread.start()
        
    for thread in lista_de_threads:
        thread.join()
        
    
    pontos_dentro_do_circulo = sum(resultados)
    
    end_time = time.time()  # Termina a medição do tempo
    
    pi_aproximado = 4 * pontos_dentro_do_circulo / numero_de_pontos
    
    
    print(f"Aproximação de π com {numero_de_pontos} pontos é: {pi_aproximado}")
    print(f"Tempo de execução: {end_time - start_time} segundos")



if __name__ == '__main__':
    numero_de_pontos = int(input("Informe o número de pontos: \n"))
    numero_de_threads = int(input("Informe o número de threads: \n"))
    
    dividir_pontos_entre_threads(numero_de_pontos, numero_de_threads)
    