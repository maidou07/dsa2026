# Infix to Postfix Algorithm Visualization

An interactive visualization of the infix-to-postfix conversion algorithm using the Shunting Yard algorithm.

## Features

- **Interactive Visualization**: Step-by-step visualization of the algorithm with color-coded tokens
- **Real-time Stack Display**: Visual representation of the operator stack
- **Input Pointer**: Shows current token being processed
- **Output Display**: Shows the growing postfix expression
- **Operator Precedence Table**: Reference for operator precedence and associativity
- **Algorithm Steps**: Highlighted algorithm steps as the visualization progresses
- **Interactive Controls**:
  - **Step**: Process one token at a time
  - **Play/Pause**: Auto-step through the algorithm
  - **Reset**: Restart the visualization
  - **Speed Control**: Adjust animation speed
- **Example Expressions**: Pre-defined expressions to try

## How to Use

1. Open `infix-to-postfix.html` in a web browser
2. Enter an infix expression in the input field (e.g., `A + B * C - D / E`)
3. Click **Validate** to parse the expression
4. Use the control buttons:
   - **Step**: Process one token at a time
   - **Play**: Auto-play through the algorithm
   - **Pause**: Pause auto-play
   - **Reset**: Start over
5. Adjust speed with the slider for auto-play
6. Try example expressions with the example buttons

## Algorithm Steps

The visualization follows these steps:

1. Initialize empty stack and output list
2. Read tokens from infix expression left to right
3. **If operand** (letter/number): add to output
4. **If operator**: 
   - While stack has operators with higher or equal precedence, pop them to output
   - Push current operator to stack
5. **If '('**: push to stack
6. **If ')'**: pop from stack to output until '(' is found
7. After reading all tokens, pop remaining operators from stack to output

## Supported Operators

| Operator | Precedence | Associativity |
|----------|------------|---------------|
| ^ (Exponentiation) | 4 | Right-to-left |
| * / % | 3 | Left-to-right |
| + - | 2 | Left-to-right |
| ( ) | 1 (special) | N/A |

## File Structure

- `infix-to-postfix.html` - Main HTML file
- `style.css` - Styling for visualization
- `script.js` - Algorithm implementation and visualization logic
- `test-algorithm.js` - Test cases for the algorithm (Node.js)

## Implementation Details

The visualization uses:
- **HTML5/CSS3** for structure and styling
- **Vanilla JavaScript** (ES6) for algorithm and interactivity
- **Flexbox/Grid** for responsive layout
- **CSS Animations** for visual feedback
- **Font Awesome** icons for UI elements
- **Google Fonts** (Roboto Mono, Inter) for typography

## Browser Compatibility

Works in modern browsers with ES6 support (Chrome 60+, Firefox 55+, Safari 11+, Edge 79+).

## License

This visualization is provided for educational purposes.