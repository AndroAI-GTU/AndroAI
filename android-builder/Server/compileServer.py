from flask import Flask, request, jsonify
import os
import subprocess
import shutil
import logging

app = Flask(__name__)

# Directory with Gradle files
NECESSARY_PATH = os.path.join(os.getcwd(), "necessary")  

GRADLE_WRAPPER_FILES = [
    "gradlew",
    "gradlew.bat",
    "gradle/wrapper/gradle-wrapper.jar",
    "gradle/wrapper/gradle-wrapper.properties"
]

logging.basicConfig(level=logging.DEBUG)

def clean_directory(path):

    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


@app.route('/build', methods=['POST'])
def build_apk():
    app.logger.info(f"DEBUG: Received request to build APK.")
    app.logger.info(f"DEBUG: Start Compiling...")

    # body {
    #     src_path: "/files_to_compile/${user_id}/genProjectStructure.py"
    #     dst_path: "/apk_files/${user_id}/final.apk"
    #     user_id: 
    # }
    # Get src_path and dst_path from the request

    body = request.get_json()

    app.logger.info(f"DEBUG: Received body: {body}")

    if not body:
        return jsonify({"error": "No body received"}), 400

    src_path = body.get('src_path')
    dst_path = body.get('dst_path')
    user_id = body.get('user_id')

    project_path = os.path.join("/volumes/files_to_compile", user_id, "MyAndroidApp")
    clean_directory(project_path)

    if not os.path.exists(src_path):
        app.logger.info(f"ERROR: Source path {src_path} does not exist.")
        return jsonify({"error": f"Source path {src_path} not found"}), 500

    try:
        # Run genProjectStructure.py
        gen_result = subprocess.run(
            ['python3', src_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        app.logger.info(f"genProjectStructure.py STDOUT:", gen_result.stdout)
        app.logger.info(f"genProjectStructure.py STDERR:", gen_result.stderr)

        if gen_result.returncode != 0:
            return jsonify({"error": "genProjectStructure.py execution failed", "details": gen_result.stderr}), 500

        # Store generated source codes in `source_codes` directory
        source_codes_path = os.path.join("/volumes/source_codes", user_id)

        if not os.path.exists(source_codes_path):
            os.makedirs(source_codes_path, exist_ok=True)

        shutil.copytree(project_path, source_codes_path, dirs_exist_ok=True)

        # Copy Gradle wrapper files to the project directory
        app.logger.info(f"DEBUG: Copying necessary Gradle files...")

        for file in GRADLE_WRAPPER_FILES:
            source_file = os.path.join(NECESSARY_PATH, file)
            target_file = os.path.join(project_path, file)
            os.makedirs(os.path.dirname(target_file), exist_ok=True)  # Ensure target directories exist
            shutil.copy(source_file, target_file)
        app.logger.info(f"DEBUG: Gradle wrapper files copied successfully.")

        # Gradle build process
        result = subprocess.run(
            ["./gradlew", "assembleDebug",
             "-Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64",
             "-Dandroid.sdk.dir=/sdk"],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        app.logger.info(f"STDOUT:", result.stdout)
        app.logger.info(f"STDERR:", result.stderr)

        if result.returncode != 0:
            return jsonify({"error": "Build failed", "details": result.stderr}), 500

        # Check the location of APK files
        debug_apk = os.path.join(project_path, "app/build/outputs/apk/debug/app-debug.apk")
        # Generate dst_path directory
        os.makedirs(dst_path, exist_ok=True)

        # Copy APK files to dst_path directory
        if os.path.exists(debug_apk):
            shutil.copy(debug_apk, os.path.join(dst_path, os.path.basename(debug_apk)))

        return jsonify({"message": "Build successful"}), 200

    except Exception as e:
        app.logger.info(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('ANDROID_SERVER_PORT', 5500))
    app.run(host='0.0.0.0', port=port, debug=True)
