# URL Shortening Service

## Description

This project (project link : https://roadmap.sh/projects/url-shortening-service) implements a URL shortening service using Python, Flask, and MongoDB. It allows users to shorten long URLs into more manageable ones. The service stores the original and shortened URLs in a MongoDB database and provides API endpoints for creating, retrieving, updating, and deleting shortened URLs. 

The goal of this project is to demonstrate the integration of Flask web framework, MongoDB database, and simple API design. It's a great tool for learning full-stack web development and working with databases.

## Table of Contents

1. [Installation Instructions](#installation-instructions)
2. [Usage Examples](#usage-examples)
3. [Contribution Guidelines](#contribution-guidelines)
4. [Contact Information](#contact-information)
5. [Credits and Acknowledgments](#credits-and-acknowledgments)

## Installation Instructions

### Prerequisites
- Python 3.6 or higher
- MongoDB running locally or remotely

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/garvitpathak27/URL-Shortening-Service.git
   cd URL-Shortening-Service
   cd url_shortner
   pip install -r requirements.txt
   mongod
   python3 app.py

The app should be accessible at http://127.0.0.1:5000/.
# Tech Stack

This project utilizes a variety of technologies to build a URL shortening service. Below is a detailed overview of the tech stack used in the project, including links to their official documentation for further reading.

## 1. Python

**Overview**: Python is a high-level programming language used for developing the core functionality of the URL Shortener service. Python’s simplicity and readability make it ideal for building rapid prototypes and web applications.

- **Version used**: Python 3.6+
- **Official Documentation**: [Python Documentation](https://docs.python.org/3/)

## 2. Flask

**Overview**: Flask is a micro web framework for Python used to create the web server that handles HTTP requests. It provides the necessary tools to create RESTful APIs, handle routes, and serve the front-end.

- **Version used**: Flask 2.x
- **Official Documentation**: [Flask Documentation](https://flask.palletsprojects.com/)

## 3. MongoDB

**Overview**: MongoDB is a NoSQL database used for storing the URL data. It allows flexible schema design and stores the original URL, shortened URL, creation time, update time, and access count for each URL.

- **Version used**: MongoDB 4.x or higher
- **Official Documentation**: [MongoDB Documentation](https://docs.mongodb.com/)

## 4. PyMongo

**Overview**: PyMongo is the official Python driver for MongoDB. It allows the Flask application to interact with the MongoDB database to perform CRUD operations like creating, retrieving, updating, and deleting URL data.

- **Version used**: PyMongo 3.x
- **Official Documentation**: [PyMongo Documentation](https://pymongo.readthedocs.io/)

## 5. Random Code Generation

**Overview**: To generate short codes for URLs, the project uses a custom Python function that generates a random alphanumeric code. This helps in creating unique identifiers for each URL.

- **Resources**: The random code generation is implemented in Python using the `random` module, which can be explored further through the Python documentation.

## 6. MongoDB Atlas (Optional)

**Overview**: If you're not using a local MongoDB instance, you can set up MongoDB Atlas, a cloud database service for MongoDB. It is fully managed and provides a simple way to host a MongoDB instance remotely.

- **Official Documentation**: [MongoDB Atlas Documentation](https://www.mongodb.com/cloud/atlas)

## 7. Postman (For API Testing)

**Overview**: Postman is a powerful tool used for testing APIs. It provides an easy interface to test all the endpoints (e.g., `POST`, `GET`, `PUT`, `DELETE`) for the URL Shortening Service.

- **Official Documentation**: [Postman Documentation](https://learning.postman.com/)

## 8. Git

**Overview**: Git is a version control system used to manage the project’s source code. It allows collaboration and tracking of changes made to the codebase over time.

- **Version used**: Git 2.x
- **Official Documentation**: [Git Documentation](https://git-scm.com/doc)

## 9. GitHub

**Overview**: GitHub is used to host the source code of this project and enable version control through Git. It also serves as a platform for collaboration through pull requests and issues.

- **Official Documentation**: [GitHub Documentation](https://docs.github.com/en/github)

## 10. HTML, CSS, and JavaScript (Frontend)

**Overview**: The frontend of this project uses HTML for structure, CSS for styling, and JavaScript for dynamic content. These are used to provide a user-friendly interface for shortening URLs and viewing statistics.

- **HTML**: [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **CSS**: [CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
- **JavaScript**: [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## 11. Docker (Optional for Deployment)

**Overview**: Docker can be used to containerize the application for easier deployment. It ensures that the application runs consistently in any environment.

- **Official Documentation**: [Docker Documentation](https://docs.docker.com/)

## 12. Heroku (Optional for Deployment)

**Overview**: Heroku is a cloud platform that can be used to deploy web applications easily. You can deploy your URL shortening service on Heroku for easy access from anywhere.

- **Official Documentation**: [Heroku Documentation](https://devcenter.heroku.com/)

---

By using this tech stack, we can create a simple yet powerful URL shortening service that handles URLs efficiently, scales well with MongoDB, and provides a user-friendly interface with Flask.

