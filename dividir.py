import json
from itertools import islice

def split_list(data_list, chunk_size):
    """Divide uma lista em pedaços menores."""
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]

def split_json(input_file, output_prefix, chunk_size):
    """Divide um arquivo JSON grande em arquivos menores."""
    # Ler o arquivo JSON grande
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Processar cada chave que contém uma lista
    for key, value in data.items():
        if isinstance(value, list):
            for i, chunk in enumerate(split_list(value, chunk_size)):
                output_file = f"{output_prefix}_{key}_{i + 1}.json"
                with open(output_file, 'w', encoding='utf-8') as f_out:
                    json.dump({key: chunk}, f_out, ensure_ascii=False, indent=4)
                print(f"Arquivo {output_file} salvo com {len(chunk)} itens.")
        else:
            # Salvar objetos ou valores que não são listas em arquivos separados
            output_file = f"{output_prefix}_{key}.json"
            with open(output_file, 'w', encoding='utf-8') as f_out:
                json.dump({key: value}, f_out, ensure_ascii=False, indent=4)
            print(f"Arquivo {output_file} salvo.")

# Exemplo de uso
input_file = 'ufla.json'  # Caminho para o arquivo JSON grande
output_prefix = 'parte'     # Prefixo dos arquivos de saída
chunk_size = 50             # Número de itens por arquivo para listas

split_json(input_file, output_prefix, chunk_size)
