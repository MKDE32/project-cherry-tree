# 🛡️ MpPreference Cheat Sheet (Windows Defender / PowerShell)

## ▶️ View Defender Configuration

Get all Defender preferences:
Get-MpPreference

---

## 🖥️ Check Defender Status

Get overall status:
Get-MpComputerStatus

---

## 🔍 Real-Time Protection Status (read-only)
(Get-MpPreference).DisableRealtimeMonitoring

---

## 🧾 Antivirus Engine & Definitions

Get signature status:
Get-MpComputerStatus | Select AntivirusSignatureLastUpdated, AntivirusSignatureVersion

Update signatures:
Update-MpSignature

---

## 📁 Exclusions (Audit / Review)

View file/path exclusions:
Get-MpPreference | Select ExclusionPath

View process exclusions:
Get-MpPreference | Select ExclusionProcess

View extension exclusions:
Get-MpPreference | Select ExclusionExtension

---

## ➕ Add Exclusions (use carefully)

Add excluded path:
Add-MpPreference -ExclusionPath "C:\Temp"

Add excluded process:
Add-MpPreference -ExclusionProcess "example.exe"

Add excluded extension:
Add-MpPreference -ExclusionExtension ".log"

---

## 🧠 Security Policies (Inspection Only)

Check cloud protection:
Get-MpPreference | Select MAPSReporting

Check sample submission:
Get-MpPreference | Select SubmitSamplesConsent

---

## 📊 Threat History / Events

View detected threats:
Get-MpThreat

Get threat detection history:
Get-MpThreatDetection

---

## 🧪 Useful Pentest / Audit Checks

Quick overview:
Get-MpComputerStatus | Select AMServiceEnabled, AntispywareEnabled, AntivirusEnabled

Check if Defender is active:
(Get-MpComputerStatus).AntivirusEnabled
