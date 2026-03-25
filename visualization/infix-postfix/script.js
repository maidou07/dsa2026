// Infix to Postfix Visualizer
class InfixToPostfixVisualizer {
    constructor() {
        this.expression = '';
        this.tokens = [];
        this.stack = [];
        this.output = [];
        this.currentIndex = 0;
        this.isPlaying = false;
        this.speed = 800;
        this.stepInterval = null;
        this.stepCount = 0;
        
        // DOM Elements
        this.inputElement = document.getElementById('expression-input');
        this.inputDisplay = document.getElementById('input-expression');
        this.outputDisplay = document.getElementById('output-expression');
        this.stackDisplay = document.getElementById('stack-items');
        this.stepDescription = document.getElementById('step-description');
        this.inputIndexElement = document.getElementById('input-index');
        this.stepsCountElement = document.getElementById('steps-count');
        this.stackSizeElement = document.getElementById('stack-size');
        this.inputPointer = document.getElementById('input-pointer');
        
        // Buttons
        this.stepBtn = document.getElementById('step-btn');
        this.playBtn = document.getElementById('play-btn');
        this.pauseBtn = document.getElementById('pause-btn');
        this.resetBtn = document.getElementById('reset-btn');
        this.validateBtn = document.getElementById('validate-btn');
        this.speedSlider = document.getElementById('speed-slider');
        this.speedValue = document.getElementById('speed-value');
        
        // Example buttons
        this.exampleButtons = document.querySelectorAll('.example-btn');
        
        // Initialize
        this.init();
    }
    
