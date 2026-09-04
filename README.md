# vs_code_python_github

Python practice and projects written in VS Code 

# Day 1 — Sprint 0, pricing-engine
# Shared library. Shelf-tag printers and POS both import it. Overnight we print on the 
# order of millions of tags. Keep these functions tiny and allocation-light.
# Two tickets. Both are required. Do PRICE-101 first.

# PRICE-101 — Format shelf-tag price from integer cents
# Type: Story · Priority: P3 · Estimate: 2 points

# Service: pricing-engine
# Printers currently concatenate strings and we get "$1.9" instead of "$1.90". Cashiers then fight customers. 
# Fix is a single function they will all call.
