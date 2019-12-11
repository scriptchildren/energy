
filename=tk.Label(text=".........")
filename.place(x=10,y=100)

var = tkinter.StringVar(master=window)

haisoulabel=tk.Label(text="配送方法選択")
haisoulabel.place(x=10,y=150)

haisoubutton=tk.Button(text="Enter")
haisoubutton.place(x=530,y=150)

haisousentaku = TestCombobox(master=window, var=var)
haisousentaku.place(x=200,y=150)

kosuulabel=tk.Label(text="個数(0~99)")
kosuulabel.place(x=10,y=200)

haisoulabel=tk.Label(text="サイト選択")
haisoulabel.place(x=10,y=250)

haisoubutton=tk.Button(text="Enter")
haisoubutton.place(x=530,y=250)

haisousentaku = TestComboboxSite(master=window, var=var)
haisousentaku.place(x=200,y=250)

e1 = tk.Entry(window)
e1.place(x=200,y=200)

e1button=tk.Button(text="Enter")
e1button.place(x=530,y=200)

seiseibutton=tk.Button(text="生成")
seiseibutton.place(x=300,y=350)



tk.mainloop()