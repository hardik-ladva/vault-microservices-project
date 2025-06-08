#!/bin/bash
export VAULT_ADDR='http://127.0.0.1:8200'
vault login root

vault secrets enable -path=secret kv-v2

vault kv put secret/service1 DB_USER=app1 DB_PASS=app1pass
vault kv put secret/service2 API_KEY=abcdef123456

vault policy write service1-policy policies/service1-policy.hcl
vault policy write service2-policy policies/service2-policy.hcl

vault auth enable approle

vault write auth/approle/role/service1-role token_policies="service1-policy"
vault write auth/approle/role/service2-role token_policies="service2-policy"

vault audit enable file file_path=./audit/vault_audit.log
