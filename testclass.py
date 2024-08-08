class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.end_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.idle_time = 0
        
        
if __name__ == "__main__":
    processes = [
        Process(1, 4, 5),
        Process(2, 6, 10),
        Process(3, 9, 5),
        Process(4, 0, 8),
        Process(5, 13, 7)
    ]
    
    print(processes[4].process_id)
    lowest_arrival_time = min(processes, key=lambda x: x.arrival_time).arrival_time

# Print the result
print("Lowest Arrival Time:", lowest_arrival_time)
"""for process in processes:
            burst = 0
            save_first_process = True
            if save_first_process:
                save_first_process = False
                arrival = processes[0].arrival_time
                burst = processes[0].burst_time
        
            print(f"Process burst:{process.burst_time}")
            idle_time=0
            if process.arrival_time > current_time:
                idle_time = process.arrival_time - current_time
                current_time = process.arrival_time
            if process.burst_time < burst:
                burst = process.burst_time
                print(f"final burst:{burst} from {process.process_id}")
            elif process.burst_time == burst:
                if process.arrival_time < arrival:
                    burst = process.burst_time
                    print(f"final burst:{burst} from {process.process_id}")
    
            process.end_time = current_time + burst
            process.turnaround_time = process.end_time - process.arrival_time
            process.waiting_time = process.turnaround_time - burst
            #process.idle_time = idle_time
            current_time += burst"""