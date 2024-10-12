from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/user/query', methods=['POST'])
def generate_prompt():

    print("DEBUG: Veriler alındı, işlenmeye başlıyor...")
    data = request.json  # Gelen verileri JSON olarak al
    
    slots = {
        "application_name": data.get("application_name", ""),
        "number_of_activities": data.get("number_of_activities", ""),
        "activity_names": data.get("activity_names", []),
        "activity_links": data.get("activity_links", ""),
        "activity_1_content": data.get("activity_1_content", ""),
        "activity_2_content": data.get("activity_2_content", ""),
        "general_explaining": data.get("general_explaining", "")
    }

    # Verileri işleyip prompt oluştur (bu adımda daha fazla işlem yapılabilir)
    prompt = generate_prompt(slots)
    print("DEBUG: Veriler başarıyla işlendi, oluşturulan prompt:", prompt)

    return jsonify({"prompt": prompt})


def generate_prompt(slots):

    """
    Alınan verilerle Android programına yönelik bir prompt oluşturur.

    Args:
        slots (dict): Sunucudan gelen veriler.

    Returns:
        str: Oluşturulmuş prompt.
    """
    activity_names = ", ".join(slots.get('activity_names', ['activity_1_name', 'activity_2_name', '...']))

    prompt = (
        "I will ask you some things to write an Android program.\n"
        "Below are some rules you must follow and I will clearly state what I want.\n\n"
        "Rules:\n\n"
        "- I do not want you to give me any other text or additional message other than the code I requested. "
        "Just write the code I want.\n"
        "- I want you to write the files I want from you completely.\n"
        "- All files must be consistent among themselves.\n\n"
        "The features of the Android program I want will be as follows:\n\n"
        f"- The name of the application will be {slots.get('application_name', 'Application Name')}.\n"
        f"- The name of the company will be `androai`. So, you will use a package like `com.androai.{slots.get('application_name', 'application_name').lower()}` "
        "in the entire project.\n"
        f"- There will be a total of {len(slots.get('activity_names', []))} activities in the application.\n"
        f"- The name of each activity will be: {activity_names}\n"
        f"- Links between activities: {slots.get('activity_links', '{}')}.\n"
        f"- Activity1 content: {slots.get('activity_1_content', 'content1')}\n"
        f"- Activity2 content: {slots.get('activity_2_content', 'content2')}\n\n"
        f"{slots.get('general_explaining', 'General explaining')}\n\n\n"
        "For this program, I want you to write code in the following format:\n\n"
        '```\n'
        "import os\n"
        "\n"
        "project_structure = {\n"
        '    "src": {\n'
        '        "androidTest": {\n'
        '            "java": {\n'
        '                "com": {\n'
        '                    "androai": {\n'
        '                        "{slots.get("application_name", "app_name").lower()}": {\n'
        '                            "ExampleInstrumentedTest.java": ""\n'
        '                        }\n'
        '                    }\n'
        '                }\n'
        '            }\n'
        '        },\n'
        '        "main": {\n'
        '            "AndroidManifest.xml": "",\n'
        '            "java": {\n'
        '                "com": {\n'
        '                    "androai": {\n'
        '                        "{slots.get("application_name", "app_name").lower()}": {\n'
        '                            "MainActivity.java": ""\n'
        '                            # and other activities ...#\n'
        '                        }\n'
        '                    }\n'
        '                }\n'
        '            },\n'
        '            "res": {\n'
        '                "drawable": {},\n'
        '                "layout": {\n'
        '                    "activity_main.xml": ""\n'
        '                    # and other activities ...#\n'
        '                },\n'
        '                "mipmap-anydpi": {\n'
        '                    "ic_launcher_round.xml": "",\n'
        '                    "ic_launcher.xml": ""\n'
        '                },\n'
        '                "mipmap-hdpi": {\n'
        '                    "ic_launcher_round.webp": "",\n'
        '                    "ic_launcher.webp": ""\n'
        '                },\n'
        '                "mipmap-mdpi": {\n'
        '                    "ic_launcher_round.webp": "",\n'
        '                    "ic_launcher.webp": ""\n'
        '                },\n'
        '                "mipmap-xhdpi": {\n'
        '                    "ic_launcher_round.webp": "",\n'
        '                    "ic_launcher.webp": ""\n'
        '                },\n'
        '                "mipmap-xxhdpi": {\n'
        '                    "ic_launcher_round.webp": "",\n'
        '                    "ic_launcher.webp": ""\n'
        '                },\n'
        '                "mipmap-xxxhdpi": {\n'
        '                    "ic_launcher_round.webp": "",\n'
        '                    "ic_launcher.webp": ""\n'
        '                },\n'
        '                "values": {\n'
        '                    "colors.xml": "",\n'
        '                    "strings.xml": "",\n'
        '                    "themes.xml": ""\n'
        '                },\n'
        '                "values-night": {\n'
        '                    "themes.xml": ""\n'
        '                },\n'
        '                "xml": {\n'
        '                    "backup_rules.xml": "",\n'
        '                    "data_extraction_rules.xml": "",\n'
        '                    "network_security_config.xml": ""\n'
        '                }\n'
        '            }\n'
        '        },\n'
        '        "test": {\n'
        '            "java": {\n'
        '                "com": {\n'
        '                    "androai": {\n'
        '                        "{slots.get("application_name", "app_name").lower()}": {\n'
        '                            "ExampleUnitTest.java": ""\n'
        '                        }\n'
        '                    }\n'
        '                }\n'
        '            }\n'
        '        }\n'
        '    },\n'
        '    "build.gradle": "",\n'
        '    "proguard-rules.pro": "",\n'
        '    "settings.gradle": "",\n'
        '    "gradle.properties": ""\n'
        "}\n\n"
        "def create_project_structure(base_path, structure):\n\n"
        "    for name, content in structure.items():\n\n"
        "        path = os.path.join(base_path, name)\n\n"
        "        if isinstance(content, dict):\n"
        "            os.makedirs(path, exist_ok=True)\n"
        "            create_project_structure(path, content)\n\n"
        "        else:\n"
        "            with open(path, 'w') as file:\n"
        "                file.write(content)\n\n"
        "def main():\n\n"
        "    project_name = \"MyAndroidApp\"\n"
        "    base_path = os.path.join(os.getcwd(), project_name)\n"
        "    os.makedirs(base_path, exist_ok=True)\n"
        "    create_project_structure(base_path, project_structure)\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n\n"
        '```\n'
        "You must correctly specify all the activities and the starting activity that we defined in the manifest file and you must not leave any `.xml` file empty. If nothing is specifically specified in files such as mipmap, fill these files with the 'xml' format of the android icon that normally comes ready-made."
        "The files you need to fill out completely for this project are:\n"
        "- All `.java` files for the desired activities.\n"
        "- All `.xml` files for the desired activities.\n"
        "- `AndroidManifest.xml` for the application manifest.\n"
        "- `build.gradle` for the build configuration.\n"
        "- `settings.gradle` for the project settings.\n"
        "- `proguard-rules.pro` for the ProGuard rules.\n"
        "- `colors.xml`, `strings.xml`, `themes.xml` in the `values` directory.\n"
        "- Any other necessary XML configuration files.\n\n"
        "Additionally, the .env content needed for some files is as follows:\n"
        '```\n'
        'ANDROID_HOME="/sdk"\n'
        'JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"\n'
        '```\n'
        "When I run this code, I should have a directory called `MyAndroidApp` that I can run as an Android program.\n" 
    )
    return prompt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
