# Calculator API - CI/CD Example 🧮

[![CI - Test and Lint](https://github.com/yourusername/python-cicd-example/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/python-cicd-example/actions/workflows/ci.yml)
[![CD - Build and Push Docker Image](https://github.com/yourusername/python-cicd-example/actions/workflows/cd.yml/badge.svg)](https://github.com/yourusername/python-cicd-example/actions/workflows/cd.yml)

A simple Flask-based calculator API demonstrating complete CI/CD pipeline with GitHub Actions, Docker, and automated testing.

## 🚀 Features

- **REST API** with basic calculator operations (add, subtract, multiply, divide)
- **Automated Testing** with pytest and coverage reporting
- **Continuous Integration** with GitHub Actions
- **Continuous Deployment** to Docker Hub
- **Containerized** with Docker for easy deployment
- **Health Check** endpoint for monitoring

## 📋 API Endpoints

| Endpoint | Method | Description | Example |
|----------|--------|-------------|---------|
| `/` | GET | API information | `http://localhost:5000/` |
| `/health` | GET | Health check | `http://localhost:5000/health` |
| `/add/<a>/<b>` | GET | Add two numbers | `http://localhost:5000/add/5/3` |
| `/subtract/<a>/<b>` | GET | Subtract b from a | `http://localhost:5000/subtract/10/4` |
| `/multiply/<a>/<b>` | GET | Multiply two numbers | `http://localhost:5000/multiply/7/6` |
| `/divide/<a>/<b>` | GET | Divide a by b | `http://localhost:5000/divide/20/4` |

## 🛠️ Local Development

### Prerequisites

- Python 3.11+
- pip
- Virtual environment (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-cicd-example.git
cd python-cicd-example

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Run Locally

```bash
# Method 1: Using Flask development server
python -m flask --app app.calculator run

# Method 2: Using Python directly
python app/calculator.py
```

Visit `http://localhost:5000` to access the API.

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_calculator.py
```

### Linting

```bash
# Check for syntax errors
flake8 app/ --count --select=E9,F63,F7,F82 --show-source --statistics

# Full linting
flake8 app/ --count --max-complexity=10 --max-line-length=127 --statistics
```

## 🐳 Docker

### Build Docker Image

```bash
docker build -t calculator-api .
```

### Run Docker Container

```bash
docker run -p 5000:5000 calculator-api
```

### Pull from Docker Hub

```bash
# Pull the latest image
docker pull yourusername/calculator-api:latest

# Run the container
docker run -p 5000:5000 yourusername/calculator-api:latest
```

## 🔄 CI/CD Pipeline

### Continuous Integration (CI)

Triggers on: Push to `main` or Pull Request to `main`

**Steps:**
1. ✅ Checkout code
2. ✅ Set up Python 3.11
3. ✅ Install dependencies
4. ✅ Run linting with flake8
5. ✅ Run tests with pytest
6. ✅ Generate coverage report
7. ✅ Upload coverage artifact

### Continuous Deployment (CD)

Triggers on: Push to `main` (after CI passes)

**Steps:**
1. ✅ Checkout code
2. ✅ Set up Docker Buildx
3. ✅ Login to Docker Hub
4. ✅ Build Docker image
5. ✅ Push to Docker Hub with tags:
   - `latest` (for main branch)
   - `main-<sha>` (commit-specific)

## 🔐 Setup Instructions

### 1. Fork/Clone Repository

```bash
git clone https://github.com/yourusername/python-cicd-example.git
cd python-cicd-example
```

### 2. Create Docker Hub Account

Sign up at [hub.docker.com](https://hub.docker.com)

### 3. Generate Docker Hub Access Token

1. Login to Docker Hub
2. Go to Account Settings → Security
3. Click "New Access Token"
4. Name it "GitHub Actions"
5. Copy the token (save it somewhere safe!)

### 4. Add GitHub Secrets

1. Go to your GitHub repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add two secrets:
   - **Name:** `DOCKER_USERNAME`, **Value:** your Docker Hub username
   - **Name:** `DOCKER_TOKEN`, **Value:** your Docker Hub access token

### 5. Update README Badges

Replace `yourusername` in the badge URLs with your GitHub username.

### 6. Update Docker Image Name

In `.github/workflows/cd.yml`, update line 26:
```yaml
images: yourusername/calculator-api  # Replace with your Docker Hub username
```

### 7. Push to GitHub

```bash
git add .
git commit -m "Initial commit with CI/CD"
git push origin main
```

### 8. Watch the Magic! ✨

- Go to the **Actions** tab in your GitHub repository
- Watch CI workflow run (tests and linting)
- Watch CD workflow run (Docker build and push)
- Check Docker Hub for your new image!

## 📊 Project Structure

```
python-cicd-example/
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI workflow
│       └── cd.yml              # CD workflow
├── app/
│   ├── __init__.py
│   └── calculator.py           # Flask application
├── tests/
│   ├── __init__.py
│   └── test_calculator.py      # Unit tests
├── .gitignore
├── Dockerfile
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
└── README.md
```

## 🧪 Testing the Deployed API

Once deployed, test your API:

```bash
# Using curl
curl http://localhost:5000/health
curl http://localhost:5000/add/10/5

# Using httpie (if installed)
http GET http://localhost:5000/multiply/7/8

# Using Python
python -c "import requests; print(requests.get('http://localhost:5000/divide/20/4').json())"
```

## 📈 What You Learn

- ✅ Writing unit tests with pytest
- ✅ Setting up CI/CD pipelines with GitHub Actions
- ✅ Containerizing Python applications with Docker
- ✅ Automating Docker builds and pushes
- ✅ Managing secrets in GitHub Actions
- ✅ Working with REST APIs in Flask
- ✅ Code coverage and quality checks
- ✅ DevOps best practices

## 🐛 Troubleshooting

### Tests Pass Locally but Fail in CI

- Check Python version matches (3.11)
- Ensure all dependencies are in requirements files
- Check for environment-specific code

### CD Workflow Fails with "unauthorized"

- Verify Docker Hub secrets are correctly set
- Check Docker Hub token hasn't expired
- Ensure username is exact (case-sensitive)

### Docker Container Won't Start

- Check logs: `docker logs <container-id>`
- Verify port 5000 is not already in use
- Ensure all files are properly copied in Dockerfile

### Coverage Report Not Generating

- Ensure pytest-cov is installed
- Check that tests are in the `tests/` directory
- Verify `__init__.py` files exist

## 🚀 Next Steps

Enhance this project by adding:

- [ ] More calculator operations (power, square root, etc.)
- [ ] Input validation and error handling
- [ ] API authentication
- [ ] Rate limiting
- [ ] Logging and monitoring
- [ ] Integration tests
- [ ] Deploy to cloud (AWS, Azure, GCP)
- [ ] Kubernetes deployment manifests
- [ ] API documentation with Swagger/OpenAPI

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Made with ❤️ for learning CI/CD with GitHub Actions**
