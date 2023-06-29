# Daily Wisdom Email Notification
This project deploys a Google Cloud Function that sends an email each morning at 9 AM with a random cool and positive sentence generated by the ChatGPT API.

## Prerequisites
* Google Cloud account with billing enabled.
* OpenAI API Key.
* Gmail account for sending emails

## Setting up Gmail for sending emails
1. Go to [Google Account main page](https://myaccount.google.com/), scroll down to the 2FA authentication and activate it. 
2. In the 2FA page scroll down to "App Password" and generate one, you will need it in the "your-password" field later

## Deploying on Cloud
1. Navigate to the Google Cloud Console.
2. Create a new project.
3. Enable the Cloud Functions and Cloud Scheduler APIs for your project.
4. Navigate to the Cloud Functions section and click "Create Function".
5. Name the function, select 1st gen, select "HTTP" trigger, and set "Allow unauthenticated invocations".
6. Save the URL of the deployment
7. In the "Source code" section, copy-paste both the code of the main.py and requirements.txt file.
8. Edit the following texts:
   1. "your-api-key" (openAI key)
   2. "sender@gmail.com"
   3. "your-password" (created before)
   4. "receiver@gmail.com"
9. Set the Runtime to Python 3.10 (or the latest version available).
10. In the "Entry point" field, enter hello_http.
11. Click "Deploy" to deploy the function.

You can test if the function works going the "Test" section

## Setting Up the Scheduler
1. Navigate to the Cloud Scheduler section in the Google Cloud Console.
2. Click "Create Job".
3. Enter a name for the job and the frequency (0 9 * * 1-5 for 9 AM on weekdays).
4. In the "Target" section, select "HTTP".
5. In the "URL" field, enter the URL of your deployed cloud function (saved before).
6. Set "HTTP Method" to "GET".
7. Click "Create" to create the job.

## Important Notes
As said, you need to replace placeholders in the code with your actual OpenAI API key, sender's email, sender's email password, and recipient's email.
You might need to enable less secure apps to access your Gmail account, generate an App Password if 2-Step Verification is enabled, or display an unlock captcha to allow sending emails through Python's smtplib.
Ensure your Google Cloud account has billing enabled, even if the Cloud Functions and Cloud Scheduler APIs are part of the free tier they're needed.
Troubleshooting
If the function is not working as expected, check the function's logs in the Google Cloud Console. This should provide information on any errors that are occurring. The most common issues are incorrect OpenAI API keys, Gmail credentials, or not allowing less secure apps in the Gmail settings.
