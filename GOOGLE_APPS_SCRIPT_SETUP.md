# Google Apps Script Setup for Growth Audit Emails

## Overview
This Google Apps Script receives quiz responses from your website and:
1. Stores responses in a Google Sheet
2. Sends personalized audit emails to users
3. Provides a webhook endpoint for the quiz form

## Step 1: Create a Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new sheet named "Growth Audit Responses"
3. You'll use this to store audit results (the script will auto-create headers)

## Step 2: Create the Apps Script

1. In the same Google Sheet, click **Extensions → Apps Script**
2. Delete any default code in the editor
3. Paste the contents of `GOOGLE_APPS_SCRIPT.gs` (see file in repo)
4. Click **Save** (name it "Growth Audit Webhook")

## Step 3: Set Up the Sheet Headers

1. In the Apps Script editor, click the **▶️ Run** button next to `setupSheet()`
2. When prompted, click **Review permissions** → **Allow**
3. This creates the column headers in your sheet

## Step 4: Deploy as Web App

1. Click **Deploy** → **New deployment**
2. **Deployment type**: Select "Web app"
3. **Execute as**: Your Google account
4. **Who has access**: Select "Anyone"
5. Click **Deploy**
6. Copy the **Deployment URL** (looks like: `https://script.google.com/macros/s/ABC123.../usercontent`)
7. **This is your webhook endpoint**

## Step 5: Configure Your Website

1. Add the deployment URL to your site's environment:
   - **For Cloudflare Pages**: Add to `wrangler.jsonc` or `.env`:
     ```
     VITE_AUDIT_ENDPOINT = "https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/usercontent"
     ```

2. Or update the quiz component directly in `src/components/GrowthAuditQuiz.astro`:
   ```javascript
   const endpoint = 'https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/usercontent';
   ```

## Step 6: Test the Flow

1. Go to your website's Growth Audit quiz
2. Answer all 5 questions
3. Enter your test email
4. Click "Get Your Audit"
5. **Check your inbox** — you should receive an email with:
   - Your audit score breakdown (0-50)
   - Scores by funnel stage (Acquisition, Activation, Conversion, Retention)
   - Personalized recommendation on where to start
   - CTA to book a call

## What Gets Stored

**Google Sheet columns:**
- Timestamp
- Email
- Acquisition score (0-14)
- Activation score (0-12)
- Conversion score (0-12)
- Retention score (0-12)
- Total score (0-50)

## Optional: Customize Email Template

Edit the `emailTemplate` in the `sendAuditEmail()` function to:
- Change the subject line format
- Adjust the tone or copy
- Add your own branding footer
- Include links to specific resources

## Troubleshooting

**"Permission denied" errors:**
- Make sure you ran `setupSheet()` and granted permissions
- Check that you deployed as "Web app" with "Anyone" access

**Emails not sending:**
- Verify the email is valid
- Check Apps Script logs (View → Logs)
- Ensure your Google account allows mail sending

**Quiz doesn't submit:**
- Check browser console (F12) for errors
- Verify the deployment URL is correct
- Test with `curl`:
  ```bash
  curl -X POST 'https://script.google.com/macros/s/YOUR_ID/usercontent' \
    -H 'Content-Type: application/json' \
    -d '{"email":"test@example.com","acquisition":10,"activation":8,"conversion":7,"retention":6,"total":31}'
  ```

## Updates

If you modify the Google Apps Script:
1. Click **Deploy** → **Manage deployments**
2. Click the pencil icon on your deployment
3. Click **Create new version**
4. The URL stays the same; the new version auto-activates

## Rollback

To revert to a previous version:
1. **Deploy** → **Manage deployments**
2. Click the version number dropdown and select an older version
