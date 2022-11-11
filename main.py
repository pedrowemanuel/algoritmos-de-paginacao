import sys
import numpy as np


def fifo(molduras_na_memoria, referencia):
	del molduras_na_memoria[0]
	molduras_na_memoria.append(referencia)


def envelhecimento(molduras_na_memoria, referencia, historico_referencias):
	# dicionario onde a chave é o indice da moldura e o valor é a sua posicao no historico
	posicoes = {0: -1, 1: -1, 2: -1, 3: -1, 4: -1}

	historico_invertido = []
	for referencia in reversed(historico_referencias):
		historico_invertido.append(referencia)

	for i in range(len(molduras_na_memoria)):
		for j in range(len(historico_invertido)):
			if (molduras_na_memoria[i] == referencia):
				posicoes[i] = j
				break

	referenciada_mais_antigamente = 0
	for moldura, posicao in posicoes.items():
		if (posicoes[referenciada_mais_antigamente] >= posicao):
			referenciada_mais_antigamente = moldura

	del molduras_na_memoria[referenciada_mais_antigamente]
	molduras_na_memoria.append(referencia)


def alocar_referencias(referencias, quantidade_molduras, algoritmo):
	faltas_de_paginas = 0
	molduras_na_memoria = []
	historico_referencias = []

	for referencia in referencias:
		if (np.size(molduras_na_memoria) <= quantidade_molduras):
			if (not referencia in molduras_na_memoria):
				faltas_de_paginas += 1
				molduras_na_memoria.append(referencia)
		else:
			if (not referencia in molduras_na_memoria):
				faltas_de_paginas += 1
				if (algoritmo == "fifo"):
					fifo(molduras_na_memoria, referencia)
				elif (algoritmo == "envelhecimento"):
					envelhecimento(molduras_na_memoria, referencia, historico_referencias)
		historico_referencias.append(referencia)

	return faltas_de_paginas


def main(args):

	quantidade_molduras = int(args[1])

	referencias = []
	referencias = np.random.randint(1, 10, size=1000)

	faltas_pagina_fifo = alocar_referencias(referencias, quantidade_molduras,
	                                        'fifo')

	faltas_pagina_enve = alocar_referencias(referencias, quantidade_molduras,
	                                        'envelhecimento')

	print("Quantidade de molduras: " + str(quantidade_molduras))
	print("Faltas de página FIFO: " + str(faltas_pagina_fifo))
	print("Faltas de página algoritmo de envelhecimento: " +
	      str(faltas_pagina_enve))

	# Escrita do arquivo
	arquivo = open("./resultados.txt", "a", encoding="utf-8")
	arquivo.write("Quantidade de molduras: " + str(quantidade_molduras) + "\n")
	arquivo.write("Faltas de página FIFO: " + str(faltas_pagina_fifo) + "\n")
	arquivo.write("Faltas de página algoritmo de envelhecimento: " +
	              str(faltas_pagina_enve) + "\n")
	arquivo.write("Referências: \n")

	for referencia in referencias:
		arquivo.write(str(referencia) + " ")
	arquivo.write(
	 "\n ================================================================== \n")

	return 0


if __name__ == "__main__":
	sys.exit(main(sys.argv))
