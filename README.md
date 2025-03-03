# Projeto 1 - Calculadora Python automatizada com Shell Script (EBAC)

Este projeto é uma calculadora em Python que realiza operações matemáticas básicas, como adição, subtração, multiplicação e divisão. Inclui um arquivo em shell script que automatiza a execução da calculadora, permitindo que os usuários iniciem o programa rapidamente, sem precisar rodar o código manualmente. Ideal para facilitar cálculos do dia.

___

# Instruções para Executar o Script `calculadora.sh`

## Descrição

O script `calculadora.sh` é uma calculadora interativa que solicita o nome do usuário e executa um arquivo Python (`Modulo1Pratico.py`) para realizar cálculos.

## Pré-requisitos

- **Python 3** deve estar instalado.
- O arquivo **`Modulo1Pratico.py`** deve estar no mesmo diretório que o **`calculadora.sh`**.

## Como Executar o Script

1. **Abra um terminal.**

2. **Navegue até o diretório onde o arquivo `calculadora.sh` está localizado.**  
   Use o comando:
   ```bash
   cd /caminho/do/diretorio

3. Execute o script com o seguinte comando:

   ```bash
   ./calculadora.sh

4. Siga as instruções na tela.

 	**Exemplos de saída**
   ```bash
   Digite o seu nome: João
   Seja Bem-vindo(a) à nossa calculadora João!

___

# Notas Finais

Dê permissão de execução ao script (se ainda não tiver feito isso):
	Comando: chmod +x calculadora.sh

Certifique-se de que o arquivo Modulo1Pratico.py está funcionando corretamente antes de executar o script.

Para encerrar a calculadora, siga as instruções apresentadas no programa.

___
# Documentação da Calculadora Python

## Descrição
Este código implementa uma calculadora interativa em Python que permite ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão). O usuário pode escolher entre realizar uma única operação ou criar um loop que permite realizar várias operações consecutivas.

## Funcionamento

1. **Loop Infinito**: O programa inicia um loop infinito que permite ao usuário continuar realizando operações até que decida parar.

2. **Entrada de Dados**:
    - **`numero1`**: Primeiro número digitado pelo usuário.
    - **`numero2`**: Segundo número digitado pelo usuário.
    - **`tipo_op`**: O usuário escolhe entre:
        - `"O"` para selecionar uma operação única.
        - `"L"` para gerar um loop de operações.

3. **Operações**:
    - **Operação Única (`tipo_op == 'O'`)**:
        - O usuário escolhe a operação matemática desejada (`+`, `-`, `*`, `/`).
        - O resultado é calculado e exibido.
        - Se a operação for uma divisão e `numero2` for zero, uma mensagem de erro é exibida.

    - **Loop de Operação (`tipo_op == 'L'`)**:
        - O usuário escolhe uma operação para repetir em um loop.
        - Dependendo da operação escolhida, o programa executa a operação em um loop até que uma condição de parada seja atendida:
            - **Adição (`+`)**: O programa soma `numero2` a `val` (inicialmente igual a `numero1`) até que `val` atinja um limite superior (999999).
            - **Subtração (`-`)**: O programa subtrai `numero2` de `val` até que `val` se torne menor ou igual a zero.
            - **Multiplicação (`*`)**: O programa multiplica `val` por `numero2` até que `val` atinja um limite superior (999999).
            - **Divisão (`/`)**: O programa divide `val` por `numero2` até que `val` se torne menor que 1. Se `numero2` for zero, uma mensagem de erro é exibida.

4. **Continuar ou Parar**:
    - Após cada operação, o programa pergunta ao usuário se deseja realizar outra operação. Se o usuário responder com algo diferente de `'s'`, o loop é encerrado e o programa termina.

## Variáveis
- **`numero1`**: Primeiro número fornecido pelo usuário.
- **`numero2`**: Segundo número fornecido pelo usuário.
- **`tipo_op`**: Tipo de operação selecionada pelo usuário (Operação única ou Loop).
- **`operacao`**: Operação matemática escolhida pelo usuário para a operação única.
- **`operacao2`**: Operação escolhida pelo usuário para o loop.
- **`val`**: Variável que armazena o valor atual para as operações em loop. Inicialmente, é definida como `numero1`.

## Observações
- O código inclui verificações para evitar divisões por zero.
- O loop de operações permite que o usuário realize cálculos contínuos, facilitando a interação.

## Exemplo de Uso
1. O usuário digita dois números.
2. O usuário escolhe entre realizar uma operação única ou um loop de operações.
3. O programa executa a operação e exibe o resultado.
4. O usuário pode continuar realizando operações até decidir parar.
