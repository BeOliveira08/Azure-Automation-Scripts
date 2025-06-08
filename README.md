Azure Automation Scripts
Scripts para automação de tarefas no Azure (PowerShell/Python).

📦 Como Usar
Instale os requisitos:

pip install azure-storage-blob  # Python
Install-Module -Name Az -AllowClobber  # PowerShell
Configure as credenciais do Azure:

Para Python:
Defina a variável de ambiente AZURE_STORAGE_CONNECTION_STRING com sua connection string do Azure Blob.
export AZURE_STORAGE_CONNECTION_STRING="sua_connection_string"
Para PowerShell:
Execute Connect-AzAccount se necessário.
🛠️ Scripts
vm_management.ps1 — Gerencia VMs no Azure.
Exemplo de uso:
.\vm_management.ps1 -vmName "MinhaVM" -resourceGroup "MeuGrupo" -action "start"
backup_to_blob.py — Faz backup de arquivos para Blob.
Exemplo de uso:
python backup_to_blob.py
