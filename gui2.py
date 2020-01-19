# import Tkinter as tk
#from Tkinter import ttk
# import ttk
import ttk
from Tkinter import *
import solve_K as K_Solver
import solve_T as T_Solver
import solve_Q as Q_Solver
import solve_W as W_Solver

root = Tk()
root.title("Kolejki")

root.config(bg='#ECECEC')

root.geometry('1000x550')
root.resizable(0, 0) #Don't allow resizing in the x or y direction

root.grid_columnconfigure(1, weight=1)

lambda_1_0 = DoubleVar(root, value=1/2.0)
lambda_2_0 = DoubleVar(root, value=1/2.0)
lambda_3_0 = DoubleVar(root, value=1/2.0)
lambda_4_0 = DoubleVar(root, value=1/2.0)
lambda_5_0 = DoubleVar(root, value=1/2.0)

#mi_numersystemu_numerklasy
mi_1_1 = DoubleVar(root, value=1/2.0)
mi_1_2 = DoubleVar(root, value=1/2.0)
mi_1_3 = DoubleVar(root, value=1/2.0)
mi_1_4 = DoubleVar(root, value=1/2.0)
mi_1_5 = DoubleVar(root, value=1/2.0)
mi_2_1 = DoubleVar(root, value=1/2.0)
mi_2_2 = DoubleVar(root, value=1/2.0)
mi_2_3 = DoubleVar(root, value=1/2.0)
mi_2_4 = StringVar(root, value='--') #W systemie 2 nie ma klas 4 ani 5
mi_2_5 = StringVar(root, value='--')
mi_3 = DoubleVar(root, value=1/2.0)
mi_4 = DoubleVar(root, value=1/2.0)
mi_5 = DoubleVar(root, value=1/2.0)
mi_6 = DoubleVar(root, value=1/2.0)
mi_7 = DoubleVar(root, value=3/2.0) #dla mi<1 otrzymujemy ujemne K
mi_8 = DoubleVar(root, value=3/2.0) #dla mi<1 otrzymujemy ujemne K

def runBtnCallback():

    lambda_0 = [lambda_1_0.get(), lambda_2_0.get(), lambda_3_0.get(), lambda_4_0.get(), lambda_5_0.get() ]
    mi_1= [mi_1_1.get(), mi_1_2.get(), mi_1_3.get(), mi_1_4.get(), mi_1_5.get()]
    mi_2= [mi_2_1.get(), mi_2_2.get(), mi_2_3.get()]
    mi = [mi_1, mi_2, mi_3.get(), mi_4.get(), mi_5.get(), mi_6.get(), mi_7.get(), mi_8.get() ]
    K = K_Solver.solve_K(lambda_0, mi)
    T = T_Solver.solve_T(lambda_0, K)
    Q = Q_Solver.solve_Q(lambda_0, mi)
    W = W_Solver.solve_W(lambda_0, Q)

    #Wyniki zakladka 1
    result_val_1['text']= print_system_result("K", "T", K[1], T[1])
    result_val_2['text']= print_system_result("K", "T", K[2], T[2])
    result_val_3['text']= print_system_result("K", "T", K[3], T[3])
    result_val_4['text']= print_system_result("K", "T", K[4], T[4])
    result_val_5['text']= print_system_result("K", "T", K[5], T[5])
    result_val_6['text']= print_system_result("K", "T", K[6], T[6])
    result_val_7['text']= print_system_result("K", "T", K[7], T[7])
    result_val_8['text']= print_system_result("K", "T", K[8], T[8])

    #Wyniki zakladka 2
    result_val_1_2['text'] = print_system_result("Q", "W", Q[1], W[1])
    result_val_2_2['text'] = print_system_result("Q", "W", Q[2], W[2])
    result_val_3_2['text'] = print_system_result("Q", "W", Q[3], W[3])
    result_val_4_2['text'] = print_system_result("Q", "W", Q[4], W[4])
    result_val_5_2['text'] = print_system_result("Q", "W", Q[5], W[5])
    result_val_6_2['text'] = print_system_result("Q", "W", Q[6], W[6])
    result_val_7_2['text'] = print_system_result("Q", "W", Q[7], W[7])
    result_val_8_2['text'] = print_system_result("Q", "W", Q[8], W[8])

