import heapq

class AllocationEngine:
    def __init__(self):
        self.request_queue = []
        self.allocated_log = []

    def register_incident(self, incident):
        incident.calculate_priority()
        heapq.heappush(self.request_queue, incident)
        print(f"[REGISTERED] Incident {incident.incident_id} | Score: {incident.priority_score:.2f}")

    def dispatch_next_resource(self, resource_id):
        if not self.request_queue:
            print("[IDLE] No pending incidents in queue.")
            return None
        
        # Pulls the highest priority item in O(log N) time
        highest_priority_incident = heapq.heappop(self.request_queue)
        
        allocation = {
            "resource_id": resource_id,
            "incident_id": highest_priority_incident.incident_id,
            "dispatched_at": time.time()
        }
        self.allocated_log.append(allocation)
        print(f"[DISPATCHED] Resource {resource_id} assigned to Incident {highest_priority_incident.incident_id}")
        return allocation