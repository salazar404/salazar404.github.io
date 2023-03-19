#!/usr/bin/env python

import cgi
import hashlib

# Generate a SHA256 hash of the password for secure storage
password_hash = hashlib.sha256("mypassword".encode()).hexdigest()

# Check if the form was submitted
form = cgi.FieldStorage()
if "link" in form and "password" in form:
    # Check if the password is correct
    if form["password"].value == "mypassword":
        # Save the link to a file
        with open("links.txt", "a") as f:
            f.write(form["link"].value + "\n")
        print("Content-type: text/html\n")
        print("<html><head><title>Links</title></head><body>")
        print("<h1>Links</h1>")
        # Read the links from the file and display them
        with open("links.txt", "r") as f:
            for line in f:
                print("<p>" + line.strip() + "</p>")
        print("</body></html>")
    else:
        # Display an error message if the password is incorrect
        print("Content-type: text/html\n")
        print("<html><body>")
        print("<h1>Access Denied</h1>")
        print("<p>Invalid password. Please try again.</p>")
        print("</body></html>")
else:
    # Display the form if it hasn't been submitted
    print("Content-type: text/html\n")
    print("<html><body>")
    print("<h1>Submit a Link</h1>")
    print("<form method='POST'>")
    print("<label for='link'>Link:</label>")
    print("<input type='url' name='link' id='link' required>")
    print("<br>")
    print("<label for='password'>Password:</label>")
    print("<input type='password' name='password' id='password' required>")
    print("<br>")
    print("<input type='submit' value='Submit'>")
    print("</form>")
    print("</body></html>")
