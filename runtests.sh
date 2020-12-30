docker build . -t horoscopecli
clear
docker run -it --entrypoint sh horoscopecli -c "cd /app && pytest $@"
