# Access and run custom nginxdemos/hello container via dgs-public repository

Navigate to https://github.com/denise-stoudt/dgs-public and download code as a zip file. If necessary, extract files. Combine Dockerfile and index files into a new folder called hello-nginx.

Navigate to parent directory of hello-nginx folder within linux system. Issue the following command to build the image locally:
```
docker build hello-nginx
```
Next, retrieve the image id of the new build:
```
docker images
```
Finally, run the container on port 8080 using the following command:
```
docker run -P -d -p 8080:80 <image id>
```
Open a new tab in the browser of your choice and navigate to http://127.0.0.1:8080 to view custom content

Helpful Info

After viewing the content of nginxdemos/hello, the container can be cleaned from the local system with the following steps:
    view all docker containers using command ```docker ps -a```
    if container is currently running, issue command docker stop <container id>
    issue command docker rm <container id>
Clean unused image from workstation
    issue command docker images to view all images stored locally on machine
    issue docker rmi <image id> to remove unwanted images

Modify my dockerfile with different index.html content
    navigate to parent directory of hello-nginx folder within linux system  
    issue command wget <content url> (ex. wget https://commons.wikimedia.org/wiki/File:Frog_on_palm_frond.jpg)
    rename file index.html and replace existing index.html file
    repeat steps to build and run container

 Run container for access on port 8081
    build the container as described in above section
    issue the following command docker run -P -d -p 8081:80 <image id>