def print_system_result(ident_val, ident_time, val, time):
    result = ""
    for (val_value,time_value, i) in zip(val.values(), time.values(), range(6)):
        # print value
        if val_value == None:
            tmp = "|"+ident_val+str(i+1)+" : -- " + ident_time +str(i+1)+" : -- "
        else:
            tmp = "|"+ident_val+str(i+1)+": " + "{0:.2f} ".format(round(val_value,2)) + ident_time +str(i+1)+": " + "{0:.2f} ".format(round(time_value,2))
        result += tmp

    return result

def add_heading(master, heading_text):
    frame = Frame(master)

    label = Label(frame, text = heading_text)
    label.pack(fill = BOTH)

    frame.pack(fill = BOTH)

def add_entry(master, label_text, text_variable):

    frame = Frame(master)

    label = Label(frame, text=label_text, width = 8)
    label.pack(side=LEFT)

    entry = Entry(frame, textvariable = text_variable, justify = CENTER, width = 20)
    entry.pack(side=RIGHT)

    frame.pack(fill=X)

def add_entry_2(master, label_text, text_variable_1, text_variable_2, text_variable_3, text_variable_4, text_variable_5):
    frame = Frame(master)

    label = Label(frame, text = label_text, width = 8)
    label.pack(side=LEFT)

    entry1 = Entry(frame, textvariable = text_variable_1, justify = CENTER, width = 3)
    entry1.pack(side=LEFT)

    entry2 = Entry(frame, textvariable = text_variable_2, justify = CENTER, width = 3)
    entry2.pack(side=LEFT)

    entry3 = Entry(frame, textvariable = text_variable_3, justify = CENTER, width = 3)
    entry3.pack(side=LEFT)

    if text_variable_4 == mi_2_4:
        entry4 = Entry(frame, textvariable = text_variable_4, justify = CENTER, width = 3, state=DISABLED)
    else:
        entry4 = Entry(frame, textvariable = text_variable_4, justify = CENTER, width = 3)
    entry4.pack(side=LEFT)

    if text_variable_5 == mi_2_5:
        entry5 = Entry(frame, textvariable = text_variable_5, justify = CENTER, width = 3, state=DISABLED)
    else:
        entry5 = Entry(frame, textvariable = text_variable_5, justify = CENTER, width = 3)
    entry5.pack(side=LEFT)

    frame.pack(fill=X)

lambdas_frame = Frame(root, relief='raised', borderwidth=1)
lambdas_frame.grid(row = 0, column = 0, sticky=W+E+N+S)
n_lambdas = ttk.Notebook(lambdas_frame)
lambdas_page = Frame(n_lambdas)   # first page
n_lambdas.add(lambdas_page, text='Lambda startowe')
n_lambdas.pack(fill = BOTH)
# add_heading(lambdas_page, 'Lambda startowe')
add_entry(lambdas_page, 'Klasa 1', lambda_1_0)
add_entry(lambdas_page, 'Klasa 2', lambda_2_0)
add_entry(lambdas_page, 'Klasa 3', lambda_3_0)
add_entry(lambdas_page, 'Klasa 4', lambda_4_0)
add_entry(lambdas_page, 'Klasa 5', lambda_5_0)

mi_frame = Frame(root, relief='raised', borderwidth=1)
mi_frame.grid(row = 1, column = 0, sticky=W+E+N+S)
n_mi = ttk.Notebook(mi_frame)
mi_page = Frame(n_mi)
n_mi.add(mi_page, text = u'\u03BC')
n_mi.pack(fill = BOTH)
# add_heading(mi_frame, u'\u03BC')
add_entry_2(mi_page, 'System 1', mi_1_1, mi_1_2, mi_1_3, mi_1_4, mi_1_5)
add_entry_2(mi_page, 'System 2', mi_2_1, mi_2_2, mi_2_3, mi_2_4, mi_2_5)
add_entry(mi_page, 'System 3', mi_3)
add_entry(mi_page, 'System 4', mi_4)
add_entry(mi_page, 'System 5', mi_5)
add_entry(mi_page, 'System 6', mi_6)
add_entry(mi_page, 'System 7', mi_7)
add_entry(mi_page, 'System 8', mi_8)

