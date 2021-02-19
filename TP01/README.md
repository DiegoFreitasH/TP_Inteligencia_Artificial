# TP01

## Equipe

* Diego Freitas Holanda - 411627
* Davi Segundo Pinheiro - 417153
* Gabriel Freire Do Vale - 418788 

## Rodando o programa

```
$ python main.py {algoritmo} {estado_do_puzzle}
```

Algoritmo -> 'a_star' ou 'bfs'
Estado do puzzle -> Lista com a posição de cada peça, onde 0 indica a posição vazia

A lista representa a matriz da puzzle usando uma dimensão, lendo a matrix da esquerda para a direita e de cima para baixo.

Para obter mais informações sobre o programa:

```
$ python main.py -h
```


## Exemplos

```
$ python main.py bfs [0,1,2,3,4,5,7,8,6]
$ python main.py a_star [1,2,0,4,5,3,7,8,6]
$ python main.py bfs [1,0,2,4,5,3,7,8,6]
```
