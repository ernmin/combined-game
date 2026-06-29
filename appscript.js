//To be used in Google Apps Script that is linked to the Google Sheets form

function sendRowToServer(e) {
  // CONFIGURATION
  var targetUrl = "https://stereo-estrogen-valid.ngrok-free.dev/webhook"; // Change this to your endpoint
  var targetSheetName = "Form responses 1";            // Change to your sheet name
  var approvedColumn = 9;                      // Column A (e.g., watch for edits here)

  var range = e.range;
  var sheet = range.getSheet();
  
// 1. Check if the edit happened on the correct sheet
  // 2. Check if the edit happened in the "Approved" column
  // 3. Check if the value typed is exactly '1'
  if (sheet.getName() === targetSheetName && 
      range.getColumn() === approvedColumn && 
      (String(e.value) === "1") || (String(e.value) === "0")) {
    
    var rowNumber = range.getRow();
    var lastColumn = sheet.getLastColumn();
    var cellValue = String(e.value)
    
    // Fetch the header row (to give Python the column names)
    var headers = sheet.getRange(1, 1, 1, lastColumn).getValues()[0];
    
    // Fetch ONLY the row that was just edited/approved
    var approvedRowData = sheet.getRange(rowNumber, 1, 1, lastColumn).getValues()[0];
    
    var payload = {
      "sheetName": sheet.getName(),
      "approvedRowIndex": rowNumber,
      "headers": headers,
      "rowData": approvedRowData,
      "cellValue": cellValue
    };
    
    var options = {
      "method" : "post",
      "contentType": "application/json",
      "payload" : JSON.stringify(payload),
      "muteHttpExceptions": true
    };
    
    // Send only the single row payload over ngrok
    try {
      UrlFetchApp.fetch(targetUrl, options);
    } catch(err) {
      Logger.log("Failed to send webhook: " + err.toString());
    }
  }
}