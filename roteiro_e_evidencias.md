Roteiro de Teste Automatizado e Evidências (Tarefa 2)

1. Contexto do Teste

Aplicação em Teste (AUT): Página de Login (simulada em implementacao_pratica_ia.py).

Ferramenta: Selenium com capacidade de Autocorreção (simulando uma ferramenta AIOps como Testim.io).

Cenário: Verificar a resiliência do teste de login após uma mudança no identificador de um elemento (simulação de falha de teste tradicional).

2. Roteiro de Teste

ID do Teste

Ação

Resultado Esperado

Resultado Observado (Simulado)

Status

CT-001

Acessar URL: http://site-ficticio.com/login

Página de login carregada.

Página de login carregada.

PASS

CT-002

Cenário de Falha Simulado: O ID do campo de usuário é alterado de username_field para user_input.

Teste Selenium tradicional falharia com NoSuchElementException.

A ferramenta de IA (Self-Healing) identifica o campo pela propriedade visual (placeholder="Usuário") e continua.

HEALED

CT-003

Inserir credenciais válidas: admin / senha123

Login bem-sucedido. Redirecionamento para o Painel.

Login bem-sucedido. Redirecionamento correto.

PASS

CT-004

Inserir credenciais inválidas: fail / 123

Falha no login. Mensagem de erro exibida: "Credenciais inválidas."

Mensagem de erro exibida.

PASS

3. Evidência Visual (Captura de Tela Conceitual)

A evidência a seguir simula o log de execução da ferramenta AIOps, mostrando que um erro de localização (que faria o Selenium puro falhar) foi automaticamente resolvido pela IA.

[IMAGEM DE LOG DE TESTE]


Descrição da Evidência (O que a imagem mostra):

Alerta de Mudança: A ferramenta de teste exibe uma notificação: "Element with ID 'username_field' not found." (Elemento com ID 'username_field' não encontrado.)

Ação da IA (Self-Healing): A próxima linha mostra: "AI Self-Healing: Re-identifying element using CSS Selector: Selector: 'input

$$plachader"Usuario"$$

'." (Auto-cura de IA: Reidentificando elemento usando Seletor CSS: Seletor: 'input

$$placeholder="Usuário"$$

'.)

Status Final: A execução do teste continua e termina com "Test Run Finished. Total Tests: 4, Passed: 3, Failed: 0, Healed: 1. Success Rate: 100%." (Execução de Teste Finalizada. Total de Testes: 4, Passou: 3, Falhou: 0, Curado: 1. Taxa de Sucesso: 100%.)

Conclusão da Evidência: A captura de tela confirma a principal vantagem da IA em testes automatizados: a resiliência. O teste não falhou devido à mudança de ID, garantindo que o pipeline de CI/CD não fosse interrompido por um problema trivial de manutenção de seletor.