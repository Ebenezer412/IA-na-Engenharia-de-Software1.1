import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.datasets import make_classification # Usado para simular dados para a Tarefa 3
import time
# Se ocorrer ModuleNotFoundError: No module named 'selenium', instale com: pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# ==============================================================================
# PARTE 2: TAREFA 1 - CONCLUSÃO DE CÓDIGO COM TECNOLOGIA DE IA
# Objetivo: Função Python para classificar uma lista de dicionários por uma chave.
# ==============================================================================

def ordenar_lista_de_dicionarios_manual(data, chave):
    """
    Função manual (e menos eficiente) para ordenar uma lista de dicionários
    usando o algoritmo Bubble Sort para fins de comparação.
    Complexidade: O(N^2)
    """
    print(f"\n--- TAREFA 1: Ordenação Manual (O(N^2)) ---")
    n = len(data)
    lista_para_ordenar = list(data) # Cria uma cópia para evitar modificar o original
    
    start_time = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_para_ordenar[j][chave] > lista_para_ordenar[j + 1][chave]:
                # Troca os elementos
                lista_para_ordenar[j], lista_para_ordenar[j + 1] = lista_para_ordenar[j + 1], lista_para_ordenar[j]
    end_time = time.time()
    
    print(f"Tempo de execução (Manual): {end_time - start_time:.6f} segundos.")
    return lista_para_ordenar

def ordenar_lista_de_dicionarios_ia(data, chave):
    """
    Função sugerida pela IA (Copilot), usando a função built-in 'sorted'.
    Esta é a abordagem Pythonica e mais eficiente (Timsort: O(N log N)).
    """
    print(f"\n--- TAREFA 1: Ordenação Sugerida pela IA (O(N log N)) ---")
    
    start_time = time.time()
    # A função lambda é a chave para o uso eficiente do 'sorted'
    lista_ordenada = sorted(data, key=lambda d: d[chave])
    end_time = time.time()
    
    print(f"Tempo de execução (IA/Built-in): {end_time - start_time:.6f} segundos.")
    return lista_ordenada

# Exemplo de uso para comparação
dados = [
    {'nome': 'João', 'idade': 30, 'pontos': 150},
    {'nome': 'Maria', 'idade': 25, 'pontos': 220},
    {'nome': 'Pedro', 'idade': 40, 'pontos': 100},
    {'nome': 'Ana', 'idade': 22, 'pontos': 300},
] * 100 # Aumentamos o tamanho para notar a diferença de desempenho

# Ordena e compara
lista_manual = ordenar_lista_de_dicionarios_manual(dados, 'pontos')
lista_ia = ordenar_lista_de_dicionarios_ia(dados, 'pontos')

# print("\nPrimeiros 5 resultados (Manual):", lista_manual[:5])
# print("Primeiros 5 resultados (IA):", lista_ia[:5])


# ==============================================================================
# PARTE 2: TAREFA 2 - TESTE AUTOMATIZADO COM IA (Conceitual)
# Objetivo: Simular um caso de teste de login com Selenium e explicar o papel da IA.
# NOTA: O Selenium precisa de um driver (como chromedriver) e de uma URL real.
# Este código é conceitual e usa um try/except para simular a execução.
# ==============================================================================

print("\n--- TAREFA 2: Estrutura Conceitual de Teste com Selenium ---")

def executar_teste_login(url, user, password):
    """
    Função conceitual para demonstrar um teste de login.
    """
    try:
        # Inicialização do WebDriver (necessita do Chrome/Gecko driver instalado)
        # driver = webdriver.Chrome() 
        # driver.get(url)
        print(f"Tentando acessar URL: {url}...")
        
        # Simulação de Ações de Teste (IA rastrearia elementos aqui)
        print(f"Simulando entrada de credenciais: {user} / {password}...")
        
        # Simulação de sucesso/falha
        if user == "admin" and password == "senha123":
            resultado = "Sucesso"
        else:
            resultado = "Falha"

        # Simulação de captura de resultado e encerramento
        # driver.quit()
        
        return resultado, f"Login com {user} / {password} resultou em {resultado}."

    except WebDriverException as e:
        return "Erro de Setup", f"Erro ao iniciar o WebDriver ou acessar a URL. \n\tDetalhe: {e.msg}"
    except Exception:
        return "Execução Simples", "Simulação de teste concluída."


