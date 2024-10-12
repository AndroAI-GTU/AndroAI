# temel imaj
FROM python:3.10


# Java JDK yükleme
RUN apt-get update && apt-get install -y openjdk-17-jdk


# JAVA_HOME'u ayarlama
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV PATH="$JAVA_HOME/bin:$PATH"


RUN mkdir -p /sdk/cmdline-tools && \
    cd /sdk/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-7302050_latest.zip -O sdk-tools.zip && \
    unzip sdk-tools.zip && \
    mv cmdline-tools latest && \
    rm sdk-tools.zip


# Set Android SDK environment variables
# This step configures the installation directory of the Android SDK and updates the PATH variable.
ENV ANDROID_HOME=/sdk

ENV PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH


# Create a file to automatically accept licenses
# Accepting licenses is required to download and install SDK tools.
RUN mkdir -p $ANDROID_HOME/licenses && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> $ANDROID_HOME/licenses/android-sdk-license && \
    echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" > $ANDROID_HOME/licenses/android-sdk-preview-license


# Install necessary Android packages
# This step downloads and installs platform tools, Android 30 platform, and necessary build tools using sdkmanager.
RUN yes | sdkmanager --licenses && \
    sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.3"

    
# Diğer kısımlar
WORKDIR /app

COPY ./Server/requirements.txt requirements.txt

COPY ./Server/compileServer.py compileServer.py

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "compileServer.py"]
