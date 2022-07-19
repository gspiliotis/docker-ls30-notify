# webhook-script-runner

[![pipeline status](https://gitlab.com/vondruska/docker-webhook-script-runner/badges/master/pipeline.svg)](https://gitlab.com/vondruska/docker-webhook-script-runner/commits/master)

## What is this?
Docker image to allow a service to hit an HTTP endpoint and execute a shell script. HTTP server is [Node HTTP](https://nodejs.org/api/http.html).
Installed for opening ZKAccess door using Lua library from here: https://github.com/vwout/zkaccess-c3-lua

## How do I use it?

The HTTP server runs on port 9080.

```
docker run -d --rm --name webhook -p 9080:9080 gspiliotis/zk-door-open
```

then visit http://localhost:9080/open. `open` is the default token and can be changed using the environment variable.

When `/thisisunsafe` is executed, by default `/scripts/helloworld.sh` will be executed outputting 'Hello World' to STDOUT. To change the script to be run, use the `WEBHOOK_SCRIPT` environment variable.

You'll likely need to mount your own shell scripts into the image. The `/scripts` directory is a good place to do that.

## Environment Variables

* `TOKEN` = the URL that must be hit for the webhook script to run (http://localhost:9080/{token})
* `WEBHOOK_SCRIPT` = path to the script that will be run when a request is received at `TOKEN`
* `STARTUP_SCRIPT` = path to the script ran at startup of container. Useful if setup is necessary on startup (credentials, service discovery, etc)
* `SCRIPT_EXECUTION_TIMEOUT` = how long the webhook shell script is allowed to run before it is terminiated
* `DELAY` = How long to keep the door open
* `ZK_IP` = IP of ZK Access

## Nice to know

* This image has `XDG_CONFIG_HOME` set to `/config` allowing Git to find the configurations easier without a home directory.
