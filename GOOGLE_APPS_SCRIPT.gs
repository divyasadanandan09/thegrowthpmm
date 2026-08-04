/**
 * Growth Audit webhook.
 *
 * Receives a submission from the on-site quiz, appends it to the bound sheet,
 * and emails the founder their audit.
 *
 * Deploy: Extensions > Apps Script > Deploy > New deployment > Web app,
 * "Execute as: Me", "Who has access: Anyone". Run setupSheet() once first.
 *
 * The site posts with Content-Type text/plain on purpose. Apps Script does not
 * answer CORS preflight, and text/plain is a "simple request", so the browser
 * skips preflight entirely. Do not change it to application/json.
 */

var STAGES = [
  { key: 'acquisition', name: 'Acquisition', max: 14 },
  { key: 'activation',  name: 'Activation',  max: 12 },
  { key: 'conversion',  name: 'Conversion',  max: 12 },
  { key: 'retention',   name: 'Retention',   max: 12 }
];

var BOOKING = 'https://calendar.app.google/LXLo1623kmwa7NWr6';

// Kept in step with the copy in src/components/GrowthAuditQuiz.astro.
var DIAGNOSIS = {
  Acquisition: {
    read: "You are spending into channels without a clean read on which ones pay back. That is why adding budget has stopped adding growth.",
    cause: "No one owns the channel portfolio, so channels get added and never retired. Blended CAC hides the losers inside the average.",
    move: "Split CAC by channel for the last 90 days, then cut or cap the worst performer for one full cycle and watch what happens to pipeline."
  },
  Activation: {
    read: "New users are not reliably reaching value, so everything you spend on acquisition leaks straight back out.",
    cause: "The activation moment is not defined in writing, so Product, Marketing, and Support are each optimising for a different finish line.",
    move: "Write down the single action that marks a user as activated, then measure what share of signups hit it within their first week."
  },
  Conversion: {
    read: "Deals are turning on the individual rep and the individual conversation rather than on a story that holds up every time.",
    cause: "Positioning and messaging have no owner, so each rep rebuilds the pitch themselves and loss reasons never get written down.",
    move: "Write up the last five lost deals in one page. The repeated objection is your messaging gap, and it is usually fixable in a week."
  },
  Retention: {
    read: "Retention is being handled reactively. You find out about churn once it has already happened, and expansion is left on the table.",
    cause: "Retention sits between Sales and CS, so no one is accountable for it and expansion revenue never gets a real number.",
    move: "Give retention one named owner, then track expansion revenue as a hard number rather than an estimate for one quarter."
  }
};

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    if (!data.email) {
      return json({ ok: false, error: 'missing email' });
    }

    var scored = STAGES.map(function (s) {
      var score = Number(data[s.key]) || 0;
      return { name: s.name, score: score, max: s.max, pct: score / s.max };
    });

    var total = scored.reduce(function (sum, s) { return sum + s.score; }, 0);

    SpreadsheetApp.getActiveSheet().appendRow([
      new Date(), data.email,
      scored[0].score, scored[1].score, scored[2].score, scored[3].score,
      total, data.biggestGap || ''
    ]);

    sendAuditEmail(data.email, scored, total);
    return json({ ok: true });
  } catch (err) {
    console.error(err);
    return json({ ok: false, error: String(err) });
  }
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function statusOf(pct) {
  if (pct >= 0.75) return { label: 'Healthy', color: '#7a9a00' };
  if (pct >= 0.50) return { label: 'At risk', color: '#b07d00' };
  return { label: 'Leaking', color: '#cc4117' };
}

