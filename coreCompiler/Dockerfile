# Temel imaj olarak Arch Linux kullanıyoruz
# 1
FROM archlinux:latest

# Python ve pip'i kuruyoruz, ardından OpenJDK 17'yi kuruyoruz
# 2
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm python python-pip jdk17-openjdk

# Android SDK'yı Docker konteynerine kopyalıyoruz
# 3
COPY Sdk /sdk

# Android SDK ortam değişkenlerini ayarlıyoruz
# 4
ENV ANDROID_HOME /sdk
# 5
ENV PATH $ANDROID_HOME/cmdline-tools/bin:$ANDROID_HOME/platform-tools:$PATH

# Gradle'ı Docker konteynerine kopyalıyoruz
# 6
COPY /virtualAndroid/gradle /opt/gradle
# 7
ENV PATH $PATH:/opt/gradle/bin

# Çalışma dizinini ayarlıyoruz
# 8
WORKDIR /app

# Proje dosyalarını çalışma dizinine kopyalıyoruz
# 9
COPY virtualAndroid /app

# Python dosyasını çalışma dizinine kopyalıyoruz
# 10
# COPY create_gradle_files.py /app

# Gradle dosyalarını oluşturuyoruz
# 11
# RUN python3 create_gradle_files.py

# Gradle wrapper'ı kuruyoruz ve daha fazla bilgi için --info bayrağını ekliyoruz
# 12
RUN gradle wrapper --info

# gradlew dosyasına izin veriyoruz
# 13
RUN chmod +x gradlew

# Docker konteyneri çalıştırıldığında yapılacak komut
# 14
CMD ["./gradlew", "build"]
