# Trilha Python - Jornada de Dados
Instrutora: Luiza Vieira

## Seção 4 - Funções e procedimentos

### Temas
- Aula 1 – Funções e Procedimentos no Dia a Dia   
- Aula 2 – Fundamentos de Funções: Parâmetros, Argumentos, Retornos, TypeHints e DocStrings

### Exercícios

---

#### **Exercício 1 – Exibindo uma mensagem**  
  
  ---

Crie uma função chamada **exibir_boas_vindas()** que exiba a mensagem: _Bem-vindo ao sistema!_  
  
Depois, chame a função para executar a mensagem.  
  
**Requisitos:**  

-   Utilize def.
-   A função não deve receber parâmetros.
-   A função não precisa retornar nenhum valor.

---

#### **Exercício 2 – Identificando um produto**  
  
  ---
  
Crie uma função chamada **exibir_produto()** que receba:  

1.  o nome de um produto;
2.  o preço do produto.

  
**A função deve exibir uma mensagem no seguinte formato:** _Produto: Teclado | Preço: R$ 150.00_  
  
Depois, chame a função passando um produto e um preço como argumentos.  
  
**Requisitos:**  

1.  Utilize parâmetros.
2.  Adicione type hints nos parâmetros.
3.  A função deve retornar None.

---

#### **Exercício 3 – Calculando o valor de uma compra**  
 
 ---
 
Crie uma função chamada **calcular_total()** que receba:  

1.  o preço de um produto;
2.  a quantidade comprada.

  
**A função deve calcular e retornar o valor total da compra.**  
  
Exemplo:  
  
total = calcular_total(50.0, 3)  
print(total)  
  
Resultado esperado: 150.0  
  
**Requisitos:**  

-   preco deve possuir type hint float.
-   quantidade deve possuir type hint int.
-   A função deve indicar que retorna um float.
-   Utilize return para devolver o resultado.

---

#### **Exercício 4 – Calculando a média de avaliações**  
  
  ---
  
Uma plataforma armazena três avaliações dadas por usuários para um produto.  
  
Crie uma função chamada **calcular_media_avaliacoes()** que receba três notas e retorne a média entre elas.  
  
**Depois, utilize o resultado retornado pela função para exibir a média das avaliações**  
  
**Requisitos:**  

-   Utilize parâmetros e argumentos.
-   Adicione type hints.
-   Utilize return.
-   Adicione uma docstring explicando o que a função recebe e o que retorna.
-   Guarde o resultado da função em uma variável antes de exibi-lo.

---

#### **Exercício 5 – Processando um pedido**  
  
  ---
Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.  
  
A primeira função deve se chamar: **calcular_valor_final()**  

**Ela deve receber:**  

-   preço unitário;
-   quantidade;
-   desconto em formato decimal.

Por exemplo, 0.10 representa 10% de desconto.  
  
A função deve **calcular e retornar o valor final do pedido após o desconto.**  
  
Depois, crie uma segunda função chamada: **exibir_resumo_pedido()**  
  
**Ela deve receber:**  

-   número do pedido;
-   valor final.

  
E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00  
  
**Requisitos:**  

-   As duas funções devem possuir type hints.
-   calcular_valor_final() deve retornar um float.
-   exibir_resumo_pedido() deve retornar None.
-   As duas funções devem possuir docstrings.
-   O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
-   Não faça o cálculo diretamente fora da função.

---

#### **Exercício 6 – Convertendo temperatura**  

---

Crie uma função chamada **converter_celsius_para_fahrenheit()**.  
  
**A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.**  
  
**Use a fórmula:** fahrenheit = (celsius * 9 / 5) + 32  
  
**Depois, armazene o resultado em uma variável e imprima a temperatura convertida.**  
  
**Requisitos:**  

-   Receba a temperatura por parâmetro.
-   Utilize type hint float.
-   A função deve retornar um float.
-   Utilize return.
-   Adicione uma docstring explicando a função.

---

#### **Exercício 7 – Calculando consumo médio**  
  
---

Um veículo percorreu determinada distância utilizando uma quantidade de combustível.  
  
Crie uma função chamada **calcular_consumo_medio()** que receba:  

-   distância percorrida em quilômetros;
-   quantidade de litros utilizados.

  
**A função deve retornar quantos quilômetros o veículo percorreu por litro.**  
  
Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)  
Resultado: 12.0  
  
Depois, crie uma segunda função chamada **exibir_consumo()** que receba o resultado e exiba: Consumo médio: _{resultado}_ km/l  
  
**Requisitos:**  

-   As duas funções devem possuir type hints.
-   calcular_consumo_medio() deve retornar float.
-   exibir_consumo() deve retornar None.
-   As duas funções devem possuir docstrings.
-   O resultado da primeira função deve ser passado como argumento para a segunda.

---

#### **Exercício 8 – Verificando uma meta de vendas**  

---

Crie uma função chamada **calcular_percentual_meta()** que receba:

1.  valor da meta;
2.  valor vendido.

  

