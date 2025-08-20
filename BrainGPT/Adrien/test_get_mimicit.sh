python3 - <<'EOF'
class Args:
    mimicit_path = "/home/tibia/Documents/LLM/BrainGPT/data/CQ500p_instruction.json"
    past_mimicit_path = ""
    images_path = "/home/tibia/Documents/LLM/BrainGPT/data/CQ500p.json"
    past_images_path = ""
    train_config_path = ""
    past_train_config_path = ""

args = Args()

all_mimicit_path = args.mimicit_path.split(",") + args.past_mimicit_path.split(",") if args.past_mimicit_path != "" else args.mimicit_path.split(",")
all_images_path = args.images_path.split(",") + args.past_images_path.split(",") if args.past_images_path != "" else args.images_path.split(",")
all_train_config_path = (args.train_config_path.split(",") + args.past_train_config_path.split(",") if args.past_train_config_path != "" else args.train_config_path.split(","))
status = ["new"] * len(args.mimicit_path.split(",")) if args.past_mimicit_path == "" else ["new"] * len(args.mimicit_path.split(",")) + ["past"] * len(args.past_mimicit_path.split(","))

print("all_mimicit_path =", all_mimicit_path)
print("all_images_path =", all_images_path)
print("all_train_config_path =", all_train_config_path)
print("status =", status)
EOF