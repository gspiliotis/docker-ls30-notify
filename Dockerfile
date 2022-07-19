ARG ARCH=library
FROM $ARCH/node:slim
RUN apt-get update && apt-get install -y git curl python \
 && rm -rf /var/lib/apt/lists/*
RUN luarocks install luasocket
ENV TOKEN=thisisunsafe WEBHOOK_SCRIPT=/scripts/notify_ls30.py XDG_CONFIG_HOME=/config

# setup XDG_CONFIG_HOME directories and make it able to write from anyone.
# it is up to whatever puts files into this directory to protect them
RUN mkdir -p /config && chmod 777 /config
EXPOSE 9080
WORKDIR /scripts
COPY scripts /scripts
RUN chmod +x /scripts/notify_ls30.py
COPY src /app
CMD ["sh","-c","/scripts/startup-wrapper.sh && node /app/server.js"]
