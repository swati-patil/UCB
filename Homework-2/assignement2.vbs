Sub calculateTotal():
    Dim tickerName As String
    Dim total As Double
    total = 0
    
    Dim summaryRowTable As Integer
    summaryRowTable = 2
    For Each ws In Worksheets
        wsName = ws.Name
        lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        ws.Range("J1").Value = "Ticker"
        ws.Range("L1").Value = "Total Stock Volume"
        For i = 2 To lastRow
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                tickerName = ws.Cells(i, 1).Value
                total = total + ws.Cells(i, 7).Value
                ws.Range("J" & summaryRowTable).Value = tickerName
                ws.Range("L" & summaryRowTable).Value = total
                total = 0
                summaryRowTable = summaryRowTable + 1
            Else
                ' Add to the Total
                total = total + ws.Cells(i, 7).Value
            End If
        Next i
        total = 0
        summaryRowTable = 2
    Next ws
End Sub

