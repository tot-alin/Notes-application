
from color import Colors
from color import Fonts
from sql_function import Function_sql
from ouput import ExportPdfDoc, Audio
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import time


class WinStart(Colors, Fonts):

    def __init__(self, master):
        Colors.__init__(self)
        Fonts.__init__(self)

        self.master = master
        self.master.title('Note App')
        self.master.config(background=self.general_bg)

        win_start_label = Label(self.master, text='My notes', font=self.font_win_start, bg=self.general_bg, fg='blue')

        sing_in_butt = Button(self.master, text='Sing in', font=self.font_win_start, width=20, height=2,
                              activebackground=self.button_abg, activeforeground=self.button_afg, bg=self.button_bg)
        create_account_butt = Button(self.master, text='Create account', width=20, height=2, font=self.font_win_start,
                                     activebackground=self.button_abg, activeforeground=self.button_afg,
                                     bg=self.button_bg)
        exit_butt = Button(self.master, text='Exit', width=20, height=2, font=self.font_win_start,
                           activebackground=self.button_abg, activeforeground=self.button_afg, bg=self.button_bg)

        # command
        sing_in_butt['command'] = self.sing_in
        create_account_butt['command'] = self.create_accont
        exit_butt['command'] = root.destroy

        # pozitione
        win_start_label.pack(pady=20)
        sing_in_butt.pack()
        create_account_butt.pack()
        exit_butt.pack()

    @staticmethod
    def sing_in():
        SingIn(Toplevel(root))
        root.withdraw()

    @staticmethod
    def create_accont():
        CreateAccount(Toplevel(root))
        root.withdraw()


class SingIn(Colors, Fonts):

    def __init__(self, master):
        Colors.__init__(self)
        Fonts.__init__(self)

        self.user_obj = Function_sql()

        self.master = master
        self.master.title('Sing in')
        # self.master.geometry('500x120')
        self.master.resizable(False, False)
        self.master.config(background=self.general_bg)

        user_label = Label(self.master, text='  User Name : ', width=20, font=self.font_sing_cont, bg=self.general_bg)
        pass_label = Label(self.master, text='   Password : ', width=20, font=self.font_sing_cont, bg=self.general_bg)
        self.user_entry = Entry(self.master, font=self.font_sing_cont, bg=self.text_bg)
        self.pass_entry = Entry(self.master, font=self.font_sing_cont, show='*', bg=self.text_bg)
        sing_in_butt = Button(self.master, text='Sing in', activebackground=self.button_abg,
                              activeforeground=self.button_afg, bg=self.button_bg)
        back_to_winstart_butt = Button(self.master, text='Back', activebackground=self.button_abg,
                                       activeforeground=self.button_afg, bg=self.button_bg)

        self.err = Label(self.master, font=self.font_sing_cont, fg='red', bg=self.general_bg)

        # command
        sing_in_butt['command'] = self.sing_in
        back_to_winstart_butt['command'] = self.back_to_win_start
        self.master.protocol('WM_DELETE_WINDOW', self.destroy_all)

        # pozitione
        user_label.grid(row=0, column=0, pady=5)
        pass_label.grid(row=1, column=0, pady=5)
        self.user_entry.grid(row=0, column=1)
        self.pass_entry.grid(row=1, column=1)
        sing_in_butt.grid(row=0, column=3, rowspan=3, pady=5, padx=20, sticky=N + S)
        back_to_winstart_butt.grid(row=3, column=0, pady=20)
        self.err.grid(row=3, column=1, columnspan=3)

    def destroy_all(self):
        del self.user_obj
        self.master.destroy()
        root.destroy()

    def back_to_win_start(self):
        del self.user_obj
        root.deiconify()
        self.master.destroy()

    def sing_in(self):
        user = self.user_obj.ver_user_password(self.user_entry.get(), self.pass_entry.get())
        while True:
            if user == '':
                self.err.configure(text='incorrect username and/or password')
                break
            else:
                self.err.configure(text=f'Logged by : {user}')
                self.err.update()  # actualize self.err
                time.sleep(1)
                self.master.destroy()
                NoteApp(Toplevel(root), user)
                break


