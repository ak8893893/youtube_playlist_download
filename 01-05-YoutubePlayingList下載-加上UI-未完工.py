"""
Title : YoutubePlayingList 下載器
Author : AK
Time : 2022/11/13
"""
from pytube import YouTube
from pytube import Playlist
import tkinter as tk                                      # 匯入 GUI 製作所需的 tkinter 函式庫
from PIL import ImageTk,Image                             # 從 PIL(pillow) 函式庫匯入 ImageTk,Image 函式庫
import tkinter.messagebox as tkbox                        # 匯入 彈出式式窗 的函示庫 tkbox
import tkinter as tk                                                       # tkinter 函式庫，用來做GUI視窗
from PIL import Image,ImageTk                                              # PIL函式庫，用來導入圖片放到GUI中
from tkinter import ttk                                                    # tkinter 中的 ttk 函式庫,用來做各種功能的GUI
from tkinter.scrolledtext import ScrolledText                              # 用來做多行輸入框的
import matplotlib.pyplot as plt                                            # 繪製圖表的函式庫
import tkinter.messagebox                                                  # 彈出式視窗函式庫
from openpyxl import Workbook,load_workbook
import matplotlib.pylab as pylab                                           # 設定圖表視窗title的函式庫

# # 定義 下載的函式
# def downloadList():
#     # yt下載區塊
#     url = input("請入輸入要下載的播放清單網址: ")                                    # 放入你的撥放清單網址
#     downloadPath = input("請輸入下載後的資料夾名稱: ")                           # 輸入下載後的檔案要存放的位置
#     playlist = Playlist(url)
#     videolist = playlist.video_urls
#     pathdir = downloadPath                      # 下載後的檔案要存放的位置
#     for video in videolist:
#         yt = YouTube(video)
#         yt.streams.filter(subtype='mp4', res='720p', progressive=True).first().download(pathdir)

# 定義 彈出式式窗 showInofY
def showInfoY():
    tkbox.showinfo("購物狀況","已放入購物車")

# 定義 彈出式式窗 showInofN
def showInfoN():
    tkbox.showinfo("購物狀況","未加入購物車")

# 定義 放入購物車的命令
def buy1():
    a = tkbox.askyesno("購物確認","確定放入購物車")
    if a == True:
        showInfoY()

        global good1
        good1 += 1
    elif a == False:
        showInfoN()

# 定義 建立第二視窗物件(moreInfo)的函式
def secnodWin():
    print("btn2 pressed.")

    # 建立一個新的視窗物件
    win2 = tk.Tk()                                         # 建立視窗物件 win2

    # 將第二視窗 要顯示出來的資料放入
    labelInfo = tk.Label(win2,text="iphone13 手機殼\n"      # 建立產品資訊標籤  並輸入文字資訊
                                   " 庫存仍有: 34  件\n"
                                   " 已售出: 130 件\n"
                                   "支付方式有:\n"
                                   "PChomePay支付連\n"
                                   "7-11取貨付款\n"
                                   "銀行或郵局轉帳\n"
                                   "全家取貨付款 65 元\n"
                                   "郵寄寄送 45 元")
    labelInfo.pack()                                        # 置中於視窗中間

    win2.mainloop()                                         # 第二視窗主循環

# 顯示更多資訊的按鈕功能
def showMore():
    tkbox.showinfo("商品資訊","此產品來自於美國")
    secnodWin()

