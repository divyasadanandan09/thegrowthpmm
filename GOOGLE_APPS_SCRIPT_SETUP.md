# Growth Audit: email delivery setup

The quiz on the site scores the founder and shows results immediately. To also
email them the written audit and log submissions, wire up this Apps Script.
Until you do, the quiz still works end to end; it just does not send anything.

## 1. Sheet

1. Create a Google Sheet called **Growth Audit Responses**.
2. **Extensions > Apps Script**.
3. Delete the placeholder code, paste all of `GOOGLE_APPS_SCRIPT.gs`, save.
4. Select `setupSheet` in the function dropdown and press Run. Approve the
   permission prompt. This writes the header row.

## 2. Deploy

1. **Deploy > New deployment > Web app**.
2. Execute as: **Me**. Who has access: **Anyone**.
3. Deploy, then copy the `/exec` URL.

## 3. Point the site at it

Astro only exposes env vars to browser code when they are prefixed `PUBLIC_`.
Create `.env` in the project root:

```
PUBLIC_AUDIT_ENDPOINT=https://script.google.com/macros/s/YOUR_ID/exec
```

For the live site, add the same variable in the Cloudflare Pages project under
**Settings > Environment variables**, then redeploy. The value is visible in the
built JS, which is fine here: the endpoint only accepts writes and returns no data.

## 4. Test

Complete the quiz with a work email. You should get a mail titled
"Your Growth Audit: NN/50" and a new row in the sheet.

To test the script alone, without the site:

```bash
curl -L -X POST 'https://script.google.com/macros/s/YOUR_ID/exec' \
  -H 'Content-Type: text/plain;charset=utf-8' \
  -d '{"email":"you@yourcompany.com","acquisition":14,"activation":6,"conversion":3,"retention":7,"biggestGap":"Conversion"}'
```

`-L` matters. Apps Script redirects, and without it you will see a 302 and
assume it failed.

## Delivery is reported honestly (2026-08-05)

The page used to say "A full written version is on its way to you@company.com"
the moment the results rendered, whether or not the mail sent. It was a
fire-and-forget post behind a bare `catch`, so a broken script or an exhausted
sending quota meant the founder was told a lie and nobody found out.

Now:

- The script writes the sheet row **before** attempting the send, so a failed
  send never costs the lead.
- It checks `MailApp.getRemainingDailyQuota()` and wraps the send in try/catch.
- Column **I, "Emailed"**, records `sent` or `NOT SENT: <reason>` per row.
  Filter that column to find every audit that was scored but never delivered.
- The response is `{ok, emailed}`. The page reads it and only claims the mail is
  on its way when `emailed` is true. Otherwise it says it could not send and
  points the founder at divya@thegrowthpmm.com.
- A failed send also fires a GA4 event, `audit_email_failed`.

**Redeploy after pasting the new script**, and run `addEmailedColumn` once to add
the header to an existing sheet. Until you redeploy, the old script's response
has no `emailed` field, which the page treats as success, so it behaves exactly
as it does today. Nothing breaks in the meantime; you just do not get the
honest signal yet.

## Payload

| Field | Range |
|---|---|
| `email` | work email, validated on the client |
| `acquisition` | 0 to 14 |
| `activation` | 0 to 12 |
| `conversion` | 0 to 12 |
| `retention` | 0 to 12 |
| `biggestGap` | stage name, lowest percentage |

Total is derived server side, so the sheet cannot disagree with the email.

## Scoring caveat

The 12 questions match the Google Form this replaced. **The per-option weights
do not**: the form's key was not recoverable. The weights in
`src/components/GrowthAuditQuiz.astro` are the simplest set that produces the
documented maxima (14/12/12/12) and reproduces a real sent audit exactly
(9/7/7/6 = 29). If you still have the form's key, check it against those
weights before treating a single founder's score as authoritative. The stage
ranking, which drives the diagnosis, is far less sensitive to this than the
raw numbers are.

## Notes

- The site posts `Content-Type: text/plain` deliberately. Apps Script does not
  answer CORS preflight; text/plain is a simple request so the browser skips it.
  Switching to `application/json` will break submissions silently.
- Editing the script: **Deploy > Manage deployments >** pencil **> New version**.
  The URL stays the same.
- Diagnosis copy lives in two places, `DIAGNOSIS` in the `.gs` and `DIAG` in the
  Astro component. Change both together.
