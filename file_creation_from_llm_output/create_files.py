import os

def create_file(file_name, file_path, file_content):
    # Dosya yolunu oluştur
    if file_path.startswith('/'):
        file_path = '.' + file_path
    
    full_path = os.path.join(file_path, file_name)
    
    # Klasör yapısını oluştur
    os.makedirs(file_path, exist_ok=True)
    
    # Dosyayı oluştur ve içeriğini yaz
    with open(full_path, 'w') as file:
        file.write(file_content)
    print(f"Created file: {full_path}")

def parse_and_create_files(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    current_file_name = ""
    current_file_path = ""
    current_file_content = ""
    
    for line in lines:
        line = line.strip()
        if line.startswith("File name :"):
            current_file_name = line.split(":")[1].strip()
        elif line.startswith("File path :"):
            current_file_path = line.split(":")[1].strip()
        elif line.startswith("/&&&&&&&&&&/"):
            create_file(current_file_name, current_file_path, current_file_content.strip())
            current_file_name = ""
            current_file_path = ""
            current_file_content = ""
        elif line.startswith("File content:"):
            continue
        else:
            current_file_content += line + "\n"

# Kullanıcıdan txt dosyasının adını ve yolunu al
#input_file_path = input("Enter the path of the input .txt file: ")

input_file_path = "llm_output.txt"

# Dosyaları oluştur
parse_and_create_files(input_file_path)

# TO DO:
# androdi dosya paketlerinde ihtiyaç duyulan default dosyaların hepsini bul
# bu dodsyaları da uygun şekilde doldur
