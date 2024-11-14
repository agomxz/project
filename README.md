# Service
This service is dedicated to handling the csv file in order to store it into a database.

## Working

https://project-production-8a47.up.railway.app/docs

## Setup
1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    ```

2. **Install Dependencies and Configuration:**
    - Use the provided `makefile` command:
        ```sh
        make init
        ```
    - Alternatively, you can set up manually:
        1. **Install the required Python packages:**
            ```sh
            pip install -r requirements.txt
            ```
        2. **Configuration:**
            - Copy `example.env` to `.env` and modify the environment variables as needed.

3. **Run the Application:**
    ```sh
    uvicorn app.main:app --reload
    ```

### Docker

Alternatively, you can run the service using Docker. Build the Docker image using:
```sh
docker build -t transactions .
```

And run it with:
```sh
docker run -p 8000:8000 transactions
```
## API

The service provides a RESTful API with endpoints. The API is versioned and the current version is v1. The base URL for the API is `/api/v1`.



## Possibilities with Service

Service users is a versatile service that can be used for a variety of user management tasks. Here are some possibilities:

- **Transactions Management**: Uploas csv file, Get Summary