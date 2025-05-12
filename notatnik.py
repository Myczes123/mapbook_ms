from tkinter import*


root = Tk()

root.title('mapbook_bs')
root.geometry('1200x700')

ramka_lista_obiektow =Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)

ramka_lista_obiektow.grid(row=0,column=0, padx=50)
ramka_formularz.grid(row=0,column=1)
ramka_szczegoly_obiektow.grid(row=1,column=0)

#ramka_lista_obiektow

label_lista_obiektow=Label(ramka_lista_obiektow, text='geoinformatyka sztos')
label_lista_obiektow.grid(row=0,column=0)

listbox_lista_obiektow=Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1,column=0)

button_poka_szczegoly=Button(label_lista_obiektow,text='Pokaż szczegóły')
button_poka_szczegoly.grid(row=3,column=0)

button_usun_obiekt=Button(label_lista_obiektow,text='Usuń obiekt')
button_usun_obiekt.grid(row=3,column=1)

button_edytuj_obiekt=Button(label_lista_obiektow,text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=3,column=2)

Label_imie=Label(ramka_formularz, text='imie')
Label_imie.grid(row=1,column=0)

Label_nazwisko=Label(ramka_formularz, text='nazwisko')
Label_nazwisko.grid(row=2,column=0)

Label_miejscowosc=Label(ramka_formularz, text='miejscowosc')
Label_miejscowosc.grid(row=3,column=0)

Label_liczba_postow=Label(ramka_formularz, text='miejscowosc')
Label_liczba_postow.grid(row=4,column=0)


entry_imie=Entry(ramka_formularz)
entry_imie.grid(row=1,column=1)
entry_nazwisko=Entry(ramka_formularz)
entry_nazwisko.grid(row=2,column=1)
entry_miejscowosc=Entry(ramka_formularz)
entry_miejscowosc.grid(row=3,column=1)
entry_liczba_postow=Entry(ramka_formularz)
entry_liczba_postow.grid(row=4,column=1)

label_szczegoly_obiektow=Label(ramka_formularz, text='szczegoly')
label_szczegoly_obiektow.grid(row=0,column=0)

label















root.mainloop()