import Tkinter as tk
#from Tkinter import ttk
import ttk
import solve_K as K_Solver

root = tk.Tk()
root.title("Kolejki")

root.config(bg='#ECECEC')
root.resizable(0, 0) #Don't allow resizing in the x or y direction

lambda_1_0 = tk.DoubleVar(root, value=1/2.0)
lambda_2_0 = tk.DoubleVar(root, value=1/2.0)
lambda_3_0 = tk.DoubleVar(root, value=1/2.0)
lambda_4_0 = tk.DoubleVar(root, value=1/2.0)
lambda_5_0 = tk.DoubleVar(root, value=1/2.0)

mi_1 = tk.DoubleVar(root, value=1/2.0)
mi_2 = tk.DoubleVar(root, value=1/2.0)
mi_3 = tk.DoubleVar(root, value=1/2.0)
mi_4 = tk.DoubleVar(root, value=1/2.0)
mi_5 = tk.DoubleVar(root, value=1/2.0)
mi_6 = tk.DoubleVar(root, value=1/2.0)
mi_7 = tk.DoubleVar(root, value=1/2.0)
mi_8 = tk.DoubleVar(root, value=1/2.0)

def runBtnCallback():

    lambda_0 = [lambda_1_0.get(), lambda_2_0.get(), lambda_3_0.get(), lambda_4_0.get(), lambda_5_0.get() ]
    mi = [mi_1.get(), mi_2.get(), mi_3.get(), mi_4.get(), mi_5.get(), mi_6.get(), mi_7.get(), mi_8.get() ]

    K_Solver.solve_K(lambda_0, mi)

#Lambdas frame
lambdas_frame = ttk.Frame(root, relief='raised', borderwidth=1)
lambdas_frame.pack(fill='both', expand=False)

#Naglowek
lambdas_frame_row0 = ttk.Frame(lambdas_frame)
lambdas_frame_row0.pack(fill='both', expand=False)

lambda_label = ttk.Label(lambdas_frame_row0, text="Lambda startowe")
lambda_label.pack(side='left', fill='both', padx=5, pady=5)

#Klasa 1
lambdas_frame_row1 = ttk.Frame(lambdas_frame)
lambdas_frame_row1.pack(fill='both', expand=False)

lambda_1_0_label = ttk.Label(lambdas_frame_row1, text="Klasa 1")
lambda_1_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_1_0_val = ttk.Entry(lambdas_frame_row1, textvariable=lambda_1_0)
lambda_1_0_val.pack(expand=True, fill='both', padx=5, pady=5)

#Klasa 2
lambdas_frame_row2 = ttk.Frame(lambdas_frame)
lambdas_frame_row2.pack(fill='both', expand=False)

lambda_2_0_label = ttk.Label(lambdas_frame_row2, text="Klasa 2")
lambda_2_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_2_0_val = ttk.Entry(lambdas_frame_row2, textvariable=lambda_2_0)
lambda_2_0_val.pack(expand=True, fill='both', padx=5, pady=5)

#Klasa 3
lambdas_frame_row3 = ttk.Frame(lambdas_frame)
lambdas_frame_row3.pack(fill='both', expand=False)

lambda_3_0_label = ttk.Label(lambdas_frame_row3, text="Klasa 3")
lambda_3_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_3_0_val = ttk.Entry(lambdas_frame_row3, textvariable=lambda_3_0)
lambda_3_0_val.pack(expand=True, fill='both', padx=5, pady=5)

#Klasa 4
lambdas_frame_row4 = ttk.Frame(lambdas_frame)
lambdas_frame_row4.pack(fill='both', expand=False)

lambda_4_0_label = ttk.Label(lambdas_frame_row4, text="Klasa 4")
lambda_4_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_4_0_val = ttk.Entry(lambdas_frame_row4, textvariable=lambda_4_0)
lambda_4_0_val.pack(expand=True, fill='both', padx=5, pady=5)

#Klasa 5
lambdas_frame_row5 = ttk.Frame(lambdas_frame)
lambdas_frame_row5.pack(fill='both', expand=False)

