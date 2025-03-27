import subprocess

# ANSI Colors
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_command(command):
    """ Runs a command and returns the formatted output """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Collect Data
kernel_info = run_command("uname -a")
sudo_version = run_command("sudo --version | head -n 1")

capabilities = run_command("getcap -r /usr/bin/ 2>/dev/null")
crontab_tasks = run_command("cat /etc/crontab | grep -v '^#'")

all_users = run_command("cut -d: -f1 /etc/passwd")
root_users = run_command("grep ':0:' /etc/passwd")

# Display Data with Formatting
print(f"\n{BLUE}═════════════════════════════════════════════════{RESET}")
print(f"{GREEN}[ ✓ ] Kernel Information:{RESET}")
print(f"    {kernel_info}\n")

print(f"{GREEN}[ ✓ ] Sudo Version:{RESET}")
print(f"    {sudo_version}\n")

print(f"{GREEN}[ ✓ ] Capabilities Information:{RESET}")
for line in capabilities.splitlines():
    print(f"    {line}")

print(f"\n{GREEN}[ ✓ ] Crontab Tasks:{RESET}")
for line in crontab_tasks.splitlines():
    print(f"    {line}")

print(f"\n{GREEN}[ ✓ ] Enumerating All Users:{RESET}")
for user in all_users.splitlines():
    print(f"    {user}")

print(f"\n{GREEN}[ ✓ ] Enumerating Root Users:{RESET}")
for root in root_users.splitlines():
    print(f"    {root}")

print(f"\n{BLUE}═════════════════════════════════════════════════{RESET}")
