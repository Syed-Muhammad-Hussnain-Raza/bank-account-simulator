# 🏦 Bank Account Simulator

A browser-based Bank Account Simulator with automated UI testing using Selenium WebDriver.

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)

---

## Features

- Live balance display
- Deposit & Withdraw with input validation
- Overdraft protection
- Transaction history with timestamps
- Reset account functionality

---

## Run the App

```bash
cd app
python -m http.server 8000
# Visit: http://localhost:8000
```

## Selenium Setup

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
python -m pytest tests/ -v
```

---

## 🌿 Branching Strategy

```
main        ← production only, releases go here
└── dev     ← default branch, all work merges here first
    ├── feature/web-app
    ├── feature/selenium-setup
    ├── feature/test-cases
    └── docs/report
```

### Rules

- `main` — protected, never push directly. Merge from `dev` when ready to release
- `dev` — default branch. All feature branches are created from here and merged back here
- `feature/*` — one branch per feature/part, deleted after merge
- `docs/*` — for report and screenshots only

### Workflow

```bash
# Always branch off from dev
git checkout dev
git checkout -b feature/web-app

# Work, commit, push
git add .
git commit -m "feat: add bank simulator web app"
git push origin feature/web-app

# Merge back to dev when done
git checkout dev
git merge feature/web-app

# When everything is complete, release to main
git checkout main
git merge dev
git push origin main
```

### Commit Message Format

```
feat: add deposit and withdraw functionality
fix: correct overdraft error message
test: add empty input test cases
docs: add report and screenshots
chore: add requirements.txt
```

---

## Resources

- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Selenium Python](https://selenium-python.readthedocs.io/)