# Simulação de Casos de Teste
url_teste = "http://site-ficticio.com/login" # Altere para uma URL real se for executar
casos_de_teste = [
    ("admin", "senha123", "Válido"),
    ("usuario_invalido", "senha_errada", "Inválido")
]

for user, pwd, tipo in casos_de_teste:
    status, mensagem = executar_teste_login(url_teste, user, pwd)
    print(f"Resultado do Teste {tipo}: {status}. Mensagem: {mensagem}")

print("\n** Papel da IA em Testes Automatizados: **")
print("Em uma ferramenta como Testim.io, a IA não usa apenas ID, mas também propriedades visuais e texto (como 'Placeholder: Email') para identificar elementos. Se o ID mudar (o que quebraria o Selenium tradicional), a IA 'se cura' (self-healing) e o teste continua rodando, aumentando a robustez.")


# ==============================================================================
# PARTE 2: TAREFA 3 - ANÁLISE PREDITIVA PARA ALOCAÇÃO DE RECURSOS
# Objetivo: Treinar um Random Forest para prever a prioridade do problema
# Usamos make_classification para simular um dataset com 3 classes (prioridade).
# ==============================================================================

print("\n--- TAREFA 3: Análise Preditiva (Prioridade de Problemas) ---")

# 1. Geração de Dados Simulados (Simulando o dataset de Câncer/Problemas)
# Features (X) simulam métricas: complexidade do código, tempo de vida do problema, logs de erro, etc.
# Target (y) simula a Prioridade: 0=Baixa, 1=Média, 2=Alta
X, y = make_classification(
    n_samples=1000, 
    n_features=10, 
    n_informative=5, 
    n_redundant=0, 
    n_classes=3, 
    n_clusters_per_class=1, 
    random_state=42
)

# Criando um DataFrame para facilitar a visualização e pré-processamento
feature_names = [f'feature_{i}' for i in range(10)]
df = pd.DataFrame(X, columns=feature_names)
df['prioridade'] = y

# Mapeando classes numéricas para rótulos para melhor entendimento
prioridade_map = {0: 'Baixa', 1: 'Média', 2: 'Alta'}
df['prioridade_rotulo'] = df['prioridade'].map(prioridade_map)

print(f"Dataset de 1000 amostras com 10 features e 3 classes de prioridade.")
print(f"Contagem de prioridades:\n{df['prioridade_rotulo'].value_counts()}")

# 2. Pré-processamento e Divisão de Dados
# Definindo features (X) e target (y)
X = df[feature_names]
y = df['prioridade']

# Dividindo o dataset em treinamento (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTamanho do conjunto de treinamento: {len(X_train)} amostras")
print(f"Tamanho do conjunto de teste: {len(X_test)} amostras")

# 3. Treinamento do Modelo (Random Forest)
print("\nIniciando Treinamento do Modelo Random Forest...")
# Random Forest é robusto e bom para classificação multi-classe
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

print("Treinamento concluído com sucesso.")

# 4. Avaliação do Modelo
y_pred = modelo.predict(X_test)

# Métrica 1: Acurácia
acuracia = accuracy_score(y_test, y_pred)
# Métrica 2: F1 Score (média ponderada útil para classes desbalanceadas)
f1_macro = f1_score(y_test, y_pred, average='macro')
f1_weighted = f1_score(y_test, y_pred, average='weighted')

print("\n--- Métricas de Desempenho no Conjunto de Teste ---")
print(f"Acurácia: {acuracia:.4f}")
print(f"F1 Score (Macro): {f1_macro:.4f} (Trata todas as classes igualmente)")
print(f"F1 Score (Weighted): {f1_weighted:.4f} (Pondera pelo suporte de cada classe)")

# Relatório de Classificação Detalhado
print("\nRelatório de Classificação (Prioridades):")
# Os rótulos (0, 1, 2) são mapeados no relatório para as classes
print(classification_report(y_test, y_pred, target_names=prioridade_map.values()))

# Exemplo de Previsão para um Novo Problema
novo_problema = pd.DataFrame(
    np.array([
        [0.5, 1.2, 0.1, -0.5, 2.0, 0.3, -1.0, 0.8, 1.5, -0.2]
    ]), 
    columns=feature_names
)
previsao = modelo.predict(novo_problema)[0]
prioridade_prevista = prioridade_map[previsao]

print(f"Previsão para um novo problema (features específicas): Prioridade {prioridade_prevista}")
