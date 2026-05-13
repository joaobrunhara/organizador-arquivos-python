# 📂 Organizador de Arquivos Automático

Este projeto é uma ferramenta de automação desenvolvida em **Python** para organizar pastas bagunçadas. O script identifica as extensões dos arquivos e os move para pastas específicas (Imagens, Documentos, etc).

## 🛠️ Tecnologias
* Python 3.x
* Bibliotecas: `os` e `shutil`

## 🚀 Como funciona
O script percorre um diretório alvo, analisa o sufixo de cada arquivo e o realoca conforme o dicionário de regras:
- **Imagens:** `.jpg`, `.png`, `.jpeg`
- **Documentos:** `.pdf`, `.docx`, `.txt`, `.xlsx`

## 💡 Desafios Superados
Durante o desenvolvimento, lidei com o desafio de extensões ocultas pelo Windows (ex: `.pdf.txt`), implementando uma lógica de tratamento de strings para garantir que o arquivo fosse para a pasta correta independentemente da visualização do sistema operacional.
