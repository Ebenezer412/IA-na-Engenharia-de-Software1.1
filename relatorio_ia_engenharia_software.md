Relatório da Semana 4: Construindo Soluções de Software Inteligentes

Disciplina: IA na Engenharia de Software
Tema: Construindo Soluções de Software Inteligentes
Data: 20 de Outubro de 2025

Parte 1: Análise Teórica (30%)

1. Perguntas de Resposta Curta

Q1: Explique como ferramentas de geração de código baseadas em IA (por exemplo, GitHub Copilot) reduzem o tempo de desenvolvimento. Quais são suas limitações?

As ferramentas de geração de código por IA reduzem o tempo de desenvolvimento principalmente através da automação do código clichê (boilerplate) e da redução da alternância de contexto. Em vez de procurar a sintaxe exata ou implementações comuns (como ler um arquivo, escrever um loop de iteração ou configurar uma função de utilidade), o desenvolvedor recebe sugestões em tempo real que completam linhas inteiras ou funções baseadas no contexto do projeto e nos comentários. Isso aumenta o fluxo (flow state) e a velocidade de escrita.

Limitações:

Segurança e Qualidade: O código gerado pode conter vulnerabilidades ou bugs, exigindo uma revisão manual rigorosa. A IA não garante que o código seja eficiente ou seguro.

Contexto Limitado: A IA pode não compreender totalmente a arquitetura complexa ou as nuances específicas de um grande sistema de software, resultando em sugestões incorretas ou incompletas.

Viés e Propriedade: As sugestões baseadas em repositórios de treinamento podem replicar padrões de código subótimos ou levantar questões de licenciamento e propriedade intelectual.

Q2: Compare o aprendizado supervisionado e não supervisionado no contexto da detecção automatizada de bugs.

Característica

Aprendizado Supervisionado

Aprendizado Não Supervisionado

Objetivo na Detecção

Classificação: Classificar uma parte do código/commit como "Bug" (positivo) ou "Não Bug" (negativo).

Detecção de Anomalias: Identificar padrões de código, logs ou métricas que se desviam significativamente da "norma" estabelecida.

Dados de Treinamento

Requer dados rotulados, onde cada amostra de código ou registro de log é explicitamente marcada como "Bug" ou "Não Bug".

Utiliza dados não rotulados, assumindo que a maioria dos dados representa o comportamento normal.

Exemplo de Aplicação

Treinar um classificador (como Regressão Logística ou SVM) em métricas de complexidade do código e histórico de commits para prever a probabilidade de um arquivo conter um defeito (bug).

Usar Algoritmos de Clusterização (como K-Means) para agrupar logs de erros semelhantes durante a execução, sinalizando quaisquer logs que não se encaixem nos clusters normais como potenciais novos bugs ou falhas.

Q3: Por que a mitigação de vieses é essencial ao usar IA para personalização da experiência do usuário?

A mitigação de vieses é essencial para garantir a equidade e a inclusão. Se os modelos de IA para personalização (como recomendação de conteúdo ou priorização de recursos) forem treinados em dados históricos que refletem preconceitos sociais (por exemplo, dados de usuários predominantemente de um grupo demográfico específico), eles podem:

Excluir ou Sub-representar: Oferecer uma experiência de usuário inferior ou irrelevante para grupos minoritários, limitando o acesso a informações ou recursos.

Reforçar Estereótipos: Sugerir conteúdo ou caminhos de carreira com base em atributos protegidos (como gênero ou etnia), perpetuando desigualdades.
A mitigação de vieses (Fairness) garante que a personalização melhore a experiência de todos os usuários de forma justa.

2. Análise de Estudo de Caso: IA em DevOps (AIOps)

Resposta: Como o AIOps melhora a eficiência da implantação de software? Dê dois exemplos.

O AIOps melhora a eficiência da implantação de software ao aplicar Machine Learning e Big Data para automatizar a tomada de decisões e a análise de logs em todo o pipeline de DevOps. Isso transforma a resposta reativa a falhas em uma abordagem proativa e preditiva.

Dois Exemplos de Melhoria de Eficiência:

