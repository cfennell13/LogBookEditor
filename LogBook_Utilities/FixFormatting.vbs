Option Explicit
Sub HIGHLIGHTER()
Dim sPos As Long, sLen As Long
Dim rng As Range
Dim findMe As String
Dim i As Integer
Dim t As Integer
Dim SearchArray

SearchArray = Array("ENGINE", "Airframe")

For t = 0 To UBound(SearchArray)

    Set rng = Range("B1:B10000")
    findMe = SearchArray(t)

    For Each rng In rng
        With rng
            If rng.Value Like "*" & findMe & "*" Then
                If Not rng Is Nothing Then
                    For i = 1 To Len(rng.Value)
                        sPos = InStr(i, rng.Value, findMe)
                        sLen = Len(findMe)

                        If (sPos <> 0) Then
                            rng.Characters(Start:=sPos, Length:=sLen).Font.Color = RGB(255, 0, 0)
                            rng.Characters(Start:=sPos, Length:=sLen).Font.Bold = True
                            i = sPos + Len(findMe) - 1
                        End If
                    Next i
                End If
            End If
        End With
    Next rng

Next t
End Sub
