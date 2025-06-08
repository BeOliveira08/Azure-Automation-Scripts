param(
    [string]$vmName = "myVM",
    [string]$resourceGroup = "myResourceGroup",
    [ValidateSet("start", "stop")]
    [string]$action = "start"
)

# Autentica se necessário
if (-not (Get-AzContext)) {
    Connect-AzAccount
}

try {
    if ($action -eq "start") {
        Start-AzVM -ResourceGroupName $resourceGroup -Name $vmName -ErrorAction Stop
        Write-Output "VM $vmName iniciada."
    } elseif ($action -eq "stop") {
        Stop-AzVM -ResourceGroupName $resourceGroup -Name $vmName -Force -ErrorAction Stop
        Write-Output "VM $vmName parada."
    }
} catch {
    Write-Error "Erro ao executar ação '${action}' na VM ${vmName}: $_"
}