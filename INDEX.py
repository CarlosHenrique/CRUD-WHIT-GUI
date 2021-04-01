from tkinter import *   
from tkinter import ttk
from tkinter import messagebox

import students
import subj
import teachers
import classes
import sqlite3
CPF_T = []
CPF_S = []

class mainwindow():
    
 # ---------- DEFS ENTRADA E SAIDA MENU   ----------------

    def entry_class(self):
        self.FrameClass.place(x=210,y=0)
        self.FrameMain.place(x=1000,y=0)

    def entry_subject(self):
        self.FrameMain.place(x=1000,y=0)
        self.FrameSubject.place(x=210,y=0)

    def entry_teacher(self):
        self.FrameMain.place(x=1000,y=1000)
        self.FrameTeacher.place(x=210,y=0)

    def entry_student(self):
        self.FrameMain.place(x=1000,y=0)
        self.FrameStudent.place(x=210,y=0)

    def back_to_main(self):
        self.FrameStudent.place(x=1000,y=1000)
        self.FrameTeacher.place(x=1000,y=1000)
        self.FrameSubject.place(x=1000,y=1000)
        self.FrameClass.place(x=1000,y=1000)
        self.FrameMain.place(x=210,y=0)

# ------------ DEF DE ENTRADA REGISTRO ---------
    def entry_register_teacher(self):
        self.FrameTeacher.place(x=1000,y=0)
        self.RegisterTeacher_Frame.place(x=210,y=0)

    def entry_register_student(self):
        self.FrameStudent.place(x=1000,y=0)
        self.RegisterStudent_Frame.place(x=210,y=0)
    
    def entry_register_subject(self):
        self.FrameSubject.place(x=1000,y=0)
        self.RegisterSubject_Frame.place(x=210,y=0)

    def entry_register_class(self):
        self.FrameClass.place(x=1000,y=0)
        self.RegisterClass_Frame.place(x=210,y=0)
    def entry_insert_class(self):
        self.RegisterClass_Frame.place(x=1000)
        self.RegisterClass2_Frame.place(x=210,y=0)
    
 

# ----------- DEF DE ENTRADA CONSULTA ----------
    def entry_consult_teacher(self):
        self.ConsultTeacher_Frame.place(x=210,y=0)
        self.FrameTeacher.place(x=1000,y=0) 
        
    def entry_consult_student(self):
        self.ConsultStudent_Frame.place(x=210,y=0)
        self.FrameStudent.place(x=1000,y=0)
    def entry_consult_subject(self):
        self.ConsultSubject_Frame.place(x=210,y=0)
        self.FrameSubject.place(x=1000,y=0)
    def entry_consult_class(self):
        self.ConsultClass_Frame.place(x=210)
        self.FrameClass.place(x=1000)

# ----------- DEF DE ENTRADA ATT ------------
    def entry_att_teacher(self):
        self.AttTeacher_Frame.place(x=210,y=0)
        self.FrameTeacher.place(x=1000,y=0)
    def entry_att_student(self):
        self.AttStudent_Frame.place(x=210,y=0)
        self.FrameStudent.place(x=1000,y=0)
    def entry_att_subject(self):
        self.AttSubject_Frame.place(x=210,y=0)
        self.FrameSubject.place(x=1000,y=0)
    def entry_att_class(self):
        self.AttClass_Frame.place(x=210,y=0)
        self.FrameClass.place(x=1000,y=0)
    def entry_att_class2(self):
        self.AttClass2_Frame.place(x=210,y=0)
        self.FrameClass.place(x=1000,y=0)
# -------------- DEF DE ENTRADA REMOVER ====-====
    def entry_remove_teacher(self):
        self.RemoveTeacher_Frame.place(x=210,y=0)
        self.FrameTeacher.place(x=1000,y=0)
    def entry_remove_student(self):
        self.RemoveStudent_Frame.place(x=210,y=0)
        self.FrameStudent.place(x=1000,y=0)
    def entry_remove_subject(self):
        self.RemoveSubject_Frame.place(x=210,y=0)
        self.FrameSubject.place(x=1000,y=0)
    def entry_remove_class(self):
        self.RemoveClass_Frame.place(x=210,y=0)
        self.FrameClass.place(x=1000,y=0)

# --------------- DEF DE SAIDA DAS OPÇOES DO MENU -------------------
    def back_to_FrameTeacher(self):
        self.RegisterTeacher_Frame.place(x=1000,y=0)
        self.RemoveTeacher_Frame.place(x=1000,y=0)
        self.AttTeacher_Frame.place(x=1000,y=0)
        self.ConsultTeacher_Frame.place(x=1000,y=0)
        self.FrameTeacher.place(x=210)
    def back_to_FrameStudent(self):
        self.RegisterStudent_Frame.place(x=1000,y=0)
        self.RemoveStudent_Frame.place(x=1000,y=0)
        self.AttStudent_Frame.place(x=1000,y=0)
        self.ConsultStudent_Frame.place(x=1000,y=0)
        self.FrameStudent.place(x=210)
    def back_to_FrameSubject(self):
        self.RegisterSubject_Frame.place(x=1000,y=0)
        self.RemoveSubject_Frame.place(x=1000,y=0)
        self.AttSubject_Frame.place(x=1000,y=0)
        self.ConsultSubject_Frame.place(x=1000,y=0)
        self.FrameSubject.place(x=210)
    def back_to_FrameClass(self):
        self.RegisterClass_Frame.place(x=1000)
        self.FrameClass.place(x=210)
        self.ConsultClass_Frame.place(x=1000)
        self.RegisterClass2_Frame.place(x=1000)
        self.AtaClass_Frame.place(x=1000)
        self.RemoveClass_Frame.place(x=1000)
        self.AttClass_Frame.place(x=1000)
      

# ------------- VALIDAÇÂO ------------
    def ValidationTeacher(self):
        test = self.entrycpf_RegisterTeacher.get()
        if test.isnumeric and len(test)==11:
            return True
        else: 
            return False
    def ValidationStudent(self):
        test = self.entrycpf_RegisterStudent.get()
        if test.isnumeric and len(test)==11:
            return True
        else: 
            return False

    def ValidationSubject(self):
        test = self.entrycod_RegisterSubject.get()
        if test.isnumeric and len(test)==5:
            return True
        else: 
            return False
