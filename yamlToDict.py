import yaml

yaml_file = "services.yaml"

with open(yaml_file, "r") as file:
    try:
        yaml_data = yaml.safe_load(file)
    except yaml.YAMLError as error:
        print(error)

print("YAML \n", yaml_data)
