FROM ubuntu:18.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install dependencies
RUN apt-get update && apt-get install -y \
    python-pip \
    ncbi-blast+ \
    git \
    mysql-server-5.7 \
    parallel \
    libmysqlclient-dev \
    libjpeg-dev \
    zlib1g-dev \
    gir1.2-gtk-3.0 \
    clustalw \
    clustalo \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages separately for caching
RUN pip install PyPDF2
RUN pip install beautifulsoup4
RUN pip install biopython==1.76
RUN pip install mysqlclient
RUN pip install reportlab
RUN pip install requests

# Create application directory
RUN mkdir -p /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Clone the specific branch of the starterator repository from your GitHub account
RUN git clone -b dockerization https://github.com/cdshaffer/starterator.git .

# Ensure the latest commit is pulled during each build
RUN git pull origin dockerization

# Copy the database file into the container
COPY Actino_Draft.sql /docker-entrypoint-initdb.d/

# Make the starterator.sh script executable
RUN chmod +x starterator.sh

# Expose MySQL port
EXPOSE 3306

# Start MySQL service, create database, and import SQL file, then start a bash shell
CMD service mysql start && mysql -u root -e "CREATE DATABASE IF NOT EXISTS Actino_Draft;" && mysql -u root Actino_Draft < /docker-entrypoint-initdb.d/Actino_Draft.sql && /bin/bash
