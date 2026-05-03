# 🌑 Design_Manipulativos

Projeto desenvolvido para analisar sites e identificar padrões manipulativos (**Manipulative Design / Dark Patterns**) utilizando inteligência artificial, com integração com modelos da OpenAI e Google Gemini.

📄 Para melhor entendimento da estrutura e uso do projeto, acesse:
`Documentation/Documentation_Overview.md`

---

## 🎯 OBJETIVO

* Identificar práticas de design manipulativo em websites
* Detectar possíveis riscos de segurança
* Comparar resultados entre diferentes modelos de IA
* Gerar relatórios estruturados em formato Excel

---

## 🛠️ TECNOLOGIAS UTILIZADAS

* Python 3.x
* OpenAI API
* Google Gemini API
* Pandas
* Requests
* BeautifulSoup
* OpenPyXL
* Matplotlib / Seaborn

---

## 🔑 CONFIGURAÇÃO DAS APIs

Antes de rodar o projeto, configure suas chaves de API:

### Google Gemini

```bash
export GOOGLE_API_KEY="sua_chave_aqui"
```

### OpenAI

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

---

## 📥 ENTRADA DE DADOS

Os dados de entrada estão localizados em:

* `Data/sites_diversos.txt`
* `Data/sites_educativos.txt`

---

## 📤 SAÍDA DE DADOS

Os resultados são salvos na pasta:

```text
Data/Resultados_Atuais
```

### 📊 Os relatórios incluem:

* URL analisada
* Presença de designs manipulativos
* Riscos de segurança
* Nível de confiança

---

## 📊 ANÁLISE

A análise visual dos dados pode ser feita no notebook:

```text
Notebook/grafico_Respostas_Sites.ipynb
```

---

## ⚠️ OBSERVAÇÕES

* Alguns sites podem bloquear requisições automáticas
* A qualidade dos resultados depende do modelo de IA utilizado
* É necessário conexão com a internet

---

## 🚀 MELHORIAS FUTURAS

* Interface web
* Integração com mais modelos de IA
* Classificação mais detalhada
* Automação completa de relatórios

---

## 👨‍💻 AUTOR

Projeto acadêmico voltado para estudo de **IA aplicada à detecção de padrões manipulativos na web**.