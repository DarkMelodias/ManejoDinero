from tkinter import *
from tkinter import ttk,font
import tkinter as tk
from tkinter import messagebox


class Interfaz(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        ancho_ventana = 1200
        alto_ventana = 800

        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.master.geometry(posicion)

        self.master.resizable(0,0)

        self.s = ttk.Style()
        self.s.configure('Cobros.TCheckbutton', font=("Arial",22), background="#DFF3EF")

        self.tt = ttk.Style()
        self.tt.configure('Title.Treeview.Heading', font=("Arial",24))
        
        self.create_header()
        self.create_body()
        self.create_footer()

    def create_header(self):
        headerFrame = Frame(self.master,bg='#eeeee0')
        headerFrame.place(x=0,y=0,width=1200,height=100)

        lbltitle = Label(headerFrame,text='Manejo de Dinero',bg="#eeeee0",fg="black",font=("Arial",22))
        lbltitle.place(x=475, y=30)

    def create_body(self):
        bodyframe = Frame(self.master,bg='#DFF3EF')
        bodyframe.place(x=0,y=100,width=1200,height=680)

        lbl_espec = Label(bodyframe,text='Especificacion: ',bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_espec.place(x=50,y=30)

        etr_espec = ttk.Entry(bodyframe,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_espec.place(x=50,y=70)

        lbl_valor = Label(bodyframe,text='Valor: ',bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_valor.place(x=380,y=30)

        etr_valor = ttk.Entry(bodyframe,width=30,font=font.Font(family="Arial",size=18),justify=CENTER)
        etr_valor.place(x=380,y=70)

        self.checkbutton_value = tk.StringVar(self)

        lbl_check = Label(bodyframe,text="Cobro:",bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_check.place(x=910,y=30)

        self.cb_mensual = ttk.Checkbutton(bodyframe, text="Mensual",style='Cobros.TCheckbutton', variable=self.checkbutton_value, onvalue="Mensual", offvalue=0)
        self.cb_mensual.place(x=820, y=67)

        self.cb_unico = ttk.Checkbutton(bodyframe, text="Unico",style='Cobros.TCheckbutton', variable=self.checkbutton_value, onvalue="Unico", offvalue=0)
        self.cb_unico.place(x=1000, y=67)

        btn_save = Button(bodyframe,bg="#351A52",activebackground="#4D2E6F")
        btn_save ["border"] = "0"
        btn_save.place(x=520,y=150,width=150,height=40)

        self.gridC = ttk.Treeview(bodyframe,columns=("col1"),style='Title.Treeview')
        self.gridC.column("#0",width=300)
        self.gridC.column("col1",width=200, anchor=CENTER)
        self.gridC.heading("#0", text="Especificacion", anchor=CENTER)
        self.gridC.heading("col1", text="Valor", anchor=CENTER)
        
        self.gridC.place(x=60,y=250,height=250)

        sb = Scrollbar(bodyframe, orient=VERTICAL)
        sb.place(x=564,y=250,height=250)
        self.gridC.config(yscrollcommand=sb.set)
        sb.config(command=self.gridC.yview)
        
        self.gridC['selectmode']='browse'

        self.gridC2 = ttk.Treeview(bodyframe,columns=("col1"),style='Title.Treeview')
        self.gridC2.column("#0",width=300)
        self.gridC2.column("col1",width=200, anchor=CENTER)
        self.gridC2.heading("#0", text="Especificacion", anchor=CENTER)
        self.gridC2.heading("col1", text="Valor", anchor=CENTER)
        
        self.gridC2.place(x=630,y=250,height=250)

        sb2 = Scrollbar(bodyframe, orient=VERTICAL)
        sb2.place(x=1134,y=250,height=250)
        self.gridC2.config(yscrollcommand=sb2.set)
        sb2.config(command=self.gridC2.yview)
        
        self.gridC2['selectmode']='browse'

        lbl_totalM = Label(bodyframe,text='Total: ',bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_totalM.place(x=280, y=500)

        lbl_totalU = Label(bodyframe,text='Total: ',bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_totalU.place(x=850, y=500)

        btn_eliminarM = Button(bodyframe, bg="#351A52",activebackground="#4D2E6F")
        btn_eliminarM ["border"] = "0"
        btn_eliminarM.place(x=280,y=550,width=150,height=40)

        btn_eliminarU = Button(bodyframe, bg="#351A52",activebackground="#4D2E6F")
        btn_eliminarU ["border"] = "0"
        btn_eliminarU.place(x=850,y=550,width=150,height=40)

    def create_footer(self):
        footerFrame = Frame(self.master,bg='#eeeee0')
        footerFrame.place(x=0,y=780,width=1200,height=20)

        lblfooter = Label(footerFrame,text='Hecho por: Samuel Triana',bg="#eeeee0",fg="black",font=("Arial",10))
        lblfooter.place(x=475, y=0)