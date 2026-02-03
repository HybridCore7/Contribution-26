# Learning Objective: Build a basic L-system interpreter in Python to generate
# fractal patterns and draw them using turtle graphics. This tutorial focuses
# on understanding L-system string generation and its translation into drawing commands.

import turtle # Import the turtle module for graphical output.

class LSystemInterpreter:
    # This class encapsulates the logic for an L-system.
    # It handles generating the fractal string and then interpreting it for drawing.

    def __init__(self, axiom, rules, angle):
        # The constructor initializes our L-system with its core components.
        # axiom: The starting string for the L-system. This is our initial state.
        # rules: A dictionary mapping characters to their replacement strings.
        #        These rules define how the system evolves.
        # angle: The turning angle (in degrees) for the turtle when it encounters
        #        '+' or '-' symbols. This controls the branching geometry.
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.current_string = axiom # Initialize the string that will be evolved.

    def generate_string(self, iterations):
        # This method evolves the L-system string over a specified number of iterations.
        # iterations: How many times to apply the rules. More iterations mean more complexity.
        print(f"Generating L-system string for {iterations} iterations...")
        for _ in range(iterations):
            # In each iteration, we build a new string based on the current one.
            next_string_parts = [] # A list to efficiently build the new string.
            for char in self.current_string:
                # For each character in the current string, apply a rule if one exists.
                # If no rule exists for a character, that character remains unchanged.
                next_string_parts.append(self.rules.get(char, char))
            # Join the list of parts back into a single string to become the current_string for the next iteration.
            self.current_string = "".join(next_string_parts)
        print("String generation complete.")
        return self.current_string # Return the final generated fractal string.

    def interpret_and_draw(self, t, segment_length):
        # This method takes the generated L-system string and translates it
        # into drawing commands for a turtle object.
        # t: The turtle object used for drawing.
        # segment_length: The distance the turtle moves for 'F' or 'f' commands.
        print("Interpreting string and drawing with Turtle...")

        # We'll use a stack (a Python list) to save and restore the turtle's state
        # (its current position and heading). This is crucial for creating
        # branching structures when '[' and ']' symbols are encountered.
        turtle_state_stack = []

        for char in self.current_string:
            # Iterate through each character in the generated L-system string.
            if char == 'F' or char == 'f':
                # 'F' (or 'f') typically means "draw forward" by a set distance.
                t.forward(segment_length)
            elif char == '+':
                # '+' means "turn right" by the specified angle.
                t.right(self.angle)
            elif char == '-':
                # '-' means "turn left" by the specified angle.
                t.left(self.angle)
            elif char == '[':
                # '[' means "push current state onto the stack".
                # We save the current (x,y) position and the direction (heading)
                # so we can return to this exact point later, which creates branches.
                turtle_state_stack.append((t.pos(), t.heading()))
            elif char == ']':
                # ']' means "pop state from the stack and restore turtle to it".
                # This allows the turtle to return to a previous branching point,
                # effectively finishing a branch and going back to continue another.
                if turtle_state_stack: # Ensure there's something to pop to prevent errors.
                    pos, heading = turtle_state_stack.pop()
                    t.penup()    # Lift the pen before moving to avoid drawing a line.
                    t.setposition(pos) # Go back to the saved position.
                    t.setheading(heading) # Restore the saved heading/direction.
                    t.pendown()  # Put the pen down to resume drawing from this point.
                else:
                    # This warning indicates a potential mismatch in '[' and ']' symbols.
                    print("Warning: ']' encountered with empty stack. Mismatched brackets?")
            # Other characters (like 'X' in our example) are part of the generation
            # rules but typically don't translate to a direct drawing action.
        print("Drawing complete.")


if __name__ == "__main__":
    # This block runs only when the script is executed directly, not when imported as a module.
    # It demonstrates how to use the LSystemInterpreter to draw a fractal plant.

    # --- 1. Define your L-system ---
    # We define an L-system that generates a basic plant fractal.
    # Axiom: The initial string from which the L-system begins to grow.
    # 'X' often acts as a placeholder that evolves into complex structures.
    initial_axiom = "X"

    # Rules: A dictionary specifying how each character transforms.
    # 'F' usually means "draw forward". 'X' defines the branching pattern.
    fractal_rules = {
        "X": "F+[[X]-X]-F[-FX]+X", # This complex rule dictates the plant's growth and branching.
        "F": "FF"                 # Each 'F' segment grows longer (or denser) with each iteration.
    }

    # Angle: The turning angle (in degrees) for the turtle's '+' and '-' commands.
    # This controls the specific geometry of the branches.
    branching_angle = 25 # A common angle for plant-like fractals.

    # --- 2. Set up Turtle Graphics Environment ---
    screen = turtle.Screen() # Create a graphics window where the turtle will draw.
    screen.setup(width=800, height=800) # Set the size of the drawing window.
    screen.bgcolor("black") # Set the background color for better contrast with the drawing.
    screen.tracer(0) # Turn off automatic screen updates. This makes drawing much faster.
                     # We will manually update the screen once drawing is complete.

    artist = turtle.Turtle() # Create a turtle object, our "artist".
    artist.speed("fastest")  # Set the drawing speed to maximum (0 is fastest).
    artist.color("green")    # Set the color of the lines the turtle draws.
    artist.penup()           # Lift the pen so the turtle can move to its starting position without drawing.
    artist.setheading(90)    # Point the turtle upwards (0 is east, 90 is north).
    artist.setposition(0, -350) # Move the turtle to the bottom center of the screen to start drawing the plant.
    artist.pendown()         # Put the pen down so the turtle starts drawing from here.

    # --- 3. Create and Run the L-system Interpreter ---
    l_system = LSystemInterpreter(initial_axiom, fractal_rules, branching_angle)

    # Choose the number of iterations. More iterations mean more detailed and complex fractals.
    # CAUTION: High iteration numbers can lead to very long strings, slow drawing times,
    # and patterns that might exceed screen boundaries.
    num_iterations = 4
    if num_iterations > 5:
        print("Warning: High iterations may cause slow drawing or very dense patterns.")

    # Generate the fractal string by applying the rules repeatedly.
    final_fractal_string = l_system.generate_string(num_iterations)

    # Define the length of each segment the turtle draws for 'F' commands.
    # We adjust it based on iterations; more iterations mean smaller segments
    # are needed to fit the increasingly complex fractal on screen.
    drawing_segment_length = 10 if num_iterations < 4 else 5

    # Interpret the generated string and instruct the turtle to draw the fractal.
    l_system.interpret_and_draw(artist, drawing_segment_length)

    # --- 4. Finalize Drawing ---
    screen.update() # Manually update the screen to show the completed drawing
                    # (since screen.tracer(0) was used for speed).
    screen.exitonclick() # Keep the graphics window open until the user clicks on it, then close.