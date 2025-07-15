# GenAI Lab Workspace

Welcome to the **GenAI Lab Workspace**, home for all my hands‑on labs in the Applied Generative AI Specialization.\
**Public**: be mindful not to commit any API keys or sensitive data.

---

## 📂 Repository Structure

```text
.
├── modules/               # one folder per course project/module
│   ├── module‑01‑expense‑tracker/   # Personal Expense Tracker code
│   ├── module‑02‑task‑manager/      # Task Manager code
│   └── …
├── services/              # reusable Python packages and microservices
├── model-data/            # sample data, model checkpoints, RAG vectors
├── k8s/                   # Kubernetes manifests for deployments
├── Dockerfile             # base container image for local dev
├── docker-compose.yml     # spin up any services locally (e.g. JupyterLab, APIs)
├── requirements.txt       # core Python dependencies
└── .gitignore
```

> **Note:** Notebooks are optional; all code can be edited and run via VS Code Remote‑SSH.

---

## 🛠 Branching Strategy

- `` – scaffolded code and final polished labs
- ``, ``, etc. – branch per module
- `` – experiments or sub‑features within a module
- `` – tag and merge when a module is complete

> 🔮 **Future Portfolio**\
> Completed, tested projects can be copied to a separate `genai-portfolio` repo for my résumé.

---

## 📖 Course Lab List

1. **Personal Expense Tracker**
2. **Task Manager with Authentication**
3. **AI‑Powered HR Assistant**
4. **AI‑Driven Design Generator**
5. **AI‑Powered BI Assistant (InsightForge)**
6. **LangChain‑Powered Image Generator**
7. **Fine‑Tune Falcon‑7b Personalized LLM**
8. **Capstone Project** – (TBD: integrate AI + Kubernetes/DevOps)

---

## 🚀 Getting Started

```bash
# 1. Clone & switch to your first module
git clone git@github.com:l8knightz/genai-lab-workspace.git
cd genai-lab-workspace
git checkout -b module-01-expense-tracker

# 2. Create & activate your venv
python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt

# 3. (Optional) Spin up JupyterLab or other services
# docker-compose up --build -d

# 4. Commit & push your scaffold
git add .
git commit -m "scaffold: module-01 expense tracker"
git push --set-upstream origin module-01-expense-tracker
```

---

## 🤝 Contributing

Feel free to open issues or pull requests for enhancements.\
Use environment variables or mounted secrets for any API keys (never commit them).

