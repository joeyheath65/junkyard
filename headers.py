import subprocess

# for simple commands
#subprocess.run(["sudo apt update"]) 

# for complex commands, with many args, use string + `shell=True`:
cmd_str = "pip3 install requests"
subprocess.run(cmd_str, shell=True)




import subprocess

# for simple commands
subprocess.run(["ls", "-l"]) 

# for complex commands, with many args, use string + `shell=True`:
cmd_str = "ls -l /tmp | awk '{print $3,$9}' | grep root"
subprocess.run(cmd_str, shell=True)