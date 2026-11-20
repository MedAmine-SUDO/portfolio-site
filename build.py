"""Build every page into site/. Run: python3 build.py"""
import runpy
for f in ("build_index.py", "build_work.py", "build_riseup.py"):
    runpy.run_path(f)
