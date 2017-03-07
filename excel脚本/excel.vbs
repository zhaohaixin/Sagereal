Private Sub CommandButton2_DblClick(ByVal Cancel As MSForms.ReturnBoolean)
    Dim wbmain   As Workbook
    Dim arr
    Dim i        As Integer
    Dim num      As Integer
    Set wbmain = ThisWorkbook
    Sheets("BOM比对").Range("A2:D60").ClearContents '清楚原先数据
    
    arrrow = wbmain.Sheets("规范使用量").Range("A65536").End(xlUp).Row '规范使用量1行数
    arr1row = wbmain.Sheets("规范使用量").Range("B65536").End(xlUp).Row '规范使用量不为1行数
    arr2row = wbmain.Sheets("规范使用量").Range("C65536").End(xlUp).Row '规范使用量固定行数
    rownum = Range("A65536").End(xlUp).Row '检测数据行数'
    arr = WorksheetFunction.Transpose(wbmain.Sheets("规范使用量").Range("a2:a" & arrrow).Value) '规范使用量1'
    arr1 = WorksheetFunction.Transpose(wbmain.Sheets("规范使用量").Range("b2:b" & arr1row).Value) '规范使用量不为1'
    arr2 = WorksheetFunction.Transpose(wbmain.Sheets("规范使用量").Range("c2:c" & arr2row).Value) '规范使用量固定'

    

    '规范使用量为1'
    For num = 1 To rownum - 1 Step 1

        For i = 1 To arrrow - 1 Step 1
        '判断检测关键词为1,num+1为所在单元格'
            If InStr(Cells(num + 1, 2), arr(i)) Then
                If Cells(num + 1, 3) <> 1 Then
                    'MsgBox (Cells(num + 1, 2) & "警告：不为 1 ！！")
                    wbmain.Sheets(1).Cells(num + 1, 4) = "错误"
                End If
            End If
        Next i
        '判断检测关键词不为1的'
        For i = 1 To arr1row - 1 Step 1
            If InStr(Cells(num + 1, 2), arr1(i)) Then
                If Cells(num + 1, 3) > 1 Or Cells(num + 1, 3) = 1 Then
                    'MsgBox (Cells(num + 1, 2) & "警告：不为 1 ！！")
                    wbmain.Sheets(1).Cells(num + 1, 4) = "错误"
                End If
            End If
        Next i
        '规范使用量固定的'
        For i = 1 To arr2row - 1 Step 1
            If InStr(Cells(num + 1, 2), arr2(i)) Then
                If Cells(num + 1, 3) <> wbmain.Sheets("规范使用量").Cells(i + 1, 4) Then
                    'MsgBox (Cells(num + 1, 2) & "警告：不为 1 ！！")
                    wbmain.Sheets(1).Cells(num + 1, 4) = "错误"
                End If
            End If
        Next i
    '步出单元格'
    Next num
    
End Sub