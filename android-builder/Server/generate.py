import os

project_structure = {
    "app": {
        "src": {
            "androidTest": {
                "java": {
                    "com": {
                        "example": {
                            "myandroidapp": {
                                "ExampleInstrumentedTest.java": ""
                            }
                        }
                    }
                }
            },
            "main": {
                "AndroidManifest.xml": "",
                "java": {
                    "com": {
                        "example": {
                            "myandroidapp": {
                                "MainActivity.java": ""
                            }
                        }
                    }
                },
                "res": {
                    "layout": {
                        "activity_main.xml": ""
                    },
                    "values": {
                        "colors.xml": "",
                        "strings.xml": "",
                        "themes.xml": ""
                    },
                    "values-night": {
                        "themes.xml": ""
                    },
                    "drawable": {},
                    "mipmap-hdpi": {},
                    "mipmap-mdpi": {},
                    "mipmap-xhdpi": {},
                    "mipmap-xxhdpi": {},
                    "mipmap-xxxhdpi": {}
                }
            },
            "test": {
                "java": {
                    "com": {
                        "example": {
                            "myandroidapp": {
                                "ExampleUnitTest.java": ""
                            }
                        }
                    }
                }
            }
        },
        "build.gradle": "",
        "proguard-rules.pro": ""
    },
    "build.gradle": "",
    "settings.gradle": "",
    "gradle.properties": ""
}


def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

def main():
    base_path = os.getcwd()
    create_project_structure(base_path, project_structure)

if __name__ == '__main__':
    main()


# /app/build.gradle
# /app/proguard-rules.pro 
# /src
# ahmete@ahmete-Inspiron-14-5401:~/AndroidStudioProjects/ChatBot/app/src$ ls -R
# .:
# androidTest  main  test

# ./androidTest:
# java

# ./androidTest/java:
# com

# ./androidTest/java/com:
# ozdemir

# ./androidTest/java/com/ozdemir:
# chatbot

# ./androidTest/java/com/ozdemir/chatbot:
# ExampleInstrumentedTest.java

# ./main:
# AndroidManifest.xml  java  res

# ./main/java:
# com

# ./main/java/com:
# ozdemir

# ./main/java/com/ozdemir:
# chatbot

# ./main/java/com/ozdemir/chatbot:
# MainActivity.java

# ./main/res:
# drawable  layout  mipmap-anydpi  mipmap-hdpi  mipmap-mdpi  mipmap-xhdpi  mipmap-xxhdpi  mipmap-xxxhdpi  values  values-night  xml

# ./main/res/drawable:
# baseline_send_24.xml   ic_launcher_background.xml  rounded_bot_message.xml  rounded_user_message.xml
# button_background.xml  ic_launcher_foreground.xml  rounded_edittext.xml

# ./main/res/layout:
# activity_main.xml

# ./main/res/mipmap-anydpi:
# ic_launcher_round.xml  ic_launcher.xml

# ./main/res/mipmap-hdpi:
# ic_launcher_round.webp  ic_launcher.webp

# ./main/res/mipmap-mdpi:
# ic_launcher_round.webp  ic_launcher.webp

# ./main/res/mipmap-xhdpi:
# ic_launcher_round.webp  ic_launcher.webp

# ./main/res/mipmap-xxhdpi:
# ic_launcher_round.webp  ic_launcher.webp

# ./main/res/mipmap-xxxhdpi:
# ic_launcher_round.webp  ic_launcher.webp

# ./main/res/values:
# colors.xml  strings.xml  themes.xml

# ./main/res/values-night:
# themes.xml

# ./main/res/xml:
# backup_rules.xml  data_extraction_rules.xml  network_security_config.xml

# ./test:
# java

# ./test/java:
# com

# ./test/java/com:
# ozdemir

# ./test/java/com/ozdemir:
# chatbot

# ./test/java/com/ozdemir/chatbot:
# ExampleUnitTest.java
# ahmete@ahmete-Inspiron-14-5401:~/AndroidStudioProjects/ChatBot/app/src$ 

