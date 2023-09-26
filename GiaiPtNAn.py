import tkinter as tk
import numpy as np

heso=[]
coso=[]
def math():
    main_frame.pack_forget()
    second_frame.pack()
    global heso, coso
    n=int(entry1.get())
    array_heso = np.empty((n,n))
    array_coso = np.empty((n,1))
    for i in range(n*n):
        heso_value=float(heso[i].get())
        array_heso[i//n, i%n]=heso_value
    for i in range(n):
        coso_value=float(coso[i].get())
        array_coso[i,0]=coso_value
    x=np.linalg.solve(array_heso,array_coso)
    label_ketqua=tk.Label(second_frame, text=f"Các nghiệm của hệ phương trình lần lượt là:")
    label_ketqua.pack()
    for i in x:
        label=tk.Label(second_frame,text=f"{i}")
        label.pack()
def bt1():
    n=int(entry1.get())
    main_frame.pack_forget()
    second_frame.pack()

    global heso
    for i in range (n*n):
        label=tk.Label(second_frame, text=f"Nhập hệ số {i+1}" )
        label.pack()
        entry=tk.Entry(second_frame)
        entry.pack()
        heso.append(entry)
    global coso
    for i in range (n):
        label=tk.Label(second_frame, text=f"Nhập cơ số {i+1}" )
        label.pack()
        entry=tk.Entry(second_frame)
        entry.pack()
        coso.append(entry)
    button2=tk.Button(second_frame,text=f"Giải",command=math)
    button2.pack()


cs=tk.Tk()
cs.title("GIẢI PHƯƠNG TRÌNH N ẨN")
cs.geometry("400x400")

main_frame=tk.Frame(cs)
main_frame.pack()

label1=tk.Label(main_frame, text="Số ẩn của hệ phương trình")
label1.pack()
entry1 = tk.Entry(main_frame)
entry1.pack()
button1=tk.Button(main_frame, text="Giải hệ phương trình", command=bt1)
button1.pack()

second_frame=tk.Frame(cs)
second_frame.pack_forget()



cs.mainloop()