class CreateAccount(Colors, Fonts):

    def __init__(self, master):
        Colors.__init__(self)
        Fonts.__init__(self)

        self.create_user_obj = Function_sql()

        self.master = master
        self.master.title('Create_account')
        # self.master.geometry('500x150')
        self.master.resizable(False, False)
        self.master.config(background=self.general_bg)

        user_label = Label(self.master, text='  User Name : ', width=20, font=self.font_sing_cont, bg=self.general_bg)
        pass_label = Label(self.master, text='   Password : ', width=20, font=self.font_sing_cont, bg=self.general_bg)
        re_pass_label = Label(self.master, text='Re-Password : ', width=20, font=self.font_sing_cont,
                              bg=self.general_bg)

        self.user_entry = Entry(self.master, font=self.font_sing_cont, bg=self.text_bg)
        self.pass_entry = Entry(self.master, font=self.font_sing_cont, show='*', bg=self.text_bg)
        self.re_pass_entry = Entry(self.master, font=self.font_sing_cont, show='*', bg=self.text_bg)

        self.err = Label(self.master, text='', font=self.font_sing_cont, fg='red', bg=self.general_bg)

        create_butt = Button(self.master, text='Create', activebackground=self.button_abg,
                             activeforeground=self.button_afg, bg=self.button_bg)
        back_butt = Button(self.master, text='Back', activebackground=self.button_abg,
                           activeforeground=self.button_afg, bg=self.button_bg)

        # command
        create_butt['command'] = self.create_account
        back_butt['command'] = self.back_win_start
        self.master.protocol('WM_DELETE_WINDOW', self.destroy_start_create)

        # positioned
        user_label.grid(row=0, column=0, pady=5)
        pass_label.grid(row=1, column=0, pady=5)
        re_pass_label.grid(row=2, column=0, pady=5)
        self.user_entry.grid(row=0, column=1)
        self.pass_entry.grid(row=1, column=1)
        self.re_pass_entry.grid(row=2, column=1)
        self.err.grid(row=3, column=1, columnspan=3)
        create_butt.grid(row=0, column=3, rowspan=3, pady=5, padx=20, sticky=N + S)
        back_butt.grid(row=3, column=0, pady=20)

    def back_win_start(self):
        root.deiconify()
        del self.create_user_obj
        self.master.destroy()

    def destroy_start_create(self):
        self.master.destroy()
        del self.create_user_obj
        root.destroy()

    def create_account(self):
        create_err = self.create_user_obj.insert_user(self.user_entry.get(), self.pass_entry.get(),
                                                      self.re_pass_entry.get())
        self.err.config(text=create_err)
        if create_err == '':
            self.back_win_start()


