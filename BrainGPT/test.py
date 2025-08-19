import torch


print("CUDA dispo:", torch.cuda.is_available())
print("Nom GPU:", torch.cuda.get_device_name(0))
print("Version torch:", torch.__version__)