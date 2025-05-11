# FastAPI Market Data

This project is a FastAPI application that exposes RESTful endpoints and supports WebSocket connections for subscribing to market data updates.

## Features

- RESTful API for market data retrieval and management.
- WebSocket support for real-time market data updates.
- Modular architecture with clear separation of concerns.

## Project Structure

```
fastapi-market-data
├── app
│   ├── api
│   │   ├── routes
│   │   └── endpoints
│   ├── core
│   ├── models
│   ├── schemas
│   └── services
├── tests
├── .env.example
├── .gitignore
├── Dockerfile
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-market-data
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://localhost:8000/docs`.

## WebSocket

To connect to the WebSocket for market data updates, use the following endpoint:
```
ws://localhost:8000/ws/market-data
```

## Testing

To run the tests, use:
```
pytest
```

## Environment Variables

You can configure the application using environment variables. An example `.env` file is provided as `.env.example`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.