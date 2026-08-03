// Google Apps Script for Growth Audit Email Integration
// Deploy as: New → Deployment → Type: Web app → Execute as: Me → Allow: Anyone

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    // Validate required fields
    if (!data.email || typeof data.total === 'undefined') {
      return ContentService.createTextOutput(
        JSON.stringify({ success: false, error: 'Missing required fields' })
      ).setMimeType(ContentService.MimeType.JSON);
    }

    // Store in Google Sheet
    const sheet = SpreadsheetApp.getActiveSheet();
    const timestamp = new Date();
    sheet.appendRow([
      timestamp,
      data.email,
      data.acquisition || 0,
      data.activation || 0,
      data.conversion || 0,
      data.retention || 0,
      data.total || 0
    ]);

    // Send personalized audit email
    sendAuditEmail(data);

    return ContentService.createTextOutput(
      JSON.stringify({ success: true })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    console.error('Error:', error);
    return ContentService.createTextOutput(
      JSON.stringify({ success: false, error: error.toString() })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}

function sendAuditEmail(data) {
  const { email, acquisition, activation, conversion, retention, total } = data;

  // Determine primary recommendation
  const scores = [
    { name: 'Retention', score: retention, msg: 'Your biggest opportunity is in retention. Without an owner focused on churn and expansion, growth stays reactive. We'd build a retention strategy that turns existing customers into revenue drivers.' },
    { name: 'Activation', score: activation, msg: 'Activation is your constraint. Users aren't experiencing value early, so messaging won't move the needle. We'd focus on understanding where new customers get stuck, then fix that before scaling.' },
    { name: 'Conversion', score: conversion, msg: 'Your conversion process needs clarity. Without owned positioning and messaging, sales becomes inconsistent. We'd build repeatable conversion motion.' },
    { name: 'Acquisition', score: acquisition, msg: 'Acquisition is where you're stuck. Without clear positioning and GTM strategy, no channel scales. We'd start by defining exactly who you're for and how to reach them.' }
  ];

  scores.sort((a, b) => a.score - b.score);
  const focus = scores[0];

  const htmlTemplate = `
    <html>
      <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.6; color: #16180f; max-width: 600px; margin: 0 auto;">
        <div style="background: #f5f5f5; padding: 40px 20px;">
          <div style="background: white; border-radius: 12px; padding: 40px; box-shadow: 0 2px 8px rgba(22, 24, 15, 0.1);">

            <!-- Header -->
            <h1 style="margin: 0 0 8px; font-size: 28px; font-weight: 800; letter-spacing: -0.5px; color: #16180f;">Your Growth Audit: <span style="color: #DBFF00;">${total}/50</span></h1>
            <p style="margin: 0 0 32px; font-size: 16px; color: #726551;">Here's where you stand across the funnel:</p>

            <!-- Scores Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 0 0 32px;">
              <div style="background: #e7ebf5; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="font-size: 32px; font-weight: 800; color: #DBFF00; margin: 0 0 8px;">${acquisition}</div>
                <div style="font-size: 12px; font-weight: 700; color: #726551; text-transform: uppercase; letter-spacing: 0.5px;">Acquisition / 14</div>
              </div>
              <div style="background: #e7ebf5; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="font-size: 32px; font-weight: 800; color: #DBFF00; margin: 0 0 8px;">${activation}</div>
                <div style="font-size: 12px; font-weight: 700; color: #726551; text-transform: uppercase; letter-spacing: 0.5px;">Activation / 12</div>
              </div>
              <div style="background: #e7ebf5; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="font-size: 32px; font-weight: 800; color: #DBFF00; margin: 0 0 8px;">${conversion}</div>
                <div style="font-size: 12px; font-weight: 700; color: #726551; text-transform: uppercase; letter-spacing: 0.5px;">Conversion / 12</div>
              </div>
              <div style="background: #e7ebf5; border-radius: 8px; padding: 20px; text-align: center;">
                <div style="font-size: 32px; font-weight: 800; color: #DBFF00; margin: 0 0 8px;">${retention}</div>
                <div style="font-size: 12px; font-weight: 700; color: #726551; text-transform: uppercase; letter-spacing: 0.5px;">Retention / 12</div>
              </div>
            </div>

            <!-- Insight Box -->
            <div style="background: #e7ebf5; border-left: 4px solid #DBFF00; border-radius: 8px; padding: 24px; margin: 0 0 32px;">
              <p style="margin: 0 0 12px; font-size: 12px; font-weight: 700; color: #726551; text-transform: uppercase; letter-spacing: 0.8px;">Where to start: ${focus.name}</p>
              <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #16180f; font-weight: 500;">${focus.msg}</p>
            </div>

            <!-- CTA -->
            <div style="text-align: center; margin: 0 0 24px;">
              <a href="https://calendar.app.google/LXLo1623kmwa7NWr6" style="display: inline-block; background: #DBFF00; color: #16180f; padding: 14px 32px; border-radius: 24px; text-decoration: none; font-weight: 600; font-size: 16px;">Book a free 20-minute consultation</a>
            </div>

            <!-- Footer -->
            <div style="border-top: 1px solid #d6dcec; padding-top: 24px; text-align: center; color: #726551; font-size: 13px;">
              <p style="margin: 0;">Questions? Reply to this email or reach out to divya@thegrowthpmm.com</p>
              <p style="margin: 8px 0 0;">The Growth PMM</p>
            </div>
          </div>
        </div>
      </body>
    </html>
  `;

  MailApp.sendEmail(
    email,
    'Your Growth Audit Results: ' + total + '/50',
    'Your audit score is ' + total + '/50. Reply to see the formatted version.',
    {
      name: 'The Growth PMM',
      replyTo: 'divya@thegrowthpmm.com',
      htmlBody: htmlTemplate
    }
  );
}

// Utility: Get sheet headers (run once to set up)
function setupSheet() {
  const sheet = SpreadsheetApp.getActiveSheet();
  sheet.clear();
  sheet.appendRow([
    'Timestamp',
    'Email',
    'Acquisition',
    'Activation',
    'Conversion',
    'Retention',
    'Total Score'
  ]);
}
