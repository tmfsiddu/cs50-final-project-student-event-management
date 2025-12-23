# Student Event Management System

#### Video Demo: https://www.youtube.com/watch?v=YOUR_VIDEO_LINK_HERE
#### Description:

The Student Event Management System is a role-based web application developed as my CS50x final project. The application is designed to streamline the process of creating, managing, and registering for academic and campus events. It addresses the common problem of unorganized event communication by providing a centralized platform where staff members can create events and students can view, register, and track their participation.

This project demonstrates core concepts taught in CS50, including web application development using Flask, user authentication, session management, database design with SQLite, and dynamic HTML rendering using Jinja templates. The system supports multiple user roles and enforces role-based access control to ensure proper functionality and security.

---

## Project Overview

In many academic environments, event information is often scattered across multiple platforms such as notice boards, messaging groups, or emails. This makes it difficult for students to keep track of events and for staff to manage registrations efficiently. The Student Event Management System solves this problem by providing a simple, structured, and user-friendly web interface for event management.

The application supports two distinct roles:

- **Staff:** Responsible for creating and managing events.
- **Students:** Can register, log in, browse events, register for them, and track their registered events.

Each user experiences a dashboard tailored to their role, ensuring clarity and ease of use.

---

## How It Works

When a user opens the application, they are presented with a login page. Based on their credentials and role, they are redirected to the appropriate dashboard.

### Student Flow
1. A student registers for an account and logs in.
2. Upon login, the student is redirected to the **Student Dashboard**, where registered events are displayed.
3. The student can navigate to the **Events** page to browse all available events.
4. By clicking the **Register** button, the student registers for an event.
5. After registration, the student is redirected back to their dashboard, where the event now appears with a “Registered” status.
6. The student can log out securely at any time.

### Staff Flow
1. Staff accounts are pre-created to prevent unauthorized event creation.
2. After logging in, staff members are redirected to the **Staff Dashboard**.
3. Staff can create new events by providing a title, description, and date.
4. Created events are stored in the database and immediately become visible to students.
5. Staff members can view all events they have created and log out securely.

All user sessions are managed using Flask’s session mechanism, ensuring that login state is preserved across requests and protected against tampering.

---

## Implementation and Technologies

The project was implemented using the following technologies:

- **Backend:** Python with Flask
- **Frontend:** HTML, CSS, and Jinja templating
- **Database:** SQLite
- **Authentication:** Password hashing using Werkzeug
- **Session Management:** Flask sessions secured with a secret key

---

## File Structure and Key Components

- **app.py**
  The main Flask application file. It contains route definitions, authentication logic, role-based access control, database queries, and session handling.

- **database.db**
  SQLite database storing users, events, and registrations.

- **init_db.py**
  Initializes the database schema and creates required tables.

- **templates/**
  Contains all HTML templates:
  - `login.html` – User login page
  - `register.html` – Student registration page
  - `student_dashboard.html` – Displays registered events for students
  - `events.html` – Lists all available events for students
  - `staff_dashboard.html` – Displays events created by staff
  - `create_event.html` – Event creation form for staff
  - `layout.html` – Base template shared across all pages

- **static/styles.css**
  Contains styling rules to ensure a clean and consistent user interface.

- **README.md**
  Documentation explaining the project, design decisions, and usage.

---

## Design Decisions

Several design choices were made intentionally:

1. **Role-Based Access Control:**
   Students and staff have different permissions, ensuring security and logical separation of responsibilities.

2. **Password Hashing:**
   Passwords are never stored in plain text. Instead, secure hashing is used, following best practices introduced in the CS50 Finance problem set.

3. **Session-Based Authentication:**
   Flask sessions are used to track logged-in users securely, with a secret key protecting session data.

4. **Separate Dashboard and Events Pages:**
   The student dashboard focuses on registered events, while a separate events page allows browsing and registering for additional events, improving user experience.

5. **SQLite Database:**
   SQLite was chosen for its simplicity, portability, and suitability for small to medium-scale applications.

---

## Features

- Secure user authentication and session management
- Role-based dashboards for students and staff
- Event creation and management by staff
- Event registration and tracking for students
- Persistent data storage using SQLite
- Clean and responsive user interface

---

## Future Enhancements

- Add an admin role for managing staff accounts
- Prevent duplicate event registrations
- Add event capacity limits
- Allow staff to view registered students per event
- Enhance UI with notifications and success messages

---

## Project Metadata

- **Project Title:** Student Event Management System
- **Creator:** Sangavarapu Venkata Sai Siddardha
- **GitHub Username:** tmfsiddu
- **edX Username:** siddarth_22
- **City/Country:** Nellore, India
- **Date Recorded:** 23-12-2025

---

## Conclusion

The Student Event Management System demonstrates the practical application of web development concepts taught in CS50. By combining Flask, SQLite, and dynamic HTML rendering, the project delivers a functional, scalable, and user-friendly solution to a real-world problem. Its clear structure, role-based design, and persistent data handling make it a strong and complete final project for CS50x.
