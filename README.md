# Package Management API

A Django-based RESTful API for managing packages in a courier service, allowing users to perform CRUD operations, track package status, and manage soft deletes.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [API Endpoints](#api-endpoints)
  - [Create Package](#create-package)
  - [List Packages](#list-packages)
  - [Get Package by Tracking Number](#get-package-by-tracking-number)
  - [Update Package](#update-package)
  - [Delete Package (Soft Delete)](#delete-package-soft-delete)
  - [Restore Package](#restore-package)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides a Django REST framework API for managing packages in a courier service. Users can perform the following tasks:

- Create and manage packages with details such as recipient, sender, weight, and tracking number.
- Track package status (pending, in transit, delivered).
- Soft delete packages (mark them as deleted without removing from the database).
- Restore previously soft-deleted packages.

## Features

- **CRUD operations** for packages.
- **Tracking status** of packages.
- **Soft delete** functionality.
- User authentication and authorization with **JWT tokens**.
- Easy integration with a front-end or other services.

## Technologies Used

- **Django**: Python-based web framework.
- **Django REST Framework**: Toolkit for building APIs in Django.
- **JWT**: JSON Web Tokens for authentication.
- **Git**: Version control for code.
- **GitHub**: Hosting and sharing the code.

## Installation Guide

### Prerequisites:
- Python 3.8+ installed

### Steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sojib96/courier_service_api.git

2. **Navigate to the project folder:**:
   ```bash
   cd courier_service_api

3. **Set up a virtual environment (optional but recommended):**:
   ```bash
   python -m venv venv

4. **Activate the virtual environment:**:
   ```bash
   venv\Scripts\activate

5. **Install the dependencies:**:
   ```bash
   pip install -r requirements.txt

6. **Set up the database:**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. **Create a superuser:**:
   ```bash
   python manage.py createsuperuser

8. **Run the development server:**:
   ```bash
   python manage.py runserver

- Your API will be available at http://127.0.0.1:8000/

## API Endpoints

### Create Package
- **URL**: `POST /api/packages/`
- **Description**: Create a new package
- **Authentication**: Required (JWT token)
- **Request Body**:
  ```json
  {
      "recipient_name": "John Doe",
      "recipient_address": "123 Main St",
      "weight": 2.5
  }
  ```

### List Packages
- **URL**: `GET /api/packages/`
- **Description**: Get a list of all packages
- **Authentication**: Required (JWT token)

### Get Package by Tracking Number
- **URL**: `POST /api/packages/get_package_by_tracking/`
- **Description**: Get details of a package by providing its tracking number.
- **Request Body**:
  ```json
  {
    "tracking_number": "9130685a-394b-4197-9"
  }

### Update Package
- **URL**: `PATCH /api/packages/{id}/`
- **Description**: Update an existing package
- **Authentication**: Required (JWT token)
- **Request Body**:
  ```json
  {
    "recipient_name": "Sojib"
  }

### Delete Package (Soft Delete)
- **URL**: `POST /api/packages/{id}/soft_delete/`
- **Description**: Soft delete a package
- **Authentication**: Required (JWT token)

### Restore Package
- **URL**: `POST /api/packages/{id}/restore/`
- **Description**: Restore a soft-deleted package
- **Authentication**: Required (JWT token)

## Conclusion

This API provides a robust solution for managing courier service packages with features like CRUD operations, soft delete functionality, and JWT authentication. For any issues or suggestions, please create an issue in the repository or submit a pull request.
