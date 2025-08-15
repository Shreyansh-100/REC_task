# Setting up the model

## Setting up WSL

# WSL Setup Guide

Follow these steps to set up WSL on your Windows machine.(if already have it you can skip this)

## Steps to Install WSL

1. **Enable WSL**:
   - Open **PowerShell** as Administrator and run:
     ```powershell
     wsl --install
     ```
   - Restart your computer if prompted.

2. **Install a Linux Distribution** (if not installed automatically):
   - Open **Microsoft Store**, search for a distribution (e.g., **Ubuntu**), and click **Install**.

3. **Set up the Linux environment**:
   - Launch the distribution (e.g., **Ubuntu**) from the Start menu.
   - Follow the prompts to create a **username** and **password**.

4. **Verify Installation**:
   - Open **PowerShell** or **Command Prompt** and run:
     ```powershell
     wsl --list --verbose
     ```
   - You should see something like:
     ```
     NAME      STATE           VERSION
     * Ubuntu    Running         2
     ```

5. **Set WSL 2 as Default** (optional):
   - Run the following in **PowerShell**:
     ```powershell
     wsl --set-default-version 2
     ```

6. **Update WSL Kernel** (if needed):
   - Download and install the latest WSL 2 kernel from [here](https://aka.ms/wsl2kernel).

7. **Access WSL**:
   - Open your distribution (e.g., **Ubuntu**) from the Start menu or run:
     ```powershell
     wsl
     ```

8. **Install Software** (e.g., `git`):
   - Inside your WSL environment, run:
     ```bash
     sudo apt update
     sudo apt install git
     ```

## Troubleshooting

- **WSL 2 not working on Windows 10**: Ensure you are running **Windows 10 version 1903** or higher.
- **"The operation could not be completed"**: Check WSL status with:
  ```powershell
  wsl --status
