# my-devops-app 🚀

A production-ready Flask web app with a complete CI/CD pipeline.

## What this project does
- Auto-tests code on every push
- Auto-builds Docker image and pushes to Docker Hub
- Auto-deploys to Render (live on internet)

## Tech Stack
- **App:** Python Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** Docker Hub
- **Hosting:** Render

## Live Demo
https://my-devops-app-hpg2.onrender.com

## Pipeline Flow
git push
↓
GitHub Actions runs tests
↓
Docker image built and pushed to Docker Hub
↓
Render auto-deploys live 🌍

## How to run locally
```bash
docker pull secrettt/my-devops-app:latest
docker run -p 5000:5000 secrettt/my-devops-app:latest
```
Then visit http://localhost:5000

## How to run tests
```bash
pip install -r requirements.txt
pytest test_app.py -v
```