# ------------ CADASTROS ---------------
   
    def RegisterTeacher(self):
        if self.ValidationTeacher() is True:

            Cpf = self.entrycpf_RegisterTeacher.get()
            Name = self.entryname_RegisterTeacher.get()
            Departamento = self.entrydept_RegisterTeacher.get()
            teachers.cursor.execute(""" INSERT INTO professores(Cpf,Name,Departamento)VALUES(?,?,?)""",(Cpf,Name,Departamento))
            teachers.conn.commit()
            messagebox.showinfo(title='Cadastro',message='Professor cadastrado com sucesso!')
            self.entrycpf_RegisterTeacher.delete(0,END)
            self.entryname_RegisterTeacher.delete(0,END)
            self.entrydept_RegisterTeacher.delete(0,END)
        else:
            messagebox.showerror('CPF INVÁLIDO','Informe um CPF válido!')
            self.entrycpf_RegisterTeacher.delete(0,END)
            

    def RegisterStudent(self):
        if self.ValidationStudent() == True:
            Cpf = self.entrycpf_RegisterStudent.get()
            Name = self.entryname_RegisterStudent.get()
            students.cursor.execute("""INSERT INTO alunos(Cpf,Name)VALUES(?,?)""",(Cpf,Name))
            students.conn.commit()
        
       
            messagebox.showinfo('Cadastro', 'Aluno cadastrado com sucesso!')
            self.entryname_RegisterStudent.delete(0, END)
            self.entrycpf_RegisterStudent.delete(0, END)
        else:
            messagebox.showerror('CPF INVÁLIDO','Informe um CPF válido!')
            self.entrycpf_RegisterStudent.delete(0, END)
            

    def RegisterSubject(self):
        if self.ValidationSubject() is True:

            Code = self.entrycod_RegisterSubject.get()
            Name = self.entryname_RegisterSubject.get()
            subj.cursor.execute("""INSERT INTO misera (Id,Materia)VALUES(?,?)""",(Code,Name))
            subj.conn.commit()
        
            self.entrycod_RegisterSubject.delete(0,END)
            self.entryname_RegisterSubject.delete(0,END)
            
    
       
            messagebox.showinfo('Cadastro', 'Disciplina cadastrada com sucesso!')
        else:
            messagebox.showerror('CÓDIGO INVÁLIDO','Informe um código válido!')
            self.entrycod_RegisterSubject.delete(0,END)
        

    def RegisterClass(self):
            Id =   self.entrycodeclass_RegisterClass.get()
            Periodo = self.entryperiod_RegisterClass.get()
            Materia = self.entrycodesub_RegisterClass.get()
          
            classes.cursor.execute("""
            INSERT INTO turmas(Id,Materia,Periodo)VALUES(?,?,?)
            """,(Id,Materia,Periodo))
            classes.conn.commit()
            messagebox.showinfo(title='Cadastro',message='Turma cadastrada com sucesso')

            
            
    def Teacher_RegisterClass2(self):
        CPF_T.append(self.entrycpft_RegisterClass2.get())
        self.entrycpft_RegisterClass2.delete(0,END)


    def Student_RegisterClass2(self):
        CPF_S.append(self.entrycpfs_RegisterClass2.get())
        self.entrycpfs_RegisterClass2.delete(0,END)

    def RegisterAll_Class2(self):
            
        classes.cursor.execute("""UPDATE turmas SET Professor= ?, Aluno = ? WHERE Id = ?""",(('-'.join(CPF_T)),'-'.join(CPF_S),self.entrycodeclass_RegisterClass.get()))
        classes.conn.commit()
        messagebox.showinfo(title='Cadastro',message='Turma cadastrada com sucesso')
        self.entrycodeclass_RegisterClass.delete(0,END)
        self.entryperiod_RegisterClass.delete(0,END)
        self.entrycodesub_RegisterClass.delete(0,END)
        
        
        
        
   
       
# ---------------- CONSULTAS ---------------
    def ConsultTeacher(self):
        
        self.listbox_ConsultTeacher.delete(0,END)
        self.listbox_ConsultTeacher.delete(1,END)
        
     
        conn = sqlite3.connect('professores.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM professores WHERE Cpf = ?''',(self.entrycpf_ConsultTeacher.get(),))
        listp = cursor.fetchone()
        self.listbox_ConsultTeacher.insert(0,'-'*20+'|CPF|'+'-'*5+'|Nome|'+'-'*5+'|DEPT|'+'-'*100)
        self.listbox_ConsultTeacher.insert(1, '-'*15+" | ".join(listp)+'-'*100)
        self.entrycpf_ConsultTeacher.delete(0,END)

        
    
    def ConsultStudent(self):
        self.listbox_ConsultStudent.delete(0,END)
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM alunos WHERE Cpf = ?''',(self.entrycpf_ConsultStudent.get(),))
        lista = cursor.fetchone()
        self.listbox_ConsultStudent.insert(0,'-'*20+'|CPF|'+'-'*5+'|Nome|'+'-'*100)
        self.listbox_ConsultStudent.insert(1, '-'*15+" | ".join(lista)+'-'*100)
        self.entrycpf_ConsultStudent.delete(0,END)
       
        
    
    def ConsultSubject(self):
        
        self.listbox_ConsultSubject.delete(0,END)
        conn = sqlite3.connect('misera.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM misera WHERE Id = ?''',(self.entrycodd_ConsultSubject.get(),))
        lista = cursor.fetchone()
        self.listbox_ConsultSubject.insert(0, '-'+'-'*15+'| Código |----------| Nome |'+'-'*30)
        self.listbox_ConsultSubject.insert(1, '-'*20+'|'+" | ".join(lista)+'|'+'-'*100)
        self.entrycodd_ConsultSubject.delete(0,END)
        
        
        
        
    
    def ConsultClass(self):
        self.listbox_ConsultClass.delete(0,END)
        conn = sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM turmas WHERE Id = ?''',(self.entrycodeclass_ConsultClass.get(),))
        listt = cursor.fetchone()
        self.listbox_ConsultClass.insert(0,listt[0]+ " -|- "+listt[1]+" -|- "+listt[2])
        self.listbox_ConsultClass.insert(1,'Professores')
        for i in listt[3].split('-'):
            self.listbox_ConsultClass.insert(2,i)
        self.listbox_ConsultClass.insert(3,'Alunos')
        for i in listt[4].split('-'):
            self.listbox_ConsultClass.insert(4,i)
            
        self.entrycodeclass_ConsultClass.delete(0,END)

    
    def ATA_Class(self):
        self.listbox_AtaClass.delete(0,END)
        conn = sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM turmas WHERE Id = ?''',(self.entrycodeclass_AtaClass.get(),))
        listt = cursor.fetchone()
        self.listbox_AtaClass.insert(0,'LISTA DE EXERCICIO')
        self.listbox_AtaClass.insert(1,listt[0]+ " -|- "+listt[1]+" -|- "+listt[2])
        self.listbox_AtaClass.insert(2,'Professores')
        for i in listt[3].split('-'):
            self.listbox_AtaClass.insert(3,i)
        self.listbox_AtaClass.insert(4,'Alunos')
        for i in listt[4].split('-'):
            self.listbox_AtaClass.insert(5,i)
            
        self.entrycodeclass_AtaClass.delete(0,END)

    def entry_ata_class(self):
        self.AtaClass_Frame.place(x=210,y=0)
        self.FrameClass.place(x=1000,y=0)




        
      
