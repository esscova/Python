# Trilha Python - Jornada de Dados
Instrutora: Luiza Vieira

## Seção 3 - Estrutura de Dados

### Temas
- Fundamentos das estruturas de dados e listas.
- Índices, tuplas, sets e dicionários.
- Trabalhando com listas, tuplas, sets e dicionários.
- Integrando estruturas de dados e fluxos de controle.

### Exercícios

#### **Exercício 1 – Cadastro de Figurinhas**  
  
Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.  
  
O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".  
  
Ao final, exiba:  
  
Todas as figurinhas cadastradas.  
A quantidade total de figurinhas.  
A primeira figurinha cadastrada.  
A última figurinha cadastrada.  
  
*Desafio: não permita que o usuário cadastre uma figurinha vazia.*

#### **Exercício 2 – Estatísticas da Partida**  
  
Crie um programa que solicite ao usuário as seguintes informações de uma partida:  
  
Seleção mandante  
Seleção visitante  
Gols da seleção mandante  
Gols da seleção visitante  
  
Armazene essas informações em um dicionário.  
  
Depois:  
  
Exiba todas as informações utilizando um for com .items().  
Informe qual seleção venceu a partida.  
Caso os gols sejam iguais, informe que a partida terminou empatada.  
  
*Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.*

#### **Exercício 3 – Seleções Classificadas**  
Durante a fase de grupos, várias seleções foram sendo classificadas.  
  
Peça ao usuário para informar o nome de 8 seleções.  
  
Armazene essas seleções em um set.  
  
Ao final:  
  
Exiba todas as seleções classificadas.  
Informe quantas seleções diferentes foram cadastradas.  
  
Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.  
  
*Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.*

#### **Exercício 4 – Menu do Álbum**  
  
Desenvolva um programa que simule um álbum de figurinhas.  
  
Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:  
  
1 - Adicionar figurinha  
2 - Remover figurinha  
3 - Buscar figurinha  
4 - Mostrar álbum  
5 - Encerrar  
  
O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.  
  
**Regras:**  
  
Ao adicionar, a figurinha deve ser inserida no final da lista.  
Ao remover, informe caso a figurinha não exista.  
Na busca, informe se a figurinha está ou não no álbum.  
Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.  
  
*Desafio: utilize if, elif, else e while.*

#### **Exercício 5 – Ranking de Artilheiros**  
  
Crie uma lista de dicionários para armazenar informações de jogadores.  
  
O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.  
  
Para cada jogador, solicite:  
  
Nome  
Seleção  
Quantidade de gols  
  
Cada jogador deverá ser armazenado como um dicionário dentro da lista.  
  
**Ao final:**  
  
Exiba todos os jogadores cadastrados.  
Informe qual jogador marcou mais gols.  
Informe a média de gols dos jogadores cadastrados.  
  
*Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.*

#### **Exercício 6 – Desafio Final: Sistema da Copa do Mundo**  
  
Desenvolva um programa para cadastrar partidas da Copa do Mundo.  
  
O programa deverá permanecer em execução até que o usuário decida encerrá-lo.  
  
Para cada partida, solicite:  
  
Seleção mandante  
Seleção visitante  
Gols da seleção mandante  
Gols da seleção visitante  
  
Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.  
  
**Ao finalizar o cadastro, exiba:**  
  
A quantidade de partidas cadastradas.  
Todas as partidas registradas.  
Quantas partidas terminaram empatadas.  
A partida com o maior número total de gols.  
A média de gols por partida.  
  
**Requisitos:**  
  
Utilize listas e dicionários.  
Utilize while para controlar o cadastro.  
Utilize for para percorrer as partidas.  
Utilize if, elif e else para identificar o resultado de cada jogo.  
Utilize try/except para validar os gols informados.  
Utilize len() para calcular a quantidade de partidas cadastradas.