Detecção e Mitigação de Anomalias em Tempo Real: Durante ou imediatamente após a implantação, o AIOps monitora logs e métricas de desempenho em tempo real. Se um pequeno desvio (anomalia) ocorrer (como um aumento sutil na latência ou taxa de erros), o sistema de IA pode alertar imediatamente, isolar a mudança exata que causou o problema e até mesmo iniciar um rollback automatizado antes que a falha afete um grande número de usuários, economizando tempo crucial de engenharia.

Alocação e Otimização Preditiva de Recursos: O AIOps analisa dados históricos de desempenho de implantações anteriores e cargas de tráfego. Com base nessa análise, ele pode prever as necessidades futuras de infraestrutura para uma nova implantação (por exemplo, quanta RAM, CPU ou instâncias de serviço serão necessárias). Isso automatiza a escalabilidade e o provisionamento antes do lançamento, garantindo que o software tenha os recursos exatos de que precisa para rodar de forma eficiente, evitando gastos excessivos ou falhas por sobrecarga.

Parte 2: Implementação Prática (60%) - Análises de Texto

Tarefa 1: Conclusão de Código com Tecnologia de IA (Análise)

Entregável: Análise de 200 palavras.

A tarefa consistia em escrever uma função Python para classificar uma lista de dicionários por uma chave específica.

Versão Sugerida pela IA (GitHub Copilot/Tabnine - Esperada):

# A IA provavelmente sugeriu o uso da função built-in 'sorted' com uma função lambda
sorted_list = sorted(data, key=lambda x: x[sort_key])


Versão de Implementação Manual (Ineficiente - Simulação):

# Simulação de uma implementação manual menos eficiente (ex: Bubble Sort ou loop complexo)
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][sort_key] > data[j + 1][sort_key]:
            data[j], data[j + 1] = data[j + 1], data[j]


Análise de Eficiência:

A versão sugerida pela IA é, sem dúvida, a mais eficiente e Pythonica. O Copilot, treinado em vastos repositórios, prioriza o uso de métodos otimizados da linguagem. A função sorted() em Python é implementada em C e utiliza o algoritmo Timsort (uma combinação de Merge Sort e Insertion Sort), garantindo uma complexidade temporal média de $O(N \log N)$, que é altamente eficiente para listas de qualquer tamanho.

Em contraste, uma implementação manual com um algoritmo ingênuo como o Bubble Sort (simulado acima) teria uma complexidade temporal de $O(N^2)$. Para listas grandes de dicionários, a diferença de tempo de execução seria enorme. A IA não apenas reduziu o tempo de escrita (basta digitar def sort_list_of_dicts(...) para que a sugestão apareça), mas também promoveu a qualidade do código, orientando o desenvolvedor a usar a biblioteca padrão mais performática, um benefício que transcende a simples automação da digitação.

Tarefa 2: Teste Automatizado com IA (Resumo)

Entregável: Resumo de 150 palavras.

A IA melhora drasticamente a cobertura de testes em comparação aos testes manuais, principalmente introduzindo a capacidade de autocorreção (self-healing) e a geração inteligente de testes.

Em um cenário tradicional de Selenium, se o ID ou XPath de um elemento de login mudar, o script de teste falha e exige intervenção manual. Ferramentas baseadas em IA (como Testim.io ou plugins de IA no Selenium) resolvem isso analisando as propriedades visuais, o texto e o contexto do elemento. Se o ID mudar, a IA ainda consegue identificar que o botão "Entrar" é o mesmo elemento, e o teste continua, aumentando a robustez e reduzindo o tempo de manutenção do script.

Além disso, a IA pode analisar o código-fonte ou o histórico de uso para gerar variações de casos de teste que o testador humano pode não ter considerado (por exemplo, combinações incomuns de caracteres em campos de credenciais). Essa geração e manutenção automatizada e adaptativa de testes resulta em uma cobertura mais ampla e consistente, liberando os testadores humanos para se concentrarem em testes exploratórios complexos.

Parte 3: Reflexão Ética (10%)