lambda_5_0_label = ttk.Label(lambdas_frame_row5, text="Klasa 5")
lambda_5_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_5_0_val = ttk.Entry(lambdas_frame_row5, textvariable=lambda_5_0)
lambda_5_0_val.pack(expand=True, fill='both', padx=5, pady=5)

#Mi frame
# mi = \u03BC
mi_frame = ttk.Frame(root, relief='raised', borderwidth=1)
mi_frame.pack(fill='both', expand=False)

#Naglowek
mi_frame_row0 = ttk.Frame(mi_frame)
mi_frame_row0.pack(fill='both', expand=False)

mi_label = ttk.Label(mi_frame_row0, text=u'\u03BC')
mi_label.pack(side='left', fill='both', padx=5, pady=5)

#System 1
mi_frame_row1 = ttk.Frame(mi_frame)
mi_frame_row1.pack(fill='both', expand=False)

mi_1_label = ttk.Label(mi_frame_row1, text="System 1")
mi_1_label.pack(side='left', fill='both', padx=5, pady=5)

mi_1_val = ttk.Entry(mi_frame_row1, textvariable=mi_1)
mi_1_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 2
mi_frame_row2 = ttk.Frame(mi_frame)
mi_frame_row2.pack(fill='both', expand=False)

mi_2_label = ttk.Label(mi_frame_row2, text="System 2")
mi_2_label.pack(side='left', fill='both', padx=5, pady=5)

mi_2_val = ttk.Entry(mi_frame_row2, textvariable=mi_2)
mi_2_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 3
mi_frame_row3 = ttk.Frame(mi_frame)
mi_frame_row3.pack(fill='both', expand=False)

mi_3_label = ttk.Label(mi_frame_row3, text="System 3")
mi_3_label.pack(side='left', fill='both', padx=5, pady=5)

mi_3_val = ttk.Entry(mi_frame_row3, textvariable=mi_3)
mi_3_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 4
mi_frame_row4 = ttk.Frame(mi_frame)
mi_frame_row4.pack(fill='both', expand=False)

mi_4_label = ttk.Label(mi_frame_row4, text="System 4")
mi_4_label.pack(side='left', fill='both', padx=5, pady=5)

mi_4_val = ttk.Entry(mi_frame_row4, textvariable=mi_4)
mi_4_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 5
mi_frame_row5 = ttk.Frame(mi_frame)
mi_frame_row5.pack(fill='both', expand=False)

mi_5_label = ttk.Label(mi_frame_row5, text="System 5")
mi_5_label.pack(side='left', fill='both', padx=5, pady=5)

mi_5_val = ttk.Entry(mi_frame_row5, textvariable=mi_5)
mi_5_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 6
mi_frame_row6 = ttk.Frame(mi_frame)
mi_frame_row6.pack(fill='both', expand=False)

mi_6_label = ttk.Label(mi_frame_row6, text="System 6")
mi_6_label.pack(side='left', fill='both', padx=5, pady=5)

mi_6_val = ttk.Entry(mi_frame_row6, textvariable=mi_6)
mi_6_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 7
mi_frame_row7 = ttk.Frame(mi_frame)
mi_frame_row7.pack(fill='both', expand=False)

mi_7_label = ttk.Label(mi_frame_row7, text="System 7")
mi_7_label.pack(side='left', fill='both', padx=5, pady=5)

mi_7_val = ttk.Entry(mi_frame_row7, textvariable=mi_7)
mi_7_val.pack(expand=True, fill='both', padx=5, pady=5)

#System 8
mi_frame_row8 = ttk.Frame(mi_frame)
mi_frame_row8.pack(fill='both', expand=False)

mi_8_label = ttk.Label(mi_frame_row8, text="System 8")
mi_8_label.pack(side='left', fill='both', padx=5, pady=5)

mi_8_val = ttk.Entry(mi_frame_row8, textvariable=mi_8)
mi_8_val.pack(expand=True, fill='both', padx=5, pady=5)


frame_bottom = ttk.Frame(root)
frame_bottom.pack(fill='both', expand=False, side='bottom')

runButton = ttk.Button(frame_bottom, text="Run", command=runBtnCallback)
runButton.pack(side='right', padx=5, pady=5)


root.mainloop()
