from tkinter import *
from tkinter import ttk, messagebox
from controller import Manager

class StudentView:
    def __init__(self, root):
        self.manager = Manager()
        root.title("Student Management")
        root.geometry("700x500")
        root.configure(bg="#1E1E1E")  

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#2A2A2A",
                        foreground="white",
                        fieldbackground="#2A2A2A",
                        rowheight=25,
                        font=("Segoe UI", 11))
        style.configure("Treeview.Heading",
                        background="#3A3A3A",
                        foreground="white",
                        font=("Segoe UI", 12, "bold"))

        self.columns = ("id", "name", "last_name", "score")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150, anchor=CENTER)
        self.tree.pack(fill=BOTH, expand=True, pady=20)

        btn_style = {
            "font": ("Segoe UI", 11, "bold"),
            "fg": "white",
            "width": 12,
            "height": 1,
            "bd": 0
        }

        Button(root, text="Add", bg="#3C6E71", command=self.add_record, **btn_style).place(x=80, y=450)
        Button(root, text="Update", bg="#284B63", command=self.open_update_window, **btn_style).place(x=220, y=450)
        Button(root, text="Delete", bg="#6E3C3C", command=self.delete_record, **btn_style).place(x=360, y=450)
        Button(root, text="Refresh", bg="#3A3A3A", command=self.refresh_tree, **btn_style).place(x=500, y=450)

        self.refresh_tree()

    def add_record(self):
        win = Toplevel()
        win.title("Add Student")
        win.geometry("400x250")
        win.configure(bg="#2A2A2A")

        Label(win, text="Name:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=30)
        name_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        name_entry.place(x=120, y=30, width=200)

        Label(win, text="Last Name:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=70)
        last_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        last_entry.place(x=120, y=70, width=200)

        Label(win, text="Score:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=110)
        score_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        score_entry.place(x=120, y=110, width=200)

        def save_add():
            ok = self.manager.add_student(name_entry.get(), last_entry.get(), score_entry.get())
            if ok:
                messagebox.showinfo("Success", "Student added successfully!")
                self.refresh_tree()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add student.")

        Button(win, text="Save", bg="#3C6E71", fg="white",
               font=("Segoe UI", 11, "bold"), command=save_add).place(x=150, y=160)

    def open_update_window(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to update.")
            return

        values = self.tree.item(selected[0], "values")

        win = Toplevel()
        win.title("Update Student")
        win.geometry("400x300")
        win.configure(bg="#2A2A2A")

        Label(win, text="ID:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=30)
        id_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        id_entry.place(x=120, y=30, width=200)
        id_entry.insert(0, values[0])
        id_entry.config(state="readonly")

        Label(win, text="Name:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=70)
        name_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        name_entry.place(x=120, y=70, width=200)
        name_entry.insert(0, values[1])

        Label(win, text="Last Name:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=110)
        last_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        last_entry.place(x=120, y=110, width=200)
        last_entry.insert(0, values[2])

        Label(win, text="Score:", fg="white", bg="#2A2A2A", font=("Segoe UI", 11)).place(x=30, y=150)
        score_entry = Entry(win, bg="#3A3A3A", fg="white", font=("Segoe UI", 11))
        score_entry.place(x=120, y=150, width=200)
        score_entry.insert(0, values[3])

        def save_update():
            ok = self.manager.update_student(values[0],
                                             name_entry.get(),
                                             last_entry.get(),
                                             score_entry.get())
            if ok:
                messagebox.showinfo("Success", "Student updated successfully!")
                self.refresh_tree()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update student.")

        Button(win, text="Save", bg="#3C6E71", fg="white",
               font=("Segoe UI", 11, "bold"), command=save_update).place(x=150, y=200)

    def delete_record(self):
        selected = self.tree.selection()
        if selected:
            student_id = self.tree.item(selected[0], "values")[0]
            ok = self.manager.remove_student(student_id)
            if ok:
                messagebox.showinfo("Success", "Student removed successfully!")
                self.refresh_tree()
            else:
                messagebox.showerror("Error", "Failed to remove student.")

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = self.manager.show_students()
        for s in students:
            self.tree.insert("", END, values=(s.id, s.Name, s.Last_name, s.Score))


if __name__ == "__main__":
    root = Tk()
    app = StudentView(root)
    root.mainloop()