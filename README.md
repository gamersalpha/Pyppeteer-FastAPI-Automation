# Pyppeteer-FastAPI-Automation

Un projet Dockerisé utilisant **FastAPI** et **Pyppeteer** pour automatiser des interactions avec des pages web, comme la prise de captures d'écran ou l'exécution de scripts de navigation (login, clic, extraction HTML, etc.).

---

## 🚀 Fonctionnalités

- 📸 Endpoint `/screenshot` : prend une capture d'écran en base64
- 🧠 Endpoint `/script` : simule une navigation (formulaires, clics, scripts JS)
- 📦 Déploiement via Docker et Docker Compose
- ✅ Chromium préinstallé pour éviter les crashs et téléchargements à l'exécution

---

## 📋 Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Installation & Lancement

1. **Clonez le dépôt** :

```bash
git clone https://github.com/votre-utilisateur/Pyppeteer-FastAPI-Automation.git
cd Pyppeteer-FastAPI-Automation
```

2. **Construisez l'image Docker** :

```bash
docker compose build
```

3. **Démarrez le conteneur** :

```bash
docker compose up -d
```

---

## 🔧 Utilisation de l'API

### 1. 📸 Prendre une capture d'écran

```bash
curl -X POST http://localhost:3000/screenshot   -H "Content-Type: application/json"   -d '{"url": "https://example.com"}'
```

### 2. 🤖 Exécuter un script automatisé

```bash
curl -X POST http://localhost:3000/script   -H "Content-Type: application/json"   -d '{
    "url": "https://example.com",
    "login_selector": "#login",
    "password_selector": "#password",
    "submit_selector": "button[type=submit]",
    "login": "user",
    "password": "pass",
    "actions": [
      "document.querySelector(\"input[name='search']\").value = 'test';",
      "document.querySelector(\"form\").submit();"
    ]
  }'
```

---

## 🔐 Sécurité

- ❗ **Ne stockez jamais d’identifiants en clair** dans vos scripts.
- Utilisez des **variables d’environnement ou des secrets Docker**.
- Maintenez vos dépendances à jour (`pip`, Docker image base).
- Limitez l’accès réseau au conteneur si nécessaire.

---

## 📁 Structure du projet

```
.
├── main.py              # Code FastAPI + Pyppeteer
├── Dockerfile           # Image complète avec Chromium
├── requirements.txt     # Dépendances Python
└── docker-compose.yml   # Stack Docker
```

---

## 🛠 À venir

- Endpoint `/extract` avec des sélecteurs CSS
- Support des cookies / headers personnalisés
- Enregistrement automatique des captures dans un dossier

---

## 📜 Licence

Projet open source sous licence MIT.