

Idea :

1. unix domains sockets for communication between two people connected to same server.
2. HiddenServer  : developer creates local hidden dev server that runs on hidden machine
2. Service Proxy : hidden server connects to public webserver to create server proxy, a 2 minute long running process that waits for work. 
3. Remote User:  connect to public url, send requests that are forwarded to Service Proxy, then to the HiddenServer.
4. Responses from Hidden Sever are sent to the Service Proxy.
5. Hidden Server can Connect via SSH and connect to sockets.
6. Multiple Hidden Servers can connect and be found via directory listing. All the servers active are found in directory. 
7. When a client connects it looks for a socket file that is newest. The newest file is symlinked when the server connects so that you will quickly find it. 

8. All Code for the server can be uploaded from an ssh connection or stored in a single file. https://pypi.python.org/pypi/wheel like the wheel file, but it does not even need to exist on disk.
9. When the server disconnects, then it removes the file and removes the symlink if it is the last one. 
