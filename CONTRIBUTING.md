# Contributing to Todo List API

Thank you for your interest in improving **Todo List API**! This document explains how you can:

- Report bugs or request features  
- Write and run tests  
- Style your code  
- Submit pull requests  

---

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and kind.

---

## Reporting Issues

1. **Search** open issues to avoid duplicates.  
2. If none exist, click **New issue** and choose the appropriate template (bug, feature request, question).  
3. Provide:
   - A clear title and description  
   - Steps to reproduce (for bugs)  
   - Expected vs. actual behavior  
   - Any relevant logs or screenshots  

---

## Development Setup

1. **Fork** the repo and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/todo-list-api.git
   cd todo-list-api
   ```

2. Install dependencies and create a local database:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env
    ```

3. Edit .env with your DB credentials, `SECRET_KEY`, etc.
4. Initialize the schema:

    1. if you have an init script:
        `python main.py`
    2. or run migrations if configured
5. Start the development server:

    ```bash
    uvicorn main:app --reload
    ```

---

**Branching & Workflow**

1. Sync your local main:

    ```bash
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```

2. Create a descriptive feature branch:

    ```bash
    git checkout -b feature/short-description
    ```
3. Work on your changes, then commit early & often (see Commit Messages below).

---

**Commit Messages**

    ```bash
    Use Conventional Commits style:
    
    <type>(<scope>): <short summary>
    
    [optional longer description]
    
    [optional footer(s)]
    ```


- **type**: feat, fix, docs, style, refactor, test, chore
- **scope**: area of change (e.g. users, todos)
- Keep the summary under  fifty characters.

Example:
```bash
feat(todos): allow filtering by completion status
```

---

Coding Standards

- **PEP 8** compliance
- **Black** for formatting:
    ```bash
    black .
    ```
- **isort** for import sorting:
    ```bash
    isort .
    ```
- **Type hints** for public functions and methods 
- **Docstrings** in Google or NumPy style

---

**Testing**

- Tests live in the tests/ directory and use pytest.
- Aim for at least 80% coverage.
- Run all tests locally before opening a PR:
    ```bash
    pytest
    ```
- Use FastAPI’s TestClient for endpoint tests:
    ```bash
    from fastapi.testclient import TestClient
    from main import app
    
    client = TestClient(app)
    ```
- Add fixtures for user setup and tear-down.

---

**Submitting a Pull Request**

1. Push your branch to your fork:
    ```bash
    git push origin feature/short-description
    ```
2. Open a PR against main in the original repo. In the description, link any related issues (e.g. “Closes #42”).
3. Ensure your PR:
   - Passes all CI checks (linting, formatting, tests)
   - Includes clear use-case examples (curl, HTTPie, or Swagger screenshots)
   - Has no merge conflicts

---

**Feature Requests**

If you’d like to propose a new feature:

1. Open an issue and discuss the design before implementing. 
2. Once agreed, create a feature branch and follow the PR process above.

---

Thank You!

Your time and effort make Todo List API better for everyone. We appreciate every contribution, big or small—happy coding! 🎉