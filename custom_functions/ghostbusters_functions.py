#!/usr/bin/env python3
"""Ghostbusters Lab | Step 3"""

def report_ghost_sighting(ghost_name, location="New York City"): # <-- these are PARAMETERS
    """Prints details about the ghost sighting."""
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")  # <-- these are ARGUMENTS
report_ghost_sighting("Stay Puft")  # Invalid call, missing 'location'

