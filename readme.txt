# 🗓️ AI Scheduler API

This is a Flask-based RESTful API for a scheduling application that supports user registration, login, email verification, and secure event management. It connects to a MySQL database and uses JWT tokens for authentication. The system is being extended to include intelligent scheduling recommendations using the OpenAI API.

---

## 🚀 Features

* **User Registration**

  * Validates email format and password strength
  * Checks for existing users
  * Sends verification link via SendGrid with JWT-based expiring token

* **User Login**

  * Authenticates user credentials
  * Returns a secure access token on success

* **Email Verification**

  * Endpoint to confirm account using secure verification link

* **Event Management**

  * View all events for a user
  * View a specific event by `event_id`
  * Create new events with metadata (title, time, type)
  * All event operations are protected via token-based authentication

* **(Planned) AI-Powered Event Recommendations**

  * Leverages OpenAI’s API to analyze a user’s schedule
  * Recommends optimal times for study, rest, or focus blocks
  * Will help balance workload, free time, and goal progress intelligently

---

## 🧠 Upcoming AI Functionality

**Goal**: Use OpenAI's API to scan a user's existing calendar and recommend:

* Optimal times to study, eat, or take breaks
* Suggestions for rescheduling based on workload distribution
* Natural language explanations for proposed changes

This feature will be modular and separated from core event logic to allow scalability.

---

## 💠 Tech Stack

* **Backend**: Python, Flask, Flask-RESTful
* **Database**: MySQL (via `flask_mysqldb`)
* **Auth**: JSON Web Tokens (JWT)
* **Email**: SendGrid API
* **AI Engine**: OpenAI API (GPT) *(planned)*

---

## 🔄 API Endpoints

| Endpoint                        | Method | Description                         | Auth Required |
| ------------------------------- | ------ | ----------------------------------- | ------------- |
| `/register`                     | POST   | Register a new user                 | ❌             |
| `/login`                        | POST   | Login and receive auth token        | ❌             |
| `/verify-email`                 | GET    | Verify account via email link       | ❌             |
| `/events`                       | GET    | Get all user events                 | ✅             |
| `/event`                        | GET    | Get one event by ID                 | ✅             |
| `/event`                        | POST   | Create a new event                  | ✅             |
| *(Planned)* `/recommend-events` | POST   | Get AI-powered schedule suggestions | ✅             |

---

