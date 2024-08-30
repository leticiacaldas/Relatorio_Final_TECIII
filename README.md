Verificador de Expressão Matemática
Descrição

Este projeto implementa um verificador de expressões matemáticas utilizando a estrutura de dados de pilha. O programa é capaz de analisar expressões contendo parênteses (), colchetes [], e chaves {} para determinar se estão bem formadas, ou seja, se todos os símbolos de abertura têm correspondentes de fechamento na ordem correta.
Funcionalidades

    Verificação de Expressões: O programa lê expressões de um arquivo texto e verifica se elas são válidas.
    Mensagens de Erro: Caso uma expressão seja mal formada, o programa indica a posição do erro.
    Testes Unitários: Inclui testes unitários para garantir a correção das funcionalidades.

Estrutura do Projeto

    codigo_pares.py: Contém a classe VerificadorExpressao que realiza a verificação das expressões.
    test_verificador.py: Contém os testes unitários usando pytest.
    expressoes.txt: Arquivo de exemplo contendo expressões para verificação.

Como Usar
Requisitos

    Python 3.x
    pytest para execução dos testes unitários.

Executando o Verificador

    Coloque suas expressões no arquivo expressoes.txt, uma por linha.

    Execute o script principal para verificar as expressões:

    bash

    python codigo_pares.py

Executando os Testes

Para rodar os testes unitários e garantir que tudo está funcionando corretamente, utilize:

bash

pytest test_verificador.py

Exemplos
Expressões Válidas

    (a + b) * [c - d]
    {[()]}
    ((2 + 3) * 5)

Expressões Inválidas

    (a + b) * [c - d}
    ([)]
    ((2 + 3) * 5

Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests. Todas as contribuições são bem-vindas!
Licença

Este projeto está licenciado sob a MIT License.
