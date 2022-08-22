from tkinter import *
from tkinter import ttk,font
import tkinter as tk
from tkinter import messagebox

from backend import save_price
from backend import get_prices
from backend import delete_price


prices = get_prices()

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

        self.cobro= ""
        self.text_error = tk.StringVar(self)
        self.text_totalM = tk.StringVar(self)
        self.text_totalU = tk.StringVar(self)

        self.s = ttk.Style()
        self.s.configure('Cobros.TCheckbutton', font=("Arial",22), background="#DFF3EF")

        self.tt = ttk.Style()
        self.tt.configure('Title.Treeview.Heading', font=("Arial",24))
        
        self.create_header()
        self.create_body()
        self.create_footer()

    def tiene_exactamente_un_punto(self,numero):
            nume = str(numero)
            primer_indice = nume.find(".")
            if primer_indice == -1:
                return False
            else:
                return True

    def validate_entry(self,text):
            return text.isdigit() or self.tiene_exactamente_un_punto(text)

    def checkbox_clicked(self):
        self.cobro = self.checkbutton_value.get()

    def llenaDatosProd(self,grid,grid2):
        prices = get_prices()
        self.limpiarGrid(grid,grid2)
        datos = prices
        totalM = 0
        totalU = 0
        for row in datos:
            if row['cobro'] == 'Mensual':
                grid.insert("",END,text=row['especificacion'],values=(row['valor']))
                totalM = totalM+int(row['valor'])
            else:
                grid2.insert("",END,text=row['especificacion'],values=(row['valor']))
                totalU = totalU+int(row['valor'])
        if len(grid.get_children()) > 0:
            grid.selection_set( grid.get_children()[0] )
        if len(grid2.get_children()) > 0:
            grid2.selection_set( grid2.get_children()[0] )

        self.text_totalM.set("Total:{}".format(totalM))
        self.text_totalU.set("Total:{}".format(totalU))
        self.lbl_totalM.config(textvariable=self.text_totalM)
        self.lbl_totalU.config(textvariable=self.text_totalU)

    def limpiarGrid(self,grid,grid2):
        for item in grid.get_children():
            grid.delete(item)
        for item in grid2.get_children():
            grid2.delete(item)

    def limpiarCajas(self):
        self.etr_espec.delete(0,END)
        self.etr_valor.delete(0,END)
        self.cobro = ""

    def camposllenos(self):
        if len(self.etr_espec.get()) == 0:
            self.text_error.set("Campo especificacion vacio")
            self.lbl_error.config(textvariable=self.text_error)
            return True
        if len(self.etr_valor.get()) == 0:
            self.text_error.set("Campo valor vacio")
            return True
        if len(self.cobro) == 0:
            self.text_error.set("Seleccione un cobro")
            return True

    def _button_save(self,espec,val,cobro):
        if self.camposllenos():
            return True
        save_price(espec,val,cobro)
        self.llenaDatosProd(self.gridC,self.gridC2)
        self.limpiarCajas()
        self.text_error.set("")

    def borrar_mensual(self):
        selected = self.gridC.focus()
        clave = self.gridC.item(selected,'text')
        r = messagebox.askquestion("Eliminar","Deseas eliminar el cobro con nombre: {}".format(clave))
        if r == messagebox.YES:
            if delete_price(clave):
                messagebox.showinfo("Eliminar","Cobro Eliminado correctamente")
                self.llenaDatosProd(self.gridC,self.gridC2)
            else:
                messagebox.showinfo("Eliminar","El cobro no ha podido ser eleminado")

    def borrar_unico(self):
        selected = self.gridC2.focus()
        clave = self.gridC2.item(selected,'text')
        r = messagebox.askquestion("Eliminar","Deseas eliminar el cobro con nombre: {}".format(clave))
        if r == messagebox.YES:
            if delete_price(clave):
                messagebox.showinfo("Eliminar","Cobro Eliminado correctamente")
                self.llenaDatosProd(self.gridC,self.gridC2)
            else:
                messagebox.showinfo("Eliminar","El cobro no ha podido ser eleminado")

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

        self.lbl_error = Label(bodyframe,bg="#DFF3EF",fg="black",font=("Arial",22))
        self.lbl_error.place(x=50,y=130)
        self.lbl_error.config(textvariable=self.text_error)

        self.etr_espec = ttk.Entry(bodyframe,width=20,font=font.Font(family="Arial",size=18),justify=CENTER)
        self.etr_espec.place(x=50,y=70)

        lbl_valor = Label(bodyframe,text='Valor: ',bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_valor.place(x=380,y=30)

        self.etr_valor = ttk.Entry(bodyframe,width=30,font=font.Font(family="Arial",size=18),justify=CENTER,validate="key",validatecommand=(self.master.register(self.validate_entry), "%S"))
        self.etr_valor.place(x=380,y=70)

        self.checkbutton_value = tk.StringVar(self)

        lbl_check = Label(bodyframe,text="Cobro:",bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_check.place(x=910,y=30)

        self.cb_mensual = ttk.Checkbutton(bodyframe, text="Mensual",style='Cobros.TCheckbutton', variable=self.checkbutton_value, onvalue="Mensual", offvalue=1,command=self.checkbox_clicked)
        self.cb_mensual.place(x=820, y=67)

        self.cb_unico = ttk.Checkbutton(bodyframe, text="Unico",style='Cobros.TCheckbutton', variable=self.checkbutton_value, onvalue="Unico", offvalue=0,command=self.checkbox_clicked)
        self.cb_unico.place(x=1000, y=67)

        btn_save = Button(bodyframe,bg="#351A52",activebackground="#4D2E6F",command=lambda: self._button_save(self.etr_espec.get(),self.etr_valor.get(),self.cobro))
        btn_save ["border"] = "0"
        btn_save.place(x=520,y=130,width=150,height=40)

        lbl_ttable = Label(bodyframe,text="Mensual",bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_ttable.place(x=60,y=200)

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

        lbl_ttable2 = Label(bodyframe,text="Unico",bg="#DFF3EF",fg="black",font=("Arial",22))
        lbl_ttable2.place(x=630,y=200)

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

        self.lbl_totalM = Label(bodyframe,bg="#DFF3EF",fg="black",font=("Arial",22))
        self.lbl_totalM.place(x=280, y=500)
        self.lbl_totalM.config(textvariable=self.text_totalM)

        self.lbl_totalU = Label(bodyframe,bg="#DFF3EF",fg="black",font=("Arial",22))
        self.lbl_totalU.place(x=850, y=500)
        self.lbl_totalU.config(textvariable=self.text_totalU)

        btn_eliminarM = Button(bodyframe, bg="#351A52",activebackground="#4D2E6F",command=lambda:self.borrar_mensual())
        btn_eliminarM ["border"] = "0"
        btn_eliminarM.place(x=280,y=550,width=150,height=40)

        btn_eliminarU = Button(bodyframe, bg="#351A52",activebackground="#4D2E6F",command=lambda:self.borrar_unico())
        btn_eliminarU ["border"] = "0"
        btn_eliminarU.place(x=850,y=550,width=150,height=40)

        self.llenaDatosProd(self.gridC,self.gridC2)

    def create_footer(self):
        footerFrame = Frame(self.master,bg='#eeeee0')
        footerFrame.place(x=0,y=780,width=1200,height=20)

        lblfooter = Label(footerFrame,text='Hecho por: Samuel Triana',bg="#eeeee0",fg="black",font=("Arial",10))
        lblfooter.place(x=475, y=0)

