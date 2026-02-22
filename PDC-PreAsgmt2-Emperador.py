from mpi4py import MPI

comm = MPI.COMM_WORLD
print("Total processes:", comm.Get_size())
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Master process started.\n")
    
    # Receive results from all worker processes
    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from process {i}:")
        print(f"  Assigned Task: {message['task']}")
        print(f"  Computed Sum: {message['result']}\n")

else:
    # Assign a simple task (data chunk based on rank)
    start = rank * 10
    end = start + 9
    data_chunk = list(range(start, end + 1))
    
    # Perform simple computation
    computed_sum = sum(data_chunk)
    
    # Create message dictionary
    message = {
        "rank": rank,
        "task": f"Sum of numbers from {start} to {end}",
        "result": computed_sum
    }
    
    # Send result to master
    comm.send(message, dest=0)
    