# 定義購物車按鈕功能 -> 顯示購物車視窗
def cartBtn():
    print("shopcart pressed")
    print(good1)
    # 建立第二個視窗物件
    win3 = tk.Toplevel()                                    # 建立視窗物件 win2 Tk()只能調用一次，第二個和以後要用Toplevel()
    win3.title(string="購物車內容")                          # 設定 title
    win3.resizable(width=True,height=True)                 # 設定可否調整大小
    win3.maxsize(580,580)                                  # 設定最大尺寸
    win3.minsize(580,580)                                  # 設定最小尺寸

    # 加上好看的背景圖片
    cartBg = Image.open("buycartBg.png")                    # 讀取 iphone13Case.png 放入 productImg 這個變數中
    cartBg = cartBg.resize((580, 580), Image.ANTIALIAS)     # 調整產品圖片大小
    cartBg = ImageTk.PhotoImage(cartBg)                     # 把要放入視窗的圖邊資訊都放入 productImg 這個變數裡面
    labelcarBg = tk.Label(win3,image=cartBg)                # 將 productImg 放入 win3 這個視窗中
    labelcarBg.place(x=0, y=0)                              # 調整 productImg 要出現的位置

    # 購物車視窗 要顯示出來的資料放入
    labelInfo = tk.Label(win3,text="購買數量: ",bg="#FFFFFF",font=("標楷體",20))
    labelInfo.place(x=150,y=60)

    # 購物車視窗產品圖片
    productImg = Image.open("iphone13Case.png")  # 讀取 iphone13Case.png 放入 productImg 這個變數中
    productImg = productImg.resize((125, 250), Image.ANTIALIAS)  # 調整產品圖片大小
    productImg = ImageTk.PhotoImage(productImg)  # 把要放入視窗的圖邊資訊都放入 productImg 這個變數裡面
    label1 = tk.Label(win3, image=productImg)  # 將 productImg 放入 win 這個視窗中
    label1.place(x=0)  # 調整 productImg 要出現的位置

    # 加入勾選按鈕
    l = tk.Label(win3, bg='white', width=20, text='請勾選要執行的動作',font=("標楷體",14))
    l.place(x=130,y=150)
    def print_selection():
        if (var1.get() == 1) & (var2.get() == 0):
            l.config(text='我想購買 ')
        elif (var1.get() == 0) & (var2.get() == 1):
            l.config(text='我想刪除')
        elif (var1.get() == 0) & (var2.get() == 0):
            l.config(text='請勾選要執行的動作')
        else:
            l.config(text='我正在猶豫')
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(win3, text='購買', variable=var1, onvalue=1, offvalue=0, command=print_selection,bg="#FFFFFF",font=("標楷體",16))
    c1.place(x=150,y=100)
    c2 = tk.Checkbutton(win3, text='刪除', variable=var2, onvalue=1, offvalue=0, command=print_selection,bg="#FFFFFF",font=("標楷體",16))
    c2.place(x=230,y=100)

    # 定義確認按鈕的回報結果Y
    def confirmInfoY():  # 定義 彈出式式窗 showInofY
        tkbox.showinfo("購物狀況", "已執行選定的動作")

    # 定義確認按鈕的回報結果N
    def confirmInfoN():  # 定義 彈出式式窗 showInofN
        tkbox.showinfo("購物狀況", "未執行選定的動作")

    # 定義 確認按鈕的功能
    def confirm():
        a = tkbox.askyesno("購物確認", "確定執行? ")
        if a == True:
            confirmInfoY()
            return True

        elif a == False:
            confirmInfoN()

    # 加入確認按鈕
    btnConfirm = tk.Button(win3, text="確認",bg="#99D9EA",command=confirm,font=("標楷體",16))  # 建立 button ，文字="press me"按下後執行 event1
    btnConfirm.place(x=190, y=190)

    # 加入 +1 -1 按鈕
    good1Num = tk.StringVar()
    good1Num.set(int(good1))

    # 定義 +1 按鈕的功能
    def plus_():
        global good1
        good1 = good1 + 1
        good1Num.set(int(good1))

    # 定義 -1 按鈕的功能
    def min_():
        global good1
        good1 = good1 - 1
        good1Num.set(int(good1))

    # 放置+1-1按鈕和數量標籤
    labelgood1Num = tk.Label(win3,text="textvariable有優先權",textvariable=good1Num,bg="#FFFFFF",font=("標楷體",22))    # 顯示購物車內的商品數量
    labelgood1Num.place(x=278,y=62)
    bt_plus = tk.Button(win3, text='+1', command=plus_,font=("標楷體",16),bg="#A9DAD5")
    bt_plus.place(x=170,y=10)
    bt_min = tk.Button(win3, text='-1', command=min_,font=("標楷體",16),bg="#A9DAD5")
    bt_min.place(x=250,y=10)

    # 第三視窗 (購物車視窗) 主循環
    win3.mainloop()

