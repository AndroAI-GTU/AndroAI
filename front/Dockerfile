FROM debian:buster

# Node.js kurulumunu yapıyoruz
RUN apt-get update && \
    apt-get install -y gnupg curl && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_21.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install -y nodejs

# npm'i güncelliyoruz
RUN npm install -g npm

# Çalışma dizinini oluşturuyoruz
RUN mkdir /app
WORKDIR /app

# Proje dosyalarını kopyalıyoruz
COPY . .

# Bağımlılıkları yüklüyoruz
RUN npm install

# Giriş dosyasını çalıştırılabilir hale getiriyoruz
RUN chmod +x /app/entrypoint.sh

# Uygulama için gerekli portu açıyoruz
EXPOSE ${FRONT_PORT}

# Giriş noktası olarak entrypoint.sh'yi ayarlıyoruz
ENTRYPOINT ["sh", "entrypoint.sh"]
