import tkinter as tk
from tkinter import messagebox
import dim_utils

def on_check():
    user_input = entry.get().strip()

    if user_input.lower() in ("q", "quit", "exit"):
        root.quit()
        return

    try:
        total_inches = dim_utils.parse_input(user_input)
        is_block, next_b, prev_b = dim_utils.check_block_dimension(total_inches)

        parsed_label.config(
            text=f"Parsed Length: {dim_utils.format_inches_to_ft_in(total_inches)}"
        )

        if is_block:
            block_label.config(text="✓ This IS a block dimension.", fg="green")
        else:
            block_label.config(text="✗ This is NOT a block dimension.", fg="red")

        next_label.config(
            text=f"🡢 Next block: {dim_utils.format_inches_to_ft_in(next_b)}"
        )

        if prev_b:
            prev_label.config(
                text=f"🡠 Previous block: {dim_utils.format_inches_to_ft_in(prev_b)}"
            )
        else:
            prev_label.config(text="🡠 No smaller block dimension.")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        parsed_label.config(text="")
        block_label.config(text="")
        prev_label.config(text="")
        next_label.config(text="")


# 🪟 Setup window
root = tk.Tk()
root.title("CMU Block Dimension Checker")
root.geometry("400x250")
root.resizable(False, False)

# 🎯 Input
tk.Label(root, text="Enter a length (e.g. 6'4\", 76\", 5-8):").pack(pady=(10, 0))
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.focus()

# ✅ Make Enter key work
entry.bind("<Return>", lambda event: on_check())

# ✅ Check Button
tk.Button(root, text="Check", command=on_check).pack(pady=5)

# 📋 Output Labels
parsed_label = tk.Label(root, text="", font=("Segoe UI", 10))
parsed_label.pack(pady=2)

block_label = tk.Label(root, text="", font=("Segoe UI", 10, "bold"))
block_label.pack(pady=2)

prev_label = tk.Label(root, text="", font=("Segoe UI", 10))
prev_label.pack(pady=2)

next_label = tk.Label(root, text="", font=("Segoe UI", 10))
next_label.pack(pady=2)

# 🏁 Start app
root.mainloop()
