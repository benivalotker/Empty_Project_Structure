@echo off
python -B -m cProfile -o ./profile/profile_output.out  corrupted_stream.py
pyprof2calltree -i ./profile/profile_output.out -o ./profile/prof.calltree

