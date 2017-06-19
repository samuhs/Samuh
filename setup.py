from cx_Freeze import setup, Executable

setup(
    name="RestaUm EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("RestaUm.py")])
