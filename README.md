# 📈 Automação Financeira — Coleta de Cotações

> Script Python que coleta automaticamente cotações de ações, FIIs e criptomoedas no **Google Finance** usando **Selenium**, e envia os resultados para o **Google Sheets** em tempo real.

---

## ✨ Funcionalidades

- 🤖 Coleta automática de preços via Selenium
- 📊 Envia os dados direto para o Google Sheets
- 🗂️ Cria uma aba nova por dia automaticamente
- ⚠️ Tratamento de erros por ativo
- 🕐 Registra o horário de cada coleta

---

## 📋 Ativos monitorados

| Ações | Criptomoedas |
|-------|-------------|
| PETR4, VALE3, ITUB4 | Bitcoin |
| TAEE11, BBDC4, BBAS3 | Ethereum |
| BPAC11, EMBJ3, RADL3 | — |

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

---

## 🚀 Como configurar e rodar

### 1. Clone o repositório
```bash
git clone https://github.com/Nluan0/Automacao_financeira.git
cd Automacao_financeira
```

### 2. Instale as dependências
```bash
pip install selenium gspread google-auth
```

### 3. Configure as credenciais do Google
- Acesse [console.cloud.google.com](https://console.cloud.google.com)
- Crie um projeto e ative a **Google Sheets API** e **Google Drive API**
- Crie uma **Service Account** e baixe o arquivo JSON
- Renomeie para `credentials.json` e coloque na pasta do projeto

### 4. Compartilhe a planilha com a Service Account
- Abra sua planilha no Google Sheets
- Clique em **Compartilhar**
- Cole o e-mail da Service Account (ex: `bot@projeto.iam.gserviceaccount.com`)
- Permissão: **Editor**

### 5. Configure o ID da planilha no script
```python
ID_PLANILHA = "seu_id_aqui"
```
> O ID está na URL da planilha entre `/d/` e `/edit`

### 6. Rode o script
```bash
python script.py
```

---

## 📸 Demonstração

### Terminal com os preços coletados
![Terminal](Print_Valore_Terminal)

### Google Sheets preenchido automaticamente
![Google Sheets](Print_Valore_Sheets)

---
## 📬 Contato

- GitHub: [@Nluan0](https://github.com/Nluan0)
- LinkedIn: [Natã Luan](https://www.linkedin.com/in/nat%C3%A3-luan-rodrigues-dos-santos-072145306/)
- 🔗 [Meu Linktree](https://linktree-nluan.vercel.app)

---

<p align="center">Feito com 💙 por <strong>Natã Luan</strong></p>
