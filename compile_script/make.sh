#!/bin/bash

# SDK yolunu buraya ekleyin
SDK_PATH="/home/ahmete/Android/Sdk"  # Burada bulduğunuz SDK yolunu ekleyin

BUILD_TOOLS_VERSION="34.0.0"
BUILD_TOOLS_PATH="$SDK_PATH/build-tools"
PLATFORM_VERSION="34"

# Araçların yolunu belirle
AAPT="$BUILD_TOOLS_PATH/$BUILD_TOOLS_VERSION/aapt"
D8="$BUILD_TOOLS_PATH/$BUILD_TOOLS_VERSION/d8"
ZIPALIGN="$BUILD_TOOLS_PATH/$BUILD_TOOLS_VERSION/zipalign"
PLATFORM="$SDK_PATH/platforms/android-$PLATFORM_VERSION/android.jar"

# Araçların varlığını kontrol et
if [ ! -f "$AAPT" ]; then
  echo "aapt not found!"
  exit 1
fi
if [ ! -f "$D8" ]; then
  echo "d8 not found!"
  exit 1
fi
if [ ! -f "$ZIPALIGN" ]; then
  echo "zipalign not found!"
  exit 1
fi
if [ ! -f "$PLATFORM" ]; then
  echo "android.jar not found!"
  exit 1
fi

# Klasörleri temizle ve oluştur
rm -v -f -r ./obj
rm -v -f -r ./bin
rm -v -f -r ./key
mkdir ./obj
mkdir ./bin
mkdir ./key

# APK paketleme ve derleme işlemleri
$AAPT package -v -f -m -S ./res/ -J ./src/ -M ./AndroidManifest.xml -I $PLATFORM
javac -d ./obj/ -source 1.7 -target 1.7 -classpath $PLATFORM -sourcepath ./src/ ./src/com/androai/helloworld/MainActivity.java
$D8 --output ./bin ./obj/
$AAPT package -f -M ./AndroidManifest.xml -S ./res/ -I $PLATFORM -F ./bin/HelloWorld.unsigned.apk ./bin

# APK imzalama ve hizalama işlemleri
keytool -genkeypair -validity 10000 -dname "CN=AndroAI, OU=AndroAI, O=AndroAI, C=US" -keystore ./key/mykey.keystore -storepass mypass -keypass mypass -alias myalias -keyalg RSA
jarsigner -keystore ./key/mykey.keystore -storepass mypass -keypass mypass -signedjar ./bin/HelloWorld.signed.apk ./bin/HelloWorld.unsigned.apk myalias
$ZIPALIGN -f 4 ./bin/HelloWorld.signed.apk ./bin/HelloWorld.apk

