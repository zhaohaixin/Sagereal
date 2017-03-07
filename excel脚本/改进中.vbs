Private Sub CommandButton2_DblClick(ByVal Cancel As MSForms.ReturnBoolean)
    Dim wbmain   As Workbook
    Dim arr
    Dim i        As Integer
    Dim num      As Integer
    Set wbmain = ThisWorkbook
    arrrow = wbmain.Sheets("缺少项提醒").Range("A65536").End(xlUp).Row '缺少项
    rownum = Range("A65536").End(xlUp).Row '检测数据行数'
    arr = WorksheetFunction.Transpose(wbmain.Sheets("规范使用量").Range("a2:a" & arrrow).Value) '缺少项
    'Sheets(1).Range("D2:D26").ClearContents '清楚原先数据
    '缺少项'
    For num = 1 To rownum - 1 Step 1
        For i = 1 To arrrow - 1 Step 1 '缺少项个数循环
            If InStr(Cells(num + 1, 2), arr(i)) Then
                MsgBox (arr(i))
                Exit For
            End If
        Next i
    '步出单元格'
    Next num
End Sub