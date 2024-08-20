from flask import Flask, request, send_file, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/build', methods=['POST'])
def build_apk():
    project_path = "/app/android"
    
    try:
        # Gradle build süreci
        result = subprocess.run(
            ["./gradlew", "build"],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.returncode != 0:
            return jsonify({"error": "Build failed", "details": result.stderr}), 500

        # APK dosyasının yerini kontrol et
        debug_apk = os.path.join(project_path, "app/build/outputs/apk/debug/app-debug.apk")
        release_apk = os.path.join(project_path, "app/build/outputs/apk/release/app-release-unsigned.apk")

        if os.path.exists(debug_apk):
            return send_file(debug_apk, as_attachment=True)
        elif os.path.exists(release_apk):
            return send_file(release_apk, as_attachment=True)
        else:
            return jsonify({"error": "APK file not found"}), 404

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