# 購物程式的主視窗
win = tk.Tk()

# 設定視窗基本設定
win.title(string="Youtube 播放清單下載器 ver 1.0  by AK")    # 視窗名稱 為 產品敘述
win.resizable(height=True,width=True)                      # 設定 可 更改視窗大小
win.maxsize(width=802,height=502)                          # 視窗最寬為 800 最高為 500
win.minsize(width=800,height=500)                          # 視窗最窄為 600  最矮為 400
#
# # 放入按鈕圖片 buy
# imgBuy = Image.open("new_purchase-512.webp")
# imgBuy = imgBuy.resize((40,40),Image.ANTIALIAS)
# imgBuy = ImageTk.PhotoImage(imgBuy)
#
# # 放入按鈕圖片 info
# imgInfo = Image.open("infoButton.jpg")
# imgInfo = imgInfo.resize((100,40),Image.ANTIALIAS)
# imgInfo = ImageTk.PhotoImage(imgInfo)

# 加上好看的背景圖片
bgImg = Image.open("herou2.jpg")                           # 讀取 iphone13Case.png 放入 productImg 這個變數中
bgImg = bgImg.resize((800,500),Image.ANTIALIAS)            # 調整產品圖片大小
bgImg = ImageTk.PhotoImage(bgImg)                          # 把要放入視窗的圖邊資訊都放入 productImg 這個變數裡面
label1 = tk.Label(win,image=bgImg)                         # 將 productImg 放入 win 這個視窗中
label1.place(x=0,y=0)                                              # 調整 productImg 要出現的位置

# # 加上按鈕1 購買      (如果不要圖片就把 image=imgBuy 刪掉)
# btn1 = tk.Button(win,text = "立刻購買",image=imgBuy,bg="#FFFFFF",command=buy1)   # 建立 button ，文字="press me"按下後執行 event1
# btn1.place(x=290,y=160)
# good1 = 0
#
# # 加上按鈕2 更多資訊  (如果不要圖片就把 image=imgInfo 刪掉)
# btn2 = tk.Button(win,text = "更多資訊",image=imgInfo,bg="#FFFFFF",command=showMore)   # 建立 button ，文字="press me"按下後執行 event1
# btn2.place(x=306,y=4)

# # 產品圖片
# productImg = Image.open("iphone13Case.png")                # 讀取 iphone13Case.png 放入 productImg 這個變數中
# productImg = productImg.resize((250,500),Image.ANTIALIAS)  # 調整產品圖片大小
# productImg = ImageTk.PhotoImage(productImg)                # 把要放入視窗的圖邊資訊都放入 productImg 這個變數裡面
# label1 = tk.Label(win,image=productImg)                    # 將 productImg 放入 win 這個視窗中
# label1.place(x=0)                                          # 調整 productImg 要出現的位置

# # 加上產品資訊 iphone 13 pro max
# iphone13promaxName = "iphone 13 手機殼"                     # 產品資訊
# iphone13promaxPrice = 80
# iphone13promaxFormat = "軍規"
# iphone13promaxInventory = 4

# # 加上產品資訊標籤
# label2 = tk.Label(win,bd=10,font=("標楷體",16),bg="#FFFFFF",text=str(iphone13promaxName)+"\n"+"售價: "+str(iphone13promaxPrice)+"\n"+"等級: "+str(iphone13promaxFormat)+"\n"+"商品庫存: "+str(iphone13promaxInventory))  # 設定文字底色放入文字
# label2.place(x=255,y=50)                                   # 文字出現位置

# # 加上購物車按鈕
# imgCart = Image.open("Cartoon-Shopping-Cart.jpg")
# imgCart = imgCart.resize((40,40),Image.ANTIALIAS)
# imgCart = ImageTk.PhotoImage(imgCart)
# shopcartBtn = tk.Button(win,image=imgCart,command=cartBtn,bg="#FFFFFF")
# shopcartBtn.place(x=370,y=160)

