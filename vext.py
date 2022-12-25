import tkinter as tk
from math import degrees, acos
from typing import overload, Union
from functools import reduce
from tkinter import messagebox


class Vector:
    """Vector object with general attributes and methods. Operations are supported. Numerical attributes are
    returned as long float objects. Please use round() for your convenience"""

    @overload
    def __init__(self, vector: "Vector") -> None:
        # The following is for pycharm's goddamn inspection saying attributes are unresolved in other methods. Interpreter wont run this ever
        self.x = self.y = self.z = self.dircos_l = self.dircos_m = self.dircos_n = None
        self.alpha = self.beta = self.gamma = self.dimension = self.length = None

    @overload
    def __init__(self, Complex: complex) -> None:
        pass

    @overload
    def __init__(self, x_comp: float = 0.0, y_comp: float = 0.0, z_comp: float = 0.0):
        pass

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
    def FromTwoPoints(cls,  A: (int, int, int), B: (int, int, int)) -> "Vector":
        return cls(B[0] - A[0], B[1] - A[1], B[2] - A[2])

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
        if isinstance(other,(float, int)):
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
        x = f"+{self.x}\u00ee " if self.x > 0 else (f"{self.x}\u00ee " if self.x < 0 else "")
        y = f"+{self.y}\u0135 " if self.y > 0 else (f"{self.y}\u0135 " if self.y < 0 else "")
        z = f"+{self.z}\u006b\u0302" if self.z > 0 else (f"{self.z}\u006b\u0302" if self.z < 0 else "")
        if x == "" and y == "" and z == "":
            return f"Vector (0)"
        else:
            return f"Vector ({x}{y}{z})"


class Window(tk.Tk):

    def __init__(self):
        super(Window, self).__init__()
        self.title("Vector Calculator")
        self.geometry("500x500")
        self.iconbitmap(r"C:\Users\Admin\Downloads\475496.ico")
        self.config(bg="Black")

        self.scroll_v = tk.Scrollbar(self, orient="vertical")
        self.scroll_v.pack(side="right", fill="y")
        self.basecan = tk.Canvas(self, bd=0, yscrollcommand=self.scroll_v.set, bg="Mediumspringgreen")
        self.basecan.pack(fill="both", expand="true")
        self.baseframe = tk.Frame(self.basecan, bd=0, bg="Mediumspringgreen")

        self.vect_num = 0

        self.f_main = tk.Frame(self.baseframe, bd=1, bg="Mediumspringgreen")
        self.f_buttons = tk.Frame(self.baseframe, bg="Mediumspringgreen")

        self.b_load = tk.Button(self.baseframe, text="Load vector", bg="Goldenrod", command=lambda: self.v_load((0, 0, 0)))
        self.b_load.pack(padx=130)
        self.b_add = tk.Button(self.f_buttons, text="Add(+)", command=self.v_add, bg="Goldenrod")
        self.b_sub = tk.Button(self.f_buttons, text="Subtract(-)", command=self.v_sub, bg="Goldenrod")
        self.b_mulc = tk.Button(self.f_buttons, text="Cross Product(x)", command=self.v_mulc, bg="Goldenrod")
        self.b_muld = tk.Button(self.f_buttons, text="Dot Product(.)", command=self.v_muld, bg="Goldenrod")
        self.b_add.grid(row=0, column=0, sticky="ew", padx=5)
        self.b_sub.grid(row=0, column=1, sticky="ew", padx=5)
        self.b_mulc.grid(row=0, column=2, sticky="ew", padx=5)
        self.b_muld.grid(row=0, column=3, sticky="ew", padx=5)

        self.basecan.create_window(75, 0, anchor="nw", window=self.baseframe)
        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)
        self.basecan.bind_all("<MouseWheel>", self.scrollwin)
        dn.grid_slaves():
            for j in i.grid_slaves():
                if isinstance(j, tk.Frame):
                    lvals = []
                    for k in (j.grid_slaves()[5], j.grid_slaves()[4], j.grid_slaves()[3]):
                        lvals.append(float(k.get()))
                    l_set.append(lvals)
        l_set.reverse()
        for i in l_set:
            v = Vector(i[0], i[1], i[2])
            l_vectors.append(v)

        return l_vectors

    def v_add(self):
        l_vect = self.collect_vect()
        if len(l_vect)>1:
            result_vect = reduce((lambda vect1, vect2: vect1 + vect2), l_vect)
            self.show_vect(result_vect, "+")
        else:
            messagebox.showerror("ERROR", "Please load another vector to perform operation")

    def v_sub(self):
        l_vect = self.collect_vect()
        if len(l_vect)>1:
            result_vect = reduce((lambda vect1, vect2: vect1 - vect2), l_vect)
            self.show_vect(result_vect, "-")
        else:/
            messagebox.showerror("ERROR", "Please load another vector to perform operation")

    def v_mulc(self):
        l_vect = self.collect_vect()
        if len(l_vect)>1:
            result_vect = reduce((lambda vect1, vect2: Vector.CrossProduct(vect1, vect2)), l_vect)
            self.show_vect(result_vect, "x")
        else:
            messagebox.showerror(" ERROR", "Please load another vector to perform operation")

    def v_muld(self):
        l_vect = self.collect_vect()
        if len(l_vect)>1:
            result_val = reduce((lambda vect1, vect2: Vector.DotProduct(vect1, vect2)), l_vect)
            self.show_vect(result_val, ".")
        else:
            messagebox.showerror("ERROR", "Please load another vector to perform operation")

    def show_vect(self, result: Union["Vector", float], oper: str):
          newwin = tk.Toplevel()
        if isinstance(result, Vector):
            vect_str = ""
            for i in range(self.vect_num):
                vect_str += f"V{str(self.vect_num + 1).translate(subscript)}{oper}"
            vect_str += str(result).replace("Vector ", "")

            tk.Label(newwin, text=vect_str, height=20, width=20, font=("Lucida", 18), bg="Brown").pack(padx=10, pady=10)
            newwin.iconbitmap(r"C:\Users\Admin\Downloads\Calculator_5122x.ico")

        elif isinstance(result, float):
            tk.Label(newwin, text=result).pack()

    def del_vect(self, closebtn):
        row = closebtn.grid_info()["in"].grid_info()["row"]
        self.f_main.grid_slaves(row, 0)[0].destroy()
        self.f_main.grid_slaves(row, 1)[0].destroy()
        self.vect_num -= 1
        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)

    def copy_vect(self, copybtn):
        row = copybtn.grid_info()["in"].grid_info()["row"]
        l_wids = self.f_main.grid_slaves(row, 0)[0].grid_slaves()[0].grid_slaves()
        x, y, z = l_wids[5].get(), l_wids[4].get(), l_wids[3].get()
        paste_btn = tk.Button(self.f_buttons, text="Paste Vector", command=lambda: self.v_load((x, y, z)))
        paste_btn.grid(row=1, column=0, columnspan=4, pady=10)

    def v_load(self, l_coord: (float, float, float)):
        f_set = tk.Frame(self.f_main, bg="Peru")
        f_vector = tk.Frame(f_set, bd=1, relief="solid", bg="Peru")
        l_spins = []
        for i in range(3):
            spin = tk.Spinbox(f_vector, from_=-100, to=10000, increment=0.5, width=6)
            spin.delete(0, "end")
            spin.insert(0, l_coord[i]
            spin.grid(row=1, column=i * 2, padx=5, pady=5)
            l_spins.append(spin)

        la_i = tk.Label(f_vector, text="\u00ee", bg="Peru")
        la_j = tk.Label(f_vector, text="\u0135", bg="Peru")
        la_k = tk.Label(f_vector, text="\u006b\u0302", bg="Peru")
        la_i.grid(row=1, column=1, padx=(0, 10))
        la_j.grid(row=1, column=3, padx=(0, 10))
        la_k.grid(row=1, column=5)

        b_close = tk.Button(f_set, text="X", command=lambda: self.del_vect(b_close))
        b_close.grid(row=0, column=0, sticky="ne")
        b_copy = tk.Button(f_set, text="COPY", command=lambda: self.copy_vect(b_copy))
        b_copy.grid(row=0, column=0, sticky="nw")

        f_vector.grid(row=1, column=0)
        tk.Label(self.f_main, text=f"V{str(self.vect_num + 1).translate(subscript)} = ", bg="Mediumspringgreen").grid(
            row=self.vect_num, column=0)
        f_set.grid(row=self.vect_num, column=1, pady=20)
        self.vect_num += 1
        if self.vect_num <= 1:
            self.f_buttons.pack(pady=20)
            self.f_main.pack()

        self.basecan.update_idletasks()
        self.basecan.configure(scrollregion=self.basecan.bbox("all"))
        self.scroll_v.configure(command=self.basecan.yview)

    def scrollwin(self, event):
        self.basecan.yview_scroll(-1 * event.delta // 120, "units")

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
if __name__ == "__main__":
    win = Window()
