# Core Traxi Users

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
docker build -t core-trx-users .
```

And run it with:
```sh
docker run -p 8000:8000 core-trx-users
```
## API

The service provides a RESTful API with endpoints for managing users and permissions. The API is versioned and the current version is v1. The base URL for the API is `/api/v1`.

Here are some of the available endpoints:

- `users`: GET, POST, PUT, DELETE operations for users.
- `permissions`: GET, POST, PUT, DELETE operations for permissions.
- `roles`: GET, POST, PUT, DELETE operations for permissions.

For a full list of available endpoints and their specifications, please refer to the API documentation available at `/docs` when the service is running.

## Possibilities with Service Core Traxi Users

Service core traxi users is a versatile service that can be used for a variety of user management tasks. Here are some possibilities:

- **User Management**: Create, update, delete, and retrieve users. You can also manage user roles and permissions.
- **Permission Management**: Define and manage permissions for different roles. You can also assign permissions to specific users.
- **Integration**: The service can be integrated with other services in the Traxi ecosystem for a comprehensive business solution.

Remember, this is just the beginning. The modular design of the service allows for easy expansion and addition of new features as per your business needs.

## Indeed Information

For detailed information on installation and prerequisites, please refer to the [template repository](git@github.com:Traxi-on/core_template_fastAPI_MS.git#required).

## Contributing

We welcome contributions from our internal collaborators! If you have the responsibility or are interested in contributing to any of our projects, please take a moment to review our [Contribution Guidelines Repository](https://github.com/Traxi-on/Contribution-Guidelines) and follow the outlined process.

## License

All software produced by our organization is proprietary and protected by intellectual property laws. The source code, binaries, and associated materials are not open-source and are the exclusive property of [Traxi](https://github.com/traxi-on).

By interacting with our repositories, you agree to adhere to our terms of use and respect the proprietary nature of our software.
