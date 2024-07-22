import os

project_dir = '/app'

# settings.gradle dosyasını oluşturma
settings_gradle_content = """
rootProject.name = 'virtualAndroid'
include ':app'
"""
with open(os.path.join(project_dir, 'settings.gradle'), 'w') as f:
    f.write(settings_gradle_content)

# build.gradle dosyasını oluşturma
build_gradle_content = """
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.0.0'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
"""
with open(os.path.join(project_dir, 'build.gradle'), 'w') as f:
    f.write(build_gradle_content)

# app/build.gradle dosyasını oluşturma
app_dir = os.path.join(project_dir, 'app')
os.makedirs(app_dir, exist_ok=True)
app_build_gradle_content = """
apply plugin: 'com.android.application'

android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.androai.helloworld"
        minSdkVersion 21
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
        namespace 'com.androai.helloworld'
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'com.google.android.material:material:1.3.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.0.4'
    testImplementation 'junit:junit:4.13.1'
    androidTestImplementation 'androidx.test.ext:junit:1.1.2'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.3.0'
}
"""
with open(os.path.join(app_dir, 'build.gradle'), 'w') as f:
    f.write(app_build_gradle_content)

# proguard-rules.pro dosyasını oluşturma
proguard_content = """
# Add your ProGuard rules here
# By default, the flags in this file are appended to flags specified
# in /usr/local/android-sdk/tools/proguard/proguard-android.txt
# You can edit the include path and order by changing the ProGuard
# include property in project.properties.

# Add any project specific keep options here:

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}
"""
with open(os.path.join(app_dir, 'proguard-rules.pro'), 'w') as f:
    f.write(proguard_content)