result_frame = Frame(root, relief='raised', borderwidth=1, background='#ECECEC')
result_frame.grid(row = 0, column = 1, rowspan = 2, sticky=W+E+N+S)
n_result = ttk.Notebook(result_frame)
result_page_1 = Frame(n_result)   # first page
result_page_2 = Frame(n_result)   # second page
n_result.add(result_page_1, text='Rozklad zgloszen w sieci')
n_result.add(result_page_2, text='Rozklad zgloszen w kolejce')
n_result.pack(fill = BOTH)

# add_heading(result_page_1, 'Rozklad zgloszen danej klasy w sieci:')
#ZAKLADKA 1 - ROZKLAD ZGLOSZEN W SIECI
result_label_frame_1 = Frame(result_page_1)
result_label_1 = Label(result_label_frame_1, text = "System 1:")
result_label_1.pack(side = LEFT, fill = BOTH)
result_label_frame_1.pack(fill = BOTH)

result_val_frame_1 = Frame(result_page_1)
result_val_1 = Label(result_val_frame_1)
result_val_1.pack(side = LEFT, fill = BOTH)
result_val_frame_1.pack(fill = BOTH)

result_label_frame_2 = Frame(result_page_1)
result_label_2 = Label(result_label_frame_2, text = "System 2:")
result_label_2.pack(side = LEFT, fill = BOTH)
result_label_frame_2.pack(fill = BOTH)

result_val_frame_2 = Frame(result_page_1)
result_val_2 = Label(result_val_frame_2)
result_val_2.pack(side = LEFT, fill = BOTH)
result_val_frame_2.pack(fill = BOTH)

result_label_frame_3 = Frame(result_page_1)
result_label_3 = Label(result_label_frame_3, text = "System 3:")
result_label_3.pack(side = LEFT, fill = BOTH)
result_label_frame_3.pack(fill = BOTH)

result_val_frame_3 = Frame(result_page_1)
result_val_3 = Label(result_val_frame_3)
result_val_3.pack(side = LEFT, fill = BOTH)
result_val_frame_3.pack(fill = BOTH)

result_label_frame_4 = Frame(result_page_1)
result_label_4 = Label(result_label_frame_4, text = "System 4:")
result_label_4.pack(side = LEFT, fill = BOTH)
result_label_frame_4.pack(fill = BOTH)

result_val_frame_4 = Frame(result_page_1)
result_val_4 = Label(result_val_frame_4)
result_val_4.pack(side = LEFT, fill = BOTH)
result_val_frame_4.pack(fill = BOTH)

result_label_frame_5 = Frame(result_page_1)
result_label_5 = Label(result_label_frame_5, text = "System 5:")
result_label_5.pack(side = LEFT, fill = BOTH)
result_label_frame_5.pack(fill = BOTH)

result_val_frame_5 = Frame(result_page_1)
result_val_5 = Label(result_val_frame_5)
result_val_5.pack(side = LEFT, fill = BOTH)
result_val_frame_5.pack(fill = BOTH)

result_label_frame_6 = Frame(result_page_1)
result_label_6 = Label(result_label_frame_6, text = "System 6:")
result_label_6.pack(side = LEFT, fill = BOTH)
result_label_frame_6.pack(fill = BOTH)

result_val_frame_6 = Frame(result_page_1)
result_val_6 = Label(result_val_frame_6)
result_val_6.pack(side = LEFT, fill = BOTH)
result_val_frame_6.pack(fill = BOTH)

result_label_frame_7 = Frame(result_page_1)
result_label_7 = Label(result_label_frame_7, text = "System 7:")
result_label_7.pack(side = LEFT, fill = BOTH)
result_label_frame_7.pack(fill = BOTH)

result_val_frame_7 = Frame(result_page_1)
result_val_7 = Label(result_val_frame_7)
result_val_7.pack(side = LEFT, fill = BOTH)
result_val_frame_7.pack(fill = BOTH)

result_label_frame_8 = Frame(result_page_1)
result_label_8 = Label(result_label_frame_8, text = "System 8:")
result_label_8.pack(side = LEFT, fill = BOTH)
result_label_frame_8.pack(fill = BOTH)

result_val_frame_8 = Frame(result_page_1)
result_val_8 = Label(result_val_frame_8)
result_val_8.pack(side = LEFT, fill = BOTH)
result_val_frame_8.pack(fill = BOTH)





