# 🚀 Documentation_Notebook (.ipynb)

## 📘 Visão Geral

Este projeto utiliza **notebooks Jupyter (`.ipynb`)** para execução de análises, manipulação de dados e geração de resultados de forma interativa.

Os notebooks permitem rodar o código em células, facilitando testes, depuração e visualização dos dados passo a passo.

---

## 📦 Instalação de Dependências (Primeira Célula)

A **primeira célula do notebook** é responsável por instalar automaticamente todas as dependências necessárias do projeto.

### ▶️ Execute sempre primeiro:

```python
!pip install -q -r requirements.txt
```

Essa célula garante que todas as bibliotecas estejam disponíveis no ambiente antes da execução do restante do código.

**⚠️ Importante:**

* Execute essa célula **antes de qualquer outra**
* Execute novamente caso reinicie o kernel
* Necessário principalmente em ambientes como:

  * GitHub Codespaces
  * Google Colab
  * Jupyter online

---

## ▶️ Como Executar o Notebook

### 💻 VS Code / Codespaces

1. Abra o arquivo `.ipynb`
2. Clique em **Select Kernel** (canto superior direito), em **Executar Tudo** ou no botão **Run ▶** de uma cédula específica
3. Selecione **Instalar/habilitar extenções sugeridas ...**
4. Clique em **Ambientes do Python** 
5. Escolha o interpretador Python desejado
6. Execute:

   * `Shift + Enter` ou `botão **Run ▶**` (célula por célula), ou
   * **Run All ▶** (executar tudo)

---

### 🌐 Jupyter Notebook pelo terminal

No terminal (`Ctrl + Shift + C`):

```bash
jupyter notebook
```

ou:

```bash
jupyter lab
```

Depois:

1. Abra o notebook
2. Execute a **primeira célula (instalação)**
3. Execute as demais células em sequência

---

## 🔄 Fluxo de Execução Recomendado

1. Selecionar o kernel correto
2. Executar célula de instalação (`pip install`)
3. Executar todas as células (**Run All**)
4. Validar saídas e análises
5. Gerar e salvar resultados

---

## 📁 Salvamento de Resultados

O notebook pode gerar arquivos automaticamente, como:

* Planilhas `.xlsx`
* Dados processados
* Resultados com timestamp

Exemplo de saída:

```text
Data/Resultados_Atuais/analise_sites_fonte_{timestamp}.xlsx
```

---

## ⚠️ Problemas Comuns

### ❌ `ModuleNotFoundError`

Mesmo com a célula de instalação, pode ocorrer erro se:

* A célula não foi executada
* O kernel foi reiniciado

**Solução:**
Execute novamente a primeira célula:

```python
!pip install -q -r requirements.txt
```

---

### ❌ Kernel incorreto

Se bibliotecas não forem reconhecidas:

1. Clique em **Select Kernel**
2. Escolha o ambiente correto

---

### ❌ Execução fora de ordem

Notebooks dependem da sequência correta.

✔ Sempre execute:

* **Run All**, ou
* siga a ordem das células

---

## 🔍 Verificar Ambiente Python

Execute uma célula com:

```python
import sys
print(sys.executable)
```

---

## 🔧 Alterar Interpretador Python (VS Code)

1. Pressione `Ctrl + Shift + P`
2. Procure por:

```
Python: Select Interpreter
```

3. Escolha o ambiente desejado

---

## 💡 Boas Práticas

* Sempre execute a célula de instalação primeiro
* Evite pular células
* Reinicie o kernel em caso de erro estranho
* Utilize nomes claros no código
* Gere arquivos com timestamp para controle de versões

---

## ✅ Recomendação Final

Fluxo ideal de uso:

1. Rodar:

```python
!pip install -q -r requirements.txt
```

2. Selecionar kernel correto
3. Executar **Run All**

Isso garante um ambiente consistente e evita erros 🚀