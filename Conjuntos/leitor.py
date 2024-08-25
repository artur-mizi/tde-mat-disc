# Artur Moretti Zimmermann

# ler arquivo e checar numero de operações (para trocar de arquivo lido apenas editar o numero)
f = open('arquivo1.txt', 'r')
num = int(f.readline())
for i in range(num):
    data0 = str(f.readline())
    op = data0.replace('\n', '')
    if op == 'I':
        result = []
        # ler ambos conjuntos
        data1 = f.readline()
        cjt1 = data1.replace('\n', '').split(',')
        data2 = f.readline()
        cjt2 = data2.replace('\n', '').split(',')
        # operação de interceção
        for j in cjt1:
            for k in cjt2:
                if j == k:
                    result.append(j)
        # display de saída
        print('Operação: Interseção:', 'Conjunto A:', cjt1, ',', 'Conjunto B:', cjt2, '.', 'Resultado:', result)
    elif op == "U":
        result = []
        # ler ambos conjuntos
        data1 = f.readline()
        cjt1 = data1.replace('\n', '').split(',')
        data2 = f.readline()
        cjt2 = data2.replace('\n', '').split(',')
        # operação de união
        for j in cjt1:
            result.append(j)
        for k in cjt2:
            result.append(k)
        # display de saída
        print('Operação: União:', 'Conjunto A:', cjt1, ',', 'Conjunto B:', cjt2, '.', 'Resultado:', result)
    elif op == "D":
        result = []
        # ler ambos conjuntos
        data1 = f.readline()
        cjt1 = data1.replace('\n', '').split(',')
        data2 = f.readline()
        cjt2 = data2.replace('\n', '').split(',')
        # operação de diferença
        for j in cjt1:
            result.append(j)
            for k in cjt2:
                if j == k:
                    result.remove(j)
        j = 0
        k = 0
        for j in cjt2:
            result.append(j)
            for k in cjt1:
                if j == k:
                    result.remove(j)
        # display de saída
        print('Operação: Diferença:', 'Conjunto A:', cjt1, ',', 'Conjunto B:', cjt2, '.', 'Resultado:', result)
    elif op == 'C':
        result = []
        # ler ambos conjuntos
        data1 = f.readline()
        cjt1 = data1.replace('\n', '').split(',')
        data2 = f.readline()
        cjt2 = data2.replace('\n', '').split(',')
        # operação de produto cartesiano
        for j in cjt1:
            for k in cjt2:
                x = j, k,
                result.append(x)
        # display de saída
        print('Operação: Produto Cartesiano:', 'Conjunto A:', cjt1, ',', 'Conjunto B:', cjt2, '.', 'Resultado:', result)

f.close()
