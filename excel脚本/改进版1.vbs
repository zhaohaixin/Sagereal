'A光照片给名字命名为a'
'CWF光照片名字命名为cwf'
'd65光照片名字命名为d65'
'tl84光照片名字命名为tl84'
'gray照片名字命名为gray'
'huika光照片名字命名为huika'
'huika1光照片名字命名为huika1'

Private Sub CommandButton1_DblClick(ByVal Cancel As MSForms.ReturnBoolean)
'设定变量'
Dim Wbmain 	 As Workbook
Dim Wba 	 As Workbook
Dim Wbcwf 	 As Workbook
Dim Wbd65 	 As Workbook
Dim Wbtl84   As Workbook
Dim Wbgray   As Workbook
Dim Wbhuika  As Workbook
Dim num		 As Integer
Dim cout     As Integer
cout=0
'打开外部文件'
Set Wbmain 	= ThisWorkbook
Set Wba 	= Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\a\Results\a_summary.csv") '后台打开外部文件
Set Wbcwf 	= Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\cwf\Results\cwf_summary.csv") '后台打开外部文件
Set Wbd65 	= Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\d65\Results\d65_summary.csv") '后台打开外部文件
Set Wbtl84 	= Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\tl84\Results\tl84_summary.csv") '后台打开外部文件
Set Wbgray 	= Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\gray\Results\gray_summary.csv") '后台打开外部文件
Set Wbhuika = Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\huika\Results\huika_LFY.csv") '后台打开外部文件
Set Wbhuika1 = Workbooks.Open("C:\Users\Administrator\Desktop\cameratest\huika\Results\huika1_LFY.csv") '后台打开外部文件


'数据写入'
' 示例Wbmain.Sheets("Sheet1").Range("A2") = Wb2.Sheets("IMG_20150102_001600_LFY").Range("B14")
'A光色彩还原'

Wbmain.Sheets("Camera客观评测标准").Range("P11") = Wba.Sheets("a_summary").Range("B143")
Wbmain.Sheets("Camera客观评测标准").Range("P12") = Wba.Sheets("a_summary").Range("B145")
Wbmain.Sheets("Camera客观评测标准").Range("P13") = Wba.Sheets("a_summary").Range("B140")
Wbmain.Sheets("Camera客观评测标准").Range("P14") = Wba.Sheets("a_summary").Range("B142")
'CWF光色彩还原'
Wbmain.Sheets("Camera客观评测标准").Range("N11") = Wbcwf.Sheets("cwf_summary").Range("B143")
Wbmain.Sheets("Camera客观评测标准").Range("N12") = Wbcwf.Sheets("cwf_summary").Range("B145")
Wbmain.Sheets("Camera客观评测标准").Range("N13") = Wbcwf.Sheets("cwf_summary").Range("B140")
Wbmain.Sheets("Camera客观评测标准").Range("N14") = Wbcwf.Sheets("cwf_summary").Range("B142")

'D65光色彩还原'
Wbmain.Sheets("Camera客观评测标准").Range("M11") = Wbd65.Sheets("d65_summary").Range("B143")
Wbmain.Sheets("Camera客观评测标准").Range("M12") = Wbd65.Sheets("d65_summary").Range("B145")
Wbmain.Sheets("Camera客观评测标准").Range("M13") = Wbd65.Sheets("d65_summary").Range("B140")
Wbmain.Sheets("Camera客观评测标准").Range("M14") = Wbd65.Sheets("d65_summary").Range("B142")

'tl84光色彩还原'
Wbmain.Sheets("Camera客观评测标准").Range("O11") = Wbtl84.Sheets("tl84_summary").Range("B143")
Wbmain.Sheets("Camera客观评测标准").Range("O12") = Wbtl84.Sheets("tl84_summary").Range("B145")
Wbmain.Sheets("Camera客观评测标准").Range("O13") = Wbtl84.Sheets("tl84_summary").Range("B140")
Wbmain.Sheets("Camera客观评测标准").Range("O14") = Wbtl84.Sheets("tl84_summary").Range("B142")


'Saturation饱和度
Wbmain.Sheets("Camera客观评测标准").Range("P10") = Wba.Sheets("a_summary").Range("B136")&"%"
Wbmain.Sheets("Camera客观评测标准").Range("N10") = Wbcwf.Sheets("cwf_summary").Range("B136")&"%"
Wbmain.Sheets("Camera客观评测标准").Range("M10") = Wbd65.Sheets("d65_summary").Range("B136")&"%"
Wbmain.Sheets("Camera客观评测标准").Range("O10") = Wbtl84.Sheets("tl84_summary").Range("B136")&"%"


