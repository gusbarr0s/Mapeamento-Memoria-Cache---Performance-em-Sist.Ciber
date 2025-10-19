quadros = 8

sequencia_a = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
sequencia_b = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
sequencia_c = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
#aqui em cima nos definimos a sequencia que o professor pediu

def fifo(paginas):
    memoria = []      
    faltas = 0        

    #percorre cada pagina 
    for p in paginas:
        if p in memoria:                   
            pass #se a pagina ja ta na memoria, nao faz nada                           
        else:
            faltas += 1                    
            if len(memoria) < quadros:     
                memoria.append(p)#se ainda tem espaco, adiciona a pagina          
            else:
                memoria.pop(0)#remove a mais antiga 
                memoria.append(p)#adiciona a nova página
    return memoria, faltas


def lru(paginas):
    memoria = []      
    uso = []#aqui criamos uma lista para controlar o uso das paginas         
    faltas = 0

    for p in paginas:
        if p in memoria:#se ja ta na memoria
            uso.remove(p)#remove da posicao atual
            uso.append(p)#coloca no final
        else:
            faltas += 1
            if len(memoria) < quadros:
                memoria.append(p)#mesma logica do FIFO se ainda tem espaco, adiciona a pagina
            else:
                lru_pag = uso.pop(0)#tira a menos usada
                pos = memoria.index(lru_pag)# pega posição dela
                memoria[pos] = p#substitui pela nova página
            uso.append(p)                  
    return memoria, faltas


def mru(paginas):
    memoria = []      
    uso = []          
    faltas = 0

    for p in paginas:
        if p in memoria:                   
            uso.remove(p)                  
            uso.append(p)                  
        else:
            faltas += 1
            if len(memoria) < quadros:     
                memoria.append(p)
            else:
                mru_pag = uso.pop()#aqui vai receber a mesma logica do fifo, a unica diferenca remove a mais recentemente usada
                pos = memoria.index(mru_pag)
                memoria[pos] = p           
            uso.append(p)
    return memoria, faltas


#testes:

print("Sequencia A:", sequencia_a)
mem, f = fifo(sequencia_a)
print("FIFO Memoria final:", mem)
print("FIFO Faltas de pagina:", f, "\n")
mem, f = lru(sequencia_a)
print("LRU Memoria final:", mem)
print("LRU Faltas de pagina:", f, "\n")
mem, f = mru(sequencia_a)
print("MRU Memoria final:", mem)
print("MRU Faltas de pagina:", f, "\n")

print("Sequencia B:", sequencia_b)
mem, f = fifo(sequencia_b)
print("FIFO Memoria final:", mem)
print("FIFO Faltas de pagina:", f, "\n")
mem, f = lru(sequencia_b)
print("LRU Memoria final:", mem)
print("LRU Faltas de pagina:", f, "\n")
mem, f = mru(sequencia_b)
print("MRU Memoria final:", mem)
print("MRU Faltas de pagina:", f, "\n")

print("Sequencia C:", sequencia_c)
mem, f = fifo(sequencia_c)
print("FIFO Memoria final:", mem)
print("FIFO Faltas de pagina:", f, "\n")
mem, f = lru(sequencia_c)
print("LRU Memoria final:", mem)
print("LRU Faltas de pagina:", f, "\n")
mem, f = mru(sequencia_c)
print("MRU Memoria final:", mem)
print("MRU Faltas de pagina:", f, "\n")

