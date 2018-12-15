docker build -t firefox .

docker run -ti --rm -e DISPLAY=192.168.1.156:0.0 firefox
