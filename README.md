# Package Management API

A Django-based RESTful API for managing packages in a courier service, allowing users to perform CRUD operations, track package status, and manage soft deletes.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Guide](#installation-guide)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Create Package](#create-package)
  - [List Packages](#list-packages)
  - [Get Package by Tracking Number](#get-package-by-tracking-number)
  - [Update Package](#update-package)
  - [Delete Package (Soft Delete)](#delete-package-soft-delete)
  - [Restore Package](#restore-package)
- [Conclusion](#conclusion)

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

### Authentication
- **URL**: `POST /api/token/`
- **Description**: Get JWT access token
- **Curl Command**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\": \"admin\", \"password\": \"your_password\"}"
  ```
- **Response**:
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
  ```

### Create Package
- **URL**: `POST /api/packages/`
- **Description**: Create a new package
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/packages/ ^
  -H "Authorization: Bearer your_jwt_token" ^
  -H "Content-Type: application/json" ^
  -d "{\"recipient_name\": \"John Doe\", \"recipient_address\": \"123 Main St\", \"weight\": 2.5, \"description\": \"Fragile items\"}"
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 3,
    "tracking_number": "65c26766-dc77-433c-9385-f24109a7df78",
    "recipient_name": "John Doe",
    "recipient_address": "123 Main St",
    "weight": 2.5,
    "description": "Fragile items",
    "status": "pending",
    "created_at": "2025-03-10T18:28:11.959890Z",
    "updated_at": "2025-03-10T18:28:11.959920Z",
    "deleted_at": null,
    "sender": 1
    }
  ```

### List Packages
- **URL**: `GET /api/packages/`
- **Description**: Get list of all packages
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/packages/ ^
  -H "Authorization: Bearer your_jwt_token"
  ```
- **Response** (200 OK):
  ```json
  [
    {
        "id": 1,
        "tracking_number": "9130685a-394b-4197-9",
        "recipient_name": "John Doe",
        "recipient_address": "123 Main St",
        "weight": 2.5,
        "description": "No Description",
        "status": "pending",
        "created_at": "2025-03-10T16:50:35.845604Z",
        "updated_at": "2025-03-10T17:05:58.347128Z",
        "deleted_at": null,
        "sender": 1
    }
  ]
  ```

### Get Package by Tracking Number
- **URL**: `GET /api/packages/get_package_by_tracking/`
- **Description**: Get package details by tracking number
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X GET http://127.0.0.1:8000//api/packages/get_package_by_tracking/ ^
  -H "Content-Type: application/json" ^
  -d "{\"tracking_number\": \"tracking number\"}"
  ```
- **Response** (200 OK):
  ```json
  {
    "sender": 1,
    "description": "No Description",
    "recipient_name": "Sojib",
    "status": "in_transit"
  }
  ```

### Update Package
- **URL**: `PATCH /api/packages/{id}/`
- **Description**: Update package details
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X PATCH http://127.0.0.1:8000/api/packages/1/ ^
  -H "Authorization: Bearer your_jwt_token" ^
  -H "Content-Type: application/json" ^
  -d "{\"status\": \"in_transit\", \"recipient_name\": \"John Smith\"}"
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "tracking_number": "",
    "recipient_name": "Saimon Sojib",
    "recipient_address": "123 Main St",
    "weight": 2.5,
    "description": "No Description",
    "status": "pending",
    "created_at": "2025-03-10T16:50:35.845604Z",
    "updated_at": "2025-03-10T18:44:10.044573Z",
    "deleted_at": null,
    "sender": 1
  }
  ```

### Delete Package (Soft Delete)
- **URL**: `DELETE /api/packages/{id}//soft_delete/`
- **Description**: Soft delete a package
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X DELETE http://127.0.0.1:8000//api/packages/{id}/soft_delete/ ^
  -H "Authorization: Bearer your_jwt_token"
  ```
- **Response** (200 OK)
 ```json
 {
    "message": "Package soft deleted"
 }
 ```
### Restore Package
- **URL**: `POST /api/packages/{id}/restore/`
- **Description**: Restore a soft-deleted package
- **Authentication**: Required (JWT token)
- **Curl Command**:
  ```bash
  curl -X POST http://127.0.0.1:8000//api/packages/{id}/restore/ ^
  -H "Authorization: Bearer your_jwt_token"
  ```
- **Response** (200 OK):
  ```json
  {
    "message": "Package restored"
  }
  ```

## Conclusion

This API provides a robust solution for managing courier service packages with features like CRUD operations, soft delete functionality, and JWT authentication. For any issues or suggestions, please create an issue in the repository or submit a pull request.
