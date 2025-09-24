/**
 * A simple calculator utility class for basic mathematical operations.
 * Provides methods for addition, subtraction, multiplication, and division.
 */
export class Calculator {
  /**
   * Adds two numbers together.
   * @param a - The first number
   * @param b - The second number
   * @returns The sum of a and b
   * @example
   * ```typescript
   * const calc = new Calculator();
   * const result = calc.add(5, 3); // returns 8
   * ```
   */
  public add(a: number, b: number): number {
    return a + b;
  }

  /**
   * Subtracts the second number from the first.
   * @param a - The minuend
   * @param b - The subtrahend
   * @returns The difference of a and b
   */
  public subtract(a: number, b: number): number {
    return a - b;
  }

  /**
   * Multiplies two numbers.
   * @param a - The first factor
   * @param b - The second factor
   * @returns The product of a and b
   */
  public multiply(a: number, b: number): number {
    return a * b;
  }

  /**
   * Divides the first number by the second.
   * @param a - The dividend
   * @param b - The divisor
   * @returns The quotient of a and b
   * @throws {Error} When divisor is zero
   */
  public divide(a: number, b: number): number {
    if (b === 0) {
      throw new Error('Division by zero is not allowed');
    }
    return a / b;
  }
}