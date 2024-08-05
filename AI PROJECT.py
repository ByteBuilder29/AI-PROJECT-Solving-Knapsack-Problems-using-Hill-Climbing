#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import matplotlib.pyplot as plt

def generate_random_solution(items):
    return [random.randint(0, 1) for _ in range(len(items))]

def calculate_value(solution, items):
    total_value = sum(item[0] for item, selected in zip(items, solution) if selected)
    total_weight = sum(item[1] for item, selected in zip(items, solution) if selected)
    return total_value, total_weight

def generate_neighbor(current_solution):
    index = random.randint(0, len(current_solution) - 1)
    neighbor = current_solution[:]
    neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
    return neighbor

def knapsack_hill_climbing(items, max_weight, max_iterations):
    current_solution = generate_random_solution(items)
    current_value, current_weight = calculate_value(current_solution, items)
    
    print("\nInitial Solution:")
    print("Solution:", current_solution)
    print("Total Value:", current_value)
    print("Total Weight:", current_weight)
    
    for i in range(max_iterations):
        neighbor = generate_neighbor(current_solution)
        neighbor_value, neighbor_weight = calculate_value(neighbor, items)
        
        if neighbor_weight <= max_weight and neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            current_weight = neighbor_weight
            print(f"\nIteration {i+1} - Improved Solution:")
            print("Solution:", current_solution)
            print("Total Value:", current_value)
            print("Total Weight:", current_weight)
        else:
            print(f"\nIteration {i+1} - No improvement.")
    
    return current_solution, current_value, current_weight

def knapsack_solver(items, max_weight, max_iterations):
    algorithm = "hill climbing"
    solution, value, weight = knapsack_hill_climbing(items, max_weight, max_iterations)
    return solution, value, weight

def get_user_input():
    print("\nWelcome to the Knapsack Problem Solver!")
    try:
        items = []
        num_items = int(input("Enter the number of items: "))
        if num_items <= 0:
            raise ValueError("Number of items must be greater than zero.")
        
        for i in range(num_items):
            value = float(input(f"Enter value for item {i+1}: "))
            weight = float(input(f"Enter weight for item {i+1}: "))
            items.append((value, weight))
        
        max_weight = float(input("Enter the maximum weight of the knapsack: "))
        if max_weight <= 0:
            raise ValueError("Maximum weight must be greater than zero.")
        
        max_iterations = int(input("Enter the maximum number of iterations: "))
        if max_iterations <= 0:
            raise ValueError("Maximum iterations must be greater than zero.")
        
        return items, max_weight, max_iterations
    except ValueError as ve:
        print(f"Error: {ve}")
        return None, None, None

def visualize_solution(items, solution, max_weight):
    selected_indices = [i for i, selected in enumerate(solution) if selected]
    selected_items = [items[i] for i in selected_indices]
    selected_values = [item[0] for item in selected_items]
    selected_weights = [item[1] for item in selected_items]

    all_values = [item[0] for item in items]
    all_weights = [item[1] for item in items]

    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.bar(range(len(all_values)), all_values, color='lightblue', label='Item Values')
    plt.bar(selected_indices, selected_values, color='red', label='Selected Item Values')
    plt.xlabel('Items')
    plt.ylabel('Values')
    plt.title('Knapsack Problem Solution - Item Values')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.bar(range(len(all_weights)), all_weights, color='lightgreen', label='Item Weights')
    plt.bar(selected_indices, selected_weights, color='green', label='Selected Item Weights')
    plt.xlabel('Items')
    plt.ylabel('Weights')
    plt.title('Knapsack Problem Solution - Item Weights')
    plt.legend()
    plt.grid(True)

    available_weight = max_weight - sum(selected_weights)
    plt.subplot(3, 1, 3)
    plt.axhline(y=max_weight, color='gray', linestyle='--', label='Max Weight')
    plt.fill_betweenx([0, max_weight], 0, len(items), color='lightgray', label='Available Weight')
    plt.xlabel('Items')
    plt.ylabel('Weight')
    plt.title('Available Weight in Knapsack')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    items, max_weight, max_iterations = get_user_input()
    if items is None:
        return

    solution, value, weight = knapsack_solver(items, max_weight, max_iterations)
    if solution is not None:
        print("\nFinal Solution:")
        print("Solution:", solution)
        print("Total Value:", value)
        print("Total Weight:", weight)

        visualize_solution(items, solution, max_weight)  

if __name__ == "__main__":
    main()


# In[4]:


import random
import matplotlib.pyplot as plt

def generate_random_solution(items):
    return [random.randint(0, 1) for _ in range(len(items))]

