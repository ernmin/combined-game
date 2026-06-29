# combined-game
Game Idea for photo human bingo

1. Do the player registration using jotform. The players will key in their name and they will receive a unique ID\

2. Once all players have registered, download as csv and put the csv in the combined-game folder.\

3. Once that CSV is read into pandas, programmatically add in 10 columns to indicate if a photo has been completed.\

4. Using google forms, players will submit photos according to the criteria and photos containing 2-5 players\

5. 2 Administrators will check if the photo is approved. If so then they will change the approved column to 1

6. When the approved column is changed to 1 then that row data will be sent to the server to be transformed and processed into a pandas row. That row will be changed into a list of dictionaries to be added to the JSON file.\

7. If the administrators change a column to 0, all the entries that are linked to that photo will be deleted but the photo will still remain in Google Drive.\

8. In order to display names on the Tableau Workbook and only display the names that are registered in the Jotform, I need to LEFT JOIN the Jotform csv to ignore all the IDs that are input wrongly.
