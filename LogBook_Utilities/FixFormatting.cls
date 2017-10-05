Sub Auto_Open()
Dim sPos As Long, sLen As Long
Dim rng As Range
Dim findMe As String
Dim i As Integer
Dim t As Integer
Dim Red_Bold
Dim Blue_Bold
Dim Black_Bold
Dim celltxt As String

Red_Bold = Array("S/N17210077")
Blue_Bold = Array("C172S")
Black_Bold = Array("AIRFRAME", "ENGINE", "PROPELLER")

celltxt = ActiveSheet.Range("K2").Text
If InStr(1, celltxt, "0") Then
For t = 0 To UBound(Red_Bold)

    Set rng = Range("B1:B10000")
    findMe = Red_Bold(t)

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

For t = 0 To UBound(Blue_Bold)

    Set rng = Range("B1:B10000")
    findMe = Blue_Bold(t)

    For Each rng In rng
        With rng
            If rng.Value Like "*" & findMe & "*" Then
                If Not rng Is Nothing Then
                    For i = 1 To Len(rng.Value)
                        sPos = InStr(i, rng.Value, findMe)
                        sLen = Len(findMe)

                        If (sPos <> 0) Then
                            rng.Characters(Start:=sPos, Length:=sLen).Font.Color = RGB(0, 0, 255)
                            rng.Characters(Start:=sPos, Length:=sLen).Font.Bold = True
                            i = sPos + Len(findMe) - 1
                        End If
                    Next i
                End If
            End If
        End With
    Next rng

Next t

For t = 0 To UBound(Black_Bold)

    Set rng = Range("B1:B10000")
    findMe = Black_Bold(t)

    For Each rng In rng
        With rng
            If rng.Value Like "*" & findMe & "*" Then
                If Not rng Is Nothing Then
                    For i = 1 To Len(rng.Value)
                        sPos = InStr(i, rng.Value, findMe)
                        sLen = Len(findMe)

                        If (sPos <> 0) Then
                            rng.Characters(Start:=sPos, Length:=sLen).Font.Bold = True
                            i = sPos + Len(findMe) - 1
                        End If
                    Next i
                End If
            End If
        End With
    Next rng

Next t

Range("K2").Value = Null
End If
End Sub
