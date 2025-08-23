import json
import os

DATA_DIR = "/home/ubuntu/portal_mentoria/data"
TEMPLATE_FILE = os.path.join(DATA_DIR, "mentor_template.json")

def _get_mentorado_file_path(mentorado_id):
    return os.path.join(DATA_DIR, f"mentorado_{mentorado_id}.json")

def load_mentorado_data(mentorado_id):
    file_path = _get_mentorado_file_path(mentorado_id)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Se o arquivo do mentorado não existe, cria um novo a partir do template
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template_data = json.load(f)
        save_mentorado_data(mentorado_id, template_data)
        return template_data

def save_mentorado_data(mentorado_id, data):
    file_path = _get_mentorado_file_path(mentorado_id)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


