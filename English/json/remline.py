input_file = "translations.tsv"
output_file = "translations.tsv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(line for line in lines if line.strip())