function sendAuditEmail(email, scored, total) {
  var ranked = scored.slice().sort(function (a, b) { return a.pct - b.pct; });
  var worst = ranked[0];
  var second = ranked[1];
  var d = DIAGNOSIS[worst.name];

  var verdict = total >= 40
    ? 'Your funnel is in good shape. The gains left are specific, not structural.'
    : total >= 28
      ? 'The foundations are there. One stage is holding the rest of the funnel back.'
      : 'Growth is leaking in more than one place, and the stages are compounding on each other.';

  // Tables, not flex or grid. Outlook ignores modern layout.
  //
  // The bar cells carry width= and bgcolor= as HTML attributes, not just CSS.
  // Gmail collapsed an earlier CSS-only version to zero width, so the bars
  // vanished while the numbers still showed. Keep the attributes.
  var rows = scored.map(function (s) {
    var st = statusOf(s.pct);
    var filled = Math.max(2, Math.round(s.pct * 100)); // 2% floor so a near-zero score still reads as a bar
    var rest = 100 - filled;
    var cell = 'style="line-height:12px;font-size:12px;height:12px;"';
    return '' +
      '<tr>' +
        '<td width="105" style="padding:9px 0;font:600 14px Arial,sans-serif;color:#16180f;">' + s.name + '</td>' +
        '<td style="padding:9px 12px;">' +
          '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;table-layout:fixed;">' +
            '<tr>' +
              '<td width="' + filled + '%" bgcolor="' + st.color + '" ' + cell + '>&nbsp;</td>' +
              (rest > 0 ? '<td width="' + rest + '%" bgcolor="#e7ebf5" ' + cell + '>&nbsp;</td>' : '') +
            '</tr>' +
          '</table>' +
        '</td>' +
        '<td width="70" style="padding:9px 0;font:700 13px Arial,sans-serif;color:#16180f;text-align:right;">' +
          s.score + '/' + s.max +
          '<div style="font:700 11px Arial,sans-serif;color:' + st.color + ';">' + st.label + '</div>' +
        '</td>' +
      '</tr>';
  }).join('');

  var html = '' +
  '<div style="background:#eef0f7;padding:32px 16px;">' +
    '<div style="max-width:600px;margin:0 auto;background:#ffffff;border-radius:16px;padding:36px;font-family:Arial,sans-serif;">' +
      '<p style="margin:0;font:700 12px Arial,sans-serif;color:#5f6470;">YOUR GROWTH AUDIT</p>' +
      '<h1 style="margin:4px 0 0;font-size:44px;line-height:1;color:#16180f;">' + total +
        '<span style="font-size:22px;color:#5f6470;">/50</span></h1>' +
      '<p style="margin:14px 0 0;font:600 16px Arial,sans-serif;color:#16180f;line-height:1.5;">' + verdict + '</p>' +

      '<table role="presentation" cellpadding="0" cellspacing="0" style="width:100%;margin:26px 0 0;">' + rows + '</table>' +

      '<div style="margin:28px 0 0;background:#e7ebf5;border-left:4px solid #DBFF00;border-radius:12px;padding:22px;">' +
        '<p style="margin:0;font:700 11px Arial,sans-serif;color:#5f6470;letter-spacing:.8px;">YOUR BIGGEST GAP</p>' +
        '<h2 style="margin:8px 0 0;font-size:20px;color:#16180f;">' + worst.name + ', at ' + worst.score + ' out of ' + worst.max + '</h2>' +
        '<p style="margin:8px 0 0;font-size:15px;line-height:1.6;color:#16180f;">' + d.read + '</p>' +
        '<p style="margin:18px 0 0;font:700 11px Arial,sans-serif;color:#5f6470;letter-spacing:.8px;">LIKELY ROOT CAUSE</p>' +
        '<p style="margin:6px 0 0;font-size:15px;line-height:1.6;color:#16180f;">' + d.cause + '</p>' +
        '<p style="margin:18px 0 0;font:700 11px Arial,sans-serif;color:#5f6470;letter-spacing:.8px;">YOUR FIRST MOVE</p>' +
        '<p style="margin:6px 0 0;font-size:15px;line-height:1.6;color:#16180f;">' + d.move + '</p>' +
        '<p style="margin:20px 0 0;padding-top:14px;border-top:1px solid #d6dcec;font-size:14px;line-height:1.55;color:#5f6470;">' +
          'Second priority: ' + second.name + ', at ' + second.score + ' out of ' + second.max +
          '. Fix ' + worst.name + ' first. Moving it usually lifts ' + second.name + ' on its own.</p>' +
      '</div>' +

      '<div style="text-align:center;margin:30px 0 0;">' +
        '<p style="margin:0 0 16px;font:600 15px Arial,sans-serif;color:#16180f;">Every one of these is fixable. The fastest way through is 20 minutes on a call.</p>' +
        '<a href="' + BOOKING + '" style="display:inline-block;background:#DBFF00;color:#16180f;padding:15px 32px;border-radius:99px;text-decoration:none;font:700 16px Arial,sans-serif;">Book your free consultation</a>' +
      '</div>' +

      '<p style="margin:28px 0 0;padding-top:18px;border-top:1px solid #d6dcec;text-align:center;font-size:13px;color:#5f6470;">' +
        'Divya Sadanandan, The Growth PMM<br>Reply here or write to divya@thegrowthpmm.com</p>' +
    '</div>' +
  '</div>';

  var plain = [
    'Your Growth Audit: ' + total + '/50',
    '',
    verdict,
    ''
  ].concat(scored.map(function (s) {
    return s.name + ': ' + s.score + '/' + s.max + ' (' + statusOf(s.pct).label + ')';
  })).concat([
    '',
    'Your biggest gap: ' + worst.name + ', at ' + worst.score + ' out of ' + worst.max,
    d.read,
    '',
    'Likely root cause: ' + d.cause,
    '',
    'Your first move: ' + d.move,
    '',
    'Second priority: ' + second.name + ', at ' + second.score + ' out of ' + second.max + '.',
    '',
    'Book a free 20-minute consultation: ' + BOOKING,
    '',
    'Divya Sadanandan, The Growth PMM'
  ]).join('\n');

  MailApp.sendEmail(email, 'Your Growth Audit: ' + total + '/50', plain, {
    name: 'The Growth PMM',
    replyTo: 'divya@thegrowthpmm.com',
    htmlBody: html
  });
}

/** Run once to write the header row. */
function setupSheet() {
  SpreadsheetApp.getActiveSheet()
    .appendRow(['Timestamp', 'Email', 'Acquisition', 'Activation', 'Conversion', 'Retention', 'Total', 'Biggest gap']);
}