# ---------  ATUALIZAR ------------
    def VerifyAttTeacher(self):
        conn=sqlite3.connect('professores.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM professores WHERE Cpf = ?''',(self.entrycpf_AttTeacher.get(),))
        var = cursor.fetchone()
        self.entryname_AttTeacher.insert(0,var[1])
        self.entrynewcpf_AttTeacher.insert(0,var[0])
        self.entrydept_AttTeacher.insert(0,var[2])

    def VerifyAttStudent(self):
        conn=sqlite3.connect('alunos.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM alunos WHERE Cpf = ?''',(self.entrycpf_AttStudent.get(),))
        var = cursor.fetchone()
        self.entryname_AttStudent.insert(0,var[1])
        self.entrynewcpf_AttStudent.insert(0,var[0])

    def VerifyAttSubject(self):
        conn=sqlite3.connect('misera.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM misera WHERE Id= ?''',(self.entrycod_AttSubject.get(),))
        var = cursor.fetchone()
        self.entryname_AttSubject.insert(0,var[1])
        self.entrynewcod_AttSubject.insert(0,var[0])
    
    def VerifyAttClass(self):
        conn=sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM turmas WHERE Id= ?''',(self.entrycodeclass_AttClass.get(),))
        var = cursor.fetchone()
        self.entrynewcodeclass_AttClass.insert(0,var[0])
        self.entrycodesub_AttClass.insert(0,var[1])
        self.entryperiod_AttClass.insert(0,var[2])
    
    def Teacher_VerifyAttClass2(self):
        conn = sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cursor.execute(''' SELECT Professor FROM turmas WHERE Id = ?''',(self.entrynewcodeclass_AttClass.get(),))
        var = cursor.fetchone()
        
       
        
     

    def Student_VerifyAttClass2(self):
        conn = sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cursor.execute(''' SELECT Alunos FROM turmas WHERE Id = ?''',(self.entrynewcodeclass_AttClass.get(),))
        var = cursor.fetchone()
        self.entrynewcpfs_AttClass2.insert(0,var)
        cursor.execute('''DELETE FROM turmas WHERE Professor = ?''',(self.entrycpfs_AttClass2_AttClass2.get()))
        conn.commit()

    def AttTeacher(self):
        conn=sqlite3.connect('professores.db')
        cursor = conn.cursor()
        Cpf = self.entrynewcpf_AttTeacher.get()
        Nome = self.entryname_AttTeacher.get()
        Departamento = self.entrydept_AttTeacher.get()
        OldCpf = self.entrycpf_AttTeacher.get()
        cursor.execute("""UPDATE professores SET Cpf = ?, Name = ?,
        Departamento = ? WHERE Cpf=?""",(Cpf,Nome,Departamento,OldCpf))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Atualizar',message='Atualizado com sucesso')
        self.entrynewcpf_AttTeacher.delete(0,END)
        self.entryname_AttTeacher.delete(0,END)
        self.entrydept_AttTeacher.delete(0,END)
        self.entrycpf_AttTeacher.delete(0,END)

    def AttStudent(self):
        conn=sqlite3.connect('alunos.db')
        cursor = conn.cursor()
        Cpf = self.entrynewcpf_AttStudent.get()
        Nome = self.entryname_AttStudent.get()
        OldCpf = self.entrycpf_AttStudent.get()
        cursor.execute("""UPDATE alunos SET Cpf = ?, Name = ? WHERE Cpf=?""",(Cpf,Nome,OldCpf))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Atualizar',message='Atualizado com sucesso')
        self.entrynewcpf_AttStudent.delete(0,END)
        self.entryname_AttStudent.delete(0,END)
        self.entrycpf_AttStudent.delete(0,END)

    def AttSubject(self):
        conn=sqlite3.connect('misera.db')
        cursor = conn.cursor()
        Cpf = self.entrynewcod_AttSubject.get()
        Nome = self.entryname_AttSubject.get()
        OldCpf = self.entrycod_AttSubject.get()
        cursor.execute("""UPDATE misera SET Id = ?, Materia = ? WHERE Id=?""",(Cpf,Nome,OldCpf))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Atualizar',message='Atualizado com sucesso')
        self.entrynewcod_AttSubject.delete(0,END)
        self.entryname_AttSubject.delete(0,END)
        self.entrycod_AttSubject.delete(0,END)

    def AttClass(self):
        conn=sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        old_Id = self.entrycodeclass_AttClass.get()
        Id =   self.entrynewcodeclass_AttClass.get()
        Periodo = self.entryperiod_AttClass.get()
        Materia = self.entrycodesub_AttClass.get()
          
        cursor.execute("""UPDATE turmas SET Id = ?, Materia = ?, Periodo = ? WHERE Id=?""",(Id,Materia,Periodo,old_Id))
        conn.commit()
        messagebox.showinfo(title='Cadastro',message='Turma atualizada com sucesso')


# ------------------REMOVER ------------

    def RemoveTeacher(self):
        conn = sqlite3.connect('professores.db')
        cursor = conn.cursor()
        Cpf = self.entrycpf_RemoveTeacher.get()
        cursor.execute("""DELETE FROM professores WHERE Cpf= ?""",(Cpf,))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Remover',message='Deletado com sucesso')
        self.entrycpf_RemoveTeacher.delete(0,END)


    def RemoveStudent(self):
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()
        Cpf = self.entrycpf_RemoveStudent.get()
        cursor.execute("""DELETE FROM alunos WHERE Cpf= ?""",(Cpf,))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Remover',message='Removido com sucesso')
        self.entrycpf_RemoveStudent.delete(0,END)
    def RemoveSubject(self):
        conn = sqlite3.connect('misera.db')
        cursor = conn.cursor()
        Cpf = self.entrycod_RemoveSubject.get()
        cursor.execute("""DELETE FROM misera WHERE Id= ?""",(Cpf,))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Remover',message='Removido com sucesso')
        self.entrycod_RemoveSubject.delete(0,END)

    def RemoveClass(self):
        conn = sqlite3.connect('turmas.db')
        cursor = conn.cursor()
        cod = self.entrycod_RemoveClass.get()
        cursor.execute("""DELETE FROM turmas WHERE Id= ?""",(cod,))
        conn.commit()
        conn.close()
        messagebox.showinfo(title='Remover',message='Removido com sucesso')
        self.entrycod_RemoveClass.delete(0,END)

# --------- DEF MAIN ---------------

    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x300+450+200')
        self.root.configure(bg='midnightblue')
        self.root.resizable(False,False)
        self.root.protocol('WM_DELETE_WINDOW')
        self.root.iconbitmap('icons/logoicon.ico')
        self.root.title('SCAS - Sistema de Controle Acadêmico Simplificado')
        self.img= PhotoImage(file='icons/logo.png')
        self.panel = Label(self.root,image=self.img,bg='midnightblue')
        self.panel.place(x=0,y=0)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------        
        #LABEL FRAME MENU PRINCIPAL
        self.FrameMain = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.FrameMain.propagate(0)
        self.FrameMain.place(x=210,y=0)
        self.lb1_main=Label(self.FrameMain,text='Sistema de Controle\nAcadêmico Simplificado',font='system 20',bg='midnightblue',fg='white')
        self.lb1_main.place(x=50,y=0)
        self.lb2_main=Label(self.FrameMain,bg='white',height=700,width=0)
        self.lb2_main.place(x=10,y=0)
        self.lb3_main=Label(self.FrameMain,text='Escolha uma opção:',font='system 10',bg='midnightblue',fg='white')
        self.lb3_main.place(x=130,y=70)
        
        self.BTteacher = Button(self.FrameMain,text='Professores',width=15,command=self.entry_teacher)
        self.BTteacher.place(x=50,y=120)
        self.BTstudent = Button(self.FrameMain,text='Alunos',width=15,command=self.entry_student)
        self.BTstudent.place(x=250,y=120)
        self.BTsubject = Button(self.FrameMain,text='Disciplinas',width=15,command=self.entry_subject)
        self.BTsubject.place(x=50,y=200)
        self.BTclass = Button(self.FrameMain,text='Turmas',width=15,command=self.entry_class)
        self.BTclass.place(x=250,y=200)
        self.BTexit = Button(self.FrameMain,text='Sair',width=10,command=self.root.destroy)
        self.BTexit.place(x=168,y=260)
#-----------------------------------------------------------------------------------------------------------------
        # MENU FRAME PROFESSORES
        self.FrameTeacher = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.lb1_Teacher = Label(self.FrameTeacher,text='Bem vindo ao\nMenu Professores',font='system 20',bg='midnightblue',fg='white')
        self.lb1_Teacher.place(x=85,y=0)
        self.lb2_Teacher = Label(self.FrameTeacher,bg='white',height=700,width=0)
        self.lb2_Teacher.place(x=10,y=0)
        self.lb3_Teacher = Label(self.FrameTeacher,text='Escolha uma opção:',font='system 10',bg='midnightblue',fg='white')
        self.lb3_Teacher.place(x=130,y=70)
        
        self.BTt_register = Button(self.FrameTeacher,text='Cadastrar',width=15,command=self.entry_register_teacher)
        self.BTt_register.place(x=50,y=120)
        self.BTt_consult = Button(self.FrameTeacher,text='Consultar',width=15,command=self.entry_consult_teacher)
        self.BTt_consult.place(x=250,y=120)
        self.BTt_att = Button(self.FrameTeacher,text='Atualizar',width=15,command=self.entry_att_teacher)
        self.BTt_att.place(x=50,y=200)
        self.BTt_remove = Button(self.FrameTeacher,text='Remover',width=15,command=self.entry_remove_teacher)
        self.BTt_remove.place(x=250,y=200)
        self.BTt_back = Button(self.FrameTeacher,text='Voltar',width=10,command=self.back_to_main)
        self.BTt_back.place(x=168,y=260)
        self.FrameTeacher.place(x=1000,y=1000)

        # REGISTRO PROFESSORES
        self.RegisterTeacher_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RegisterTeacher_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RegisterTeacher = Label(self.RegisterTeacher_Frame,bg='white',height=700,width=0)
        self.bar_RegisterTeacher.place(x=10,y=0)
        self.info_RegisterTeacher = Label(self.RegisterTeacher_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_RegisterTeacher.place(x=65,y=10)
        self.name_RegisterTeacher = Label(self.RegisterTeacher_Frame,text='Nome:',font='system 15',fg='white',bg='midnightblue')
        self.name_RegisterTeacher.place(x=20,y=110)
        self.cpf_RegisterTeacher = Label(self.RegisterTeacher_Frame,text='CPF:',font='system 15',fg='white',bg='midnightblue')
        self.cpf_RegisterTeacher.place(x=20,y=140)
        self.dept_RegisterTeacher = Label(self.RegisterTeacher_Frame,text='Departamento:',font='system 15',fg='white',bg='midnightblue')
        self.dept_RegisterTeacher.place(x=20,y=170)
                    #ENTRY
        self.entryname_RegisterTeacher = Entry(self.RegisterTeacher_Frame,font='ariel 10',width=40)
        self.entryname_RegisterTeacher.place(x=70,y=110)
        self.entrycpf_RegisterTeacher = Entry(self.RegisterTeacher_Frame,font='ariel 10',width=40)
        self.entrycpf_RegisterTeacher.place(x=70,y=140)
        self.entrydept_RegisterTeacher = Entry(self.RegisterTeacher_Frame,font='ariel 10',width=31)
        self.entrydept_RegisterTeacher.place(x=130,y=170)
             #BUTTONS
        self.BTconfirm_RegisterTeacher = Button(self.RegisterTeacher_Frame,text='Registrar',width=15,command=self.RegisterTeacher)
        self.BTconfirm_RegisterTeacher.place(x=50,y=250)
        self.BTback_RegisterTeacher = Button(self.RegisterTeacher_Frame,text='Voltar',width=15,command=self.back_to_FrameTeacher)
        self.BTback_RegisterTeacher.place(x=240,y=250)

        # def cadastro prof
        

        # CONSULTA DE PROFESSORES
        self.ConsultTeacher_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.ConsultTeacher_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_ConsultTeacher = Label(self.ConsultTeacher_Frame,bg='white',height=700,width=0)
        self.bar_ConsultTeacher.place(x=10,y=0)
        self.info_ConsultTeacher = Label(self.ConsultTeacher_Frame,text='Insira o CPF que\ndeseja consultar:',font='system 18',bg='midnightblue',fg='white')
        self.info_ConsultTeacher.place(x=80,y=10)
        self.cpf_ConsultTeacher=Label(self.ConsultTeacher_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_ConsultTeacher.place(x=40,y=90)
                    #ENTRY
        self.entrycpf_ConsultTeacher = Entry(self.ConsultTeacher_Frame,font='ariel 10',width=40)
        self.entrycpf_ConsultTeacher.place(x=80,y=90)
                    #BUTTONS
        self.BTconfirm_ConsultTeacher = Button(self.ConsultTeacher_Frame,text='Consultar',width=10,command=self.ConsultTeacher)
        self.BTconfirm_ConsultTeacher.place(x=50,y=260)
        self.BTback_ConsultTeacher = Button(self.ConsultTeacher_Frame,text='Voltar',width=10,command=self.back_to_FrameTeacher)
        self.BTback_ConsultTeacher.place(x=260,y=260)
                    #LIST BOX
        self.listbox_ConsultTeacher = Listbox(self.ConsultTeacher_Frame,selectbackground= 'gray15', font='System 15', width='40', height='7',bg='gray70',fg='gray10')
        self.listbox_ConsultTeacher.place(x=40,y=120)


        # ATUALIZAR PROFESSORES FRAME

        self.AttTeacher_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.AttTeacher_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_AttTeacher = Label(self.AttTeacher_Frame,bg='white',height=700,width=0)
        self.bar_AttTeacher.place(x=10,y=0)
        self.info_AttTeacher = Label(self.AttTeacher_Frame,text='Insira o CPF que\ndeseja atualizar:',font='system 18',bg='midnightblue',fg='white')
        self.info_AttTeacher.place(x=90,y=10)
        self.cpf_AttTeacher=Label(self.AttTeacher_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_AttTeacher.place(x=100,y=85)
        self.info2_AttTeacher = Label(self.AttTeacher_Frame,text='Confira e atualize as informações desejadas abaixo:',font='system 10',bg='midnightblue',fg='white')
        self.info2_AttTeacher.place(x=30,y=120)
        self.name_AttTeacher = Label(self.AttTeacher_Frame,text='Nome:',font='system 15',bg='midnightblue',fg='white')
        self.name_AttTeacher.place(x=30,y=150)
        self.newcpf_AttTeacher = Label(self.AttTeacher_Frame,text='CPF',font='system 15',bg='midnightblue',fg='white')
        self.newcpf_AttTeacher.place(x=30,y=180)
        self.dept_AttTeacher = Label(self.AttTeacher_Frame,text='DEPT:',font='system 15',bg='midnightblue',fg='white')
        self.dept_AttTeacher.place(x=30,y=210)
                    #ENTRY
        self.entrycpf_AttTeacher = Entry(self.AttTeacher_Frame,font='ariel 10',width=18)
        self.entrycpf_AttTeacher.place(x=140,y=85)
        self.entryname_AttTeacher = Entry(self.AttTeacher_Frame,font='ariel 10',width=18)
        self.entryname_AttTeacher.place(x=80,y=150)
        self.entrynewcpf_AttTeacher = Entry(self.AttTeacher_Frame,font='ariel 10',width=18)
        self.entrynewcpf_AttTeacher.place(x=80,y=180)
        self.entrydept_AttTeacher = Entry(self.AttTeacher_Frame,font='ariel 10',width=18)
        self.entrydept_AttTeacher.place(x=80,y=210)
                    #BUTTONS
        self.BTverify_AttTeacher = Button(self.AttTeacher_Frame,text='Verificar',width=8,command=self.VerifyAttTeacher)
        self.BTverify_AttTeacher.place(x=280,y=82)
        self.BTconfirm_AttTeacher = Button(self.AttTeacher_Frame,text='Atualizar',width=15,command=self.AttTeacher)
        self.BTconfirm_AttTeacher.place(x=50,y=250)
        self.BTback_AttTeacher = Button(self.AttTeacher_Frame,text='Voltar',width=15,command=self.back_to_FrameTeacher)
        self.BTback_AttTeacher.place(x=240,y=250)

        # FRAME REMOVER PROFESSORES 
        self.RemoveTeacher_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RemoveTeacher_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RemoveTeacher = Label(self.RemoveTeacher_Frame,bg='white',height=700,width=0)
        self.bar_RemoveTeacher.place(x=10,y=0)
        self.info_RemoveTeacher = Label(self.RemoveTeacher_Frame,text='Insira o CPF que\ndeseja remover:',font='system 18',bg='midnightblue',fg='white')
        self.info_RemoveTeacher.place(x=90,y=10)
        self.cpf_RemoveTeacher=Label(self.RemoveTeacher_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_RemoveTeacher.place(x=40,y=110)
                    #ENTRY
        self.entrycpf_RemoveTeacher = Entry(self.RemoveTeacher_Frame,font='ariel 10',width=40)
        self.entrycpf_RemoveTeacher.place(x=80,y=110)
                    #BUTTONS
        self.BTconfirm_RemoveTeacher = Button(self.RemoveTeacher_Frame,text='Remover',width=15,command=self.RemoveTeacher)
        self.BTconfirm_RemoveTeacher.place(x=50,y=250)
        self.BTback_RemoveTeacher = Button(self.RemoveTeacher_Frame,text='Voltar',width=15,command=self.back_to_FrameTeacher)
        self.BTback_RemoveTeacher.place(x=240,y=250)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
        # LABEL FRAME ALUNOS

        self.FrameStudent = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.lb1_Student = Label(self.FrameStudent,text='Bem vindo ao\nMenu Alunos',font='system 20',bg='midnightblue',fg='white')
        self.lb1_Student.place(x=115,y=0)
        self.lb2_Student = Label(self.FrameStudent,bg='white',height=700,width=0)
        self.lb2_Student.place(x=10,y=0)
        self.lb3_Student = Label(self.FrameStudent,text='Escolha uma opção:',font='system 10',bg='midnightblue',fg='white')
        self.lb3_Student.place(x=130,y=70)
        
        self.BTst_register = Button(self.FrameStudent,text='Cadastrar',width=15,command=self.entry_register_student)
        self.BTst_register.place(x=50,y=120)
        self.BTst_consult = Button(self.FrameStudent,text='Consultar',width=15,command=self.entry_consult_student)
        self.BTst_consult.place(x=250,y=120)
        self.BTst_att = Button(self.FrameStudent,text='Atualizar',width=15,command=self.entry_att_student)
        self.BTst_att.place(x=50,y=200)
        self.BTst_remove = Button(self.FrameStudent,text='Remover',width=15,command=self.entry_remove_student)
        self.BTst_remove.place(x=250,y=200)
        self.BTst_back = Button(self.FrameStudent,text='Voltar',width=10,command=self.back_to_main)
        self.BTst_back.place(x=168,y=260)
        self.FrameStudent.place(x=1000,y=1000)
        # REGISTRO DE ALUNOS

        self.RegisterStudent_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RegisterStudent_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RegisterStudent = Label(self.RegisterStudent_Frame,bg='white',height=700,width=0)
        self.bar_RegisterStudent.place(x=10,y=0)
        self.info_RegisterStudent = Label(self.RegisterStudent_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_RegisterStudent.place(x=65,y=10)
        self.name_RegisterStudent = Label(self.RegisterStudent_Frame,text='Nome:',font='system 15',fg='white',bg='midnightblue')
        self.name_RegisterStudent.place(x=20,y=110)
        self.cpf_RegisterStudent = Label(self.RegisterStudent_Frame,text='CPF:',font='system 15',fg='white',bg='midnightblue')
        self.cpf_RegisterStudent.place(x=20,y=140)
        
                    #ENTRY
        self.entryname_RegisterStudent = Entry(self.RegisterStudent_Frame,font='ariel 10',width=40)
        self.entryname_RegisterStudent.place(x=70,y=110)
        self.entrycpf_RegisterStudent = Entry(self.RegisterStudent_Frame,font='ariel 10',width=40)
        self.entrycpf_RegisterStudent.place(x=70,y=140)
        
             #BUTTONS
        self.BTconfirm_RegisterStudent = Button(self.RegisterStudent_Frame,text='Registrar',width=15,command=self.RegisterStudent)
        self.BTconfirm_RegisterStudent.place(x=50,y=250)
        self.BTback_RegisterStudent = Button(self.RegisterStudent_Frame,text='Voltar',width=15,command=self.back_to_FrameStudent)
        self.BTback_RegisterStudent.place(x=240,y=250)

        # CONSULTA DE ALUNOS
         
        self.ConsultStudent_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.ConsultStudent_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_ConsultStudent = Label(self.ConsultStudent_Frame,bg='white',height=700,width=0)
        self.bar_ConsultStudent.place(x=10,y=0)
        self.info_ConsultStudent = Label(self.ConsultStudent_Frame,text='Insira o CPF que\ndeseja consultar:',font='system 18',bg='midnightblue',fg='white')
        self.info_ConsultStudent.place(x=80,y=10)
        self.cpf_ConsultStudent=Label(self.ConsultStudent_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_ConsultStudent.place(x=40,y=90)
                    #ENTRY
        self.entrycpf_ConsultStudent = Entry(self.ConsultStudent_Frame,font='ariel 10',width=40)
        self.entrycpf_ConsultStudent.place(x=80,y=90)
                    #BUTTONS
        self.BTconfirm_ConsultStudent = Button(self.ConsultStudent_Frame,text='Consultar',width=10,command=self.ConsultStudent)
        self.BTconfirm_ConsultStudent.place(x=50,y=260)
        self.BTback_ConsultStudent = Button(self.ConsultStudent_Frame,text='Voltar',width=10,command=self.back_to_FrameStudent)
        self.BTback_ConsultStudent.place(x=260,y=260)
                    #LIST BOX
        self.listbox_ConsultStudent = Listbox(self.ConsultStudent_Frame,selectbackground= 'gray15', font='System 15', width='40', height='7',bg='gray70',fg='gray10')
        self.listbox_ConsultStudent.place(x=40,y=120)

        # ATUALIZAR ALUNOS
        self.AttStudent_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.AttStudent_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_AttStudent = Label(self.AttStudent_Frame,bg='white',height=700,width=0)
        self.bar_AttStudent.place(x=10,y=0)
        self.info_AttStudent = Label(self.AttStudent_Frame,text='Insira o CPF que\ndeseja atualizar:',font='system 18',bg='midnightblue',fg='white')
        self.info_AttStudent.place(x=90,y=10)
        self.cpf_AttStudent=Label(self.AttStudent_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_AttStudent.place(x=100,y=85)
        self.info2_AttStudent = Label(self.AttStudent_Frame,text='Confira e atualize as informações desejadas abaixo:',font='system 10',bg='midnightblue',fg='white')
        self.info2_AttStudent.place(x=30,y=120)
        self.name_AttStudent = Label(self.AttStudent_Frame,text='Nome:',font='system 15',bg='midnightblue',fg='white')
        self.name_AttStudent.place(x=30,y=150)
        self.newcpf_AttStudent = Label(self.AttStudent_Frame,text='CPF',font='system 15',bg='midnightblue',fg='white')
        self.newcpf_AttStudent.place(x=30,y=180)
       
                    #ENTRY
                
        self.entrycpf_AttStudent = Entry(self.AttStudent_Frame,font='ariel 10',width=18)
        self.entrycpf_AttStudent.place(x=140,y=85)
        self.entryname_AttStudent = Entry(self.AttStudent_Frame,font='ariel 10',width=18)
        self.entryname_AttStudent.place(x=80,y=150)
        self.entrynewcpf_AttStudent = Entry(self.AttStudent_Frame,font='ariel 10',width=18)
        self.entrynewcpf_AttStudent.place(x=80,y=180)
        
                    #BUTTONS
        self.BTverify_AttStudent = Button(self.AttStudent_Frame,text='Verificar',width=8,command=self.VerifyAttStudent)
        self.BTverify_AttStudent.place(x=280,y=82)
        self.BTconfirm_AttStudent = Button(self.AttStudent_Frame,text='Atualizar',width=15,command=self.AttStudent)
        self.BTconfirm_AttStudent.place(x=50,y=250)
        self.BTback_AttStudent = Button(self.AttStudent_Frame,text='Voltar',width=15,command=self.back_to_FrameStudent)
        self.BTback_AttStudent.place(x=240,y=250)

        #REMOVER ALUNOS
        self.RemoveStudent_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RemoveStudent_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RemoveStudent = Label(self.RemoveStudent_Frame,bg='white',height=700,width=0)
        self.bar_RemoveStudent.place(x=10,y=0)
        self.info_RemoveStudent = Label(self.RemoveStudent_Frame,text='Insira o CPF que\ndeseja remover:',font='system 18',bg='midnightblue',fg='white')
        self.info_RemoveStudent.place(x=90,y=10)
        self.cpf_RemoveStudent=Label(self.RemoveStudent_Frame,text='CPF:',font='system 15',bg='midnightblue',fg='white')
        self.cpf_RemoveStudent.place(x=40,y=110)
                    #ENTRY
        self.entrycpf_RemoveStudent = Entry(self.RemoveStudent_Frame,font='ariel 10',width=40)
        self.entrycpf_RemoveStudent.place(x=80,y=110)
                    #BUTTONS
        self.BTconfirm_RemoveStudent = Button(self.RemoveStudent_Frame,text='Consultar',width=15,command=self.RemoveStudent)
        self.BTconfirm_RemoveStudent.place(x=50,y=250)
        self.BTback_RemoveStudent = Button(self.RemoveStudent_Frame,text='Voltar',width=15,command=self.back_to_FrameStudent)
        self.BTback_RemoveStudent.place(x=240,y=250)



#-----------------------------------------------------------------------------------------------------------------------------------------------------
        # LABEL FRAME DISCIPLINAS
        self.FrameSubject = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.lb1_Subject = Label(self.FrameSubject,text='Bem vindo ao\nMenu Disciplinas',font='system 20',bg='midnightblue',fg='white')
        self.lb1_Subject.place(x=90,y=0)
        self.lb2_Subject = Label(self.FrameSubject,bg='white',height=700,width=0)
        self.lb2_Subject.place(x=10,y=0)
        self.lb3_Subject = Label(self.FrameSubject,text='Escolha uma opção:',font='system 10',bg='midnightblue',fg='white')
        self.lb3_Subject.place(x=130,y=70)
        
        self.BTsu_register = Button(self.FrameSubject,text='Cadastrar',width=15,command = self.entry_register_subject)
        self.BTsu_register.place(x=50,y=120)
        self.BTsu_consult = Button(self.FrameSubject,text='Consultar',width=15,command = self.entry_consult_subject)
        self.BTsu_consult.place(x=250,y=120)
        self.BTsu_att = Button(self.FrameSubject,text='Atualizar',width=15,command=self.entry_att_subject)
        self.BTsu_att.place(x=50,y=200)
        self.BTsu_remove = Button(self.FrameSubject,text='Remover',width=15,command=self.entry_remove_subject)
        self.BTsu_remove.place(x=250,y=200)
        self.BTsu_back = Button(self.FrameSubject,text='Voltar',width=10,command=self.back_to_main)
        self.BTsu_back.place(x=168,y=260)
        self.FrameSubject.place(x=1000,y=1000)

    # REGISTRO DE DISCIPLINAS
        self.RegisterSubject_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RegisterSubject_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RegisterSubject = Label(self.RegisterSubject_Frame,bg='white',height=700,width=0)
        self.bar_RegisterSubject.place(x=10,y=0)
        self.info_RegisterSubject = Label(self.RegisterSubject_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_RegisterSubject.place(x=65,y=10)
        self.name_RegisterSubject = Label(self.RegisterSubject_Frame,text='Nome:',font='system 15',fg='white',bg='midnightblue')
        self.name_RegisterSubject.place(x=20,y=110)
        self.cod_RegisterSubject = Label(self.RegisterSubject_Frame,text='Código:',font='system 15',fg='white',bg='midnightblue')
        self.cod_RegisterSubject.place(x=20,y=140)
        
                    #ENTRY
        self.entryname_RegisterSubject = Entry(self.RegisterSubject_Frame,font='ariel 10',width=40)
        self.entryname_RegisterSubject.place(x=80,y=110)
        self.entrycod_RegisterSubject = Entry(self.RegisterSubject_Frame,font='ariel 10',width=40)
        self.entrycod_RegisterSubject.place(x=80,y=140)
        
             #BUTTONS
        self.BTconfirm_RegisterSubject = Button(self.RegisterSubject_Frame,text='Registrar',width=15,command=self.RegisterSubject)
        self.BTconfirm_RegisterSubject.place(x=50,y=250)
        self.BTback_RegisterSubject = Button(self.RegisterSubject_Frame,text='Voltar',width=15,command=self.back_to_FrameSubject)
        self.BTback_RegisterSubject.place(x=240,y=250)
    
        # CONSULTA DISCIPLINAS
        self.ConsultSubject_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.ConsultSubject_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_ConsultSubject = Label(self.ConsultSubject_Frame,bg='white',height=700,width=0)
        self.bar_ConsultSubject.place(x=10,y=0)
        self.info_ConsultSubject = Label(self.ConsultSubject_Frame,text='Insira o código que\ndeseja consultar:',font='system 18',bg='midnightblue',fg='white')
        self.info_ConsultSubject.place(x=80,y=10)
        self.cod_ConsultSubject=Label(self.ConsultSubject_Frame,text='Código:',font='system 15',bg='midnightblue',fg='white')
        self.cod_ConsultSubject.place(x=40,y=90)
                    #ENTRY
        self.entrycodd_ConsultSubject = Entry(self.ConsultSubject_Frame,font='ariel 10',width=30)
        self.entrycodd_ConsultSubject.place(x=100,y=90)
                    #BUTTONS
        self.BTconfirm_ConsultSubject = Button(self.ConsultSubject_Frame,text='Consultar',width=10,command=self.ConsultSubject)
        self.BTconfirm_ConsultSubject.place(x=50,y=260)
        self.BTback_ConsultSubject = Button(self.ConsultSubject_Frame,text='Voltar',width=10,command=self.back_to_FrameSubject)
        self.BTback_ConsultSubject.place(x=260,y=260)
                    #LIST BOX
        self.listbox_ConsultSubject = Listbox(self.ConsultSubject_Frame,selectbackground= 'gray15', font='System 15', width='40', height='7',bg='gray70',fg='gray10')
        self.listbox_ConsultSubject.place(x=40,y=120)
       
        # ATUAIZAR DISCIPLINAS

        self.AttSubject_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.AttSubject_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_AttSubject = Label(self.AttSubject_Frame,bg='white',height=700,width=0)
        self.bar_AttSubject.place(x=10,y=0)
        self.info_AttSubject = Label(self.AttSubject_Frame,text='Insira o CPF que\ndeseja atualizar:',font='system 18',bg='midnightblue',fg='white')
        self.info_AttSubject.place(x=90,y=10)
        self.cod_AttSubject=Label(self.AttSubject_Frame,text='Código:',font='system 15',bg='midnightblue',fg='white')
        self.cod_AttSubject.place(x=100,y=85)
        self.info2_AttSubject = Label(self.AttSubject_Frame,text='Confira e atualize as informações desejadas abaixo:',font='system 10',bg='midnightblue',fg='white')
        self.info2_AttSubject.place(x=30,y=120)
        self.name_AttSubject = Label(self.AttSubject_Frame,text='Nome:',font='system 15',bg='midnightblue',fg='white')
        self.name_AttSubject.place(x=30,y=150)
        self.newcod_AttSubject = Label(self.AttSubject_Frame,text='Código:',font='system 15',bg='midnightblue',fg='white')
        self.newcod_AttSubject.place(x=30,y=180)
       
                    #ENTRY
        self.entrycod_AttSubject = Entry(self.AttSubject_Frame,font='ariel 10',width=18)
        self.entrycod_AttSubject.place(x=160,y=85)
        self.entryname_AttSubject = Entry(self.AttSubject_Frame,font='ariel 10',width=18)
        self.entryname_AttSubject.place(x=90,y=150)
        self.entrynewcod_AttSubject = Entry(self.AttSubject_Frame,font='ariel 10',width=18)
        self.entrynewcod_AttSubject.place(x=90,y=180)
        
                    #BUTTONS
        self.BTverify_AttSubject = Button(self.AttSubject_Frame,text='Verificar',width=8,command=self.VerifyAttSubject)
        self.BTverify_AttSubject.place(x=296,y=82)
        self.BTconfirm_AttSubject = Button(self.AttSubject_Frame,text='Atualizar',width=15,command=self.AttSubject)
        self.BTconfirm_AttSubject.place(x=50,y=250)
        self.BTback_AttSubject = Button(self.AttSubject_Frame,text='Voltar',width=15,command=self.back_to_FrameSubject)
        self.BTback_AttSubject.place(x=240,y=250)

        # REMOVER DISCIPLINAS
        
        self.RemoveSubject_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RemoveSubject_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RemoveSubject = Label(self.RemoveSubject_Frame,bg='white',height=700,width=0)
        self.bar_RemoveSubject.place(x=10,y=0)
        self.info_RemoveSubject = Label(self.RemoveSubject_Frame,text='Insira o CPF que\ndeseja remover:',font='system 18',bg='midnightblue',fg='white')
        self.info_RemoveSubject.place(x=90,y=10)
        self.cod_RemoveSubject=Label(self.RemoveSubject_Frame,text='Código:',font='system 15',bg='midnightblue',fg='white')
        self.cod_RemoveSubject.place(x=40,y=110)
                    #ENTRY
        self.entrycod_RemoveSubject = Entry(self.RemoveSubject_Frame,font='ariel 10',width=35)
        self.entrycod_RemoveSubject.place(x=100,y=110)
                    #BUTTONS
        self.BTconfirm_RemoveSubject = Button(self.RemoveSubject_Frame,text='Remover',width=15,command=self.RemoveSubject)
        self.BTconfirm_RemoveSubject.place(x=50,y=250)
        self.BTback_RemoveSubject = Button(self.RemoveSubject_Frame,text='Voltar',width=15,command=self.back_to_FrameSubject)
        self.BTback_RemoveSubject.place(x=240,y=250)



#-----------------------------------------------------------------------------------------------------------------------------------------------------
    # LABEL FRAME TURMAS

        self.FrameClass = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.lb1_Class = Label(self.FrameClass,text='Bem vindo ao\nMenu Turmas',font='system 20',bg='midnightblue',fg='white')
        self.lb1_Class.place(x=115,y=0)
        self.lb2_Class = Label(self.FrameClass,bg='white',height=700,width=0)
        self.lb2_Class.place(x=10,y=0)
        self.lb3_Class = Label(self.FrameClass,text='Escolha uma opção:',font='system 10',bg='midnightblue',fg='white')
        self.lb3_Class.place(x=130,y=70)
        
        self.BTc_register = Button(self.FrameClass,text='Cadastrar',width=15,command=self.entry_register_class)
        self.BTc_register.place(x=50,y=120)
        self.BTc_consult = Button(self.FrameClass,text='Consultar',width=15,command=self.entry_consult_class)
        self.BTc_consult.place(x=250,y=120)
        self.BTc_att = Button(self.FrameClass,text='Atualizar',width=15,command=self.entry_att_class)
        self.BTc_att.place(x=50,y=200)
        self.BTc_remove = Button(self.FrameClass,text='Remover',width=15,command=self.entry_remove_class)
        self.BTc_remove.place(x=250,y=200)
        self.BTc_ata = Button(self.FrameClass,text='Atas',width=10,command=self.entry_ata_class)
        self.BTc_ata.place(x=168,y=160)

        self.BTc_back = Button(self.FrameClass,text='Voltar',width=10,command=self.back_to_main)
        self.BTc_back.place(x=168,y=260)
        self.FrameClass.place(x=1000,y=1000)

        # REGISTRO TURMAS P1
        self.RegisterClass_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RegisterClass_Frame.place(x=1000,y=0)
        self.bar_RegisterClass = Label(self.RegisterClass_Frame,bg='white',height=700,width=0)
        self.bar_RegisterClass.place(x=10,y=0)
        self.info_RegisterClass = Label(self.RegisterClass_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_RegisterClass.place(x=65,y=10)
        self.codeclass_RegisterClass = Label(self.RegisterClass_Frame,text='Cód. turma:',font='system 15',fg='white',bg='midnightblue')
        self.codeclass_RegisterClass.place(x=20,y=90)
        self.period_RegisterClass = Label(self.RegisterClass_Frame,text='Período:',font='system 15',fg='white',bg='midnightblue')
        self.period_RegisterClass.place(x=20,y=120)
        self.codesub_RegisterClass = Label(self.RegisterClass_Frame,text='Cód. disciplina:',font='system 15',fg='white',bg='midnightblue')
        self.codesub_RegisterClass.place(x=20,y=150)
       
        # ENTRYs
        self.entrycodeclass_RegisterClass = Entry(self.RegisterClass_Frame,font='ariel 10',width=30)
        self.entrycodeclass_RegisterClass.place(x=140,y=90)
        self.entryperiod_RegisterClass = Entry(self.RegisterClass_Frame,font='ariel 10',width=30)
        self.entryperiod_RegisterClass.place(x=140,y=120)
        self.entrycodesub_RegisterClass = Entry(self.RegisterClass_Frame,font='ariel 10',width=30)
        self.entrycodesub_RegisterClass.place(x=140,y=150)
        
        # BUTTONS
        self.BTcreate_RegisterClass = Button(self.RegisterClass_Frame,text='Criar',width=8,command=self.RegisterClass)
        self.BTcreate_RegisterClass.place(x=90,y=245)

        self.BTinsert_RegisterClass = Button(self.RegisterClass_Frame,text='Inserir CPF',width=8,command=self.entry_insert_class)
        self.BTinsert_RegisterClass.place(x=170,y=245)
       
        self.BTback_RegisterClass = Button(self.RegisterClass_Frame,text='Voltar',width=8,command=self.back_to_FrameClass)
        self.BTback_RegisterClass.place(x=250,y=245)

        # REGISTRO CLASSES PT2



        self.RegisterClass2_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RegisterClass2_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RegisterClass2 = Label(self.RegisterClass2_Frame,bg='white',height=700,width=0)
        self.bar_RegisterClass2.place(x=10,y=0)
        self.info_RegisterClass2 = Label(self.RegisterClass2_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_RegisterClass2.place(x=65,y=10)
        self.cpfs_RegisterClass2 = Label(self.RegisterClass2_Frame,text='CPF Aluno:',font='system 15',fg='white',bg='midnightblue')
        self.cpfs_RegisterClass2.place(x=20,y=110)
        self.cpft_RegisterClass2 = Label(self.RegisterClass2_Frame,text='CPF Prof.:',font='system 15',fg='white',bg='midnightblue')
        self.cpft_RegisterClass2.place(x=20,y=140)
        
                    #ENTRY
        self.entrycpfs_RegisterClass2 = Entry(self.RegisterClass2_Frame,font='ariel 10',width=25)
        self.entrycpfs_RegisterClass2.place(x=100,y=110)
        self.entrycpft_RegisterClass2 = Entry(self.RegisterClass2_Frame,font='ariel 10',width=25)
        self.entrycpft_RegisterClass2.place(x=100,y=140)
        
             #BUTTONS
        self.BTconfirmStu_RegisterClass2 = Button(self.RegisterClass2_Frame,text='Registrar',width=8,command=self.Student_RegisterClass2)
        self.BTconfirmStu_RegisterClass2.place(x=290,y=108)
        self.BTconfirmT_RegisterClass2 = Button(self.RegisterClass2_Frame,text='Registrar',width=8,command=self.Teacher_RegisterClass2)
        self.BTconfirmT_RegisterClass2.place(x=290,y=138)
        self.BTback_RegisterClass2 = Button(self.RegisterClass2_Frame,text='Voltar',width=15,command=self.back_to_FrameClass)
        self.BTback_RegisterClass2.place(x=240,y=250)
        self.BTregister_RegisterClass2 = Button(self.RegisterClass2_Frame,text='Registrar',width=8,command=self.RegisterAll_Class2)
        self.BTregister_RegisterClass2.place(x=40,y=250)
    
        
        


    # CONSULTA DE TURMAS
  
        self.ConsultClass_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.ConsultClass_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_ConsultClass = Label(self.ConsultClass_Frame,bg='white',height=700,width=0)
        self.bar_ConsultClass.place(x=10,y=0)
        self.info_ConsultClass = Label(self.ConsultClass_Frame,text='Insira o código que\ndeseja consultar:',font='system 18',bg='midnightblue',fg='white')
        self.info_ConsultClass.place(x=80,y=10)
        self.cod_ConsultClass=Label(self.ConsultClass_Frame,text='Cód.Turma:',font='system 15',bg='midnightblue',fg='white')
        self.cod_ConsultClass.place(x=40,y=90)
                    #ENTRY
        self.entrycodeclass_ConsultClass = Entry(self.ConsultClass_Frame,font='ariel 10',width=30)
        self.entrycodeclass_ConsultClass.place(x=130,y=90)
                    #BUTTONS
        self.BTconfirm_ConsultClass = Button(self.ConsultClass_Frame,text='Consultar',width=10,command=self.ConsultClass)
        self.BTconfirm_ConsultClass.place(x=50,y=260)
        self.BTback_ConsultClass = Button(self.ConsultClass_Frame,text='Voltar',width=10,command=self.back_to_FrameClass)
        self.BTback_ConsultClass.place(x=260,y=260)
                    #LIST BOX
        self.listbox_ConsultClass = Listbox(self.ConsultClass_Frame,selectbackground= 'gray15', font='System 15', width='45', height='7',bg='gray70',fg='gray10')
        self.listbox_ConsultClass.place(x=20,y=120)

        # FRAME Remover TURMAS 
        self.RemoveClass_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.RemoveClass_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_RemoveClass = Label(self.RemoveClass_Frame,bg='white',height=700,width=0)
        self.bar_RemoveClass.place(x=10,y=0)
        self.info_RemoveClass = Label(self.RemoveClass_Frame,text='Insira o CPF que\ndeseja remover:',font='system 18',bg='midnightblue',fg='white')
        self.info_RemoveClass.place(x=90,y=10)
        self.cod_RemoveClass=Label(self.RemoveClass_Frame,text='Código:',font='system 15',bg='midnightblue',fg='white')
        self.cod_RemoveClass.place(x=40,y=110)
                    #ENTRY
        self.entrycod_RemoveClass = Entry(self.RemoveClass_Frame,font='ariel 10',width=35)
        self.entrycod_RemoveClass.place(x=100,y=110)
                    #BUTTONS
        self.BTconfirm_RemoveClass = Button(self.RemoveClass_Frame,text='Remover',width=15,command=self.RemoveClass)
        self.BTconfirm_RemoveClass.place(x=50,y=250)
        self.BTback_RemoveClass = Button(self.RemoveClass_Frame,text='Voltar',width=15,command=self.back_to_FrameClass)
        self.BTback_RemoveClass.place(x=240,y=250)
        

        # ---- ATA ------------
        self.AtaClass_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.AtaClass_Frame.place(x=1000,y=0)
                      #LABELS
        self.bar_AtaClass = Label(self.AtaClass_Frame,bg='white',height=700,width=0)
        self.bar_AtaClass.place(x=10,y=0)
        self.info_AtaClass = Label(self.AtaClass_Frame,text='Insira o código que\ndeseja consultar:',font='system 18',bg='midnightblue',fg='white')
        self.info_AtaClass.place(x=80,y=10)
        self.cod_AtaClass=Label(self.AtaClass_Frame,text='Cód.Turma:',font='system 15',bg='midnightblue',fg='white')
        self.cod_AtaClass.place(x=40,y=90)
                    #ENTRY
        self.entrycodeclass_AtaClass = Entry(self.AtaClass_Frame,font='ariel 10',width=30)
        self.entrycodeclass_AtaClass.place(x=130,y=90)
                    #BUTTONS
        self.BTconfirm_AtaClass = Button(self.AtaClass_Frame,text='Consultar',width=10,command=self.ATA_Class)
        self.BTconfirm_AtaClass.place(x=50,y=260)
        self.BTback_AtaClass = Button(self.AtaClass_Frame,text='Voltar',width=10,command=self.back_to_FrameClass)
        self.BTback_AtaClass.place(x=260,y=260)
                    #LIST BOX
        self.listbox_AtaClass = Listbox(self.AtaClass_Frame,selectbackground= 'gray15', font='System 15', width='45', height='7',bg='gray70',fg='gray10')
        self.listbox_AtaClass.place(x=20,y=120)


    # -------------- ATUALIZAR TURMAS PT1 -------------------------
        self.AttClass_Frame = Frame(self.root,width=390,height=300,bg='midnightblue')
        self.AttClass_Frame.place(x=1000,y=0)
        self.bar_AttClass = Label(self.AttClass_Frame,bg='white',height=700,width=0)
        self.bar_AttClass.place(x=10,y=0)
        self.info_AttClass = Label(self.AttClass_Frame,text='Preencha os campos\nde registro:',font='system 18',bg='midnightblue',fg='white')
        self.info_AttClass.place(x=65,y=10)
        self.codeclass_AttClass = Label(self.AttClass_Frame,text='Cód. turma:',font='system 15',fg='white',bg='midnightblue')
        self.codeclass_AttClass.place(x=20,y=90)
        self.newcodeclass_AttClass = Label(self.AttClass_Frame,text='Novo Cód.:',font='system 15',fg='white',bg='midnightblue')
        self.newcodeclass_AttClass.place(x=20,y=120)
        self.period_AttClass = Label(self.AttClass_Frame,text='Período:',font='system 15',fg='white',bg='midnightblue')
        self.period_AttClass.place(x=20,y=150)
        self.codesub_AttClass = Label(self.AttClass_Frame,text='Cód. disciplina:',font='system 15',fg='white',bg='midnightblue')
        self.codesub_AttClass.place(x=20,y=180)
       
        # ENTRYs
        self.entrycodeclass_AttClass = Entry(self.AttClass_Frame,font='ariel 10',width=20)
        self.entrycodeclass_AttClass.place(x=140,y=90)
        self.entrynewcodeclass_AttClass = Entry(self.AttClass_Frame,font='ariel 10',width=30)
        self.entrynewcodeclass_AttClass.place(x=140,y=120)
        self.entryperiod_AttClass = Entry(self.AttClass_Frame,font='ariel 10',width=30)
        self.entryperiod_AttClass.place(x=140,y=150)
        self.entrycodesub_AttClass = Entry(self.AttClass_Frame,font='ariel 10',width=30)
        self.entrycodesub_AttClass.place(x=140,y=180)
        
        # BUTTONS
        self.BTverify_AttClass = Button(self.AttClass_Frame,text='Verificar',width=8,command=self.VerifyAttClass)
        self.BTverify_AttClass.place(x=290,y=86)

        self.BTcreate_AttClass = Button(self.AttClass_Frame,text='Atualizar',width=8,command=self.AttClass)
        self.BTcreate_AttClass.place(x=70,y=245)

        
        self.BTback_AttClass = Button(self.AttClass_Frame,text='Voltar',width=8,command=self.back_to_FrameClass)
        self.BTback_AttClass.place(x=290,y=245)
  
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

try:
    mainwindow()
except:
    raise Exception('Janela não pode ser criada.')
