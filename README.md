# Stock Market Backed Docker Compose setup

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vkmguy/mdfs-docker-config.git
    cd mdfs-docker-config
    ```

2. **Copy the sample environment file and configure:**

    ```bash
    cp .env.sample .env
    ```

   Edit the `.env` file with your configuration.

3. **Build and start the services:**

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker images and start the services.

4. **Access your application:**

    - Conductor console: [http://localhost:8080/admin/login](http://localhost:8080/admin/login)
    - PostGreSQL console: [http://localhost:5432/market](http://localhost:5432/market) (username: postgres, password: root)
    - Apache Kafka: Access the Kafka container for further configuration
    - Apache ZooKeeper: Access the ZooKeeper container for further configuration

5. **To stop the services, press `Ctrl + C` in the terminal where `docker-compose` is running.**

## Configuration

- Update environment variables in the `.env` file as needed for your project.

## Services

### PostgreSQL Database

The PostgreSQL database stores the market data and ML model results. You can access the database using tools like `pgAdmin` or connect directly to the database container.

### Apache Kafka

Apache Kafka is used for asynchronous communication between components. Configuration details can be found in the Kafka container.

### Apache ZooKeeper

ZooKeeper is a coordination service required by Kafka. Configuration details can be found in the ZooKeeper container.

## Troubleshooting

- If you encounter issues, check the logs of individual containers for more details.

## License

This project is licensed under the [MIT License](LICENSE).
