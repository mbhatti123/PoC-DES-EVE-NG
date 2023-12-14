import os
import paramiko  # TODO - SCP

server = '192.168.30.13'
username = 'root'
password = 'eve'

custom_temp = 'test.yml'
image_file = 'test.qcow2'
intel_temp_path = '/opt/unetlab/html/templates/intel/test.yml'
amd_temp_path = '/opt/unetlab/html/templates/amd/test.yml'
image_file_dir = '/opt/unetlab/addons/qemu/TEST1'
image_file_path = f'{image_file_dir}/{image_file}'

# connect to eve-ng server
ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)  # TODO - add prarms for user/pass or ssh key file

# place template into templates directory
sftp = ssh.open_sftp()
sftp.put(custom_temp, intel_temp_path)
sftp.put(custom_temp, amd_temp_path)

# create directory for image and place image in directory
sftp.mkdir(image_file_dir)
sftp.put(image_file, image_file_path)

# close ssh session
sftp.close()
ssh.close()