class NoteApp(Colors, Fonts):

    def __init__(self, master, user_name):
        Colors.__init__(self)
        Fonts.__init__(self)

        self.select_reg_dade = ''
        self.user_obj = Function_sql()

        self.master = master
        self.master.title(f'Logged by :{user_name}')
        self.master.geometry('1150x675')
        self.master.attributes('-fullscreen', False)
        # self.master.maxsize(1150, 540)


        self.user_name = user_name

        self.canvas_note = Canvas(self.master, borderwidth=0, background=self.general_bg)
        self.frame_note = Frame(self.canvas_note, background=self.general_bg)
        vsb = Scrollbar(self.master, orient="vertical", command=self.canvas_note.yview)
        hsb = Scrollbar(self.master, orient="horizontal", command=self.canvas_note.xview)
        self.canvas_note.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')
        self.canvas_note.pack(side="left", fill="both", expand=True)
        self.canvas_note.create_window((4, 4), window=self.frame_note, anchor=NW)

        self.frame_note.bind("<Configure>",
                             lambda event: self.canvas_note.configure(scrollregion=self.canvas_note.bbox("all")))
        # detecteaza evenimente din mainloop() in cazul asta evenimentul "<Configure>"
        # .bind - metoda de a detecta -event-

        export_butt = Button(self.frame_note, text='Export .pdf', font=self.font_note_app,
                             activebackground=self.button_abg,
                             activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)
        speech_butt = Button(self.frame_note, text='Speech', font=self.font_note_app, activebackground=self.button_abg,
                             activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)
        language_label = Label(self.frame_note, text='set language\nto speak :', font=self.font_note_app,
                               bg=self.general_bg)

        self.lang_set = StringVar()
        lang_ro_radio = Radiobutton(self.frame_note, text='   Ro   ', variable=self.lang_set, value='ro',
                                    indicatoron=False, activebackground=self.button_abg, activeforeground=self.button_afg,
                                    bg=self.button_bg)
        lang_en_radio = Radiobutton(self.frame_note, text='   En   ', variable=self.lang_set, value='en',
                                    indicatoron=False, activebackground=self.button_abg, activeforeground=self.button_afg,
                                    bg=self.button_bg)
        lang_ro_radio.invoke()

        title_label = Label(self.frame_note, text='Title : ', font=self.font_note_app, bg=self.general_bg)

        self.notes_title_in = Text(self.frame_note, font=self.font_note_app, bg=self.text_bg, width=70, height=1)

        note_label = Label(self.frame_note, text='Note : ', font=self.font_note_app, bg=self.general_bg)

        self.notes_in = Text(self.frame_note, font=self.font_note_app, bg=self.text_bg, width=68, height=20)

        notes_scrollbar = Scrollbar(self.frame_note, orient=VERTICAL, width=15, command=self.notes_in.yview,
                                    background=self.button_bg, troughcolor=self.text_bg, highlightcolor=self.button_afg)
        self.notes_in.config(yscrollcommand=notes_scrollbar.set)

        ref_date_label = Label(self.frame_note, text='Set reference\ndate of the note :', bg=self.general_bg)

        self.cal = Calendar(self.frame_note, selectmode='day', date_pattern="yyyy-mm-dd", background=self.general_bg,
                            bordercolor=self.general_bg, normalbackground=self.general_bg,
                            headersbackground=self.general_bg)

        date_now_butt = Button(self.frame_note, text='Date\nnow', font=self.font_note_app,
                               activebackground=self.button_abg, activeforeground=self.button_afg, bg=self.button_bg,
                               width=5, height=4)

        click_select_label = Label(self.frame_note, text='double-click to select :', bg=self.general_bg)

        self.list_box = Listbox(self.frame_note, bg=self.text_bg)  # , width=50
        self.list_box.bind('<Double-1>', self.data_get)
        list_scrolbar = Scrollbar(self.frame_note, orient=VERTICAL, width=15, command=self.list_box.yview,
                                  background=self.button_bg, troughcolor=self.text_bg, highlightcolor=self.button_afg)
        self.list_box.config(yscrollcommand=list_scrolbar.set)

        now_butt = Button(self.frame_note, text='New', font=self.font_note_app, activebackground=self.button_abg,
                          activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)

        self.save_new_butt = Button(self.frame_note, text='Save new', font=self.font_note_app,
                               activebackground=self.button_abg, disabledforeground='white',
                               activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)

        self.button_update = Button(self.frame_note, text='Update', font=self.font_note_app,
                                    activebackground=self.button_abg,
                                    activeforeground=self.button_afg, bg=self.button_bg, disabledforeground='white',
                                    width=10, height=2)

        self.delete_butt = Button(self.frame_note, text='Delete', font=self.font_note_app, activebackground=self.button_abg,
                             activeforeground=self.button_afg, disabledforeground='white',
                                  bg=self.button_bg, width=10, height=2)

        self.sort_radio = StringVar()
        sort_regis_radio = Radiobutton(self.frame_note, text='Registration date', indicatoron=False,
                                       font=self.font_note_app, variable=self.sort_radio, value='sort_regis', width=20, height=2,
                                       activebackground=self.button_abg, activeforeground=self.button_afg,
                                       bg=self.button_bg)
        sort_date_radio = Radiobutton(self.frame_note, text='Reference date', indicatoron=False, font=self.font_note_app,
                                      variable=self.sort_radio, value='sort_date', width=20, height=2,
                                      activebackground=self.button_abg,
                                      activeforeground=self.button_afg, bg=self.button_bg)
        sort_title_radio = Radiobutton(self.frame_note, text='Title', indicatoron=False, font=self.font_note_app,
                                       variable=self.sort_radio, value='sort_title', width=20, height=2,
                                       activebackground=self.button_abg,
                                       activeforeground=self.button_afg, bg=self.button_bg)
        sort_regis_radio.invoke()

        back_butt = Button(self.frame_note, text='Back', font=self.font_note_app, activebackground=self.button_abg,
                           activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)

        close_butt = Button(self.frame_note, text='Close', font=self.font_note_app, activebackground=self.button_abg,
                            activeforeground=self.button_afg, bg=self.button_bg, width=10, height=2)

        # command
        export_butt['command'] = self.export_pdf
        speech_butt['command'] = self.speak
        lang_ro_radio['command'] = self.speak
        lang_en_radio['command'] = self.speak
        date_now_butt['command'] = self.now_date
        now_butt['command'] = self.new
        self.save_new_butt['command'] = self.save_new
        self.button_update['command'] = self.update_record
        self.delete_butt['command'] = self.delete_record
        sort_regis_radio['command'] = self.sort_db
        sort_date_radio['command'] = self.sort_db
        sort_title_radio['command'] = self.sort_db
        back_butt['command'] = self.back_to_start
        close_butt['command'] = self.close_all
        self.master.protocol('WM_DELETE_WINDOW', self.close_all)

        # pozitione

        # distantiere
        Label(self.frame_note, width=5, bg=self.general_bg).grid(row=0, column=6, pady=5, padx=5)  # text='6',
        Label(self.frame_note, width=5, bg=self.general_bg).grid(row=0, column=9, sticky=EW)  # text='9',
        Label(self.frame_note, bg=self.general_bg).grid(row=3, column=0, pady=5, padx=5,
                                                        sticky=S)  # , width=5, height=2 text='3',
        Label(self.frame_note, text='          ', font=('Arial', '10'), bg=self.general_bg).grid(row=0, column=0)

        Label(self.frame_note, height=2, bg=self.general_bg).grid(row=8, column=0, pady=5)  # , text=8

        export_butt.grid(row=0, column=1, pady=5, padx=5)
        speech_butt.grid(row=0, column=2, pady=5, padx=5)
        language_label.grid(row=0, column=3, pady=5, padx=5)
        lang_ro_radio.grid(row=0, column=4, pady=5, padx=5, sticky=W)
        lang_en_radio.grid(row=0, column=4, pady=5, padx=5, sticky=E)
        title_label.grid(row=1, column=0, pady=5, sticky=NE)
        self.notes_title_in.grid(row=1, column=1, columnspan=5, pady=5, sticky=NW)
        note_label.grid(row=2, column=0, sticky=NE)
        self.notes_in.grid(row=2, column=1, rowspan=5, columnspan=4, sticky=N + S + E + W)
        notes_scrollbar.grid(row=2, column=5, rowspan=5, sticky=N + S + E)
        ref_date_label.grid(row=1, column=7, pady=5, sticky=NE)
        self.cal.grid(row=1, column=8, rowspan=2, columnspan=3, pady=5, sticky=NW)
        date_now_butt.grid(row=1, column=10, rowspan=2, pady=5, padx=5, sticky=NE)
        click_select_label.grid(row=3, column=7, columnspan=4, sticky=SW)
        self.list_box.grid(row=4, column=7, rowspan=3, columnspan=4, sticky=N + S + E + W)
        list_scrolbar.grid(row=4, column=10, rowspan=3, sticky=N + S + E)
        now_butt.grid(row=7, column=1, pady=5, padx=5)
        self.save_new_butt.grid(row=7, column=2, pady=5, padx=5)
        self.button_update.grid(row=7, column=3, pady=5, padx=5)
        self.delete_butt.grid(row=7, column=4, pady=5, padx=5)
        sort_regis_radio.grid(row=7, column=7, pady=5, padx=5)
        sort_date_radio.grid(row=7, column=8, pady=5, padx=5)
        sort_title_radio.grid(row=7, column=9, columnspan=2, pady=5, padx=5)
        back_butt.grid(row=9, column=8, pady=5, padx=5)
        close_butt.grid(row=9, column=10, pady=5, padx=5)

        self.sort_db()
        # self.speak()

        self.button_update['state'] = DISABLED
        self.delete_butt['state'] = DISABLED
        self.save_new_butt['state'] = DISABLED

    def close_all(self):
        del self.user_obj
        root.destroy()

    def back_to_start(self):
        del self.user_obj
        root.deiconify()
        self.master.destroy()

    def now_date(self):
        self.cal.selection_set(datetime.now().strftime('%Y-%m-%d'))

    def new(self):
        self.notes_title_in.delete("1.0", "end")
        self.notes_in.delete("1.0", "end")
        self.now_date()
        self.button_update['state'] = DISABLED  # dezactiveaza butonul
        self.delete_butt['state'] = DISABLED
        self.save_new_butt['state'] = NORMAL

    def save_new(self):
        time.sleep(2)  # spatiu de timp pentru inregistrare corecta a ordini
        date_reg = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # data si ora inregistrari, la momentul inregistrari
        date_ref = self.cal.get_date()  # data de referinta, selectata din calendar
        notes_title = self.notes_title_in.get('1.0', 'end-1c')  # 'end-1c' - sterge ultimul randa care se adauga automat
        notes = self.notes_in.get('1.0', 'end-1c')
        # Raise a prompt for missing values
        if (len(str(notes_title).strip()) <= 1) or (len(str(notes).strip()) <= 1):  # verifica sa fie mai mult
            # de un caracter
            messagebox.showerror(message='Enter details, notes and title ', parent=self.master)
            self.save_new_butt['state'] = NORMAL
            self.button_update['state'] = DISABLED
            self.delete_butt['state'] = DISABLED
        else:
            self.user_obj.save_data(self.user_name, date_reg, date_ref, notes_title, notes)
            self.new()
        self.re_list_box()



    def sort_db(self):
        self.user_obj.in_sort(self.user_name, self.sort_radio.get())
        self.re_list_box()

    def re_list_box(self):
        self.list_box.delete(0, END)
        index = 0
        for i in self.user_obj.refresh_list_box():
            self.list_box.insert(index, f'  {str(i[0])}     {str(i[1])}     {str(i[2])}')
            index += 1

    def data_get(self, event):
        indice = int(self.list_box.curselection()[0])  # indica numarul de ordine corespunzator elementului selectat
        # in list_box
        self.select_reg_dade = self.list_box.get(indice)[2:21]  # extrage (date_reg) data si ora de inregistrare
        data = self.user_obj.get_data_db(self.user_name, self.select_reg_dade)
        # date_reg_indices = data[0][0]
        self.cal.selection_set(data[0][1])
        self.notes_title_in.delete("1.0", "end")
        self.notes_title_in.insert(INSERT, data[0][2])
        self.notes_in.delete("1.0", "end")
        self.notes_in.insert(INSERT, data[0][3])
        self.button_update['state'] = NORMAL
        self.delete_butt['state'] = NORMAL
        self.save_new_butt['state'] = DISABLED

    def delete_record(self):
        self.user_obj.del_record(self.user_name, self.select_reg_dade)
        self.re_list_box()
        self.new()
        self.delete_butt['state'] = DISABLED

    def update_record(self):
        # notes_title = self.notes_title_in.get('1.0', 'end-1c')
        # notes = self.notes_in.get('1.0', 'end-1c')
        self.user_obj.up_record(self.user_name, self.select_reg_dade, self.notes_title_in.get('1.0', 'end-1c'),
                                self.notes_in.get('1.0', 'end-1c'))
        self.re_list_box()


    def speak(self):
        text = self.notes_title_in.get('1.0', 'end') + self.notes_in.get('1.0', 'end')
        audio_obj = Audio
        audio_obj.create_sound(text, self.lang_set.get())
        del audio_obj

    def export_pdf(self):
        doc_pdf = ExportPdfDoc.export_to_pdf(self.notes_title_in.get('1.0', 'end-1c'),
                                         self.notes_in.get('1.0', 'end-1c'))
        del doc_pdf


root = Tk()
WinStart(root)
root.mainloop()
