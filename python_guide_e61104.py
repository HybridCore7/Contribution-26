# Python Visual Debugger Tutorial

# Learning Objective:
# This tutorial will guide you through building a simple graphical debugger
# to visualize Python code execution and variable changes. We'll focus on
# understanding how to intercept code execution, inspect program state,
# and present this information in a user-friendly graphical interface.
# This will provide a hands-on understanding of debugging concepts.

# Core Concept: Using Python's `sys.settrace` for Code Interception

import sys
import tkinter as tk
from tkinter import scrolledtext, ttk

# --- Debugger Class ---
# This class will manage the debugging process and the GUI.

class VisualDebugger:
    def __init__(self, master):
        self.master = master
        master.title("Simple Python Visual Debugger")

        # --- GUI Setup ---
        # We'll use Tkinter for our graphical interface.
        # The interface will have areas to display the code,
        # the call stack, and local variables.

        self.setup_gui()

        # --- Debugging State ---
        # These variables will hold the state of our debugger.
        self.code_lines = []             # Stores the lines of the code being debugged.
        self.current_line_num = 0        # The line number currently being executed.
        self.breakpoints = set()         # A set of line numbers where execution should pause.
        self.variable_values = {}        # A dictionary to store the values of local variables.
        self.is_debugging = False        # Flag to indicate if debugging is active.
        self.execution_paused = False    # Flag to indicate if execution is currently paused.

        # --- GUI Elements ---
        # These are references to the Tkinter widgets we'll use.
        self.code_display = None
        self.variable_display = None
        self.stack_display = None
        self.output_display = None
        self.run_button = None
        self.step_button = None
        self.continue_button = None
        self.breakpoint_button = None

    def setup_gui(self):
        # Create the main frame for better organization.
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # --- Code Display Pane ---
        # This area will show the Python code being debugged.
        code_frame = ttk.LabelFrame(main_frame, text="Code", padding="5")
        code_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        self.code_display = scrolledtext.ScrolledText(code_frame, wrap=tk.WORD, width=50, height=15, font=("Courier", 10))
        self.code_display.grid(row=0, column=0)
        self.code_display.bind("<Button-3>", self.handle_right_click) # Bind right-click for breakpoints

        # --- Debugging Info Pane ---
        # This pane will show variable values and the call stack.
        debug_info_frame = ttk.Frame(main_frame, padding="5")
        debug_info_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        # Variable Display
        variable_frame = ttk.LabelFrame(debug_info_frame, text="Local Variables", padding="5")
        variable_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        self.variable_display = scrolledtext.ScrolledText(variable_frame, wrap=tk.WORD, width=30, height=8, font=("Courier", 10), state=tk.DISABLED)
        self.variable_display.grid(row=0, column=0)

        # Stack Display
        stack_frame = ttk.LabelFrame(debug_info_frame, text="Call Stack", padding="5")
        stack_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        self.stack_display = scrolledtext.ScrolledText(stack_frame, wrap=tk.WORD, width=30, height=8, font=("Courier", 10), state=tk.DISABLED)
        self.stack_display.grid(row=0, column=0)

        # --- Control Buttons Pane ---
        # Buttons for controlling the debugging process.
        control_frame = ttk.Frame(main_frame, padding="5")
        control_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        self.run_button = ttk.Button(control_frame, text="Load & Run", command=self.load_and_run)
        self.run_button.grid(row=0, column=0, padx=5)

        self.step_button = ttk.Button(control_frame, text="Step Over", command=self.step_over, state=tk.DISABLED)
        self.step_button.grid(row=0, column=1, padx=5)

        self.continue_button = ttk.Button(control_frame, text="Continue", command=self.continue_execution, state=tk.DISABLED)
        self.continue_button.grid(row=0, column=2, padx=5)

        self.breakpoint_button = ttk.Button(control_frame, text="Clear Breakpoints", command=self.clear_all_breakpoints)
        self.breakpoint_button.grid(row=0, column=3, padx=5)

        # --- Output Pane ---
        # To capture the program's standard output.
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="5")
        output_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        self.output_display = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=80, height=8, font=("Courier", 10), state=tk.DISABLED)
        self.output_display.grid(row=0, column=0)

    def load_and_run(self):
        # Loads the code from the text area and starts the debugging process.
        code = self.code_display.get("1.0", tk.END)
        self.code_lines = code.splitlines()
        self.current_line_num = 0
        self.variable_values = {}
        self.breakpoints = set() # Clear any previous breakpoints
        self.is_debugging = True
        self.execution_paused = False

        # Clear previous displays.
        self.update_variable_display()
        self.update_stack_display()
        self.update_output_display("")
        self.highlight_current_line()

        # Prepare the execution environment.
        # We'll use a local namespace to execute the code safely.
        local_namespace = {}
        try:
            # Compile the code for execution.
            compiled_code = compile(code, '<string>', 'exec')
            # Set up the trace function.
            sys.settrace(self.trace_function)
            # Execute the compiled code.
            exec(compiled_code, {}, local_namespace)
            self.update_output_display("Program finished successfully.\n")
        except Exception as e:
            self.update_output_display(f"Error during execution: {e}\n")
            self.reset_debugger_state()
        finally:
            # Always disable tracing when done or on error.
            sys.settrace(None)
            self.reset_debugger_state()

    def trace_function(self, frame, event, arg):
        # This is the core of our debugger.
        # `sys.settrace` calls this function for various events during execution.
        # `frame`: The current frame object. Contains info about function calls.
        # `event`: Type of event ('call', 'line', 'return', 'exception').
        # `arg`: Event-specific argument.

        if event == 'line':
            # We are interested in 'line' events to track execution line by line.
            self.current_line_num = frame.f_lineno - 1 # Adjust for 0-based indexing
            self.update_variable_values(frame)         # Update variable display
            self.update_stack_display_from_frame(frame) # Update stack display
            self.highlight_current_line()              # Visually highlight the current line

            # Check for breakpoints.
            if self.current_line_num in self.breakpoints:
                self.pause_execution("Breakpoint hit.")
            else:
                # If not paused at a breakpoint, we can auto-continue if not explicitly paused.
                if not self.execution_paused:
                    return self.trace_function # Continue tracing
                else:
                    # If we are paused, we wait for user input.
                    pass # Stay paused

        elif event == 'call':
            # We can potentially add call stack tracking here, but for simplicity,
            # we'll rely on `frame.f_back` when a 'line' event occurs.
            pass

        elif event == 'return':
            # When a function returns, its local variables are no longer relevant
            # in the same way. We can update the display to reflect this.
            pass

        elif event == 'exception':
            # Handle exceptions if needed. For now, we'll let Python's default
            # exception handling take over after logging.
            exc_type, exc_value, exc_traceback = arg
            self.update_output_display(f"Exception: {exc_type.__name__}: {exc_value}\n")
            # We might want to pause execution on exception for inspection.
            self.pause_execution(f"Exception: {exc_type.__name__}")

        # If we are paused, we want to prevent the code from automatically running
        # until 'Continue' is pressed.
        if self.execution_paused:
            return self.trace_function # Keep tracing, but stay paused

        return self.trace_function # Essential for continuing execution tracing.

    def update_variable_values(self, frame):
        # Updates the `self.variable_values` dictionary with local variables from the current frame.
        self.variable_values = frame.f_locals.copy() # Copy local variables.
        self.update_variable_display()

    def update_variable_display(self):
        # Updates the Tkinter widget to show the current local variables.
        self.variable_display.config(state=tk.NORMAL)
        self.variable_display.delete("1.0", tk.END)
        if not self.variable_values:
            self.variable_display.insert(tk.END, "No variables found.\n")
        else:
            for name, value in self.variable_values.items():
                self.variable_display.insert(tk.END, f"{name}: {repr(value)}\n")
        self.variable_display.config(state=tk.DISABLED)

    def update_stack_display_from_frame(self, frame):
        # Builds and updates the call stack display by traversing frame back.
        self.stack_display.config(state=tk.NORMAL)
        self.stack_display.delete("1.0", tk.END)
        stack_frames = []
        current_frame = frame
        while current_frame:
            # Get function name and line number for each frame.
            func_name = current_frame.f_code.co_name
            lineno = current_frame.f_lineno
            # We are primarily interested in frames originating from our code.
            if "<string>" in current_frame.f_code.co_filename:
                stack_frames.append(f"{func_name}() at line {lineno}")
            current_frame = current_frame.f_back # Move to the caller's frame.

        # Display the stack from the oldest call to the most recent.
        for frame_info in reversed(stack_frames):
            self.stack_display.insert(tk.END, f"{frame_info}\n")
        self.stack_display.config(state=tk.DISABLED)

    def update_stack_display(self):
        # Placeholder for when no active frame is available.
        self.stack_display.config(state=tk.NORMAL)
        self.stack_display.delete("1.0", tk.END)
        self.stack_display.insert(tk.END, "No active call stack.\n")
        self.stack_display.config(state=tk.DISABLED)

    def highlight_current_line(self):
        # Visually highlights the current line of code in the `code_display`.
        self.code_display.tag_remove("current", "1.0", tk.END)
        self.code_display.tag_add("current", f"{self.current_line_num + 1}.0", f"{self.current_line_num + 1}.end")
        self.code_display.tag_config("current", background="yellow")
        # Ensure the current line is visible.
        self.code_display.see(f"{self.current_line_num + 1}.0")

    def pause_execution(self, reason=""):
        # Pauses the execution of the program.
        self.execution_paused = True
        self.step_button.config(state=tk.NORMAL)
        self.continue_button.config(state=tk.NORMAL)
        self.run_button.config(state=tk.DISABLED)
        self.update_output_display(f"Execution paused: {reason}\n")

    def resume_execution(self):
        # Resumes execution from the paused state.
        self.execution_paused = False
        self.step_button.config(state=tk.DISABLED)
        self.continue_button.config(state=tk.DISABLED)
        self.run_button.config(state=tk.DISABLED) # Keep run button disabled during step/continue
        self.update_output_display("Resuming execution...\n")
        # The `sys.settrace` will continue to be called, and if `execution_paused`
        # is false, it will naturally proceed.

    def step_over(self):
        # Executes the current line and stops at the next line.
        # If the current line is a function call, it will execute the entire function
        # and stop at the line after the call.
        self.resume_execution() # Allow tracing to proceed for one step.

    def continue_execution(self):
        # Continues execution until the next breakpoint or program end.
        self.resume_execution()

    def reset_debugger_state(self):
        # Resets the debugger buttons to their initial state.
        self.is_debugging = False
        self.execution_paused = False
        self.step_button.config(state=tk.DISABLED)
        self.continue_button.config(state=tk.DISABLED)
        self.run_button.config(state=tk.NORMAL)

    def update_output_display(self, text):
        # Appends text to the output display area.
        self.output_display.config(state=tk.NORMAL)
        self.output_display.insert(tk.END, text)
        self.output_display.see(tk.END) # Auto-scroll to the end.
        self.output_display.config(state=tk.DISABLED)

    def handle_right_click(self, event):
        # Handles right-click events on the code display to add/remove breakpoints.
        try:
            # Get the line number where the click occurred.
            line_index = self.code_display.index(f"@{event.x},{event.y}").split('.')[0]
            line_num = int(line_index) - 1 # Convert to 0-based index

            # Toggle breakpoint.
            if line_num in self.breakpoints:
                self.breakpoints.remove(line_num)
                self.code_display.tag_remove(f"breakpoint_{line_num}", f"{line_num + 1}.0", f"{line_num + 1}.end")
            else:
                # Ensure we don't add breakpoints on blank lines or comments if desired (optional complexity).
                # For simplicity, we'll allow breakpoints on any line.
                self.breakpoints.add(line_num)
                self.code_display.tag_add(f"breakpoint_{line_num}", f"{line_num + 1}.0", f"{line_num + 1}.end")
                self.code_display.tag_config(f"breakpoint_{line_num}", background="red")
            self.update_output_display(f"Breakpoint toggled on line {line_num + 1}\n")
        except tk.TclError:
            # Click might be outside of text area or on an empty line.
            pass

    def clear_all_breakpoints(self):
        # Clears all set breakpoints from the code.
        for bp_line in list(self.breakpoints): # Iterate over a copy to allow modification
            self.code_display.tag_remove(f"breakpoint_{bp_line}", f"{bp_line + 1}.0", f"{bp_line + 1}.end")
        self.breakpoints.clear()
        self.update_output_display("All breakpoints cleared.\n")


# --- Example Usage ---
# This part demonstrates how to run the debugger.

if __name__ == "__main__":
    # Create the main Tkinter window.
    root = tk.Tk()
    # Create an instance of our VisualDebugger.
    debugger = VisualDebugger(root)

    # --- Default Code Example ---
    # Provide some sample Python code for the debugger to visualize.
    sample_code = """
def greet(name):
    message = f"Hello, {name}!"
    print(message)
    return message

def main():
    x = 10
    y = 20
    z = x + y
    print(f"Sum is: {z}")
    result = greet("World")
    print(f"Greeting result: {result}")

main()
"""
    debugger.code_display.insert(tk.END, sample_code.strip())

    # Start the Tkinter event loop. This makes the GUI interactive.
    root.mainloop()