'白平衡'

'A光白平衡'
If CSng(Wba.Sheets("a_summary").cells(8,"J"))>CSng(Wba.Sheets("a_summary").cells(9,"J")) Then
	Wbmain.Sheets("Camera客观评测标准").Range("P20") = Wba.Sheets("a_summary").Range("J8")
	else
	Wbmain.Sheets("Camera客观评测标准").Range("P20") = Wba.Sheets("a_summary").Range("J9")
End If

'CWF光白平衡'
If CSng(Wbcwf.Sheets("cwf_summary").cells(8,"J"))>CSng(Wbcwf.Sheets("cwf_summary").cells(9,"J")) Then
	Wbmain.Sheets("Camera客观评测标准").Range("N18") = Wbcwf.Sheets("cwf_summary").Range("J8")
	else
	Wbmain.Sheets("Camera客观评测标准").Range("N18") = Wbcwf.Sheets("cwf_summary").Range("J9")
End If

'D65光白平衡'
If CSng(Wbd65.Sheets("d65_summary").cells(8,"J"))>CSng(Wbd65.Sheets("d65_summary").cells(9,"J")) Then
	Wbmain.Sheets("Camera客观评测标准").Range("M17") = Wbd65.Sheets("d65_summary").Range("J8")
	else
	Wbmain.Sheets("Camera客观评测标准").Range("M17") = Wbd65.Sheets("d65_summary").Range("J9")
End If

'tl84光白平衡'
If CSng(Wbtl84.Sheets("tl84_summary").cells(8,"J"))>CSng(Wbtl84.Sheets("tl84_summary").cells(9,"J")) Then
	Wbmain.Sheets("Camera客观评测标准").Range("O19") = Wbtl84.Sheets("tl84_summary").Range("J8")
	else
	Wbmain.Sheets("Camera客观评测标准").Range("O19") = Wbtl84.Sheets("tl84_summary").Range("J9")
End If

'Lens Shading'
Wbmain.Sheets("Camera客观评测标准").Range("M29") = CSng(Wbhuika.Sheets("huika_LFY").Range("B14"))&"%"

 'Color Shading; Max(R/G)'

If CSng(Wbhuika.Sheets("huika_LFY").cells(34,"B"))>CSng(Wbhuika1.Sheets("huika1_LFY").cells(34,"B")) Then
	Wbmain.Sheets("Camera客观评测标准").cells(31,"M")=1-CSng(Wbhuika.Sheets("huika_LFY").cells(34,"B"))
	else
	Wbmain.Sheets("Camera客观评测标准").cells(31,"M")=1-CSng(Wbhuika1.Sheets("huika1_LFY").cells(34,"B"))
End If

'imatest读取灰阶卡最亮值'

Wbmain.Sheets("Camera客观评测标准").Range("M33")=Wbgray.Sheets("gray_summary").Range("B9")

'SNR信噪比     
Wbmain.Sheets("Camera客观评测标准").Cells(24, "P") = Wba.Sheets("a_summary").Evaluate("Min(B49:E49)")
Wbmain.Sheets("Camera客观评测标准").Cells(24, "M") = Wbd65.Sheets("d65_summary").Evaluate("Min(B49:E49)")
Wbmain.Sheets("Camera客观评测标准").Cells(24, "N") = Wbcwf.Sheets("cwf_summary").Evaluate("Min(B49:E49)")
Wbmain.Sheets("Camera客观评测标准").Cells(24, "O") = Wbtl84.Sheets("tl84_summary").Evaluate("Min(B49:E49)")

'Kodak gray scale卡，相邻两阶亮度值差异'
For num=17 To 1 step -1
	If Wbgray.Sheets("gray_summary").cells(26-num,"B")-Wbgray.Sheets("gray_summary").cells(27-num,"B")>=8 Then
		cout=cout+1
	End If
Next num
Wbmain.Sheets("Camera客观评测标准").cells(27,"M") = cout

'关闭外部文件'
Wba.Close 		False '关闭外部文件
Wbcwf.Close 	False '关闭外部文件
Wbd65.Close 	False '关闭外部文件
Wbtl84.Close 	False '关闭外部文件
Wbgray.Close 	False '关闭外部文件
Wbhuika.Close 	False '关闭外部文件
Wbhuika1.Close	False '关闭外部文件

End Sub
