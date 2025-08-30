import subprocess
import shlex

def list_user_files_safe(username):
    if not username.isalnum():
        raise ValueError("invalid username")
    subprocess.run(["ls", f"/home/{username}"], check=True)

