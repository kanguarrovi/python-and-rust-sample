use pyo3::prelude::*;

/// Calculate the nth Fibonacci number.
#[pyfunction]
fn fib(n:u32) -> u32 { // This can be changed to u64 for bigger numbers.
    if n <= 1 {
        return n;
    }
    fib(n - 1) + fib(n - 2)
}

/// A Python module implemented in Rust.
#[pymodule]
fn fibbers(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)?; // Every new function is added as this.
    Ok(())
}
