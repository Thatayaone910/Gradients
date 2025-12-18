# Gradients
A small Python project that generates a smooth color gradient directly in your terminal. This project is designed to teach color interpolation, RGB manipulation, and terminal formatting using ANSI escape codes.

Features

Creates smooth horizontal gradients between two colors

Fully displays in the terminal using ANSI escape codes

Beginner-friendly Python code

No third-party libraries required.

How it Works

Interpolate Colors
The program calculates intermediate colors between a start color and an end color using linear interpolation.

Generate RGB Values
Each pixel (or terminal block) is assigned an RGB value based on its position in the gradient.

Print to Terminal
ANSI escape codes are used to set the background color of spaces printed in the terminal, creating a visible gradient.

\x1b[48;2;{r};{g};{b}m → sets the background color

" " * 50 → prints 50 spaces to form a block

\x1b[0m → resets terminal colors back to default

Usage

Run the Python script:

python gradient.py


The gradient will print directly to your terminal, transitioning from red to blue across 50 steps.

Example Output

A horizontal gradient made of colored blocks from red (left) to blue (right) in the terminal.
