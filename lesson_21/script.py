# Цей скрипт читає hblog.txt і створює logs.py зі списком рядків log_data

def convert_log_to_python_list(input_file="hblog.txt", output_file="logs.py"):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("log_data = [\n")
        for line in lines:
            escaped = line.strip().replace('"', r'\"')
            f.write(f'    "{escaped}",\n')
        f.write("]\n")

if __name__ == "__main__":
    convert_log_to_python_list()
