FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

#Download dependencies
RUN apt-get update && apt-get -y --no-install-recommends install libc6-dev libgtk2.0-0 libgtk-3-0 libpango-1.0-0 libcairo2 libfontconfig1 libgconf2-4 libnss3 libasound2 libxtst6 unzip libglib2.0-bin libcanberra-gtk-module libgl1-mesa-glx curl build-essential gettext libstdc++6 software-properties-common wget git xterm automake libtool autogen nodejs libnotify-bin aspell aspell-en htop git emacs mono-complete gvfs-bin libxss1 rxvt-unicode-256color x11-xserver-utils sudo vim libxkbfile1 gnupg libsecret-1-0

RUN wget -O code.deb https://go.microsoft.com/fwlink/?LinkID=760868
RUN dpkg -i code.deb

RUN adduser jitin
RUN su jitin
workdir /jitin

#CMD /usr/bin/code --user-data-dir /jitin
