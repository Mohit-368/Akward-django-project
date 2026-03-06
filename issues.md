# Akward — GitHub Issues & Contribution Scope

Copy each issue below and create it manually on your GitHub repository under the Issues tab.
Apply the mentioned labels to each issue before publishing.

---

## 🟢 GOOD FIRST ISSUES (Beginner Friendly)

---

### Issue #1
**Title:** Add character limit counter to the post creation form
**Label:** `good first issue` `enhancement`

**Description:**
Currently the post creation form has no visual indicator of how many characters the user has typed. Add a real time character counter below the description field that updates as the user types and warns them when approaching the limit.

**Expected Outcome:**
A live character counter is visible below the post description textarea on the post creation and edit form.

**Skills involved:** HTML, CSS, JavaScript, Django Templates

---

### Issue #2
**Title:** Improve error messages on login and registration pages
**Label:** `good first issue` `enhancement`

**Description:**
The current error messages on the login and registration pages are generic Django defaults. Improve them to be more user friendly, descriptive, and visually styled to match the existing UI.

**Expected Outcome:**
Clear, styled, and helpful error messages are shown for wrong password, unregistered email, and unverified account scenarios.

**Skills involved:** Django Forms, HTML, CSS

---

### Issue #3
**Title:** Add a back button to the post detail page
**Label:** `good first issue` `enhancement`

**Description:**
Users on the post detail page have no easy way to navigate back to the post feed. Add a styled back button that takes users back to the post list page.

**Expected Outcome:**
A back button is visible on the post detail page and navigates correctly to the post feed.

**Skills involved:** HTML, CSS, Django Templates

---

### Issue #4
**Title:** Improve mobile responsiveness of the post feed
**Label:** `good first issue` `bug`

**Description:**
The post feed layout does not render optimally on smaller screen sizes. Improve the CSS to ensure the feed is fully responsive and readable on mobile devices.

**Expected Outcome:**
The post feed renders cleanly on screen sizes 320px and above without horizontal scrolling or layout breaking.

**Skills involved:** CSS, Responsive Design

---

### Issue #5
**Title:** Add placeholder text to all form fields
**Label:** `good first issue` `enhancement`

**Description:**
Several form fields across the app lack placeholder text, making it unclear what input is expected. Add meaningful placeholder text to all input fields across registration, login, post creation, and profile edit forms.

**Expected Outcome:**
All form fields have descriptive placeholder text that guides the user on what to enter.

**Skills involved:** Django Forms, HTML

---

## 🟡 MEDIUM ISSUES (Intermediate)

---

### Issue #6
**Title:** Implement a likes system for posts
**Label:** `medium` `enhancement`

**Description:**
Add a like button to each post that allows authenticated users to like or unlike a post. The total like count should be visible on both the post list and post detail pages.

**Expected Outcome:**
Authenticated users can like and unlike posts. Like count updates dynamically and is stored in the database.

**Skills involved:** Django Models, Views, PostgreSQL, HTML, CSS

---

### Issue #7
**Title:** Add a comments section to post detail page
**Label:** `medium` `enhancement`

**Description:**
Allow authenticated users to leave comments on posts. Comments should be visible on the post detail page with the commenter's username and timestamp. Users should also be able to delete their own comments.

**Expected Outcome:**
A working comments section is present on the post detail page with add and delete functionality for authenticated users.

**Skills involved:** Django Models, Forms, Views, PostgreSQL, HTML, CSS

---

### Issue #8
**Title:** Implement user search functionality
**Label:** `medium` `enhancement`

**Description:**
Add a search bar to the post feed that allows users to search for posts by title or keyword. Results should be filtered and displayed dynamically on the same page.

**Expected Outcome:**
A functional search bar filters posts by title or content keywords and displays matching results on the feed.

**Skills involved:** Django ORM, Views, HTML, CSS

---

### Issue #9
**Title:** Add OTP expiry and resend OTP functionality
**Label:** `medium` `bug` `enhancement`

**Description:**
Currently OTPs do not expire after a set time and there is no option to resend an OTP if it was not received. Implement a 10 minute OTP expiry and add a resend OTP button on the verification page.

**Expected Outcome:**
OTPs expire after 10 minutes and users can request a new OTP from the verification page without re-registering.

**Skills involved:** Django, Python, Email Backend, Session Management

---

### Issue #10
**Title:** Add user follow and unfollow system
**Label:** `medium` `enhancement`

**Description:**
Allow users to follow and unfollow other users. A user's profile page should display their follower count and following count. A personalized feed showing posts from followed users should be accessible from the main navigation.

**Expected Outcome:**
Follow and unfollow functionality works correctly. Profile pages show follower and following counts. A following feed is accessible to authenticated users.

**Skills involved:** Django Models, Views, PostgreSQL, HTML, CSS

---

## 🔴 HARD ISSUES (Advanced)

---

### Issue #11
**Title:** Build a REST API using Django REST Framework
**Label:** `hard` `enhancement`

**Description:**
Expose the core functionality of Akward as a REST API using Django REST Framework. This includes endpoints for user registration, login, post CRUD operations, and profile management. All endpoints should be properly authenticated using token based authentication.

**Expected Outcome:**
A fully functional REST API is available with documented endpoints for all core features of the platform.

**Skills involved:** Django REST Framework, Token Authentication, API Design, PostgreSQL

---

### Issue #12
**Title:** Containerize the application using Docker
**Label:** `hard` `enhancement`

**Description:**
Create a Dockerfile and docker-compose.yml that containerizes the Django application along with PostgreSQL. The setup should allow any contributor to spin up the entire project with a single docker-compose up command without manual environment setup.

**Expected Outcome:**
A working Dockerfile and docker-compose.yml are present in the repository. The app and database run correctly inside Docker containers.

**Skills involved:** Docker, Docker Compose, PostgreSQL, Django

---

### Issue #13
**Title:** Deploy Akward to Render or Railway with CI/CD
**Label:** `hard` `enhancement`

**Description:**
Set up a production deployment of Akward on Render or Railway with a PostgreSQL database. Configure a GitHub Actions CI/CD pipeline that automatically runs tests and deploys on every push to the main branch.

**Expected Outcome:**
Akward is live on a public URL. A GitHub Actions workflow runs on every push to main, checks for errors, and deploys automatically on success.

**Skills involved:** Render or Railway, GitHub Actions, CI/CD, Django Production Settings

---

### Issue #14
**Title:** Add real time notifications using Django Channels
**Label:** `hard` `enhancement`

**Description:**
Implement real time notifications using Django Channels and WebSockets. Users should receive instant notifications when someone likes or comments on their post without needing to refresh the page.

**Expected Outcome:**
Real time notifications appear for authenticated users when their posts receive likes or comments.

**Skills involved:** Django Channels, WebSockets, Redis, JavaScript

---

## 📄 DOCUMENTATION ISSUES

---

### Issue #15
**Title:** Add screenshots and demo GIF to README
**Label:** `documentation` `good first issue`

**Description:**
The README currently has no visual preview of the application. Add screenshots of the home feed, post detail page, registration flow, and profile page. A short demo GIF of the core user flow would be a bonus.

**Expected Outcome:**
The README includes at least 4 screenshots and optionally a demo GIF showcasing the app.

**Skills involved:** Markdown, Screenshot tools

---
