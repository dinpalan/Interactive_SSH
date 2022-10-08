#! /usr/bin/env python3
import sys, os, string, threading
import time
try:
    import paramiko
    #import paramiko package
except:
    im = input("Paramiko module is missing. Do you want to install[Y/N]:")
    im = im.upper()
    if im == "Y":
        try:
            try:
                os.system("pip install paramiko")
            except:
                os.system("pip3 install paramiko")
        except:
            print("Please install paramiko package manually")
    else:
        print("Rerun and type 'y' to install")

#Running paramiko module with interactive password sending function
#this function helps to send password when sudo command is executed
def sudossh():
    host = "type host ip"
    port = 22
    username = "type username"
    password = "type password"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        ssh.get_transport()
        #In this example we will run HTTP module on server in port 80
        command = "sudo su -c 'sudo python -m SimpleHTTPServer 80'"
        print(f"Running: {command}\n")
        stdin, stdout, stderr = ssh.exec_command(command=command,get_pty=True)
        stdin.write("password\n")
        print("sent password\n")
        print("HTTP service is running now\n")
        stdin.flush()
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error: {stderr.readlines()}")
        else:
            print(f"Output: \n{stdout.read().decode()}")
        ssh.close()
    except Exception as err:
        print(str(err));
        print("Thanks for using my application");

#Running another paramiko module with interactive password sending function
def grepverification():
    host = "type host ip"
    port = 22
    username = "type username"
    password = "type password"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        ssh.get_transport()
        #Open new session and check port 80 status on server
        command = "sudo su -c 'netstat | grep 80'"
        print(f"Running: {command}\n")
        stdin, stdout, stderr = ssh.exec_command(command=command,get_pty=True)
        stdin.write("password\n")
        print("sent password\n")
        print("Connection is established. Check below output\n")
        stdin.flush()
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error: {stderr.readlines()}")
        else:
            print(f"Output: \n{stdout.read().decode()}")
        ssh.close()
    except Exception as err:
        print(str(err));
        print("Thanks for using my application");


def main():
    #Multithreading helps to run both at a same time. Useful for verification.
    # creating thread
    th1 = threading.Thread(target=sudossh)
    th2 = threading.Thread(target=grepverification)
    # starting thread 1
    th1.start()
    # starting thread 2
    time.sleep(2)
    th2.start()
    # wait until thread 1 is completely executed
    th1.join()
    # wait until thread 2 is completely executed
    th2.join()
    # both threads completely executed
    print("Completed!")
#you can use for loop to reduce lines but for understanding & smooth multithreading process will keep it as separate functions
#Comments are welcome. Thanks. Follow me on https://www.linkedin.com/in/dinesh-kumar-palanivelu-858441128/
#you need to change line - 23-26,36,51-54,64

if __name__=='__main__':
       main() 
        
