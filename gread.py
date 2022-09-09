import gspread
import sys

# Credentials [Keys etc]
credFileName = "credentials.json"

mServiceAccount = gspread.service_account(filename=credFileName)
#mGoogleSheetId = "12BAQpZSq6quewIY7hp4ia54ysClTrCJc7CPBcmx2dIs"
mGoogleSheetId = sys.argv[1].split('sheetname')[0]

#gs = sa.open("Test_JSON")
mGoogleSheet = mServiceAccount.open_by_key(mGoogleSheetId)

#if sys.argv[1] == "":
#sheetName = mGoogleSheet.worksheets()[0].title
if sys.argv[1].split('sheetname')[1] == "null":                   #checking if variable is None
    sheetName = mGoogleSheet.worksheets()[0].title
else :
    sheetName = sys.argv[1].split('sheetname')[1]

mSelectedWorkSheet = mGoogleSheet.worksheet(sheetName)

# Converting Data to Required JSON
print(mSelectedWorkSheet.get_all_records())
# for default sheet at 0
#print(mGoogleSheet.worksheets()[0].title) 




