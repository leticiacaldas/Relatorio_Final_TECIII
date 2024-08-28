class VerificadorExpressao:
    def __init__(self):
        self.pares = {'(': ')', '{': '}', '[': ']'} # Simbolos de abertura e fechamento

    def verificar_expressao(self, expressao: str) -> bool:
      # Inicializa uma pilha vazia para armazenar os simbolos
        pilha = []
      # Itera sobre cada caractere da expressao  
        for index, char in enumerate(expressao):
      # Se o caractere for um simbolo de abertura, adiciona na pilha    
            if char in self.pares:
                pilha.append(char)
      # Se o caractere for um simbolo de fechamento          
            elif char in self.pares.values():
      # Se a pilha estiver vazia        
                if not pilha:
                    print(f"ERRO: Expressao nao valida na posicao {index + 1}")
                    return False
      # Remove o ultimo simbolo de abertura da pilha            
                topo = pilha.pop()
      # Verifica se o simbolo de fechamento corresponde ao simbolo de abertura removido da pilha          
                if self.pares[topo] != char:
                    print(f"ERRO: Expressao nao valida na posicao {index + 1}")
                    return False
      # Se a pilha não estiver vazia, a expressao não é válida            
        if pilha:
            print("ERRO: Expressao nao valida, falta simbolo de fechamento.")
            return False
      # Se todas as verificaçoes passarem, a expressao é válida    
        print("Expressao valida.")
        return True

    def arquivo_file(self, arquivo_path: str):
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
            for linha_num, linha in enumerate(arquivo, start=1):
                expressao = linha.strip()
                print(f"Verificando linha {linha_num}: {expressao}")
                self.verificar_expressao(expressao)

# Exemplo de uso
verificador = VerificadorExpressao()
verificador.arquivo_file('expressoes.txt')