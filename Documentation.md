# 🚀 Documentation

## Como Executar o Projeto

Este repositório utiliza códigos Python para execução de alguns objetivos do projeto. Você pode rodar o projeto pelo terminal ou pelo botão **Run ▶** dentro do código presente na IDE.


## 📦 Instalar Dependências

Antes de executar, abra o terminal (`Ctrl + Shift + C`) e instale as bibliotecas necessárias:

```bash
python -m pip install -r requirements.txt
```

Esse comando instala as dependências no mesmo ambiente Python configurado no projeto.

Obs: Execute este comando após clonar o repositório. Apenas repita esse processo se houver mudança no ambiente Python ou no arquivo requirements.txt.


## 💻 Executar Pelo Terminal

No diretório do projeto, execute:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python main.py
```

---

## ▶ Executar Pelo Botão Run

1. Abra o arquivo `.py` desejado.
2. Clique no botão **Run ▶** da IDE.

A IDE utilizará o interpretador Python atualmente selecionado.

Obs: Esta opção estará disponível apenas se a extensão Python estiver instalada. Caso contrário, acesse a aba **Extensões** (`Ctrl + Shift + X`), pesquise por **Python** e instale a extensão oficial da Microsoft.

---


## ⚠️ Erro de Biblioteca Não Encontrada (`ModuleNotFoundError`)

Se ocorrer erro informando que uma biblioteca não foi encontrada, normalmente significa que o botão **Run ▶** está usando um Python diferente daquele onde as dependências foram instaladas.

### 🔍 Como Verificar o Python em Uso

Execute o script abaixo presente no projeto:

```bash
python Verificacoes_integridade/run.py
```

Esse script exibirá:

- caminho do interpretador Python em uso
- versão do Python
- diretório atual de execução

---

## 🔧 Como Alterar o Python da IDE

### Visual Studio Code / GitHub Codespaces

1. Pressione `Ctrl + Shift + P`
2. Procure por:

```text
Python: Select Interpreter
```

3. Escolha o interpretador desejado.

Após isso, o botão **Run ▶** passará a utilizar o novo ambiente.


## ✅ Recomendação Final

Sempre utilize os comandos abaixo para evitar conflitos entre versões:

```bash
python -m pip install -r requirements.txt
python nome_do_arquivo.py
```

Assim, instalação e execução ocorrerão no mesmo ambiente Python.