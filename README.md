# Starterator

unedited README.md as created by github Copilot

Active working clone of SEA-PHAGES Starterator

## Description

Starterator is a tool for analyzing phage genomes. This repository contains the active working clone of the SEA-PHAGES Starterator project.

## Installation

### Using Docker

1. Clone the repository:
    ```sh
    git clone https://github.com/cdshaffer/starterator.git
    cd starterator
    ```

2. Build the Docker image:
    ```sh
    docker build -t starterator .
    ```

3. Run the Docker container:
    ```sh
    docker run -it starterator
    ```

### Manual Installation

1. Install dependencies:
    ```sh
    sudo apt-get update
    sudo apt-get install -y python-pip ncbi-blast+ git mysql-server-5.7
    pip install PyPDF2 beautifulsoup4 biopython==1.76
    ```

2. Clone the repository:
    ```sh
    git clone https://github.com/cdshaffer/starterator.git
    cd starterator
    ```

3. Run the installation script:
    ```sh
    chmod +x installStarterator.sh
    ./installStarterator.sh
    ```

## Usage

To run the command-line version of Starterator, start the Docker container with an interactive bash prompt and execute the desired commands.

```sh
docker run -it starterator
# Inside the container
./starterator.sh
# Dockerize_starterator
