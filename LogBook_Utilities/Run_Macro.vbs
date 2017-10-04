Option Explicit

Dim xlApp, xlBook

Set xlApp = CreateObject("Excel.Application")
'~~> Change Path here
Set xlBook = xlApp.Workbooks.Open("C:\Test.xls", 0, True)
xlApp.Run "Formatting_Macros.xlsm!HIGHLIGHTER"
xlBook.Close
xlApp.Quit

Set xlBook = Nothing
Set xlApp = Nothing

WScript.Echo "Finished."
WScript.Quit