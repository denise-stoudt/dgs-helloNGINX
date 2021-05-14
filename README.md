# Access and run custom nginxdemos/hello container via dgs-public repository

1. Navigate to https://github.com/denise-stoudt/dgs-public and download code as a zip file. If necessary, extract files. Combine Dockerfile and index files into a new folder called hello-nginx.

2. Navigate to parent directory of hello-nginx folder within linux system. Issue the following command to build the image locally:
```
docker build hello-nginx
```
3. Next, issue the following command to view and retrieve the image id of the new build:
```
docker images
```
4. Finally, run the container on port 8080 using the following command:
```
docker run -P -d -p 8080:80 <image id>
```
5. Open a new tab in the browser of your choice and navigate to http://127.0.0.1:8080 to view the custom content

# Helpful Info

After viewing the content of nginxdemos/hello, the container can be cleaned from the local system with a few simple steps. First, you'll want to view all docker 
containers using command ```docker ps -a``` to retrieve the ID of the container you'd like to remove. If the container is currently running, issue ```docker 
stop <container id>``` to stop the running container. Next, issue ```docker rm <container id>``` to remove the container. Once the container is removed, the image can 
be deleted as well. Issue command ```docker images``` to view all images stored locally on machine and retrieve the ID of the image you'd like to remove. Finally, 
issue ```docker rmi <image id>``` to remove the unwanted image.

The dockerfile included in this repository can be modified to serve different index.html content. Navigate to the parent directory of hello-nginx folder within linux 
system and issue command ```wget <desired content url>``` (ex. ```wget https://commons.wikimedia.org/wiki/File:Frog_on_palm_frond.jpg```) to download the content to your 
local machine. Rename that file index.html and replace the existing index.html file. Repeat above steps 2-5 to build and run the container.

To run the container for access on a port other than 8080 such as 8081, build the container as described in above steps 2 and 3, then issue the following command to run 
the container on port 8081: ```docker run -P -d -p 8081:80 <image id>```. Open a new tab in the browser of your choice and navigate to http://127.0.0.1:8081 to view the
custom content.
