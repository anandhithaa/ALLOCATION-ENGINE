import time

class Incident:
    def __init__(self, incident_id, severity, elapsed_time_mins):
        self.incident_id = incident_id
        self.severity = severity  # Scale of 1-10 (10 being critical)
        self.elapsed_time_mins = elapsed_time_mins
        self.priority_score = 0
        
    def calculate_priority(self):
        # Algorithmic logic: Priority scales exponentially with severity 
        # and linearly with waiting time to prevent starvation.
        self.priority_score = (self.severity * 1.5) + (self.elapsed_time_mins * 0.8)
        return self.priority_score

    # Custom comparison operators so the Heap knows how to sort the objects
    def __lt__(self, other):
        return self.calculate_priority() > other.calculate_priority() # Max-Heap behavior