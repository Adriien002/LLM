import os
import orjson
import ijson
from LLM.BrainGPT.Adrien.mimicit_dataset_v2 import MimicitDataset
from argparse import Namespace

# --- Paramètres à adapter ---
mimicit_path = "/home/tibia/Documents/LLM/BrainGPT/data/CQ500p_instruction.json"
images_path = "/home/tibia/Documents/LLM/BrainGPT/data/CQ500p.json"
train_config_path = "" 
status = ["new"]

# Paramètres simulés pour args
args = Namespace(
    task="pretrain",
    tokenizer=type("DummyTokenizer", (), {"bos_token_id": 0, "eos_token_id": 1})(),
    max_src_length=512,
    max_tgt_length=512,
    patch_image_size=224,
    seed=42,
    inst_format="default",
    past_subset_ration=0.5 
)

# Instanciation du dataset
dataset = MimicitDataset(
    args,
    mimicit_paths=[mimicit_path],
    images_paths=[images_path],
    train_config_paths=[train_config_path],
    status_list=status
)

# --- Vérifications ---
print("=== Dataset Keys ===")
print(list(dataset.dataset.keys())[:5])  # affiche les 5 premières clés

print("\n=== Images Keys ===")
print(list(dataset.images.keys())[:5])

print("\n=== Train Data List ===")
print(dataset.train_data_list[:5])

print("\n=== Train Config (extrait) ===")
for k in list(dataset.train_config.keys())[:5]:
    print(k, dataset.train_config[k])
