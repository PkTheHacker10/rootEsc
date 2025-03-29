import subprocess
from time import perf_counter

start_time = perf_counter()

def run_command(command):
    """ Runs a command and returns the formatted output """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())

commands = ["./test/test.sh", "./test/test1.sh", "./test/test2.sh", "./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh","./test/test3.sh"]

for cmd in commands:
    run_command(cmd)

end_time = perf_counter()
print(f"Time completion: {end_time - start_time:.5f} seconds")
