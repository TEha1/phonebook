# Phonebook Application
A simple phonebook application using Django and PostgreSQL, containerized with Docker.

## Features

- Add a contact with multiple phone numbers.
- List all contacts.
- View details of a contact.

## Schema Diagram

**Contact**
- id (Primary Key)
- name (Character Varying)

**PhoneNumber**
- id (Primary Key)
- contact (ForeignKey to Contact)
- number (Character Varying)

## Setup

### Prerequisites

- Docker and Docker Compose

### Installation

1. Clone the repository:
    ```sh
    $ git clone https://github.com/TEha1/phonebook_project.git
    $ cd phonebook_project
    ```

2. Build and run the application with Docker:
    ```sh
    docker compose up --build
    ```

3. Access the application at `http://localhost:8000`.


## Development

### Apply Migrations

To apply migrations:

```sh
docker compose run web python manage.py migrate
```

To create superuser:

```sh
docker compose run web python manage.py createsuperuser
```
