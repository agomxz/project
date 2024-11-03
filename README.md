# Users

Welcome to "Core Traxi Users". This service is dedicated to handling user-related actions for Traxi projects.

The service is built based on the [Core fastAPI MS Template](git@github.com:Traxi-on/core_template_fastAPI_MS.git). For comprehensive technical details, instructions on how to run, deploy, and any other related considerations, please refer to the documentation provided in the [template repository](git@github.com:Traxi-on/core_template_fastAPI_MS.git).


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
docker build -t users .
```

And run it with:
```sh
docker run -p 8000:8000 users
```
## API

The service provides a RESTful API with endpoints for managing users and permissions. The API is versioned and the current version is v1. The base URL for the API is `/api/v1`.

Here are some of the available endpoints:

- `users`: GET, POST, PUT, DELETE operations for users.



## Possibilities with Users Service

Service users is a versatile service that can be used for a variety of user management tasks. Here are some possibilities:

- **User Management**: Create, update, delete, and retrieve users.