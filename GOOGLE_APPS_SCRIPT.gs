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

  const emailTemplate = `
Hi there,

Thanks for taking the Growth Audit. Here's your personalized breakdown:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your Growth Audit Score: ${total}/50
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Acquisition:  ${acquisition}/14
Activation:   ${activation}/12
Conversion:   ${conversion}/12
Retention:    ${retention}/12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Where to start: ${focus.name}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${focus.msg}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to dig deeper? Let's talk.

Book a free 20-minute consultation to walk through your specific situation:
https://calendar.app.google/LXLo1623kmwa7NWr6

Looking forward to talking,
Divya
The Growth PMM
  `;

  MailApp.sendEmail(
    email,
    'Your Growth Audit Results: ' + total + '/50',
    emailTemplate,
    {
      name: 'The Growth PMM',
      replyTo: 'divya@thegrowthpmm.com'
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
