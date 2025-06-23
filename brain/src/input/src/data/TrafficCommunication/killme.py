import subprocess
import re

def find_and_kill_port(port):
    try:
        # Find processes using the port
        result = subprocess.run(
            ["sudo", "netstat", "-tulnp"],
            capture_output=True,
            text=True,
            check=True
        )

        lines = result.stdout.splitlines()
        pids_to_kill = set()

        for line in lines:
            if f":{port} " in line:
                # Extract the PID from the last column
                match = re.search(r"\s+(\d+)/", line)
                if match:
                    pid = match.group(1)
                    pids_to_kill.add(pid)

        if not pids_to_kill:
            print(f"No process found using port {port}.")
            return

        # Kill the found PIDs
        for pid in pids_to_kill:
            print(f"Killing process with PID: {pid}")
            subprocess.run(["sudo", "kill", "-9", pid])

        print(f"Finished killing processes using port {port}.")

    except subprocess.CalledProcessError as e:
        print(f"Error running netstat: {e}")

if __name__ == "__main__":
    find_and_kill_port(9000)
    find_and_kill_port(5007)