def calculate_value(solution, items):
    total_value = sum(item[0] for item, selected in zip(items, solution) if selected)
    total_weight = sum(item[1] for item, selected in zip(items, solution) if selected)
    return total_value, total_weight

def generate_neighbor(current_solution):
    index = random.randint(0, len(current_solution) - 1)
    neighbor = current_solution[:]
    neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
    return neighbor

def knapsack_hill_climbing(items, max_weight, max_iterations):
    current_solution = generate_random_solution(items)
    current_value, current_weight = calculate_value(current_solution, items)
    
    print("\nInitial Solution:")
    print("Solution:", current_solution)
    print("Total Value:", current_value)
    print("Total Weight:", current_weight)
    
    solution_history = [(current_solution, current_value, current_weight)]
    
    for i in range(max_iterations):
        neighbor = generate_neighbor(current_solution)
        neighbor_value, neighbor_weight = calculate_value(neighbor, items)
        
        if neighbor_weight <= max_weight and neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            current_weight = neighbor_weight
            print(f"\nIteration {i+1} - Improved Solution:")
            print("Solution:", current_solution)
            print("Total Value:", current_value)
            print("Total Weight:", current_weight)
            solution_history.append((current_solution, current_value, current_weight))
        else:
            print(f"\nIteration {i+1} - No improvement.")
    
    return solution_history

def knapsack_solver(items, max_weight, max_iterations):
    algorithm = "hill climbing"
    solution_history = knapsack_hill_climbing(items, max_weight, max_iterations)
    return solution_history

def get_user_input():
    print("\nWelcome to the Knapsack Problem Solver!")
    try:
        items = []
        num_items = int(input("Enter the number of items: "))
        if num_items <= 0:
            raise ValueError("Number of items must be greater than zero.")
        
        for i in range(num_items):
            value = float(input(f"Enter value for item {i+1}: "))
            weight = float(input(f"Enter weight for item {i+1}: "))
            items.append((value, weight))
        
        max_weight = float(input("Enter the maximum weight of the knapsack: "))
        if max_weight <= 0:
            raise ValueError("Maximum weight must be greater than zero.")
        
        max_iterations = int(input("Enter the maximum number of iterations: "))
        if max_iterations <= 0:
            raise ValueError("Maximum iterations must be greater than zero.")
        
        return items, max_weight, max_iterations
    except ValueError as ve:
        print(f"Error: {ve}")
        return None, None, None

def visualize_solution_history(items, solution_history, max_weight):
    num_iterations = len(solution_history)
    plt.figure(figsize=(12, 6*num_iterations))
    
    for i, (solution, value, weight) in enumerate(solution_history):
        selected_indices = [i for i, selected in enumerate(solution) if selected]
        selected_items = [items[i] for i in selected_indices]
        selected_values = [item[0] for item in selected_items]
        selected_weights = [item[1] for item in selected_items]

        all_values = [item[0] for item in items]
        all_weights = [item[1] for item in items]

        plt.subplot(num_iterations, 1, i+1)
        plt.bar(range(len(all_values)), all_values, color='lightblue', label='Item Values')
        plt.bar(selected_indices, selected_values, color='red', label='Selected Item Values')
        plt.xlabel('Items')
        plt.ylabel('Values')
        plt.title(f'Iteration {i+1} - Knapsack Problem Solution - Item Values')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()

    plt.show()

def main():
    items, max_weight, max_iterations = get_user_input()
    if items is None:
        return

    solution_history = knapsack_solver(items, max_weight, max_iterations)
    if solution_history:
        print("\nFinal Solution:")
        final_solution, final_value, final_weight = solution_history[-1]
        print("Solution:", final_solution)
        print("Total Value:", final_value)
        print("Total Weight:", final_weight)

        visualize_solution_history(items, solution_history, max_weight)  

if __name__ == "__main__":
    main()


# In[10]:


import tkinter as tk
from tkinter import ttk, messagebox

class KnapsackSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Knapsack Problem Solver")

        # Variables to store user inputs
        self.items = []
        self.max_weight = tk.StringVar()
        self.algorithm = tk.StringVar()

        # Create input frame
        input_frame = ttk.Frame(root, padding=(20, 10))
        input_frame.pack(pady=20)

        # Number of items entry
        num_items_label = ttk.Label(input_frame, text="Number of Items:")
        num_items_label.grid(row=0, column=0, padx=5, pady=5)
        self.num_items_entry = ttk.Entry(input_frame)
        self.num_items_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create button to add item fields dynamically
        add_items_button = ttk.Button(input_frame, text="Add Items", command=self.add_item_fields)
        add_items_button.grid(row=0, column=2, padx=5, pady=5)

        # Algorithm selection
        algorithm_label = ttk.Label(input_frame, text="Algorithm:")
        algorithm_label.grid(row=1, column=0, padx=5, pady=5)
        self.algorithm_combobox = ttk.Combobox(input_frame, values=["Greedy", "Dynamic Programming"])
        self.algorithm_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Max weight entry
        max_weight_label = ttk.Label(input_frame, text="Max Weight:")
        max_weight_label.grid(row=2, column=0, padx=5, pady=5)
        self.max_weight_entry = ttk.Entry(input_frame, textvariable=self.max_weight)
        self.max_weight_entry.grid(row=2, column=1, padx=5, pady=5)

        # Solve button
        solve_button = ttk.Button(input_frame, text="Solve", command=self.solve_knapsack)
        solve_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

    def add_item_fields(self):
        try:
            num_items = int(self.num_items_entry.get())
            if num_items <= 0:
                raise ValueError("Number of items must be greater than zero.")
            
            # Destroy existing item fields if any
            for widget in self.root.winfo_children():
                widget.destroy()

            # Create new item entry fields
            self.items = []
            for i in range(num_items):
                item_frame = ttk.Frame(self.root, padding=(20, 10))
                item_frame.pack(pady=10)
                value_label = ttk.Label(item_frame, text=f"Item {i+1} Value:")
                value_label.grid(row=0, column=0, padx=5, pady=5)
                value_entry = ttk.Entry(item_frame)
                value_entry.grid(row=0, column=1, padx=5, pady=5)
                weight_label = ttk.Label(item_frame, text=f"Item {i+1} Weight:")
                weight_label.grid(row=1, column=0, padx=5, pady=5)
                weight_entry = ttk.Entry(item_frame)
                weight_entry.grid(row=1, column=1, padx=5, pady=5)
                self.items.append((value_entry, weight_entry))

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")

    def solve_knapsack(self):
        try:
            max_weight = float(self.max_weight.get())
            algorithm = self.algorithm.get()

            # Get items' values and weights from entry fields
            items = [(float(value_entry.get()), float(weight_entry.get())) for value_entry, weight_entry in self.items]

            # Call knapsack solver function based on selected algorithm
            if algorithm == "Greedy":
                solution = self.greedy_solver(items, max_weight)
            elif algorithm == "Dynamic Programming":
                solution = self.dp_solver(items, max_weight)
            else:
                raise ValueError("Invalid algorithm selected.")

            # Display solution
            messagebox.showinfo("Solution", f"Selected Items: {solution}")

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")

    def greedy_solver(self, items, max_weight):
        # Implement greedy knapsack solver algorithm
        pass

    def dp_solver(self, items, max_weight):
        # Implement dynamic programming knapsack solver algorithm
        pass

root = tk.Tk()
app = KnapsackSolverGUI(root)
root.mainloop()


# In[24]:


import tkinter as tk
from tkinter import scrolledtext
import random
import matplotlib.pyplot as plt

class KnapsackSolverGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Knapsack Problem Solver")

        # Number of items entry
        self.num_items_entry = tk.Entry(self.root)
        self.num_items_entry.grid(row=0, column=1)
        self.num_items_label = tk.Label(self.root, text="Number of Items:")
        self.num_items_label.grid(row=0, column=0)

        # Maximum weight entry
        self.max_weight_entry = tk.Entry(self.root)
        self.max_weight_entry.grid(row=1, column=1)
        self.max_weight_label = tk.Label(self.root, text="Maximum Weight of the Knapsack:")
        self.max_weight_label.grid(row=1, column=0)

        # Maximum iterations entry
        self.max_iterations_entry = tk.Entry(self.root)
        self.max_iterations_entry.grid(row=2, column=1)
        self.max_iterations_label = tk.Label(self.root, text="Maximum Number of Iterations:")
        self.max_iterations_label.grid(row=2, column=0)

        # Add items button
        self.add_items_button = tk.Button(self.root, text="Add Items", command=self.add_items)
        self.add_items_button.grid(row=3, column=0, columnspan=2)

        # Scrolled text widget to display solution
        self.solution_text = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.solution_text.grid(row=5, columnspan=2)

        self.root.mainloop()

    def add_items(self):
        try:
            self.num_items = int(self.num_items_entry.get())
            self.max_weight = float(self.max_weight_entry.get())
            self.max_iterations = int(self.max_iterations_entry.get())

            # Entry fields for item values and weights
            self.items = []
            for i in range(self.num_items):
                value_entry = tk.Entry(self.root)
                value_entry.grid(row=6 + i, column=1)
                value_label = tk.Label(self.root, text=f"Value for Item {i + 1}:")
                value_label.grid(row=6 + i, column=0)

                weight_entry = tk.Entry(self.root)
                weight_entry.grid(row=6 + i + self.num_items, column=1)
                weight_label = tk.Label(self.root, text=f"Weight for Item {i + 1}:")
                weight_label.grid(row=6 + i + self.num_items, column=0)

                self.items.append((value_entry, weight_entry))

            # Solve Knapsack button
            self.solve_button = tk.Button(self.root, text="Solve Knapsack", command=self.solve_knapsack)
            self.solve_button.grid(row=6 + self.num_items * 2, column=0, columnspan=2)

        except ValueError as ve:
            print(f"Error: {ve}")

    def solve_knapsack(self):
        try:
            items = [(float(value_entry.get()), float(weight_entry.get())) for value_entry, weight_entry in self.items]

            solution_history = self.knapsack_solver(items, self.max_weight, self.max_iterations)

            if solution_history:
                self.display_solution(solution_history)
        except ValueError as ve:
            print(f"Error: {ve}")

    def knapsack_solver(self, items, max_weight, max_iterations):
        current_solution = self.generate_random_solution(items)
        current_value, current_weight = self.calculate_value(current_solution, items)

        solution_history = [(current_solution, current_value, current_weight)]

        for i in range(max_iterations):
            neighbor = self.generate_neighbor(current_solution)
            neighbor_value, neighbor_weight = self.calculate_value(neighbor, items)

            if neighbor_weight <= max_weight and neighbor_value > current_value:
                current_solution = neighbor
                current_value = neighbor_value
                current_weight = neighbor_weight
                solution_history.append((current_solution, current_value, current_weight))
            else:
                solution_history.append((current_solution, current_value, current_weight))

        return solution_history

    def generate_random_solution(self, items):
        return [random.randint(0, 1) for _ in range(len(items))]

    def calculate_value(self, solution, items):
        total_value = sum(item[0] for item, selected in zip(items, solution) if selected)
        total_weight = sum(item[1] for item, selected in zip(items, solution) if selected)
        return total_value, total_weight

    def generate_neighbor(self, current_solution):
        index = random.randint(0, len(current_solution) - 1)
        neighbor = current_solution[:]
        neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
        return neighbor

    def display_solution(self, solution_history):
        self.solution_text.delete('1.0', tk.END)
        for i, (solution, value, weight) in enumerate(solution_history):
            iteration_info = f"Iteration {i+1} - "
            solution_info = f"Solution: {solution}\n"
            value_info = f"Total Value: {value}\n"
            weight_info = f"Total Weight: {weight}\n\n"
            self.solution_text.insert(tk.END, iteration_info)
            self.solution_text.insert(tk.END, solution_info)
            self.solution_text.insert(tk.END, value_info)
            self.solution_text.insert(tk.END, weight_info)

KnapsackSolverGUI()


# In[1]:


import tkinter as tk
from tkinter import scrolledtext
import random

class KnapsackSolverGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Knapsack Problem Solver")
        self.root.geometry("600x500")  # Set window size
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Create frame for input fields
        input_frame = tk.Frame(self.root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        input_frame.pack(pady=20)

        # Number of items entry
        self.num_items_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bd=1)
        self.num_items_entry.grid(row=0, column=1, padx=10, pady=10)
        self.num_items_label = tk.Label(input_frame, text="Number of Items:", font=("Arial", 12), bg="#f0f0f0")
        self.num_items_label.grid(row=0, column=0, padx=10, pady=10)

        # Maximum weight entry
        self.max_weight_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bd=1)
        self.max_weight_entry.grid(row=1, column=1, padx=10, pady=10)
        self.max_weight_label = tk.Label(input_frame, text="Maximum Weight of the Knapsack:", font=("Arial", 12), bg="#f0f0f0")
        self.max_weight_label.grid(row=1, column=0, padx=10, pady=10)

        # Maximum iterations entry
        self.max_iterations_entry = tk.Entry(input_frame, width=10, font=("Arial", 12), bd=1)
        self.max_iterations_entry.grid(row=2, column=1, padx=10, pady=10)
        self.max_iterations_label = tk.Label(input_frame, text="Maximum Number of Iterations:", font=("Arial", 12), bg="#f0f0f0")
        self.max_iterations_label.grid(row=2, column=0, padx=10, pady=10)

        # Add items button
        self.add_items_button = tk.Button(input_frame, text="Add Items", font=("Arial", 12), bg="#4caf50", fg="white", relief=tk.FLAT, command=self.add_items)
        self.add_items_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Solve Knapsack button
        self.solve_button = tk.Button(input_frame, text="Solve Knapsack", font=("Arial", 12), bg="#2196f3", fg="white", relief=tk.FLAT, command=self.solve_knapsack)
        self.solve_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create frame for item entries
        self.items_frame = tk.Frame(self.root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.items_frame.pack(pady=20)

        # Scrolled text widget to display solution
        self.solution_text = scrolledtext.ScrolledText(self.root, width=50, height=15, font=("Arial", 12), bg="#ffffff", bd=2, relief=tk.GROOVE)
        self.solution_text.pack(pady=20, fill=tk.BOTH, expand=True)

        self.root.mainloop()

    def add_items(self):
        try:
            self.num_items = int(self.num_items_entry.get())
            self.max_weight = float(self.max_weight_entry.get())
            self.max_iterations = int(self.max_iterations_entry.get())

            # Clear previous item entries
            for widget in self.items_frame.winfo_children():
                widget.destroy()

            # Entry fields for item values and weights
            self.items = []
            for i in range(self.num_items):
                value_entry = tk.Entry(self.items_frame, width=10, font=("Arial", 12), bd=1)
                value_entry.grid(row=i, column=1, padx=10, pady=5)
                value_label = tk.Label(self.items_frame, text=f"Value for Item {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
                value_label.grid(row=i, column=0, padx=10, pady=5)

                weight_entry = tk.Entry(self.items_frame, width=10, font=("Arial", 12), bd=1)
                weight_entry.grid(row=i, column=3, padx=10, pady=5)
                weight_label = tk.Label(self.items_frame, text=f"Weight for Item {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
                weight_label.grid(row=i, column=2, padx=10, pady=5)

                self.items.append((value_entry, weight_entry))

        except ValueError as ve:
            print(f"Error: {ve}")

    def solve_knapsack(self):
        try:
            items = [(float(value_entry.get()), float(weight_entry.get())) for value_entry, weight_entry in self.items]

            current_solution = self.generate_random_solution(items)
            current_value, current_weight = self.calculate_value(current_solution, items)

            solution_history = [(current_solution, current_value, current_weight)]

            for i in range(1, self.max_iterations + 1):  # Start from 1 since we already have the initial solution
                neighbor = self.generate_neighbor(current_solution)
                neighbor_value, neighbor_weight = self.calculate_value(neighbor, items)

                if neighbor_weight <= self.max_weight and neighbor_value > current_value:
                    current_solution = neighbor
                    current_value = neighbor_value
                    current_weight = neighbor_weight
                    solution_history.append((current_solution, current_value, current_weight))
                else:
                    break  # Stop iterating if there's no improvement

            if solution_history:
                self.display_solution("Final", current_solution, current_value, current_weight)  # Display the final solution
        except ValueError as ve:
            print(f"Error: {ve}")

    def generate_random_solution(self, items):
        return [random.randint(0, 1) for _ in range(len(items))]

    def calculate_value(self, solution, items):
        total_value = sum(float(item[0].get()) for item, selected in zip(self.items, solution) if selected)
        total_weight = sum(float(item[1].get()) for item, selected in zip(self.items, solution) if selected)
        return total_value, total_weight

    def generate_neighbor(self, current_solution):
        index = random.randint(0, len(current_solution) - 1)
        neighbor = current_solution[:]
        neighbor[index] = 1 - neighbor[index]  # Flip 0 to 1 or 1 to 0
        return neighbor

    def display_solution(self, iteration, solution, value, weight):
        if iteration == "Final":
            self.solution_text.delete('1.0', tk.END)  # Clear previous output
            self.solution_text.insert(tk.END, f"Final Solution:\n", "bold")
            self.solution_text.insert(tk.END, f"Solution: {solution}\n")
            self.solution_text.insert(tk.END, f"Total Value: {value}\n")
            self.solution_text.insert(tk.END, f"Total Weight: {weight}\n")
        else:
            self.solution_text.insert(tk.END, f"Iteration {iteration}:\n", "bold")
            self.solution_text.insert(tk.END, f"Solution: {solution}\n")
            self.solution_text.insert(tk.END, f"Total Value: {value}\n")
            self.solution_text.insert(tk.END, f"Total Weight: {weight}\n")
        self.solution_text.insert(tk.END, "\n", "normal")

KnapsackSolverGUI()


# In[ ]:




