import tkinter as tk
from math import degrees, acos, modf
from typing import overload, Tuple
from itertools import chain
from tkinter import messagebox
from copy import deepcopy


class Vector:
    """Vector object with general attributes and methods. Operations are supported. Numerical attributes are
    returned as long float objects. Please use round() for your convenience"""

    @overload
    def __init__(self, vector: "Vector"): ...

    @overload
    def __init__(self, Complex: complex): ...

    @overload
    def __init__(self, x_comp=0.0, y_comp=0.0, z_comp=0.0): ...

    def __init__(self, x_comp=0.0, y_comp=0.0, z_comp=0.0):
        if isinstance(x_comp, Vector) and not y_comp and not z_comp:
            self.x, self.y, self.z = x_comp.x, x_comp.y, x_comp.z
        elif isinstance(x_comp, complex) and not y_comp and not z_comp:
            self.x, self.y, self.z = x_comp.real, x_comp.imag, 0.0
        elif isinstance(x_comp, (int, float)) and isinstance(y_comp, (int, float)) and isinstance(z_comp, (int, float)):
            self.x, self.y, self.z = float(x_comp), float(y_comp), float(z_comp)
        else:
            raise TypeError("The type of values passed is unacceptable")

        if (self.x, self.y, self.z) == (0, 0, 0):
            self.dimension = 0
        elif not (self.x, self.y, self.z) == (0, 0, 0):
            self.dimension: int = 3
        elif not (self.x, self.y) == (0, 0) or (self.y, self.z) == (0, 0) or (self.x, self.z) == (0, 0):
            self.dimension = 2
        else:
            self.dimension = 1
        self.length: float = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        try:
            self.dircos_l: float = self.x / self.length
            self.dircos_m: float = self.y / self.length
            self.dircos_n: float = self.z / self.length
            float()
            self.alpha: float = degrees(acos(self.dircos_l))
            self.beta: float = degrees(acos(self.dircos_m))
            self.gamma: float = degrees(acos(self.dircos_n))
        except ZeroDivisionError:
            self.dircos_l = self.dircos_m = self.dircos_n = None  # They are actually infinite

    def UnitVector(self) -> "Vector":
        if self.dircos_l is not None and self.dircos_m is not None and self.dircos_n is not None:
            return Vector(self.dircos_l, self.dircos_m, self.dircos_n)

    @classmethod
    def FromTwoPoints(cls, A: Tuple[int, int, int], B: Tuple[int, int, int]) -> "Vector":
        return Vector(B[0] - A[0], B[1] - A[1], B[2] - A[2])

    @classmethod
    def DotProduct(cls, vector1: "Vector", vector2: "Vector") -> float:
        return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)

    @classmethod
    def CrossProduct(cls, vector1: "Vector", vector2: "Vector") -> "Vector":
        return Vector((vector1.y * vector2.z - vector1.z * vector2.y), -(vector1.x * vector2.z - vector1.z * vector2.x),
                      (vector1.x * vector2.y - vector1.y * vector2.x))

    @classmethod
    def angle(cls, vector1: "Vector", vector2: "Vector") -> float:
        return degrees(acos(cls.DotProduct(vector1, vector2) / (vector1.length * vector2.length)))

    def __add__(self, other) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            print("Please use class methods - Vector.DotProduct() or Vector.CrossProduct")

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y, -self.z)

    def __complex__(self) -> complex:
        if self.dimension <= 2:
            return complex(self.x, self.y)

    def __abs__(self) -> float:  # because we use the modulus symbol to express length of vector
        return self.length

    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        if modf(self.x)[0] == 0.0:
            self.x = int(self.x)
        if modf(self.y)[0] == 0.0:
            self.y = int(self.y)
        if modf(self.z)[0] == 0.0:
            self.z = int(self.z)
        x = f"+{self.x}\u00ee " if self.x > 0 else (f"{self.x}\u00ee " if self.x < 0 else "")
        y = f"+{self.y}\u0135 " if self.y > 0 else (f"{self.y}\u0135 " if self.y < 0 else "")
        z = f"+{self.z}\u006b\u0302" if self.z > 0 else (f"{self.z}\u006b\u0302" if self.z < 0 else "")
        if x == "" and y == "" and z == "":
            return f"Vector(0)"
        else:
            return f"Vector({x}{y}{z})"


