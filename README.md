# Calculator API - CI/CD Example 🧮

[![CI - Test and Lint](https://github.com/YOUR_USERNAME/python-cicd-example/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/python-cicd-example/actions/workflows/ci.yml)
[![CD - Build and Push Docker Image](https://github.com/YOUR_USERNAME/python-cicd-example/actions/workflows/cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/python-cicd-example/actions/workflows/cd.yml)

A simple Flask-based calculator API demonstrating a complete CI/CD pipeline with GitHub Actions, Docker, and automated testing.

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
git clone https://github.com/YOUR_USERNAME/python-cicd-example.git
cd python-cicd-example

# Create and activate virtual environment
# Linux/Mac:
python3 -m venv venv
source venv/bin/activate

# Windows PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (for testing)
pip install -r requirements-dev.txt
```

### Run Locally

```bash
# Run the Flask application
python app/calculator.py

# The server will start at http://127.0.0.1:5000
```

Visit `http://localhost:5000` to access the API.

### Run Tests

```bash
# Run all tests
pytest tests/test_calculator.py -v

# Run with coverage
pytest tests/test_calculator.py --cov=app --cov-report=html

# View coverage report in browser
# Windows:
start htmlcov/index.html
# Linux/Mac:
open htmlcov/index.html
```

### Linting

```bash
# Check for critical errors
flake8 app/ --count --select=E9,F63,F7,F82 --show-source --statistics

# Full linting check
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
# Pull the latest image (replace YOUR_USERNAME with your Docker Hub username)
docker pull YOUR_USERNAME/calculator-api:latest

# Run the container
docker run -p 5000:5000 YOUR_USERNAME/calculator-api:latest
```

## 🔄 CI/CD Pipeline

### Continuous Integration (CI)

**Triggers:** Push to `main` or Pull Request to `main`

**Pipeline Steps:**
1. ✅ Checkout code
2. ✅ Set up Python 3.11
3. ✅ Install dependencies (with caching)
4. ✅ Verify project structure
5. ✅ Check test discovery
6. ✅ Run linting with flake8
7. ✅ Run tests with pytest (coverage enabled)
8. ✅ Upload coverage report as artifact
9. ✅ Display coverage summary

**Success Criteria:**
- All tests pass (16+ tests)
- No critical linting errors
- Coverage report generated

### Continuous Deployment (CD)

**Triggers:** Push to `main` (only after CI passes)

**Pipeline Steps:**
1. ✅ Checkout code
2. ✅ Set up Docker Buildx
3. ✅ Login to Docker Hub (using secrets)
4. ✅ Extract metadata and generate tags
5. ✅ Build Docker image
6. ✅ Push to Docker Hub with tags:
   - `latest` (for main branch)
   - `main-<commit-sha>` (specific version)
7. ✅ Display deployment information

**Image Tags:**
- `YOUR_USERNAME/calculator-api:latest` - Most recent build
- `YOUR_USERNAME/calculator-api:main-abc1234` - Specific commit

## 🔐 Setup Instructions

### 1. Fork or Clone Repository

```bash
git clone https://github.com/peyman-t/python-cicd-example.git
cd python-cicd-example

# Remove original remote
git remote remove origin
```

### 2. Create Your GitHub Repository

1. Go to https://github.com/new
2. Name it `my-python-cicd-pipeline` (or any name you prefer)
3. Set to **Public**
4. **DO NOT** initialize with README (we have files already)
5. Click "Create repository"

### 3. Add Your Repository as Remote

```bash
# Add your repository as origin
git remote add origin https://github.com/YOUR_USERNAME/my-python-cicd-pipeline.git

# Verify
git remote -v
```

### 4. Create Docker Hub Account

1. Sign up at [hub.docker.com](https://hub.docker.com) (free tier is fine)
2. Remember your username (you'll need it for secrets)

### 5. Generate Docker Hub Access Token

1. Login to Docker Hub
2. Go to **Account Settings** → **Security**
3. Click **"New Access Token"**
4. **Description:** `GitHub Actions CI/CD`
5. **Permissions:** `Read, Write, Delete`
6. Click **"Generate"**
7. **IMPORTANT:** Copy the token immediately! It looks like `dckr_pat_...`
   - Save it somewhere safe
   - You won't see it again!

### 6. Add GitHub Secrets (CRITICAL!)

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Under **"Repository secrets"** section (NOT Environment secrets):

**Add DOCKER_USERNAME:**
- Click "New repository secret"
- **Name:** `DOCKER_USERNAME` (exact spelling, all caps)
- **Secret:** Your Docker Hub username
- Click "Add secret"

**Add DOCKER_TOKEN:**
- Click "New repository secret" again
- **Name:** `DOCKER_TOKEN` (exact spelling, all caps)
- **Secret:** Paste your Docker Hub access token
- Click "Add secret"

**Verify:** You should now see both secrets listed under "Repository secrets"

### 7. Update README Badges (Optional)

Replace `YOUR_USERNAME` in the badge URLs at the top of this README with your actual GitHub username.

### 8. Test Locally First

```bash
# Install dependencies
pip install -r requirements.txt requirements-dev.txt

# Run tests
pytest tests/test_calculator.py -v

# Should show: 16 passed

# Test the app
python app/calculator.py
# Visit http://localhost:5000/health
```

### 9. Push to GitHub

```bash
# Stage all files
git add .

# Commit
git commit -m "Initial commit: Set up CI/CD pipeline"

# Push (this triggers the CI/CD pipeline!)
git push -u origin main
```

### 10. Watch the Pipeline! ✨

1. Go to your GitHub repository
2. Click the **"Actions"** tab
3. Watch the CI workflow run (testing and linting)
4. Watch the CD workflow run (Docker build and push)
5. Check Docker Hub for your new image!

**Pipeline completes in ~5-8 minutes**

## 📊 Project Structure

```
python-cicd-example/
├── .github/
│   └── workflows/
│       ├── ci.yml              # CI workflow configuration
│       └── cd.yml              # CD workflow configuration
├── app/
│   ├── __init__.py            # Package initialization
│   └── calculator.py          # Flask application
├── tests/
│   ├── __init__.py            # Test package initialization
│   └── test_calculator.py     # Unit tests (16 tests)
├── .gitignore
├── Dockerfile                  # Docker image configuration
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
└── README.md
```

## 🧪 Testing the Deployed API

Once your Docker image is on Docker Hub:

```bash
# Pull your image
docker pull YOUR_USERNAME/calculator-api:latest

# Run it
docker run -p 5000:5000 YOUR_USERNAME/calculator-api:latest

# Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/add/10/5
curl http://localhost:5000/multiply/7/8
curl http://localhost:5000/divide/20/4
```

**Expected response (for add):**
```json
{
  "a": 10.0,
  "b": 5.0,
  "operation": "addition",
  "result": 15.0
}
```

## 📈 What You'll Learn

- ✅ Setting up CI/CD pipelines with GitHub Actions
- ✅ Writing unit tests with pytest
- ✅ Generating code coverage reports
- ✅ Containerizing Python applications with Docker
- ✅ Automating Docker builds and deployments
- ✅ Managing secrets securely in GitHub
- ✅ Working with REST APIs in Flask
- ✅ Implementing DevOps best practices

## 🐛 Troubleshooting

### CI Fails: "collected 0 items"

**Problem:** Pytest can't find tests

**Solution:**
```bash
# Verify test file name (must use underscore!)
ls tests/
# Should show: test_calculator.py (NOT test-calculator.py)

# Verify __init__.py files exist
ls app/__init__.py tests/__init__.py

# Create if missing
touch app/__init__.py tests/__init__.py

# Test locally
pytest tests/test_calculator.py -v
```

### CD Fails: "Username and password required"

**Problem:** Docker Hub secrets not configured correctly

**Solution:**
1. Go to Settings → Secrets and variables → Actions
2. Verify secrets are under **"Repository secrets"** (NOT "Environment secrets")
3. Both `DOCKER_USERNAME` and `DOCKER_TOKEN` must exist
4. If wrong, delete and re-add them correctly
5. Re-run the failed workflow

### Tests Pass Locally but Fail in CI

**Problem:** Missing files or environment differences

**Solution:**
```bash
# Check what's committed
git ls-files tests/

# Should include:
# tests/__init__.py
# tests/test_calculator.py

# Ensure Python version matches
python --version  # Should be 3.11+

# Run exact CI command
pytest tests/test_calculator.py -v --cov=app
```

### Docker Container Won't Start

**Problem:** Port conflict or missing dependencies

**Solution:**
```bash
# Check if port 5000 is in use
# Windows PowerShell:
Get-NetTCPConnection -LocalPort 5000

# Linux/Mac:
lsof -i :5000

# Kill process using port 5000 if needed
# Or use different port:
docker run -p 8080:5000 YOUR_USERNAME/calculator-api:latest
```

### Can't Push to GitHub

**Problem:** Authentication failure

**Solution:**
```bash
# Use Personal Access Token (not password)
# 1. Go to: GitHub Settings → Developer settings
# 2. Personal access tokens → Tokens (classic)
# 3. Generate new token with 'repo' scope
# 4. Use token as password when pushing
```

## 🚀 Next Steps & Enhancements

### Add More Features
- [ ] Power operation (x^y)
- [ ] Square root function
- [ ] Modulo operation
- [ ] Scientific calculator functions

### Improve Testing
- [ ] Integration tests
- [ ] API endpoint testing with pytest
- [ ] Load testing
- [ ] Security testing

### Enhance CI/CD
- [ ] Add staging environment
- [ ] Implement blue-green deployment
- [ ] Add manual approval gates
- [ ] Deploy to cloud (AWS, Azure, GCP)

### Code Quality
- [ ] Add type hints (mypy)
- [ ] Code formatting (black)
- [ ] Security scanning (bandit)
- [ ] Dependency updates (Dependabot)

### Monitoring & Observability
- [ ] Application logging
- [ ] Health check improvements
- [ ] Metrics collection (Prometheus)
- [ ] Error tracking (Sentry)

### Documentation
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Architecture diagrams
- [ ] Deployment guides
- [ ] Contributing guidelines

## 📚 Learning Resources

- **GitHub Actions:** https://docs.github.com/en/actions
- **Docker:** https://docs.docker.com
- **Flask:** https://flask.palletsprojects.com
- **Pytest:** https://docs.pytest.org
- **CI/CD Best Practices:** https://www.atlassian.com/continuous-delivery

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Tips

- **Test locally first:** Always run `pytest` before pushing
- **Small commits:** Make incremental changes for easier debugging
- **Descriptive messages:** Write clear commit messages
- **Monitor Actions:** Check the Actions tab after each push
- **Read logs:** If something fails, read the complete log output

## 🎯 Success Checklist

Before you're done, verify:

- [ ] Local tests pass: `pytest tests/test_calculator.py -v`
- [ ] Docker builds locally: `docker build -t test .`
- [ ] Secrets configured in GitHub (Repository secrets)
- [ ] CI workflow passes (green checkmark in Actions)
- [ ] CD workflow passes (image on Docker Hub)
- [ ] Can pull and run image: `docker pull YOUR_USERNAME/calculator-api:latest`
- [ ] API responds: `curl http://localhost:5000/health`

## 🌟 Acknowledgments

This project demonstrates modern DevOps practices using:
- **GitHub Actions** for CI/CD automation
- **Docker** for containerization
- **Flask** for the web framework
- **Pytest** for testing

---

**Made with ❤️ for learning CI/CD with GitHub Actions**

*Questions? Issues? Open an issue on GitHub!*

