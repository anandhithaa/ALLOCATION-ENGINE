from models import Incident
from engine import AllocationEngine

if __name__ == "__main__":
    engine = AllocationEngine()

    # Simulating random incoming incidents out of order
    incidents = [
        Incident(incident_id="INC-001", severity=3, elapsed_time_mins=10), # Low severity, waiting long
        Incident(incident_id="INC-002", severity=9, elapsed_time_mins=1),  # Critical severity, just arrived
        Incident(incident_id="INC-003", severity=6, elapsed_time_mins=5),  # Medium severity
    ]

    print("--- Polling Incoming Incidents ---")
    for inc in incidents:
        engine.register_incident(inc)

    print("\n--- Processing Allocations (Highest Priority First) ---")
    engine.dispatch_next_resource(resource_id="AMB-101")
    engine.dispatch_next_resource(resource_id="AMB-102")
    engine.dispatch_next_resource(resource_id="AMB-103")