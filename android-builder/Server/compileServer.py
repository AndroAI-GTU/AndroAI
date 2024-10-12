from flask import Flask, request, jsonify
import os
import subprocess
import shutil

app = Flask(__name__)

@app.route('/build', methods=['POST'])
def build_apk():
    print(f"DEBUG: Start Compiling...")

    # body {
    #     src_path: "/files_to_compile/${user_id}/generate.py"
    #     dst_path: "/apk_files/${user_id}/final.apk"
    # }
    # İstekten src_path ve dst_path değerlerini al

    body = request.get_json()
    src_path = body['src_path']
    dst_path = body['dst_path']

    try:
        # generate.py dosyasını çalıştır
        gen_result = subprocess.run(
            ['python3', src_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("Generate.py STDOUT:", gen_result.stdout)
        print("Generate.py STDERR:", gen_result.stderr)

        if gen_result.returncode != 0:
            return jsonify({"error": "generate.py execution failed", "details": gen_result.stderr}), 500

        project_path = os.path.dirname(src_path)

        # Gradle build süreci
        result = subprocess.run(
            ["./gradlew", "assembleDebug",
             "-Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64",
             "-Dandroid.sdk.dir=/sdk"],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.returncode != 0:
            return jsonify({"error": "Build failed", "details": result.stderr}), 500

        # APK dosyalarının yerini kontrol et
        debug_apk = os.path.join(project_path, "app/build/outputs/apk/debug/app-debug.apk")
        # release_apk = os.path.join(project_path, "app/build/outputs/apk/release/app-release-unsigned.apk")

        # dst_path dizinini oluştur
        os.makedirs(dst_path, exist_ok=True)

        # APK dosyalarını dst_path dizinine kopyala
        if os.path.exists(debug_apk):
            shutil.copy(debug_apk, os.path.join(dst_path, os.path.basename(debug_apk)))

        # if os.path.exists(release_apk):
        #     shutil.copy(release_apk, os.path.join(dst_path, os.path.basename(release_apk)))

        return jsonify({"message": "Build successful"}), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)
