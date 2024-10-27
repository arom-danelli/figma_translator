import requests
import json
from deep_translator import GoogleTranslator
from tqdm import tqdm

# Insira seu token da API do Figma e a chave do arquivo
figma_token = "xxxxxxxxx"
file_key = "xxxxxx"  # Apenas o ID do arquivo

headers = {
    "X-Figma-Token": figma_token
}

def get_figma_text_nodes(file_key):
    url = f"https://api.figma.com/v1/files/{file_key}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        text_nodes = []

        def extract_text(node):
            if node["type"] == "TEXT" and "characters" in node:
                text_nodes.append({"id": node["id"], "text": node["characters"]})
            for child in node.get("children", []):
                extract_text(child)
        
        extract_text(data["document"])
        return text_nodes
    else:
        print("Erro na requisição:", response.status_code)
        print(response.json())
        return []

# Função para traduzir e salvar progressivamente com verificação de tradução simulada
def translate_json(file_path):
    translator = GoogleTranslator(source="russian", target="portuguese") # Traduzindo do russo para o português mas pode ser alterado para qualquer idioma.

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text_nodes = json.load(f)
        
        for idx, node in enumerate(tqdm(text_nodes, desc="Traduzindo textos")):
            if "translated_text" not in node or node["translated_text"].startswith("Traduzido:"):
                translated_text = translator.translate(node["text"])
                
                node["translated_text"] = translated_text

                # Salvamento progressivo
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(text_nodes, f, ensure_ascii=False, indent=4)
        
        print("Tradução completa e salva em", file_path)
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado. Certifique-se de baixar os textos primeiro.")



def main():
    print("Escolha uma opção:")
    print("1 - Baixar JSON de textos do Figma")
    print("2 - Traduzir JSON existente")
    option = input("Digite o número da opção: ")

    if option == "1":
        text_nodes = get_figma_text_nodes(file_key)
        if text_nodes:
            with open("translated_text_nodes.json", "w", encoding="utf-8") as f:
                json.dump(text_nodes, f, ensure_ascii=False, indent=4)
            print("JSON de textos baixado e salvo como 'translated_text_nodes.json'")
        else:
            print("Nenhum texto encontrado ou erro na requisição.")
    
    elif option == "2":
        file_path = "translated_text_nodes.json"
        try:
            translate_json(file_path)
        except FileNotFoundError:
            print(f"Arquivo '{file_path}' não encontrado. Certifique-se de baixar os textos primeiro.")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
