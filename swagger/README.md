# Swagger API Documentation

## Overview
This project provides an API documentation system using Swagger UI. It allows developers to explore and test API endpoints conveniently.

## Project Structure
```
project-root/
│── openapi.yaml        # Main OpenAPI definition file
│── server.js           # Express server to host Swagger UI
│── package.json        # Project dependencies
│── node_modules/       # Installed libraries
│── resources/
    ├── auth.yaml       # Authentication-related API definitions
    ├── user.yaml       # User-related API definitions
    ├── ...
```

## Installation
Before running the project, install the required dependencies:
```sh
cd swagger
```

```sh
npm install
```

```sh
cd ..
```

## Running the Swagger UI
To start the Swagger documentation server, use:
```sh
node swagger/server.js
```
Once started, open your browser and visit:
```
http://localhost:3001/api-docs
```