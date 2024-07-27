
# Profiling API Documentation

Welcome to this api documentation! This API allows you to perform a background search on a potential client before having a meeting. It conducts a Google search, extracts data from the first page of search results, and then summarizes that data using OpenAI.

## Base URL

The base URL for accessing the API is:

```
https://mainfilm.pythonanywhere.com/api/research
```

## Endpoints

### 1. Perform Background Search

**Endpoint:** `/research`

**Method:** GET

**Description:** This endpoint performs a background search on a specified person. It takes a query parameter with the name of the person to research and returns a summary of the data extracted from the first page of Google search results.

**Request Parameters:**

- `query` (required): The name of the person to research.

**Example Request:**

```
GET https://mainfilm.pythonanywhere.com/api/research?query=John%20Doe
```

**Response:**

The response is a JSON object containing a summary of the data extracted from the first page of Google search results.

**Example Response:**

```json
{
  "query": "John Doe",
  "summary": "John Doe is a renowned author and speaker known for his work in the field of technology. He has written several books on artificial intelligence and has been a keynote speaker at numerous conferences..."
}
```

## Error Handling

The API may return the following error responses:

- `400 Bad Request`: If the `query` parameter is missing or invalid.
- `500 Internal Server Error`: If there is an issue with processing the request.

**Example Error Response:**

```json
{
  "error": "Missing query parameter"
}
```

## Usage

To use the API, simply send a GET request to the endpoint with the name of the person you want to research as the `query` parameter. The API will return a summary of the data found on the first page of Google search results for that person.

## Rate Limiting

There are currently no rate limits imposed on the API. However, it is recommended to use the API responsibly to avoid potential issues.

## Changelog

**Version 1.0.0**

- Initial release with the `/research` endpoint for performing background searches.

Thank you for using the Background Search API! We hope it helps you gather the information you need efficiently and effectively.
