# Arquivo com funções matemáticas

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b


def calcular_multiplicacao(valor1, valor2):
    return valor1 * valor2


def calcular_divisao(valor1, valor2):
    if valor2 == 0:
        raise ValueError("Não é possível dividir por zero.")

cat >> operacoes.py << 'EOF'


def calcular_divisao(valor1, valor2):
    if valor2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    return valor1 / valor2