class Window(tk.Tk):

    def __init__(self):
        super(Window, self).__init__()
        self.title("Vector Calculator")
        self.geometry("540x268")
        self.iconbitmap(r"C:\Users\Admin\Downloads\475497.ico")
        self.config(bg="Black")

        self.scroll_v = tk.Scrollbar(self, orient="vertical")
        self.scroll_v.pack(side="right", fill="y")
        self.basecan = tk.Canvas(self, bd=0, yscrollcommand=self.scroll_v.set, bg="Black")
        self.basecan.pack(fill="both", expand="true")
        self.baseframe = tk.Frame(self.basecan, bd=0, bg="Black")

        self.vect_num, self.vect_dict, self.current_op = 0, {}, "+"

        # Frames
        self.f_top = tk.Frame(self.baseframe, bg="Black")
        self.f_main = tk.Frame(self.baseframe, bg="Black")
        self.f_buttons = tk.Frame(self.baseframe, bg="Black")
        self.f_buttons.grid(row=1, column=1, rowspan=2, sticky="n")

        self.la_stat = tk.Label(self.baseframe, text="", anchor="w", bd=2, relief="sunken", font=("Lucida", 16),
                                bg="white")
        self.la_stat.grid(row=0, column=0, columnspan=2, sticky="ew", padx=(5, 0), pady=5)

        # Spins and labels
        self.l_uni = ["\u00ee", "\u0135", "\u006b\u0302"]
        for i in range(3):
            spin = tk.Spinbox(self.f_top, from_=-100, to=10000, increment=0.5, width=6)
            spin.grid(row=0, column=i * 2)
            spin.delete(0, "end")
            spin.insert(0, 0)
            tk.Label(self.f_top, text=self.l_uni[i], bg="Black").grid(row=0, column=(i * 2) + 1, padx=10)
        self.f_top.grid(row=1, column=0, sticky="n", padx=5, pady=5)

        # Buttons
        self.b_load = tk.Button(self.f_top, text="Load vector", bg="Goldenrod", command=self.v_load)
        self.b_load.grid(row=0, column=6, padx=15)
        self.b_result = tk.Button(self.baseframe, text="Result", command=self.show_vect, bg="Goldenrod",
                                  state="disabled")
        self.b_result.grid(row=0, column=2, padx=10)
        tk.Button(self.f_buttons, text="Add(+)", state="disabled", command=lambda: self.v_oper("+"),
                  bg="Goldenrod").grid(row=0, column=0, sticky="ew", pady=5)
        tk.Button(self.f_buttons, text="Subtract(-)", state="disabled", command=lambda: self.v_oper("-"),
                  bg="Goldenrod").grid(row=1, column=0, sticky="ew", pady=5)
        tk.Button(self.f_buttons, text="Cross Product(x)", state="disabled",
                  command=lambda: self.v_oper("x"), bg="Goldenrod").grid(row=2, column=0, sticky="ew", pady=5)
        tk.Button(self.f_buttons, text="Dot Product(\u00b7)", state="disabled",
                  command=lambda: self.v_oper("\u00b7"), bg="Goldenrod").grid(row=3, column=0, sticky="ew", pady=5)

        # Bindings
        self.bind_all("<MouseWheel>", self.scrollwin)
        self.basecan.create_window(0, 0, window=self.baseframe)
        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)
        self.mainloop()

    def v_oper(self, oper):
        self.b_load.config(state="active", activebackground="Goldenrod")
        self.current_op = oper
        self.la_stat["text"] += oper
        self.b_result["state"] = "disabled"
        for i in self.f_buttons.winfo_children():
            i["state"] = "disabled"

    def show_vect(self):
        l_vals = deepcopy(list(self.vect_dict.values()))
        for i in l_vals:
            i.reverse()
        l_vals = list(chain(*l_vals))
        vect_result = l_vals[1]
        i = 2
        while i < len(l_vals):
            if isinstance(l_vals[i], str):
                if l_vals[i] == "+":
                    try:
                        vect_result += l_vals[i + 1]
                    except TypeError:
                        messagebox.showerror("ERROR", "A number cannot be added to a vector (Can arise due to a dot "
                                                      "or operation in between")
                        return
                elif l_vals[i] == "-":
                    vect_result -= l_vals[i + 1]
                elif l_vals[i] == "\u00b7":
                    vect_result = Vector.DotProduct(vect_result, l_vals[i + 1])
                elif l_vals[i] == "x":
                    vect_result = Vector.CrossProduct(vect_result, l_vals[i + 1])
                i += 2
        newwin = tk.Toplevel(bg="White")
        newwin.iconbitmap(r"C:\Users\Admin\Downloads\475497.ico")
        la_result = tk.Label(newwin, bg="White", font=("Calibri", 18), fg="Black")
        if isinstance(vect_result, Vector):
            la_result["text"] = f"{self.la_stat['text']} = {str(vect_result).replace('Vector(', '')[:-1]}"
        else:
            la_result["text"] = f"{self.la_stat['text']} = {str(vect_result)}"
        la_result.pack(padx=20)

    def del_vect(self, closebtn):
        row = closebtn.nametowidget(closebtn.winfo_parent()).grid_info()["row"]
        s_vname, s_vname1 = f"V{str(row).translate(sub)}", f"V{str(row + 1).translate(sub)}"
        closebtn.nametowidget(closebtn.winfo_parent()).destroy()
        v_op = self.vect_dict[s_vname][1]
        del self.vect_dict[s_vname]
        if self.vect_num > 1 and self.vect_num - row >= 1:
            if row == 0:
                self.la_stat["text"] = self.la_stat["text"].replace(f"{s_vname}{self.vect_dict[s_vname1][1]}", "")
            else:
                self.la_stat["text"] = self.la_stat["text"].replace(f"{v_op}{s_vname}", "")
            if self.vect_num - row == 2:
                la_vect = self.f_main.grid_slaves(row + 1, 0)[0].winfo_children()[2]
                la_vect["text"] = la_vect["text"].replace(s_vname1, s_vname)
                self.f_main.grid_slaves(row + 1, 0)[0].grid(row=row)
                self.la_stat["text"] = self.la_stat["text"].replace(s_vname1, s_vname)
                self.vect_dict[s_vname] = self.vect_dict.pop(s_vname1)
            elif self.vect_num - row > 2:
                for i in range(row + 1, self.vect_num):
                    iter_vect1, iter_vect2 = f'V{str(i).translate(sub)}', f'V{str(i - 1).translate(sub)}'
                    if i - 1 == 0:
                        self.la_stat["text"] = self.la_stat["text"].replace(f"{iter_vect1}", f"{iter_vect2}")
                    else:
                        self.la_stat["text"] = self.la_stat["text"].replace(
                            f"{self.vect_dict[iter_vect1][1]}{iter_vect1}",
                            f"{self.vect_dict[iter_vect1][1]}{iter_vect2}")
                    self.vect_dict[iter_vect2] = self.vect_dict.pop(iter_vect1)
                    la_vect = self.f_main.grid_slaves(i, 0)[0].winfo_children()[2]
                    la_vect["text"] = la_vect["text"].replace(iter_vect1, iter_vect2)
                    self.f_main.grid_slaves(i, 0)[0].grid(row=i - 1)
        elif self.vect_num == 1:
            self.la_stat["text"] = ""
            self.b_load["state"] = "active"
            for i in self.f_buttons.winfo_children():
                i["state"] = "disabled"

        self.vect_num -= 1
        if self.vect_num < 2:
            self.b_result["state"] = "disabled"
        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)

    def copy_vect(self, copybtn):
        v_text = copybtn.nametowidget(copybtn.winfo_parent()).grid_slaves(1, 0)[0]["text"]
        paste_btn = tk.Button(self.f_top, text="Paste", command=lambda: self.paste_vect(v_text, paste_btn),
                              bg="Goldenrod")
        paste_btn.grid(row=1, column=6, pady=10)

    def paste_vect(self, text, btn_paste):
        if self.f_buttons.winfo_children()[0]["state"] == "disabled":
            self.v_load(False, text)
            btn_paste.destroy()
        else:
            messagebox.showerror("ERROR", "Enter operation to be performed")

    def v_load(self, trueload: bool = True, s_text: str = ""):
        """Both trueload and s_text are only for pasting vectors. if trueload is False, and s_text has the copied
        vector's text, it means vector is ready to be pasted"""
        s_vname = f"V{str(self.vect_num).translate(sub)}"
        if trueload:
            l_vals = []
            for i in self.f_top.grid_slaves():
                if isinstance(i, (tk.Button, tk.Label)):
                    continue
                else:
                    l_vals.append(float(i.get()))
            l_vals.reverse()
            vect = Vector(l_vals[0], l_vals[1], l_vals[2])
            vect_text = s_vname + f" = {str(vect).replace('Vector ', '')}"
            self.vect_dict[s_vname] = [None, None]
            self.vect_dict[s_vname][0], self.vect_dict[s_vname][1] = vect, self.current_op
            self.la_stat["text"] += s_vname
        else:
            vect_text = s_vname + f" = {s_text[5:]}"
            self.vect_dict[s_vname] = [None, None]
            self.vect_dict[s_vname][0] = self.vect_dict[s_text[:2]][0]
            self.vect_dict[s_vname][1] = self.la_stat["text"][-1]
            self.la_stat["text"] += s_vname

        f_vect = tk.Frame(self.f_main, bg="Mediumspringgreen")
        b_copy = tk.Button(f_vect, text="Copy", command=lambda: self.copy_vect(b_copy))
        b_copy.grid(row=0, column=0, sticky="w")
        b_close = tk.Button(f_vect, text="X", command=lambda: self.del_vect(b_close))
        b_close.grid(row=0, column=1, sticky="e")
        la_vect = tk.Label(f_vect, text=vect_text, bg="green", font=("Calibri", 16))
        la_vect.grid(row=1, column=0, columnspan=2)
        f_vect.grid(row=self.vect_num, column=0, sticky="n", pady=10)

        self.f_main.grid(row=2, column=0, sticky="n", pady=5)
        if self.vect_num > 0:
            self.b_result.config(state="active", activebackground="Goldenrod")

        for i in self.f_buttons.winfo_children():
            i.config(state="active", activebackground="Goldenrod")
        self.b_load["state"] = "disabled"

        self.vect_num += 1
        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)

    def scrollwin(self, event):
        self.basecan.yview_scroll(-1 * event.delta // 120, "units")


sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
if __name__ == "__main__":
    win = Window()
