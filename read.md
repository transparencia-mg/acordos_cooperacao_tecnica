📊 Dashboard de Acordos de Cooperação Técnica – Governo de Minas Gerais
Dashboard interativo para visualização, consulta e download de dados públicos sobre acordos de cooperação técnica não financeiros celebrados pelos órgãos do Governo do Estado de Minas Gerais, com base em arquivos CSV padronizados e publicação em dados abertos.

🔍 Visão Geral
Este projeto disponibiliza um dashboard web público para consulta e análise dos dados de acordos de cooperação técnica que não envolvem recursos financeiros. A solução permite o acompanhamento transparente das parcerias institucionais firmadas pelo Estado, atendendo às diretrizes de transparência pública e dados abertos. As informações seguem padrões abertos para garantir reutilização e consistência.

Principais funcionalidades:

Visão Geral por Órgão: Visualização agregada da quantidade de acordos por situação (Vigentes, Concluídos, Expirados, Suspensos)

Consulta Individual de Acordos: Busca detalhada por número do termo, SEI, órgão, parceiro, período de vigência e situação

Carregamento Automático de Dados: Integração direta com arquivo CSV hospedado no repositório

Análise Visual com Gráficos: Gráficos interativos para análise da distribuição por situação, evolução anual e órgãos mais ativos

Exportação de Dados: Possibilidade de exportar os dados filtrados ou completos para formato CSV

Atualização Contínua: O dashboard se atualiza automaticamente quando novos dados são publicados no repositório

🌐 Acesso Online
O dashboard está disponível publicamente em:

👉 [Link para o GitHub Pages do Repositório]

Substitua o texto acima pelo URL real após a publicação.

Não é necessário login ou autenticação para acesso aos dados.

🗂️ Estrutura dos Dados
Os dados seguem a estrutura padronizada para acordos de cooperação técnica não financeiros firmados pelo Estado, alinhada com a legislação de transparência.

O arquivo principal acordos_cooperacao_tecnica_sem_recursos.csv contém as seguintes colunas:

Campo	Descrição	Tipo
ano	Ano de celebração do acordo	Número
numero_termo	Número identificador do termo de cooperação	Texto
numero_sei	Número do processo no Sistema Eletrônico de Informações (SEI)	Texto
orgao_acordo	Órgão ou entidade do Governo de Minas Gerais signatário	Texto
parceiro_acordo	Instituição parceira (outro órgão público, entidade, etc.)	Texto
objeto	Descrição do objetivo e escopo da cooperação técnica	Texto
natureza_cooperacao	Natureza da cooperação (técnica, científica, institucional, etc.)	Texto
inicio_vigencia	Data de início da vigência do acordo	Data (AAAA-MM-DD)
fim_vigencia	Data de término da vigência do acordo	Data (AAAA-MM-DD)
situacao	Situação atual (VIGENTE, CONCLUÍDO, EXPIRADO, SUSPENSO)	Texto
link_documento	Hiperlink para acesso ao documento integral do acordo	URL
numero_documento	Número de identificação do documento relacionado	Texto
Observação importante: Estes acordos são exclusivamente de cooperação técnica sem transferência de recursos financeiros, envolvendo compartilhamento de conhecimentos, capacitação, assistência técnica e outras formas de colaboração institucional.

⚙️ Atualização dos Dados
A atualização do dashboard é automática. O processo segue o fluxo de trabalho típico de Dados Abertos do Governo de Minas Gerais:

Inclusão/Atualização de Dados: O arquivo CSV na pasta data/ do repositório é atualizado ou substituído

Versionamento: As alterações são registradas no histórico do GitHub

Publicação Automática: O site no GitHub Pages é reconstruído, refletindo imediatamente os novos dados para os cidadãos

Para solicitar a abertura de novas bases de dados ou relatar problemas, os cidadãos podem utilizar o e-SIC ou o canal Fale Conosco do Portal de Dados Abertos.

📦 Dados Abertos e Transparência
Este projeto está alinhado à política de Transparência Ativa e Dados Abertos do Estado, que determina a divulgação de informações de interesse coletivo em formatos abertos e legíveis por máquina. A gestão e abertura desses dados são coordenadas pela Controladoria-Geral do Estado (CGE-MG) e pela Secretaria de Estado de Planejamento e Gestão (SEPLAG-MG), órgãos centrais para essas políticas.

Os dados publicados seguem as melhores práticas, utilizando padrões como o Frictionless Data, para garantir qualidade, documentação adequada e fácil reutilização por outros sistemas e cidadãos.

🛠️ Tecnologias Utilizadas
Frontend: HTML5, CSS3, JavaScript (Vanilla)

Bibliotecas: DataTables (para tabelas interativas), Chart.js (para gráficos), PapaParse (para processamento de CSV)

Hospedagem e Controle de Versão: GitHub Pages e Git

Padrão de Dados: CSV padronizado

📄 Licença
Os dados e o código deste repositório são disponibilizados sob a licença:

Creative Commons Attribution 4.0 (CC-BY-4.0)

É permitida a reutilização dos dados, desde que citada a fonte.

🏛️ Órgãos Responsáveis e Contexto
Controladoria-Geral do Estado de Minas Gerais (CGE-MG): Órgão central do sistema de controle interno e responsável pela coordenação da política de dados abertos e transparência no estado

Secretaria de Estado de Planejamento e Gestão (SEPLAG-MG): Responsável pela gestão das informações sobre contratos e parcerias, e líder do processo de transformação digital no estado

Contexto de Transparência: A publicação detalhada desses dados atende a exigências legais e reforça o compromisso do Governo de Minas Gerais com a prestação de contas e o controle social sobre as parcerias de cooperação técnica institucional
