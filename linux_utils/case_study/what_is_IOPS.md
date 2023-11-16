# Define IOPS:

IOPS is stands for "input output operations per second", and its used to measure the speed and efficiency of storage devices. IOPS represents the number of read and write operations a storage can perform within a second.

# Explain the difference between throughput and IOPS:

- IOPS is used to measure speed and efficiency of storage devices within a second. 
- throughput is the actual measure of the amount of data that succesfully passes through a system or network within a specified time period. This measurements are expressed in *bytes per second, bits per second, packets per second, etc.*

# Name a limitation with *fdisk* for creating partitions that *parted* doesn't have:

- *fdisk* is the default way to create partitions, but it doesn't work well with large files. In this case, *parted* is used. 

# Name three tools that can provide disk information:
- IOPS
- fio - *fio --name=mytest --ioengine=sync --rw=randwrite --bs=4k --numjobs=16 --size=8G --time_based*
- iostat - *iostat -d -x 1*
- fdisk - sudo fdisk -l

# What can an SSH tunnel do? When is it useful?: 
- SSH tunneling is useful when access to a remote service, such as HTTP, is restricted, and the only available access is via SSH.

- SSH tunneling works by creating an SSH connection with the remote server and then forwards a remote port (e.g., 16363, PORT) to a local port on the originating machine.

**test case**: 
ssh -ssh -L 9008:localhost:16363 -p 2503 bacon@prod7.apache2.service.internal -N
**triggers**: 
Here, the -L flag signals that forwarding should be enabled, creating a local port of 9008 to bind to a remote port (e.g., RabbitMQ, Apache2, or Nginx). The -p flag indicates the custom SSH port of the remote server (2503), along with its username and address. The -N flag dictates that it shouldn't connect to a remote shell but perform forwarding only.