**A função deve calcular e retornar o percentual da meta que foi atingido.**  
  
Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)  
Resultado: 75.0  
  
Depois, crie uma função chamada **exibir_status_meta()** que receba esse percentual.  
  
Ela deve exibir: _Meta atingida!_  
**caso o percentual seja maior ou igual a 100.**  
  
**Caso contrário, deve exibir:** _Meta ainda não atingida._  
  
**Requisitos:**  

-   Utilize type hints.
-   calcular_percentual_meta() deve retornar float.
-   exibir_status_meta() deve retornar None.
-   Utilize o valor retornado por uma função como argumento da outra.
-   Adicione docstrings nas duas funções.
-   Não repita o cálculo do percentual fora da função.

---

#### **Exercício 9 – Analisando uma entrega**  
  
 ---
 
Você está desenvolvendo uma pequena parte de um sistema de entregas.  
  
Crie uma função chamada **calcular_tempo_estimado()** que receba:  

1.  distância da entrega em quilômetros;
2.  velocidade média do veículo em km/h.

  
**A função deve calcular e retornar o tempo estimado da entrega em horas.**  
  
Use: tempo = distancia / velocidade  
  
Depois, crie uma função chamada **classificar_entrega() que receba o tempo calculado e retorne:**  
  
"_Entrega rápida_" **se o tempo for menor ou igual a 1;**  
"_Entrega normal_" **se o tempo for maior que 1 e menor ou igual a 3;**  
"_Entrega demorada_" **se o tempo for maior que 3.**  
Por fim, crie uma terceira função chamada **exibir_resumo_entrega()** que receba:  

1.  o tempo estimado;
2.  a classificação.

  
**Ela deve exibir algo como:**

-   Tempo estimado: 2.5 horas
-   Classificação: Entrega normal

  
  
**Requisitos:**

-   As três funções devem possuir type hints.
-   calcular_tempo_estimado() deve retornar float.
-   classificar_entrega() deve retornar str.
-   exibir_resumo_entrega() deve retornar None.
-   Todas devem possuir docstrings.
-   O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
-   Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
-   Cada função deve possuir apenas uma responsabilidade.

---

#### **Exercício 10 – Sistema de Aprovação de Empréstimo**

---

Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.

O programa deverá utilizar **várias funções**, e cada uma terá uma responsabilidade específica.

####   

**1. Calcular comprometimento da renda**

Crie uma função chamada `calcular_comprometimento_renda()` que receba:

-   renda mensal;
-   valor da parcela do empréstimo.

Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.

Use:

```
percentual = (parcela / renda) * 100
```

  

A função deve **retornar** esse percentual.

#### 

#### 

**2. Analisar o empréstimo**

Crie uma segunda função chamada `analisar_emprestimo()` que receba:

-   renda mensal;
-   valor solicitado;
-   percentual de comprometimento da renda.

A função deve retornar uma das seguintes classificações:

```
"Aprovado""Análise manual""Recusado"
```

**Utilize estas regras:**

-   Se o comprometimento da renda for **maior que 40%**, retorne `"Recusado"`.
-   Se o comprometimento for **menor ou igual a 40%**, mas o valor solicitado for **maior que 5 vezes a renda mensal**, retorne `"Análise manual"`.
-   Caso contrário, retorne `"Aprovado"`.

 **3. Calcular o total do pagamento**

Crie uma terceira função chamada `calcular_total_pagamento()` que receba:

-   valor da parcela;
-   quantidade de parcelas.

**Ela deve retornar o valor total que será pago ao final do empréstimo.**

Exemplo:

```
Parcela: R$ 850.00
Quantidade: 24

Total pago: R$ 20400.00
```

**4. Exibir o resultado final**

Por fim, crie uma função chamada `exibir_resultado()` que receba:

-   valor solicitado;
-   percentual de comprometimento;
-   total que será pago;
-   resultado da análise.

Ela deve apenas exibir um resumo como:

```
--- Análise do empréstimo ---
Valor solicitado: R$ 15000.00
Comprometimento da renda: 28.3%
Total a pagar: R$ 20400.00

Resultado: Aprovado
```

  

**Essa função não deve retornar nenhuma informação.**

**Requisitos**

-   Todas as funções devem possuir **type hints**.
-   Todas devem possuir **docstrings**.
-   `calcular_comprometimento_renda()` deve retornar `float`.
-   `analisar_emprestimo()` deve retornar `str`.
-   `calcular_total_pagamento()` deve retornar `float`.
-   `exibir_resultado()` deve retornar `None`.
-   Os cálculos devem acontecer dentro das funções responsáveis por eles.
-   Não repita cálculos fora das funções.
-   Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
-   A função `exibir_resultado()` deve apenas receber os resultados já calculados e exibi-los.
-   Não utilize `*args`, `**kwargs`, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.

**Fluxo esperado**

```
dados do empréstimo    

↓

calcular comprometimento da renda
												            ↓
															analisar empréstimo
															↓

calcular total do pagamento              

↓
																											            exibir resultado final
```

**O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.**
