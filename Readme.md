# Farm Management System

## Overview

The **Farm Management System** is a Django-based application designed to manage farms, crops, and animals. It features user authentication and permissions using Django REST Framework (DRF) and JSON Web Tokens (JWT) to secure API access.

## Features

- JWT-based user authentication
- CRUD operations for farms, crops, and animals
- Custom permissions to restrict operations to farm owners

## Models

### User
A custom user model with the following fields:
- Username
- Password
- Email
- Phone number
- Address

### Farm
Represents a farm and includes:
```python
class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
```

### Crop
Represents a crop and includes:
```python
class Crop(models.Model):
    name = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    planting_date = models.DateField()
    harvest_date = models.DateField()
```

### Animal
Represents an animal and includes:
```python
class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    birth_date = models.DateField()
```

## API Operations

### User Operations
- **Register a new user**
- **Authenticate users with JWT**

### Farm Operations
- **Create a new farm**
- **Retrieve details of a farm**
- **Update farm details** (restricted to the owner)
- **Delete a farm** (restricted to the owner)

### Crop Operations
- **Add a new crop**
- **Retrieve details of a crop**
- **Update crop details** (restricted to the farm owner)
- **Delete a crop** (restricted to the farm owner)

### Animal Operations
- **Add a new animal**
- **Retrieve details of an animal**
- **Update animal details** (restricted to the farm owner)
- **Delete an animal** (restricted to the farm owner)


## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Run tests**:
    ```bash
    python manage.py test
    ```
   

## Postman Collection
you can find the postman collection for the API endpoints in the root directory of the project.
or you can see the collection online [here](https://www.postman.com/interstellar-station-543920/workspace/bortoqala-assessment)
and make sure to select the development environment to test the endpoints. 