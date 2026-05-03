# 🧠 Documentation_Class_Logic

## 📘 Visão Geral

Esta documentação descreve a **lógica estrutural do projeto**, detalhando a função de cada componente, diretório e script.

O objetivo é fornecer uma visão clara de:

* Como o ambiente é configurado
* Como os dados são manipulados
* Como os resultados são gerados
* Como os componentes se conectam

---

## 🧩 Componentes do Projeto

### 1️⃣ `.devcontainer/devcontainer.json`

Responsável por configurar automaticamente o ambiente no **GitHub Codespaces**.

#### 🔧 Função

* Instalar dependências Python
* Configurar extensões (ex: Python)
* Preparar o ambiente sem intervenção manual

#### ✅ Benefícios

* Padronização do ambiente
* Evita erros de configuração
* Setup automático ao abrir o projeto

---

### 2️⃣ `.vscode/settings.json`

Define configurações locais do **Visual Studio Code**.

#### 🔧 Função

* Fixar o interpretador Python do projeto

#### 🔗 Integração

* Utiliza o mesmo ambiente configurado no `devcontainer.json`

#### ✅ Benefícios

* Evita erros ao usar o botão **Run ▶**
* Garante que as bibliotecas instaladas sejam reconhecidas

---

### 3️⃣ 📁 `Data`

Diretório central de armazenamento de dados.

#### 📂 Estrutura

* Arquivos de entrada:

  * `.txt`
  * `.xlsx`

#### 📁 Subpastas

##### `Resultados_Completos`

* Contém análises finais completas
* Usado para consolidação de dados

##### `Resultados_Atuais`

* Contém resultados recentes
* Gerados em análises exploratórias
* Pode incluir versionamento (timestamp)

#### 📄 Arquivos adicionais

* `.txt` → define ponto inicial da análise
* `.xlsx` → gabarito para validação dos resultados

#### 🔄 Fluxo

```text
Dados Brutos → Processamento → Resultados_Atuais → Resultados_Completos
```

---

### 4️⃣ 🧹 `Tratar_Dados`

Responsável pelo **pré-processamento dos dados**.

#### 📂 Arquivos

##### `converter_txt_Lista.py`

#### 🔧 Função

* Converter dados de arquivos `.txt` em estruturas utilizáveis (ex: listas ou DataFrames)

#### 🧠 Objetivo

* Transformar dados brutos em formato manipulável
* Preparar entrada para análise

---

##### `salvar_Df.py`

#### 🔧 Função

* Salvar DataFrames em arquivos `.xlsx`

#### ⚙️ Funcionalidades

* Criação automática de diretórios
* Geração de nomes com timestamp
* Organização dos resultados

#### 🧠 Objetivo

* Persistir resultados de forma estruturada
* Facilitar rastreabilidade das análises

---

### 5️⃣ 📓 `Notebook`

Representa os arquivos `.ipynb` do projeto.

#### 🔧 Função

* Execução interativa do código
* Análise exploratória de dados
* Visualização de resultados

#### ⚙️ Características

* Execução célula por célula
* Primeira célula dedicada a:

  * instalação de dependências (`pip install`)
* Integração com funções de tratamento e salvamento

#### 🔄 Papel no fluxo

```text
Entrada → Tratamento → Análise → Exportação de Resultados
```

---

### 6️⃣ 🔍 `Verificacoes_Integridade`

Responsável por validar o ambiente de execução.

#### 📂 Arquivo

##### `run.py`

#### 🔧 Função

* Exibir informações do ambiente ao executar via **Run ▶**

#### 📊 Informações exibidas

* Caminho do interpretador Python
* Versão do Python
* Diretório atual

#### 🧠 Objetivo

* Diagnosticar problemas de ambiente
* Verificar se o interpretador correto está sendo utilizado

#### ⚠️ Uso comum

* Resolver erros como:

  * `ModuleNotFoundError`
  * conflito de ambientes Python

---

## 🔗 Integração Geral

O projeto funciona de forma integrada:

```text
devcontainer → configura ambiente
settings.json → garante execução correta
Data → fornece dados
Tratar_Dados → processa dados
Notebook → executa análises
salvar_Df → salva resultados
Verificacoes → valida ambiente
```

---

## 🎯 Conclusão

A arquitetura do projeto foi pensada para:

* Automatizar o ambiente de desenvolvimento
* Organizar o fluxo de dados
* Separar responsabilidades
* Facilitar manutenção e escalabilidade

Cada componente possui um papel bem definido, contribuindo para um sistema coeso, confiável e reutilizável 🚀