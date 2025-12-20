# 📊 Dashboard de Acordos de Cooperação Técnica – Governo de Minas Gerais

Dashboard interativo para **visualização, consulta e download de dados públicos** sobre **acordos de cooperação técnica não financeiros** celebrados pelos órgãos do Governo do Estado de Minas Gerais, com base em **arquivos CSV padronizados** e **publicação em dados abertos**.

---

## 🔍 Visão Geral

Este projeto disponibiliza um **dashboard web público** para consulta e análise dos dados de acordos de cooperação técnica que **não envolvem recursos financeiros**.  
A solução permite o acompanhamento transparente das parcerias institucionais firmadas pelo Estado, atendendo às diretrizes de **transparência pública** e **dados abertos**.

As informações seguem **padrões abertos**, garantindo reutilização, interoperabilidade e consistência.

### Principais funcionalidades

- **Visão Geral por Órgão**  
  Visualização agregada da quantidade de acordos por situação  
  *(Vigentes, Concluídos, Expirados, Suspensos)*

- **Consulta Individual de Acordos**  
  Busca detalhada por:
  - Número do termo  
  - Número SEI  
  - Órgão  
  - Parceiro  
  - Período de vigência  
  - Situação

- **Carregamento Automático de Dados**  
  Integração direta com arquivo CSV hospedado no repositório

- **Análise Visual com Gráficos**  
  Gráficos interativos para:
  - Distribuição por situação  
  - Evolução anual  
  - Órgãos mais ativos

- **Exportação de Dados**  
  Download dos dados filtrados ou completos em formato CSV

- **Atualização Contínua**  
  O dashboard se atualiza automaticamente sempre que novos dados são publicados no repositório

---

## 🌐 Acesso Online

O dashboard está disponível publicamente em:

👉 **[(tps://transparencia-mg.github.io/acordos_cooperacao_tecnica/**

Não é necessário login ou autenticação para acesso aos dados.

---

## 🗂️ Estrutura dos Dados

Os dados seguem uma **estrutura padronizada** para acordos de cooperação técnica **sem transferência de recursos financeiros**, alinhada com a legislação de transparência.

### Observação importante

Estes acordos são **exclusivamente de cooperação técnica**, **sem transferência de recursos financeiros**, envolvendo:

- Compartilhamento de conhecimentos  
- Capacitação  
- Assistência técnica  
- Cooperação institucional

---

## ⚙️ Atualização dos Dados

A atualização do dashboard é **automática**, seguindo o fluxo de Dados Abertos do Governo de Minas Gerais:

1. **Inclusão ou atualização dos dados**  
   O arquivo CSV na pasta `data/` do repositório é atualizado ou substituído

2. **Versionamento**  
   As alterações ficam registradas no histórico do GitHub

3. **Publicação automática**  
   O GitHub Pages é reconstruído, refletindo imediatamente os novos dados no site

Para solicitar abertura de novas bases ou relatar problemas, os cidadãos podem utilizar:
- e-SIC  
- Canal *Fale Conosco* do Portal de Dados Abertos

---

## 📦 Dados Abertos e Transparência

Este projeto está alinhado à política de **Transparência Ativa** e **Dados Abertos** do Estado de Minas Gerais, que determina a divulgação de informações de interesse coletivo em **formatos abertos e legíveis por máquina**.

A coordenação da política de dados abertos é realizada pela:

- **:contentReference[oaicite:0]{index=0} (CGE-MG)**
- **:contentReference[oaicite:1]{index=1} (SEPLAG-MG)**

Os dados seguem boas práticas e padrões como **Frictionless Data**, garantindo:
- Qualidade
- Documentação adequada
- Fácil reutilização por cidadãos, pesquisadores e sistemas

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Bibliotecas:**
  - DataTables — tabelas interativas
  - Chart.js — gráficos
  - PapaParse — processamento de CSV
- **Hospedagem e Versionamento:** GitHub Pages e Git
- **Padrão de Dados:** CSV padronizado

---

## 📄 Licença

Os dados e o código deste repositório são disponibilizados sob a licença:

**Creative Commons Attribution 4.0 (CC-BY-4.0)**

É permitida a reutilização dos dados, desde que citada a fonte.

---

## 🏛️ Órgãos Responsáveis e Contexto

- **Controladoria-Geral do Estado de Minas Gerais (CGE-MG)**  
  Órgão central do sistema de controle interno e responsável pela coordenação da política de dados abertos e transparência

- **Secretaria de Estado de Planejamento e Gestão (SEPLAG-MG)**  
  Responsável pela gestão das informações sobre contratos e parcerias e líder do processo de transformação digital no Estado

### Contexto de Transparência

A publicação detalhada desses dados atende às exigências legais e reforça o compromisso do Governo de Minas Gerais com:

- Prestação de contas
- Controle social
- Transparência das parcerias institucionais


