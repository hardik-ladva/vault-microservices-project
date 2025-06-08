
# Vault Microservices Project

## 🧩 Overview

This project demonstrates how to use **HashiCorp Vault** to securely manage secrets in a microservices architecture. It simulates two services (Python scripts) that retrieve their own secrets from Vault. The goal is to help beginners prepare for the **HashiCorp Vault Associate Certification** while building a practical portfolio project.

---

## 🎯 Objectives

- Learn Vault setup and configuration
- Understand secrets engines and policies
- Automate secret provisioning
- Connect applications (services) to Vault
- Enable and monitor Vault audit logging
- Use Git and GitHub for version-controlled infrastructure

---

## 🗂️ Project Structure

```

vault-microservices-project/
│
├── services/                   # Simulated microservices (Python)
│   ├── service1/main.py        # Service 1
│   └── service2/main.py        # Service 2
│
├── vault/                      # Vault setup & policy definitions
│   ├── config.hcl              # Vault configuration file
│   ├── setup.sh                # Automated bootstrap script
│   └── policies/
│       ├── service1-policy.hcl # Policy for service1
│       └── service2-policy.hcl # Policy for service2
│
├── audit/                      # Vault audit logs
│   └── vault\_audit.log
│
├── scripts/
│   └── test-secrets.sh         # Test secret retrieval using curl
│
├── .gitignore                  # Ignore logs, tokens, etc.
└── README.md                   # This file

````

---

## 🛠️ Prerequisites

- [HashiCorp Vault](https://www.vaultproject.io/downloads)
- Python 3.x
- `curl` for testing
- Git & GitHub

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/hardik-ladva/vault-microservices-project.git
cd vault-microservices-project
````

### 2. Start Vault (Dev Mode)

```bash
vault server -dev
```

Or with the config file:

```bash
vault server -config=vault/config.hcl
```

### 3. Export VAULT\_ADDR

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
```

### 4. Run the Vault Setup Script

```bash
bash vault/setup.sh
```

This script will:

* Enable the KV secret engine
* Add secrets for each service
* Create policies and tokens
* Enable file-based audit logs

### 5. Run Services

```bash
# Service 1
export VAULT_TOKEN='<TOKEN-FROM-SETUP>'
python3 services/service1/main.py

# Service 2
export VAULT_TOKEN='<TOKEN-FROM-SETUP>'
python3 services/service2/main.py
```

### 6. Test with Curl

```bash
bash scripts/test-secrets.sh
```

---

## 🔐 What You'll Learn

| Feature             | Covered In This Project                   |
| ------------------- | ----------------------------------------- |
| Vault server config | `vault/config.hcl`                        |
| Policies            | `vault/policies/*.hcl`                    |
| KV engine           | `vault setup.sh`                          |
| API calls           | `curl` and Python services                |
| Tokens              | Scoped service tokens                     |
| Audit log           | File log at `audit/vault_audit.log`       |
| Access restriction  | Each service can only read its own secret |

---

## 🧪 Example Secret Paths

* `secret/service1` → accessed only by `service1`
* `secret/service2` → accessed only by `service2`

---


## 🔍 Useful Vault Commands

```bash
vault status
vault secrets list
vault kv get secret/service1
vault policy list
vault token lookup
```