Sugestão: Seu modelo preditivo da Tarefa 3 é implantado em uma empresa para prever a prioridade do problema (alta/média/baixa).

Discussão:

Possíveis Vieses no Conjunto de Dados

O conjunto de dados usado para treinar o modelo de prioridade de problemas pode apresentar vieses históricos significativos, levando à injustiça algorítmica.

Exemplo de Viés: Se o histórico de dados de problemas (issues) mostrar que:

Problemas relatados por equipes minoritárias (por exemplo, uma equipe de QA júnior ou uma equipe em um fuso horário menos central) foram historicamente classificados como "Baixa" prioridade, enquanto problemas semelhantes relatados por equipes de liderança foram classificados como "Alta".

O campo "Descrição" do problema continha termos que, apesar de técnicos, eram mais comuns em um subconjunto da equipe, e o modelo correlacionou incorretamente esses termos com "Baixa" prioridade.

O modelo aprenderá esse padrão enviesado e perpetuará o tratamento desigual, atribuindo automaticamente "Baixa" prioridade a novos problemas provenientes dessas equipes ou com características textuais semelhantes, ignorando a gravidade real.

Como Ferramentas de Justiça (Fairness) Podem Lidar com Esses Preconceitos

Ferramentas como o IBM AI Fairness 360 (AIF360) fornecem métricas e algoritmos para auditar e mitigar esses vieses.

Auditoria (Metrics): O AIF360 permite definir grupos protegidos (por exemplo, "equipe júnior" vs. "equipe sênior" ou "país de origem"). Ele calcula métricas de disparidade, como o Disparate Impact (Impacto Disparitário). Se o modelo tiver um Disparate Impact baixo (ex: o grupo privilegiado recebe prioridade 'Alta' 80% das vezes, mas o grupo desfavorecido recebe apenas 20%), o viés é quantificado.

Mitigação (Algorithms):

Pré-processamento: Algoritmos como o Reweighting (Rebalanceamento) ajustam os pesos dos pontos de dados no conjunto de treinamento para que o modelo dê importância igual às amostras de ambos os grupos, antes do treinamento.

Pós-processamento: Algoritmos como o Calibrated Equalized Odds (Probabilidades Equalizadas Calibradas) ajustam os resultados do modelo, aplicando limiares de classificação diferentes para os grupos protegidos, garantindo que a taxa de falsos positivos e falsos negativos seja mais equilibrada entre eles.

Tarefa Bônus: Desafio de Inovação (10% extra)

Proposta de Ferramenta de IA: Documentador Arquitetural Automático (DAA)

Propósito: O DAA visa resolver a dor da documentação arquitetural desatualizada, que se torna obsoleta assim que o código é alterado. Ele gera e mantém diagramas C4 (Contexto, Contêineres, Componentes, Código) e especificações de serviços automaticamente.

Fluxo de Trabalho:

Análise de Código Estático: O DAA rastreia o projeto e usa análise estática para identificar limites de serviços (microsserviços, funções, classes principais), contratos de API (endpoints, payloads) e dependências entre eles (chamadas de funções, HTTP requests).

Análise de Histórico Git: Ele escaneia o Git history e os metadados de Pull Requests (PRs). Se um PR introduzir uma nova dependência ou alterar um contrato de API, o DAA marca o diagrama arquitetural relevante como "Obsoleto" ou "Precisa de Revisão".

Geração de Diagramas: Usando um LLM, o DAA converte o "modelo" interno de componentes e relações (extraído do código) em código de descrição de diagrama (ex: PlantUML ou Mermaid).

Integração de Revisão: O DAA propõe a atualização do diagrama diretamente no PR (como um comentário ou arquivo alterado), permitindo que a equipe de engenharia aprove ou ajuste a nova documentação em conjunto com a mudança de código.

Impacto:

O DAA garante que a documentação arquitetural permaneça uma "fonte única de verdade" (Single Source of Truth), reduzindo o atrito de onboarding para novos desenvolvedores, facilitando revisões de segurança e arquitetura e eliminando o custo manual de manter diagramas. A documentação torna-se um artefato de primeira classe no pipeline de CI/CD.