    init() {
        // Set initial expression
        this.expression = this.inputElement.value;
        this.parseExpression(this.expression);
        this.render();
        
        // Event Listeners
        this.stepBtn.addEventListener('click', () => this.step());
        this.playBtn.addEventListener('click', () => this.play());
        this.pauseBtn.addEventListener('click', () => this.pause());
        this.resetBtn.addEventListener('click', () => this.reset());
        this.validateBtn.addEventListener('click', () => this.validateAndParse());
        this.inputElement.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') this.validateAndParse();
        });
        
        this.speedSlider.addEventListener('input', () => {
            this.speed = parseInt(this.speedSlider.value);
            this.speedValue.textContent = `${this.speed}ms`;
            if (this.isPlaying) {
                this.pause();
                this.play();
            }
        });
        
        // Example buttons
        this.exampleButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.inputElement.value = btn.getAttribute('data-expr');
                this.validateAndParse();
            });
        });
        
        // Initial speed display
        this.speedValue.textContent = `${this.speed}ms`;
    }
    
    validateAndParse() {
        const expr = this.inputElement.value.trim();
        if (!expr) {
            alert('Please enter an expression');
            return;
        }
        
        // Basic validation - allow alphanumerics, operators, parentheses, spaces
        const validPattern = /^[A-Za-z0-9\+\-\*\/\^\(\)\s]+$/;
        if (!validPattern.test(expr)) {
            alert('Invalid expression. Only alphanumerics, + - * / ^ ( ) and spaces are allowed.');
            return;
        }
        
        // Check parentheses balance
        let balance = 0;
        for (let char of expr) {
            if (char === '(') balance++;
            if (char === ')') balance--;
            if (balance < 0) break;
        }
        if (balance !== 0) {
            alert('Parentheses are not balanced');
            return;
        }
        
        this.reset();
        this.expression = expr;
        this.parseExpression(expr);
        this.render();
    }
    
    parseExpression(expr) {
        // Simple tokenizer - split by spaces or handle contiguous operators/operands
        // This is a simplified version for visualization
        const tokenized = [];
        let current = '';
        
        for (let i = 0; i < expr.length; i++) {
            const char = expr[i];
            if (char === ' ') {
                if (current) {
                    tokenized.push(current);
                    current = '';
                }
                continue;
            }
            
            if (this.isOperator(char) || char === '(' || char === ')') {
                if (current) {
                    tokenized.push(current);
                    current = '';
                }
                tokenized.push(char);
            } else {
                // Operand (letter or digit)
                current += char;
            }
        }
        
        if (current) {
            tokenized.push(current);
        }
        
        this.tokens = tokenized;
    }
    
    isOperator(token) {
        return ['+', '-', '*', '/', '^'].includes(token);
    }
    
    getPrecedence(operator) {
        const precedence = {
            '^': 4,
            '*': 3,
            '/': 3,
            '%': 3,
            '+': 2,
            '-': 2
        };
        return precedence[operator] || 0;
    }
    
    getAssociativity(operator) {
        return operator === '^' ? 'right' : 'left';
    }
    
    step() {
        if (this.currentIndex >= this.tokens.length) {
            // Process remaining stack
            if (this.stack.length > 0) {
                const operator = this.stack.pop();
                this.output.push(operator);
                this.stepDescription.textContent = `Popped remaining operator "${operator}" from stack to output`;
                this.stepCount++;
                this.render();
                return;
            } else {
                this.stepDescription.textContent = 'Conversion complete!';
                return;
            }
        }
        
        const token = this.tokens[this.currentIndex];
        this.currentIndex++;
        this.stepCount++;
        
        if (this.isOperator(token)) {
            this.handleOperator(token);
        } else if (token === '(') {
            this.handleLeftParenthesis(token);
        } else if (token === ')') {
            this.handleRightParenthesis(token);
        } else {
            // Operand
            this.output.push(token);
            this.stepDescription.textContent = `Operand "${token}" → added to output`;
        }
        
        this.render();
    }
    
    handleOperator(operator) {
        while (this.stack.length > 0) {
            const top = this.stack[this.stack.length - 1];
            if (top === '(') break;
            
            const precedenceCurrent = this.getPrecedence(operator);
            const precedenceTop = this.getPrecedence(top);
            const associativity = this.getAssociativity(operator);
            
            if ((associativity === 'left' && precedenceCurrent <= precedenceTop) ||
                (associativity === 'right' && precedenceCurrent < precedenceTop)) {
                const popped = this.stack.pop();
                this.output.push(popped);
                this.stepDescription.textContent = `Operator "${operator}": popped "${popped}" from stack (higher/equal precedence)`;
            } else {
                break;
            }
        }
        
        this.stack.push(operator);
        if (!this.stepDescription.textContent.includes('popped')) {
            this.stepDescription.textContent = `Operator "${operator}" → pushed to stack`;
        } else {
            this.stepDescription.textContent += `, then pushed "${operator}" to stack`;
        }
    }
    
    handleLeftParenthesis(token) {
        this.stack.push(token);
        this.stepDescription.textContent = `"(" → pushed to stack`;
    }
    
    handleRightParenthesis(token) {
        let found = false;
        let poppedTokens = [];
        
        while (this.stack.length > 0) {
            const popped = this.stack.pop();
            if (popped === '(') {
                found = true;
                break;
            }
            this.output.push(popped);
            poppedTokens.push(popped);
        }
        
        if (!found) {
            this.stepDescription.textContent = 'Mismatched parentheses!';
        } else {
            this.stepDescription.textContent = `")" → popped operators ${poppedTokens.join(', ')} from stack until "("`;
        }
    }
    
    play() {
        if (this.isPlaying) return;
        this.isPlaying = true;
        this.playBtn.disabled = true;
        this.pauseBtn.disabled = false;
        
        this.stepInterval = setInterval(() => {
            if (this.currentIndex >= this.tokens.length && this.stack.length === 0) {
                this.pause();
                return;
            }
            this.step();
        }, this.speed);
    }
    
    pause() {
        this.isPlaying = false;
        clearInterval(this.stepInterval);
        this.playBtn.disabled = false;
        this.pauseBtn.disabled = true;
    }
    
    reset() {
        this.pause();
        this.stack = [];
        this.output = [];
        this.currentIndex = 0;
        this.stepCount = 0;
        this.parseExpression(this.expression);
        this.render();
        this.stepDescription.textContent = 'Enter an expression and click Step or Play to start';
    }
    
    render() {
        // Update input display with active token
        this.inputDisplay.innerHTML = '';
        this.tokens.forEach((token, index) => {
            const tokenElement = document.createElement('div');
            tokenElement.className = 'token';
            tokenElement.textContent = token;
            tokenElement.dataset.index = index;
            
            if (index === this.currentIndex - 1) {
                tokenElement.classList.add('active');
            }
            
            this.inputDisplay.appendChild(tokenElement);
        });
        
        // Update pointer position
        if (this.currentIndex > 0 && this.currentIndex <= this.tokens.length) {
            const activeToken = this.inputDisplay.querySelector('.token.active');
            if (activeToken) {
                const rect = activeToken.getBoundingClientRect();
                const containerRect = this.inputDisplay.getBoundingClientRect();
                const left = rect.left - containerRect.left + rect.width / 2;
                this.inputPointer.style.left = `${left}px`;
                this.inputPointer.style.display = 'block';
            }
        } else {
            this.inputPointer.style.display = 'none';
        }
        
        // Update stack display
        this.stackDisplay.innerHTML = '';
        this.stack.forEach((item, index) => {
            const stackItem = document.createElement('div');
            stackItem.className = 'stack-item';
            
            if (this.isOperator(item)) {
                stackItem.classList.add('operator');
            } else if (item === '(' || item === ')') {
                stackItem.classList.add('parenthesis');
            }
            
            stackItem.textContent = item;
            stackItem.style.opacity = 1 - (index * 0.1);
            this.stackDisplay.appendChild(stackItem);
        });
        
        // Update output display
        this.outputDisplay.innerHTML = '';
        this.output.forEach(token => {
            const tokenElement = document.createElement('div');
            tokenElement.className = 'token';
            tokenElement.textContent = token;
            this.outputDisplay.appendChild(tokenElement);
        });
        
        // Update stats
        this.inputIndexElement.textContent = this.currentIndex;
        this.stepsCountElement.textContent = this.stepCount;
        this.stackSizeElement.textContent = this.stack.length;
        
        // Update algorithm steps highlighting
        this.updateAlgorithmSteps();
    }
    
    updateAlgorithmSteps() {
        const steps = document.querySelectorAll('#algorithm-steps li');
        steps.forEach(step => step.classList.remove('step-active'));
        
        if (this.currentIndex >= this.tokens.length && this.stack.length === 0) {
            // Complete
            steps[6].classList.add('step-active');
        } else if (this.currentIndex === 0) {
            steps[0].classList.add('step-active');
        } else if (this.currentIndex < this.tokens.length) {
            const token = this.tokens[this.currentIndex - 1];
            if (this.isOperator(token)) {
                steps[3].classList.add('step-active');
            } else if (token === '(') {
                steps[4].classList.add('step-active');
            } else if (token === ')') {
                steps[5].classList.add('step-active');
            } else {
                steps[2].classList.add('step-active');
            }
        } else {
            steps[1].classList.add('step-active');
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const visualizer = new InfixToPostfixVisualizer();
    
    // Make visualizer globally available for debugging
    window.visualizer = visualizer;
});