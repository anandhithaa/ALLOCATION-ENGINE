# Dynamic Priority-Based Allocation Engine

A high-performance, algorithmic backend engine designed to solve resource allocation conflicts (e.g., dispatch systems, order-matching) using dynamic priority queues.

## Key Features
- **O(log N) Optimization:** Leverages a binary heap structure for priority sorting, avoiding costly O(N log N) full-list re-sorting.
- **Starvation Mitigation:** Features an aging algorithm where item priority scales based on both initial severity weight and total elapsed wait time.
- **Clean Architecture:** Separates data modeling, core heap operations, and simulation drivers.

## Tech Stack
- Language: Python 3.x
- Core Modules: `heapq`, `time`

## Algorithmic Logic
The priority score is dynamically computed as:
Score = (Severity * 1.5) + (Elapsed_Time * 0.8)