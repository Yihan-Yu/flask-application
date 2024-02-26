
# Instructions

This is a Flask application with some of the code already written for you.

You will see that the index page, defined in the `index()` function in app.py
is rendering a template with a form. The form accepts a name, an email, and a
message. 

## Your task

In app.py, your task is to write code that handles the form data submission. This should be
done in the function `submit_page()`. The `submit_page()` function should:
* be associated with the URL path `/submit-page`
* accept both GET and POST requests
* extract data from the form fields (user_name and user_email) using request.form, when a POST request is received (which typically happens when a form is submitted)
* render another HTML template named "results.html" and pass the name and email variables to the template

Then in results.html, your task is to write a conditional statement that checks if the length of the name variable is zero (i.e., if it's an empty string). If true, it displays a message saying "An error occurred. Please enter a name."
If the condition is false (i.e., if the name is not empty), it should show the following message:

> Thanks for your message, [name]. We will get back to you shortly at [email].

_Note: [name] and [email] should be replaced by the name and email address submitted by the user through the form._
