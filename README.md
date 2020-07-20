Hello, I will report it as follows.
Task -> Screenshot/Code
1.	Install a virtualization tool (VBox / VMware) and create a ubuntu virtual machine.
I used Oracle VM VirtualBox and Ubuntu 20.04
![Image 1](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image1.png)
 
2.	Login to the virtual machine, open the terminal and execute commands to find the the following.
a.	Current CPU load I used command “top”
![Image 2](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image2.png)
 
b.	Available memory  I used command “vmstat – s”
![Image 3](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image3.png)
 
c.	Available disk space I used command df -h --total
![Image 4](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image4.png)
 
d.	Uptime I used command “top’ we can see “up 4 min” uptime of 4 minutes
![Image 5](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image5.png)
 
Install docker-ce latest version in the created virtual machine. Show the output of `docker info` command.
![Image 6](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image6.png) 

Create a simple python script that does the following.
It accepts one command line argument. The expected argument should be path to a directory.
Upon execution the script will check if the directory exists. 
If the directory doesn’t exist, the script should print a warning that directory doesn’t exist and it should terminate gracefully.
![Image 7](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image7.png)  

If the directory exists, the script should check if there are any .json files exists in that directory. It should print the number of .json files exists in that directory to the console output. 
![Image 8](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image8.png)  

Creating a docker image.

Create a simple dockerfile that will build above application to a docker image and share the Dockerfile with your report. You may refer to examples here; https://docs.docker.com/get-started/part2/
![Image 9](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image9.png) 

Execute `docker build` command on the file and create a docker image. Please include the outputs in the report.
![Image 10](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image10.png) 

Next, run the docker image created in above step, as a docker container. During the execution of the docker container, it should accept command line argument and pass it to the script created in the previous step.
I am using a volume to point to the folders that I have created with JSON files.
Folder WithJson = 2 Files   Folder WithoutJson = 0 files  to prove the concept
![Image 11](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image11.png) 

Two folders I used are pasted below
![Image 12](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image12.png) 
![Image 13](https://github.com/patryk-jedrzejewski/Neudea/blob/master/Images%20for%20task/Image13.png) 
  

