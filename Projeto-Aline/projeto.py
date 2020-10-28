from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class Alunologin: #tela de quando é efetuado o loguin do Aluno

    sqlite_var = 0
    theCursor = 0
    curItem = 0

    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Atualizar")

    def search_record(self): # *Lembrar de adicionar outros dados
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Books where Titulo like ? or Anol like  ?", ('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length = str(len(self.result))
            if (length == 0):
                messagebox.showinfo("Não foi possivel encontrar cadastro com esse valor informado")
            if (length != '0'):
                i = 0
                for row in self.result:
                    if (i%2 == 0):
                        self.tree.insert("", END, values=row,tag='1')
                    else:
                        self.tree.insert("", END, values=row,tag= '2')
                    i = i+1
        except:
            raise print("Não foi possivel entrar dados (1)")

    def clear_entries(self):
        self.search_value.set("")

    def update_tree(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("Select * FROM Books")
            self.rows = self.theCursor.fetchall()
            i = 0
            for row in self.rows:
                if(i%2==0):
                    self.tree.insert("", END, values=row,tag='1')
                else:
                    self.tree.insert("", END, values=row, tag= '2')
                i=i+1
        except:
            print("Não foi possível atualizar os dados (1)")

    def setup_db(self): #banco de dados
        try:
            self.sqlite_var = sqlite3.connect('Books.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Não foi possivel conectar ao bando de DADOS")

        try:
            self.theCursor.execute("CREATE TABLE if not exists Books(ID INTEGER PRIMARY KEY AUTOINCREMENT , Titulo TEXT UNIQUE NOT NULL , Anol TEXT NOT NULL, NomeA TEXT NOT NULL, Categoria TEXT NOT NULL, Tematica TEXT NOT NULL);")
        except:
            print("Não foi possivel criar a tabela")
        finally:
            self.sqlite_var.commit()
            self.update_tree()

    def __init__(self):

        self.user_window=Tk()
        self.user_window.resizable(False, False)
        self.user_window.title("Painel Aluno")
        self.user_window.iconbitmap("test.ico")

        self.tree= ttk.Treeview(self.user_window, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')
        self.tree.column("column1", width=100,minwidth=100,stretch=NO)
        self.tree.heading("#1", text="Quantidade")
        self.tree.column("column2", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#2", text="Titulo")
        self.tree.column("column3", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#3", text="Ano do livro")
        self.tree.column("column4", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#4", text="Nome do Autor")
        self.tree.column("column5", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#5", text="Categoria")
        self.tree.column("column6", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#6", text="Temática")
        self.tree.tag_configure('1', background='ivory2')
        self.tree.tag_configure('2', background= 'alice blue')
        self.tree.grid(row=5,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)


        #self.submit_button = ttk.Button(self.user_window,text="Cadastrar")
        #self.submit_button.grid(row=0, column=3, padx=9,sticky=W+E)

        #self.update_button = ttk.Button(self.user_window, text= "Atualizar")
        #self.update_button.grid(row=1, column=3,padx=9, sticky=W+E)

        #self.delete_button = ttk.Button(self.user_window,text="Deletar")
        #self.delete_button.grid(row=2, column=3,padx=9, sticky=W+E)


        Label(self.user_window,text = "Pesquisar por Titulo,Ano,Nome do Autor :").grid(row=6,column=0,columnspan=2,pady=9,padx=9,sticky=E)
        self.search_value = StringVar(self.user_window, value="")
        Entry(self.user_window,textvariable=self.search_value).grid(row=6, column=2,pady=9,padx=9,sticky=W+E)
        self.search_button = ttk.Button(self.user_window,text="Pesquisar",command=self.search_record)
        self.search_button.grid(row=6,column=3,pady=9,padx=9,sticky=W+E)

        self.refresh_button = ttk.Button(self.user_window,text="Atualizar",command=self.refresh)
        self.refresh_button.grid(row=7, column=3,padx=9,pady=9,sticky=W+E)


        self.setup_db()
        self.user_window.mainloop()





class adminlogin: #Tela de quando é efetuado o login de alguem da coordenação!

    sqlite_var = 0
    theCursor = 0
    curItem = 0

    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Atualizar dados")

    def search_record(self): # Metodo de fazer a pesquisa de dados. Lembrar de adicionar outros dados
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Books where Titulo like ? or Anol like ?", ('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length= str(len(self.result))
            if (length==0):
                messagebox.showinfo("Não é possivel encontrar resultado")
            if(length!='0'):
                i = 0
                for row in self.result:
                    if(i%2==0):
                        self.tree.insert("", END, values=row,tag='1')
                    else:
                        self.tree.insert("", END, values=row,tag='2')
                    i= i+1
        except:
            raise print("não foi possivel encontrar dados")

    def reset_db(self): # metodo para apagar os dados do banco de dados.
        sn = messagebox.askquestion("Erro","Deseja realmente deletar todos os dados  do BD?") #Sim ou não
        if(sn=='yes'):
            self.theCursor.execute("DROP TABLE Books")
            print("DADOS APAGADOS!!!")
            self.setup_db()
            self.update_tree()

    def clear_entries(self):
        self.Name_entry.delete(0, "end")
        self.ano_no_entry.delete(0, "end")
        self.autor_entry.delete(0,"end")
        self.categoria_entry.delete(0, "end")
        self.tematica_entry.delete(0, "end")

    def delete_record(self): # Metodo para deletar um livro específico
        try:
            self.theCursor.execute("delete FROM Books WHERE ID=?",(self.curItem['values'][0],))
            print("DADOS DELETADOS")
        except:
            print("Não é possivel deletar este dado!")
        finally:
            self.curItem=0
            self.clear_entries()
            self.update_tree()
            self.sqlite_var.commit()

    def update_record(self): # Atualiza dados de livro.
        if(self.Name_value.get() != "" and self.ano_no_value.get() !="" and self.autor_value.get() != "" and self.categoria_value.get() != "" and self.tematica_value.get() != ""):
            #print("Entrou")
            try:
                self.theCursor.execute("""UPDATE Books SET Titulo = ? , Anol = ?, NomeA = ? , Categoria = ?, Tematica = ? WHERE ID = ?""",
                (self.Name_value.get(), self.ano_no_value.get(), self.autor_value.get(), self.categoria_value.get(), self.tematica_value.get(), self.curItem['values'][0]))
                print("ATUALIZADO COM SUCESSO")
            except sqlite3.IntegrityError:
                messagebox.showerror("Esse livro ja se encontra no banco de dados (2)")
            except:
                print("Não foi possivel atualizar os dados !")
            finally:
                self.update_tree()
                self.sqlite_var.commit()
        else:
            messagebox.showwarning("ERROR", "Favor preencher todos os campos")

    def selectItem(self,event): #seleciona os itens de cada tabela.
        self.curItem = self.tree.item(self.tree.focus())
        print(self.curItem)
        self.Name_value.set(self.curItem["values"][1])
        self.ano_no_value.set(self.curItem["values"][2])
        self.autor_value.set(self.curItem["values"][3])
        self.categoria_value.set(self.curItem["values"][4])
        self.tematica_value.set(self.curItem["values"][5])


    def update_tree(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("SELECT * FROM Books")
            self.rows = self.theCursor.fetchall()
            i = 0
            for row in self.rows:
                if(i%2==0):
                    self.tree.insert("", END, values=row,tag='1')
                else:
                    self.tree.insert("", END, values=row,tag='2')
                i = i+1
        except:
            raise print("Erro ao atualizar os dados")


    def write_record(self):#Cadastra livro e testa se já existe
        if(self.Name_value.get()!="" and self.ano_no_value.get()!="" and self.autor_value.get()!=""):
            try:
                self.theCursor.execute("""INSERT INTO Books (Titulo, Anol, NomeA, Categoria, Tematica) VALUES (?,?,?,?,?)""",
                (self.Name_value.get(),self.ano_no_value.get(),self.autor_value.get(),self.categoria_value.get(),self.tematica_value.get()))
                self.sqlite_var.commit()
                self.theCursor.execute("SELECT *,max(id) FROM Books")
                self.rows=self.theCursor.fetchall()
                print(self.rows[0][0],"{Titulo : ",self.rows[0][1],"| No : ",self.rows[0][2],"| NomeA :",self.rows[0][3], "| Categoria : ",self.rows[0][4],"| Tematica :",self.rows[0][5],"} FOI CADASTRADO!")
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro!", "Este livro ja se encontra no BD(1)")
            except:
                print("Error!", "Não FOI POSSIVEL ATUALIZAR OS DADOS!(1)")
            finally:
                self.update_tree()
        else:
            messagebox.showwarning("Error!", "Preencha todos os dados!")

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('Books.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("NÃO FOI POSSIVEL CONECTAR NO BD!")

        try:
            self.theCursor.execute("CREATE TABLE if not exists Books(ID INTEGER PRIMARY KEY AUTOINCREMENT , Titulo TEXT UNIQUE NOT NULL , Anol TEXT NOT NULL, NomeA TEXT NOT NULL, Categoria TEXT NOT NULL, Tematica TEXT NOT NULL);")
        except:
            print("NAO FOI POSSIVEL CRIAR A TABELA")
        finally:
            self.sqlite_var.commit()
            self.update_tree()



    def __init__(self):
        self.admin_janela=Tk()
        self.admin_janela.title("Cadastrar ADM :")
        self.admin_janela.resizable(False,False)
        self.admin_janela.iconbitmap("test.ico")

        self.Name_Label = Label(self.admin_janela, text = "Titulo") ###
        self.Name_Label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.Name_value = StringVar(self.admin_janela, value="")#
        self.Name_entry = ttk.Entry(self.admin_janela,textvariable=self.Name_value)#
        self.Name_entry.grid(row=0, column=1, columnspan=2,padx=10, pady=10,sticky=W+E)

        self.ano_Label = Label(self.admin_janela, text ="Ano Do Livro.") ###
        self.ano_Label.grid(row=1, column=0, padx=10,pady=10,sticky=W)

        self.ano_no_value = StringVar(self.admin_janela, value ="")
        self.ano_no_entry = ttk.Entry(self.admin_janela,textvariable=self.ano_no_value)
        self.ano_no_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=W+E)


        self.autor_Label = Label(self.admin_janela, text="Nome do Autor") ###
        self.autor_Label.grid(row=2, column=0, padx=10,pady=10, sticky=W)

        self.autor_value = StringVar(self.admin_janela, value="")
        self.autor_entry = ttk.Entry(self.admin_janela,textvariable=self.autor_value)
        self.autor_entry.grid(row=2, column=1,columnspan=2, padx=10, pady=10, sticky=W+E)

        self.categoria_Label = Label(self.admin_janela, text="Categoria do livro") ###
        self.categoria_Label.grid(row=3, column=0, padx=10,pady=10, sticky=W)

        self.categoria_value = StringVar(self.admin_janela, value="")
        self.categoria_entry = ttk.Entry(self.admin_janela,textvariable=self.categoria_value)
        self.categoria_entry.grid(row=3, column=1,columnspan=2, padx=10, pady=10, sticky=W+E)

        self.tematica_Label = Label(self.admin_janela, text = "Temática do livro") ###
        self.tematica_Label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.tematica_value = StringVar(self.admin_janela, value="")#
        self.tematica_entry = ttk.Entry(self.admin_janela,textvariable=self.tematica_value)#
        self.tematica_entry.grid(row=4, column=1, columnspan=2,padx=10, pady=10,sticky=W+E)

        self.submit_button = ttk.Button(self.admin_janela,text="Cadastrar",command=self.write_record)
        self.submit_button.grid(row=0, column=3, padx=9,sticky=W+E)

        self.update_button = ttk.Button(self.admin_janela, text= "Atualizar",command=self.update_record)
        self.update_button.grid(row=1, column=3,padx=9, sticky=W+E)

        self.delete_button = ttk.Button(self.admin_janela,text="Deletar",command=self.delete_record)
        self.delete_button.grid(row=2, column=3,padx=9, sticky=W+E)

        self.tree= ttk.Treeview(self.admin_janela, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')
        self.tree.column("column1", width=100,minwidth=100,stretch=NO)
        self.tree.heading("#1", text="Quantidade")
        self.tree.column("column2", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#2", text="Titulo")
        self.tree.column("column3", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#3", text="Ano do livro")
        self.tree.column("column4", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#4", text="Nome do Autor")
        self.tree.column("column5", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#5", text="Categoria")
        self.tree.column("column6", width=100, minwidth=100, stretch=NO)
        self.tree.heading("#6", text="Temática")
        self.tree.bind("<ButtonRelease-1>",self.selectItem)
        self.tree.bind("<space>",self.selectItem)
        self.tree.tag_configure('1', background='ivory2')
        self.tree.tag_configure('2', background= 'alice blue')
        self.tree.grid(row=5,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)
        Label(self.admin_janela,text = "Pesquisar por Titulo,Ano,Nome do Autor :").grid(row=6,column=0,columnspan=2,pady=9,padx=9,sticky=E)
        self.search_value = StringVar(self.admin_janela, value="")
        Entry(self.admin_janela,textvariable=self.search_value).grid(row=6, column=2,pady=9,padx=9,sticky=W+E)
        self.search_button = ttk.Button(self.admin_janela,text="Pesquisar",command=self.search_record)
        self.search_button.grid(row=6,column=3,pady=9,padx=9,sticky=W+E)

        self.refresh_button = ttk.Button(self.admin_janela,text="Atualizar",command=self.refresh)
        self.refresh_button.grid(row=7, column=3,padx=9,pady=9,sticky=W+E)

        #Label(self.admin_janela,text="Francisco Neto").grid(row=9,column=0,pady=9,padx=9,sticky=W)
        self.reset_button = ttk.Button(self.admin_janela,text="Limpar dados do BD!!",command=self.reset_db)
        self.reset_button.grid(row=4, column=3,padx=9,pady=9,sticky=W+E)

        self.setup_db()
        self.admin_janela.mainloop()

class entrajanela: #janela para cadastrar novo usuario.

    sqlite_var = 0
    theCursor = 0
    curItem = 0

    def refresh(self):
        self.user_tree_update()
        self.clear_entries()
        print("Atualizar dados")

    def search_record(self): # Metodo de fazer a pesquisa de dados de usuario.
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from users where usuario like ? or senha like ?", ('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length= str(len(self.result))
            if (length==0):
                messagebox.showinfo("Não é possivel encontrar resultado")
            if(length!='0'):
                i = 0
                for row in self.result:
                    if(i%2==0):
                        self.tree.insert("", END, values=row,tag='1')
                    else:
                        self.tree.insert("", END, values=row,tag='2')
                    i= i+1
        except:
            raise print("não foi possivel encontrar dados")
    
    
    def show_users(self):
        try:
            self.theCursor.execute("SELECT * from users")
            res=self.theCursor.fetchall()
        except:
            print("Não foi possivel carregar BD")

        self.show_u=Tk()
        self.show_u.title("Lista de Usuarios")
        self.show_u.resizable(False,False)
        self.show_u.iconbitmap("test.ico")





        self.username_value = StringVar(self.show_u, value="")#
        self.username_entry = ttk.Entry(self.show_u,textvariable=self.username_value)#


        self.password_value = StringVar(self.show_u, value ="")
        self.password_entry = ttk.Entry(self.show_u,textvariable=self.password_value)


        self.delete_button = ttk.Button(self.show_u,text="Deletar",command=self.delete_record)
        self.delete_button.grid(row=7, column=3,padx=9, sticky=W+E)

        self.tree= ttk.Treeview(self.show_u, selectmode="browse", column=("column1", "column2", "column3"), show='headings')
        self.tree.column("column1", width=100,minwidth=100)
        self.tree.heading("#1", text="ID")
        self.tree.column("column2", width=100, minwidth=100 )
        self.tree.heading("#2", text="Usuario")
        self.tree.column("column3", width=100, minwidth=100)
        self.tree.heading("#3", text="Senha")
        self.tree.bind("<ButtonRelease-1>",self.selectItem)
        self.tree.bind("<space>",self.selectItem)
        self.tree.tag_configure('1', background='ivory2')
        self.tree.tag_configure('2', background= 'alice blue')
        self.tree.grid(row=5,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)
        Label(self.show_u,text = "Pesquisar por Usuario :").grid(row=6,column=0,columnspan=2,pady=9,padx=9,sticky=E)
        self.search_value = StringVar(self.show_u, value="")
        Entry(self.show_u,textvariable=self.search_value).grid(row=6, column=2,pady=9,padx=9,sticky=W+E)
        self.search_button = ttk.Button(self.show_u,text="Pesquisar",command=self.search_record)
        self.search_button.grid(row=6,column=3,pady=9,padx=9,sticky=W+E)

        #Label(self.admin_janela,text="Francisco Neto").grid(row=9,column=0,pady=9,padx=9,sticky=W)
        self.reset_button = ttk.Button(self.show_u,text="Deletar todos os usuarios!!",command=self.reset_db)
        self.reset_button.grid(row=4, column=3,padx=9,pady=9,sticky=W+E)

        self.user_tree_update()
        self.show_u.mainloop()
    
    
    def reset_db(self): # metodo para apagar os dados do banco de dados.
        sn = messagebox.askquestion("o/","Deseja realmente deletar todos os dados de usuarios do BD?") #Sim ou não
        if(sn=='yes'):
            self.theCursor.execute("DROP TABLE users")
            print("DADOS APAGADOS!!!")
            self.entra_janela.destroy()
            self.setup_db()
            self.user_tree_update()

    def clear_entries(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")


    def delete_record(self): # Metodo para teletar um livro específico
        try:
            self.theCursor.execute("delete FROM users WHERE ID=?",(self.curItem['values'][0],))
            print("DADOS DELETADOS")
        except:
            print("Não é possivel deletar este dado!")
        finally:
            self.curItem=0
            self.clear_entries()
            self.user_tree_update()
            self.sqlite_var.commit()

    def update_record(self): # Atualiza dados de livro.
        if(self.username_value.get() != "" and self.password_value.get() !=""):
            #print("Entrou")
            try:
                self.theCursor.execute("""UPDATE users SET usuario = ? , senha = ? WHERE ID = ?""",
                (self.username_value.get(), self.password_value.get(), self.curItem['values'][0]))
                print("ATUALIZADO COM SUCESSO")
            except sqlite3.IntegrityError:
                messagebox.showerror("Esse usuario ja se encontra no banco de dados (2)")
            except:
                print("Não foi possivel atualizar os dados !")
            finally:
                self.user_tree_update()
                self.sqlite_var.commit()
        else:
            messagebox.showwarning("ERROR", "Favor preencher todos os campos")

    def selectItem(self,event): #seleciona os itens de cada tabela.
        self.curItem = self.tree.item(self.tree.focus())
        print(self.curItem)
        self.username_value.set(self.curItem["values"][1])
        self.password_value.set(self.curItem["values"][2])


    def user_tree_update(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("SELECT * FROM users")
            self.rows = self.theCursor.fetchall()
            i = 0
            for row in self.rows:
                if(i%2==0):
                    self.tree.insert("", END, values=row,tag='1')
                else:
                    self.tree.insert("", END, values=row,tag='2')
                i = i+1
        except:
            raise print("Erro ao atualizar os dados(1)")


    def write_record(self):
        if(self.username_value.get()!="" and self.password_value.get()!=""):
            try:
                self.theCursor.execute("""INSERT INTO users (usuario, senha) VALUES (?,?)""",
                (self.username_value.get(),self.password_value.get()))
                self.sqlite_var.commit()
                self.theCursor.execute("SELECT *,max(id) FROM users")
                self.rows=self.theCursor.fetchall()
                print(self.rows[0][0],"{usuario : ",self.rows[0][1],"| senha : ",self.rows[0][2],"} FOI CADASTRADO!")
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro!", "Este usuario ja se encontra no BD(1)")
            except:
                print("Error!", "Não FOI POSSIVEL ATUALIZAR OS DADOS!(1)")
            finally:
                self.user_tree_update()
        else:
            messagebox.showwarning("Error!", "Preencha todos os dados!")

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('users.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("NÃO FOI POSSIVEL CONECTAR NO BD!")

        try:
            self.theCursor.execute("CREATE TABLE if not exists users(ID INTEGER PRIMARY KEY AUTOINCREMENT , usuario TEXT UNIQUE NOT NULL , senha TEXT NOT NULL);")
        except:
            print("NAO FOI POSSIVEL CRIAR A TABELA")
        finally:
            self.sqlite_var.commit()


    def new_user(self):
        try:
            if(self.username_value.get()!="" and self.password_value.get()!=""):
                self.theCursor.execute("INSERT INTO users (usuario,senha) VALUES (?,?)",(self.username_value.get(),self.password_value.get()))
                self.entra_janela.destroy()
                messagebox.showinfo("Up!!", "Cadastro realizado com sucesso ")
            else:
                messagebox.showwarning("Error!", "Preencha todos os campos")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error!", "Este usuario ja se encontra no BD")
        except:
            print("Error!", "Naõ foi possivel efetuar cadastro")
        finally:
            self.sqlite_var.commit()
            self.theCursor.execute("SELECT * from users")
            res=self.theCursor.fetchall()
            self.username_value.set("")
            self.password_value.set("")


    def __init__(self):
        self.entra_janela=Toplevel()
        self.entra_janela.title("Cadastrar Usuarios :")
        self.entra_janela.resizable(False,False)
        self.entra_janela.iconbitmap("test.ico")

        self.password_value=StringVar()
        self.username_value=StringVar()

        Label(self.entra_janela,text = "Cadastrar",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)
        Label(self.entra_janela,text = "Usuario : ",font="Ariel, 12").grid(row=1,column=0)
        Label(self.entra_janela,text= "Senha : ",font="Ariel, 12").grid(row=2,column=0,pady=(0,20))

        Entry(self.entra_janela,font="Atiel, 10",textvariable=self.username_value).grid(row=1,column=1)
        Entry(self.entra_janela, font="Atiel, 10", textvariable=self.password_value).grid(row=2,column=1,pady=(0,20))

        user_add=Button(self.entra_janela,font="Ariel, 17", text="Cadastrar",background='white',command=self.new_user)
        user_add.grid(row=1,column=2,rowspan=2,padx=20,pady=(0,20))

        view_existing=Button(self.entra_janela,text="Visualizar usuarios cadastrados",background='white', command=self.show_users)
        view_existing.grid(row=3,column=0,columnspan=4,padx=20,pady=(0,20),sticky=W+E)
        self.setup_db()
        self.entra_janela.mainloop()

class loginprograma: #Tela do login
    sqlite_var = 0
    theCursor = 0
    curItem= 0

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('users.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Não foi possivel conectar ao BD")
        try:
            self.theCursor.execute("CREATE TABLE if not exists users(usuario TEXT NOT NULL,senha TEXT NOT NULL);")
        except:
            print("Não foi possivel criar a TABELA")
        finally:
            self.sqlite_var.commit()

    def logg(self):# ver se é um aluno ou alguem da coordenação.
        try:
            self.theCursor.execute("SELECT * from users")
            res = self.theCursor.fetchall()
            flag = 0
            for x in res:
                if(self.var.get()==2 and self.username_text.get()==x[0] and self.password_text.get()==x[1]):
                    self.loginp.destroy()
                    Alunologin()
                    flag = 1
            if(self.var.get()==1 and self.username_text.get()=="admin" and self.password_text.get()=="neto"):
                self.loginp.destroy()
                adminlogin()
                flag=1
            if(flag==0):
                messagebox.showinfo("Erro!", "Esse ID não tem essa permissão!")

        except:
            print("Ocorreu um erro ao logar")
            raise
        finally:
            self.password_text.set("")
            self.username_text.set("")


    def __init__(self):
        self.loginp = Toplevel()
        self.loginp.title("ProjetoAline")
        self.loginp.resizable(False,False)
        self.loginp.iconbitmap("test.ico")

        self.password_text=StringVar(self.loginp)
        self.username_text=StringVar(self.loginp)
        self.var=IntVar(self.loginp)

        Label(self.loginp,text="Login",font="Ariel, 20").grid(row=0,column=0,sticky=W,pady=10)
        Label(self.loginp,text="Usuario :",font="Ariel, 12").grid(row=1,column=0)
        Label(self.loginp,text="Senha :",font="Ariel, 12").grid(row=2,column=0)

        self.username = Entry(self.loginp,font="Ariel, 10",textvariable =self.username_text).grid(row=1,column=1)
        self.password = Entry(self.loginp,font="Ariel, 10",textvariable =self.password_text, show='*').grid(row=2,column=1)

        self.botao = Button(self.loginp, text="LOGIN", font="Ariel,17", command=self.logg)
        self.botao.grid(row=1,column=2,rowspan=2, pady=20)

        self.var.set(1)

        Radiobutton(self.loginp,text="Coordenação",variable =self.var,value=1).grid(row=3, column=0, pady=15)
        Radiobutton(self.loginp,text="Alunos", variable =self.var,value=2).grid(row=3, column=1)

        self.setup_db()
        self.loginp.mainloop()


class mainprograma():

    def upsobre(self):
        messagebox.showinfo("Sobre", """Projeto da disciplina Estrutura de Dados
        \n\n Professora: Aline Marques\n\n
        \n\n Aluno: Francisco Neto\n
        \n Linguagem utilizada: Python""")



    def upjanela(self):
        try:
            entrajanela()
        except:
            raise Exception("Não foi possivel chamar entrajanela!")

    def creatlogin(self):
        try:
            loginprograma()
        except:
            raise Exception("Não foi possivel chamar loginprograma! ")

    def sairjanela(self):
        if messagebox.askokcancel("o/", "Deseja realmente sair ?"):
            self.root.destroy()
        

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.sairjanela)
        self.root.iconbitmap("test.ico")
        self.root.title("ProjetoAline")
        self.img = ImageTk.PhotoImage(Image.open("book.png"))
        self.painel = Label(self.root, image=self.img)
        self.painel.grid(row=0, column=0)

        Label(self.root, text="Projeto Estrutura de Dados", font="Times,20", foreground='blue').grid(row=1, column=0, sticky=W+E, padx=40)
        Label(self.root, text="Cadastro de Livros", font="Times,30", foreground='red4').grid(row=2, column=0, sticky=W+E, padx=40)
        Label(self.root, text="Francisco Neto ", font="Ariel,10").grid(row=3, column=0, columnspan=2, sticky=W+E, pady=40)


        self.botao = Button(self.root, text="LOGIN",command=self.creatlogin)
        self.botao.configure(width=18,height=2, foreground="white",background="black")
        self.botao.grid(row=5,column=0,columnspan=2,sticky='N', pady=30)


        self.menubar = Menu(self.root)
        self.menubar.add_separator()

        self.filemenu=Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Entrar",command=self.upjanela)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Sair",command=self.sairjanela)
        self.menubar.add_cascade(label="New",menu=self.filemenu)

        self.menubar.add_separator()

        self.helpmenu=Menu(self.menubar,tearoff=0)
        self.helpmenu.add_command(label="Sobre",command=self.upsobre)
        self.menubar.add_cascade(label="Info",menu=self.helpmenu)

        self.root.configure(menu=self.menubar)
        self.root.mainloop()



        self.root.mainloop()


try:
    mainprograma()
except:
    raise Exception("Nao pode ser criado essa janela no maintela")
