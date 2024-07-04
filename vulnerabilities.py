# Vulnerability: Directly using user-controlled input to execute a command.
command = input("Enter a command to execute: ")
os.system(command)

# Vulnerability: Using subprocess with shell=True and unsanitized user input.
command = input("Enter a command for subprocess: ")
subprocess.run(command, shell=True)

# Vulnerability: Dynamically constructing commands without sanity checks.
user_input = input("Enter a parameter: ")
command = f"echo Printing {user_input}"
os.system(command)

# Vulnerability: Insecure use of the eval() method.
user_input = input("Enter a Python expression to evaluate: ")
try:
    result = eval(user_input)
    print(f"Result:\n{result}")
except Exception as e:
    print(f"Error:\n{e}")