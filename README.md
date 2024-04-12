#  python-and-rust-sample

A simple Rust integration into Python. This repo is just as a note of how to extend python functionality with Rust.

Reference: https://www.youtube.com/watch?v=jlWhnrk8go0

## Installation

Clone this repository

	$ git clone https://github.com/kanguarrovi/python-and-rust-sample.git

Create a virtualenv (on Debian-based Linux)

    $ cd python-and-rust-sample
	$ python3 -m venv venv
	$ source venv/bin/activate

Upgrade pip if it is required 

	$ pip install --upgrade pip

Install requirements 

	$ pip install -r requirements.txt
	

## Run in development

	$ python fib.py 10

## Additional important notes

These are include into the project. This is just a complement.

This library is for build Rust crates and publish them as Python packages. 

    $ pip install maturin

After install Maturin, create a folder and run:

    $ maturin init

Select pyo3

Then ener into the src file and begin to build the Rust crate.

After doing some coding, run into the crate

    $ maturin develop

This will will complile the Rust package and install it into the virtual enviroment.

"Use dev builds for dev speed and release builds for customer speed"

To have it as optimized version into a production environment, run 

    $ maturin develop --release


Crate 'num_bigint' can be used.

Other libraries for experimentation:

| Library | Description |
| --- | --- |
| uuidt | Timestamp-orderable UUIDs for Python, written in Rust |
| polars | Blazingly fast DataFrames |
| pydantic-core | Core validation logic for pydantic |