# 2.建立兩個 label Enter 商品名稱 金額
entryTextName = tk.StringVar()                                                  # 建立名字輸入框的內容變數
entryMerchandiseName=tk.Entry(win,font=("標楷體",20),textvariable=entryTextName)  # 新增名字輸入框 Entry
entryMerchandiseName.place(x=140,y=120)                                         # 放置名字輸入框到主視窗
entryTextPrice = tk.Variable()                                                  # 建立價格輸入框的內容變數
entryPrice=tk.Entry(win,font=("標楷體",20),textvariable=entryTextPrice)          # 新增價格輸入框 Entry
entryPrice.place(x=140,y=170)                                                   # 加入價格輸入框到主視窗

# 1.建立四個標籤 訂單編號  商品名稱 金額 備註
labelBookNum = tk.Label(win,text="解析度",font=("標楷體",20))              # 訂單編號文字標籤
labelBookNum.place(x=10,y=70)                                             # 訂單編號文字標籤放置位置
labelMerchandiseName = tk.Label(win,text="商品名稱",font=("標楷體",20))      # 商品名稱文字標籤
labelMerchandiseName.place(x=10,y=120)                                    # 商品名稱文字標籤放置位置
labelPrice = tk.Label(win,text="存放資料夾名稱",font=("標楷體",12))                 # 金額文字標籤
labelPrice.place(x=10,y=170)                                              # 金額文字標籤放置位置
labelNote = tk.Label(win,text="清單連結",font=("標楷體",20))                 # 備註文字標籤
labelNote.place(x=10,y=220)                                               # 備註文字標籤放置位置
labelWay = tk.Label(win,text="下載格式",font=("標楷體",20))                # 運送方式文字標籤
labelWay.place(x=500,y=70)                                               # 運送方式文字標籤放置位置

# 4. 1個 ScrolledText 備註
# separator = ttk.Separator(win, orient='horizontal')                       # 建立一個分割線
# separator.pack(fill='x')                                                  # 分割線放置位置
st = ScrolledText(win, width=18,  height=2,font=("標楷體",20))             # 建立一個 備註 多行輸入格 scrolledtext
st.place(x=140,y=220)                                                     # 備註 多行輸入格放置在這個位置

# 9. menu 下拉式選單(畫面就好了)
def on_field_change(index, value, op):                                                             # 定義 運送方式 下拉式選單選取時的功能
    print("combobox updated to ", comboboxValue1.get())                                            # 印出 運送方式 下拉式選單目前的值
comboboxValue1 = tk.StringVar()                                                                    # 建立 運送方式 下拉式選單的變數
comboboxValue1.trace('w',on_field_change)                                                          # 注意：當資料不同時，就會呼叫 on_field_change
wayChoosen = ttk.Combobox(win, width=27, textvariable=comboboxValue1,font=("標楷體",20))            # 建立 運送方式 下拉式選單的物件於主式窗
wayChoosen['values'] = ('mp4',                                                                     # Adding combobox drop down list
                          '海運',
                          '陸運',
                          '宅配',
                          '超商店到店')
wayChoosen.place(x=630,y=70)                                                                      # 運送方式 下拉式選單的放置位置

# 9. 解析度 下拉式選單(畫面就好了)
def on_field_change(index, value, op):                                                             # 定義 運送方式 下拉式選單選取時的功能
    print("combobox updated to ", comboboxValue1.get())                                            # 印出 運送方式 下拉式選單目前的值
comboboxValue1 = tk.StringVar()                                                                    # 建立 運送方式 下拉式選單的變數
comboboxValue1.trace('w',on_field_change)                                                          # 注意：當資料不同時，就會呼叫 on_field_change
wayChoosen = ttk.Combobox(win, width=27, textvariable=comboboxValue1,font=("標楷體",20))            # 建立 運送方式 下拉式選單的物件於主式窗
wayChoosen['values'] = ('mp4',                                                                     # Adding combobox drop down list
                          '海運',
                          '陸運',
                          '宅配',
                          '超商店到店')
wayChoosen.place(x=140,y=70)                                                                      # 運送方式 下拉式選單的放置位置

# 最後步驟：程式做無限循環
win.mainloop()