#ZAKLADKA 2 - ROZKLAD W KOLEJCE
result_label_frame_1_2 = Frame(result_page_2)
result_label_1_2 = Label(result_label_frame_1_2, text = "System 1:")
result_label_1_2.pack(side = LEFT, fill = BOTH)
result_label_frame_1_2.pack(fill = BOTH)

result_val_frame_1_2 = Frame(result_page_2)
result_val_1_2 = Label(result_val_frame_1_2)
result_val_1_2.pack(side = LEFT, fill = BOTH)
result_val_frame_1_2.pack(fill = BOTH)

result_label_frame_2_2 = Frame(result_page_2)
result_label_2_2 = Label(result_label_frame_2_2, text = "System 2:")
result_label_2_2.pack(side = LEFT, fill = BOTH)
result_label_frame_2_2.pack(fill = BOTH)

result_val_frame_2_2 = Frame(result_page_2)
result_val_2_2 = Label(result_val_frame_2_2)
result_val_2_2.pack(side = LEFT, fill = BOTH)
result_val_frame_2_2.pack(fill = BOTH)

result_label_frame_3_2 = Frame(result_page_2)
result_label_3_2 = Label(result_label_frame_3_2, text = "System 3:")
result_label_3_2.pack(side = LEFT, fill = BOTH)
result_label_frame_3_2.pack(fill = BOTH)

result_val_frame_3_2 = Frame(result_page_2)
result_val_3_2 = Label(result_val_frame_3_2)
result_val_3_2.pack(side = LEFT, fill = BOTH)
result_val_frame_3_2.pack(fill = BOTH)

result_label_frame_4_2 = Frame(result_page_2)
result_label_4_2 = Label(result_label_frame_4_2, text = "System 4:")
result_label_4_2.pack(side = LEFT, fill = BOTH)
result_label_frame_4_2.pack(fill = BOTH)

result_val_frame_4_2 = Frame(result_page_2)
result_val_4_2 = Label(result_val_frame_4_2)
result_val_4_2.pack(side = LEFT, fill = BOTH)
result_val_frame_4_2.pack(fill = BOTH)

result_label_frame_5_2 = Frame(result_page_2)
result_label_5_2 = Label(result_label_frame_5_2, text = "System 5:")
result_label_5_2.pack(side = LEFT, fill = BOTH)
result_label_frame_5_2.pack(fill = BOTH)

result_val_frame_5_2 = Frame(result_page_2)
result_val_5_2 = Label(result_val_frame_5_2)
result_val_5_2.pack(side = LEFT, fill = BOTH)
result_val_frame_5_2.pack(fill = BOTH)

result_label_frame_6_2 = Frame(result_page_2)
result_label_6_2 = Label(result_label_frame_6_2, text = "System 6:")
result_label_6_2.pack(side = LEFT, fill = BOTH)
result_label_frame_6_2.pack(fill = BOTH)

result_val_frame_6_2 = Frame(result_page_2)
result_val_6_2 = Label(result_val_frame_6_2)
result_val_6_2.pack(side = LEFT, fill = BOTH)
result_val_frame_6_2.pack(fill = BOTH)

result_label_frame_7_2 = Frame(result_page_2)
result_label_7_2 = Label(result_label_frame_7_2, text = "System 7:")
result_label_7_2.pack(side = LEFT, fill = BOTH)
result_label_frame_7_2.pack(fill = BOTH)

result_val_frame_7_2 = Frame(result_page_2)
result_val_7_2 = Label(result_val_frame_7_2)
result_val_7_2.pack(side = LEFT, fill = BOTH)
result_val_frame_7_2.pack(fill = BOTH)

result_label_frame_8_2 = Frame(result_page_2)
result_label_8_2 = Label(result_label_frame_8_2, text = "System 8:")
result_label_8_2.pack(side = LEFT, fill = BOTH)
result_label_frame_8_2.pack(fill = BOTH)

result_val_frame_8_2 = Frame(result_page_2)
result_val_8_2 = Label(result_val_frame_8_2)
result_val_8_2.pack(side = LEFT, fill = BOTH)
result_val_frame_8_2.pack(fill = BOTH)



runButton = Button(root, text="Run", command=runBtnCallback)
runButton.grid(row = 3, column = 0)

quitButton = Button(root, text="Quit", command=root.destroy)
quitButton.grid(row = 3, column = 1)

mainloop()
