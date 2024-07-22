#!/bin/bash

# Docker'ı başlat
sudo systemctl start docker

# Docker'ı her başlatmada otomatik başlatmak için etkinleştir
sudo systemctl enable docker

# Kullanıcıyı Docker grubuna ekle
sudo usermod -aG docker $USER

# Grup değişikliklerini uygula
newgrp docker

# Docker'ın durumunu kontrol et
sudo systemctl status docker
