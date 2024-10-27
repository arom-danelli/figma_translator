
# Figma Text Translation Script


Este script é projetado para extrair textos de um projeto Figma, traduzir esses textos para outro idioma, e salvar as traduções em um arquivo JSON. Ele também permite reimportar as traduções para o Figma usando um plugin como o CopyDoc.

## Funcionalidades

1. **Extrair textos do Figma**: Obtém todos os textos de um arquivo Figma com base em um `file_key` fornecido.
2. **Traduzir textos**: Traduz os textos extraídos para um idioma específico.
3. **Salvar o progresso**: Salva as traduções progressivamente em um arquivo JSON para evitar perda de dados em caso de interrupção.
4. **Menu interativo**: Permite escolher entre duas opções - baixar o JSON com os textos ou traduzir o JSON existente.



## Pré-requisitos


1. **Python 3.x** instalado.
2. Instalar as dependências do script:
   - [requests](https://pypi.org/project/requests/): para fazer requisições à API do Figma.
   - [deep-translator](https://pypi.org/project/deep-translator/): para traduzir os textos automaticamente.
   - [tqdm](https://pypi.org/project/tqdm/): para exibir uma barra de progresso.

Para instalar todas as dependências, execute:
```bash
pip install requests deep-translator tqdm
```

3. **Token da API do Figma:** Gere um token da API do Figma em Figma Developer Settings e substitua pelo seu token no script.

4. **File Key do Figma:** Extraia o file_key da URL do arquivo Figma (exemplo: https://www.figma.com/file/FILE_KEY/ProjectName).
## Como usar
1. **Clone este repositório ou baixe o script** em seu diretório de trabalho.

2. **Configure o script:**
   - Substitua `figma_token` pelo seu token da API do Figma.
   - Substitua `file_key` pelo ID do arquivo Figma.

3. **Na linha do código Selecione o idioma:**
   - na linha `37` é possível alterar o idioma.

4. **Execute o script:**
```bash
python figma_translate.py

```

3. **Escolha uma das opções:**
   - **Opção 1:** Baixar o JSON de textos do Figma. Isso criará um arquivo chamado `translated_text_nodes.json` com todos os textos extraídos.
   - **Opção 2:** Traduzir o JSON existente. Isso carregará o arquivo `translated_text_nodes.json`, traduzirá os textos e salvará o progresso no mesmo arquivo.






## Estrutura do JSON

O arquivo `translated_text_nodes.json` é gerado com a seguinte estrutura:

```json
[
    {
        "id": "I344:15692;298:5977",
        "text": "Texto original em russo",
        "translated_text": "Texto traduzido em português"
    },
    ...
]

```

- **id:** Identificador único do texto no Figma.
- **text:** Texto original extraído do Figma.
- **translated_text:** Texto traduzido para o português.
 


# OBSERVAÇÕES
- Este script apenas baixa e traduz os textos; ele não pode enviar as traduções de volta ao Figma automaticamente. Para isso, é necessário usar um plugin.
- Verifique a compatibilidade da fonte no Figma com o idioma de destino (como português) para garantir que todos os caracteres sejam exibidos corretamente.
## Autores

- [@arom-danelli](https://github.com/arom-danelli)

