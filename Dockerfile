FROM python:3.10.1

#sorry for noob dockerfile

# Installing Required Packages
RUN apt-get update && apt-get upgrade -y && \
    apt install --no-install-recommends -y \
    python3-pip \
    python3-requests \
    python3-tz \
    python3-aiohttp \
    curl \
    figlet \
    git \
    bash \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

COPY . /rikudo
WORKDIR /rikudo
RUN chmod 777 /rikudo
RUN pip3 install --upgrade pip setuptools
RUN sudo apt install python3-pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

#fuck I'm noob in docker 

CMD ["python3", "-m", "Stella"]
