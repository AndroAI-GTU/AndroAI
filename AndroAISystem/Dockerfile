##### ANDRO-AI COMPILER SYSTEM DOCKERFILE #####

# This Dockerfile sets up a compiler system for the AndroAI project.
# It includes essential tools for compiling and testing Android applications.
#
# Written by: Ahmet ÖZDEMİR
# Ahmet ÖZDEMİR is a 4th-year student at Gebze Technical University with expertise in 
# artificial intelligence, machine learning for smart assistants, system programming, 
# Android development, and interpreter design.
#
# 03.08.2024



# Use Ubuntu as the base image
# 1
FROM ubuntu:latest



# Install necessary packages: openjdk-17-jdk, gradle, git, wget, unzip, and other dependencies
# This step also clears the apt-get cache to keep the Docker image size small.
# 2
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk gradle git wget unzip && \
    rm -rf /var/lib/apt/lists/*



# Download and install the Android SDK
# The Android SDK provides the necessary tools to build and run Android applications.
# 3
RUN mkdir -p /sdk/cmdline-tools && \
    cd /sdk/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-7302050_latest.zip -O sdk-tools.zip && \
    unzip sdk-tools.zip && \
    mv cmdline-tools latest && \
    rm sdk-tools.zip



# Set Android SDK environment variables
# This step configures the installation directory of the Android SDK and updates the PATH variable.
# 4
ENV ANDROID_HOME=/sdk



# 5
ENV PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH



# Create a file to automatically accept licenses
# Accepting licenses is required to download and install SDK tools.
# 6
RUN mkdir -p $ANDROID_HOME/licenses && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> $ANDROID_HOME/licenses/android-sdk-license && \
    echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" > $ANDROID_HOME/licenses/android-sdk-preview-license



# Install necessary Android packages
# This step downloads and installs platform tools, Android 30 platform, and necessary build tools using sdkmanager.
# 7
RUN yes | sdkmanager --licenses && \
    sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.3"



# Set JAVA_HOME environment variable
# The JAVA_HOME environment variable is set to locate the Java compiler.
# 8
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64



# 9
ENV PATH=$JAVA_HOME/bin:$PATH



# Set the working directory
# This step sets the /app directory as the working directory inside the Docker image.
# 10
WORKDIR /app



# Create target directory with full permissions
# 11
RUN mkdir -p /app/target && chmod 777 /app/target

