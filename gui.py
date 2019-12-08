import tkinter as tk
from tkinter import ttk
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


lambdas_frame = ttk.Frame(root, relief='raised', borderwidth=1)
lambdas_frame.pack(fill='both', expand=False)


lambdas_frame_row0 = ttk.Frame(lambdas_frame)
lambdas_frame_row0.pack(fill='both', expand=False)

lambda_label = ttk.Label(lambdas_frame_row0, text="Lambda startowe")
lambda_label.pack(side='left', fill='both', padx=5, pady=5)


lambdas_frame_row1 = ttk.Frame(lambdas_frame)
lambdas_frame_row1.pack(fill='both', expand=False)

lambda_1_0_label = ttk.Label(lambdas_frame_row1, text="Klasa 1")
lambda_1_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_1_0_val = ttk.Entry(lambdas_frame_row1, textvariable=lambda_1_0)
lambda_1_0_val.pack(expand=True, fill='both', padx=5, pady=5)


lambdas_frame_row2 = ttk.Frame(lambdas_frame)
lambdas_frame_row2.pack(fill='both', expand=False)

lambda_2_0_label = ttk.Label(lambdas_frame_row2, text="Klasa 2")
lambda_2_0_label.pack(side='left', fill='both', padx=5, pady=5)

lambda_2_0_val = ttk.Entry(lambdas_frame_row2, textvariable=lambda_2_0)
lambda_2_0_val.pack(expand=True, fill='both', padx=5, pady=5)




mi_frame = ttk.Frame(root, relief='raised', borderwidth=1)
mi_frame.pack(fill='both', expand=False)


mi_frame_row0 = ttk.Frame(mi_frame)
mi_frame_row0.pack(fill='both', expand=False)

mi_label = ttk.Label(mi_frame_row0, text="Mi")
mi_label.pack(side='left', fill='both', padx=5, pady=5)


mi_frame_row1 = ttk.Frame(mi_frame)
mi_frame_row1.pack(fill='both', expand=False)

mi_1_label = ttk.Label(mi_frame_row1, text="System 1")
mi_1_label.pack(side='left', fill='both', padx=5, pady=5)

mi_1_val = ttk.Entry(mi_frame_row1, textvariable=mi_1)
mi_1_val.pack(expand=True, fill='both', padx=5, pady=5)


mi_frame_row2 = ttk.Frame(mi_frame)
mi_frame_row2.pack(fill='both', expand=False)

mi_2_label = ttk.Label(mi_frame_row2, text="System 2")
mi_2_label.pack(side='left', fill='both', padx=5, pady=5)

mi_2_val = ttk.Entry(mi_frame_row2, textvariable=mi_2)
mi_2_val.pack(expand=True, fill='both', padx=5, pady=5)



frame_bottom = ttk.Frame(root)
frame_bottom.pack(fill='both', expand=False, side='bottom')

runButton = ttk.Button(frame_bottom, text="Run", command=runBtnCallback)
runButton.pack(side='right', padx=5, pady=5)


root.mainloop()
