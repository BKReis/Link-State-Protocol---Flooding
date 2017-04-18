# Link-State-Protocol using Flooding
Bruno José Bergamaschi Kumer Reis - 14/0017666
Victor Zaffalon Marra - 13/0136760
Lucas Rezende de Macedo - 14/0026363

Versão do python usada -  2.7.10
Execução do programa: python main.py

Após a execução do algoritmo o programa pedira dois valores de entrada para aplicação do dijkstra.
O primeiro numero pedido é o no de inicio do dijkstra e o segundo numero pedido é o no de destino.
Os valores de entrada devem estar entre 0 a 27 de acordo com a tabela abaixo.

Tabela de numeros com a correspondente localização na rede ipe:

0: Porto Alegre
1: Florianópolis
2: Curitiba
3: São Paulo
4: Rio de Janeiro
5: Vitória
6: Campo Grande
7: Cuiabá
8: Belo Horizonte
9: Goiânia
10: Brasília
11: Salvador
12: Aracajú
13: Maceió
14: Recife
15: João Pessoa
16: Campina Grande
17: Natal
18: Fortaleza
19: São Luís
20: Belém
21: Palmas
22: Macapá
23: Manaus
24: Boa Vista
25: Porto Velho
26: Rio Branco
27: Teresina

Alterações em  relação ao Link State  contido no livro

Basicamente, como  no  requisito  do trabalho  nos  foi informado que   não  era necessário a   implementação de  um algoritmo
que levasse em consideração a queda de arestas, de nodos no grafo,  de alterações de peso, bem como a inserção de novos nodos,
descartamos   a inclusão do sequence counter e do aging na implementação das mensagens de nosso flooding, visto que como os pe-
sos serão sempre fixos e os nodos e arestas sempre  presentes, e não haverão  mensagens referentes  à mesma aresta com informa-
ções discrepantes, julgamos que ambos são irrelevantes em nossa implementação e os removemos. No flooding o  algoritmo verifica
se uma mensagem referente a uma aresta já foi recebida pelo nó, em caso positivo, o nó não recebe a mesma mensagem  novamente,
como forma de otimização do código

Quanto as mensagens, criamos um laço que percorria cada nó adicionando informações referentes a cada aresta a uma lista de men-
sagemsagens para posteriormente serem enviadas após percorridos todos os nós. Esse procedimento se repetia até que as tabelas
convergissem.
