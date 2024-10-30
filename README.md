<h1 align="center">Visitor Counter</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/flask-2.0-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/redis-6.2-red.svg" alt="Redis Version">
  <img src="https://img.shields.io/badge/docker-20.10-blue.svg" alt="Docker Version">
  <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT License">
</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

## About

The Visitor Counter is a simple web application that displays the number of visits to the web page. It is built using Flask, Redis, and Docker, and provides a user-friendly interface for tracking website traffic.

## Features

- Displays the total number of visits to the web page
- Provides a "Refresh Count" button to update the visit count
- Uses Redis as the backend cache to store the visit count
- Dockerized application for easy deployment

## Installation

To run the Visitor Counter web application, you'll need to have Docker and Docker Compose installed on your system.

1. Clone the repository:

    git clone https://github.com/karannchaudhari04/Visitor-Counter-docker-project

2. Navigate to the project directory:

    cd Visitor-Counter-docker-project

3. Build and start the Docker containers:

    docker-compose up --build


This will build the Docker image and start the application container and the Redis container.

## Usage

Once the containers are running, you can access the web application by opening your web browser and navigating to `http://localhost:5000`.

You should see the Visitor Counter page, displaying the current visit count. Click the "Refresh Count" button to update the visit count.

## Configuration

The application uses the following environment variables for configuration:

- `REDIS_HOST`: The hostname or IP address of the Redis server. Default is `redis`.
- `REDIS_PORT`: The port number of the Redis server. Default is `6379`.

You can set these environment variables in the `docker-compose.yml` file or by creating a `.env` file in the project directory.

## Contributing

If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE).
