# PDC Assignment 2
## by Radge Michael A. Emperador 

---

# Simple Distributed Message-Passing Coding Exercise

## Objective

The objective of this project is to implement a simple distributed program where multiple processes communicate using message passing. The program demonstrates coordination between a master process and worker processes, with workers sending computed results back to the master.

---

## Instructions

### Step 1: Understand the Task

* One process acts as the **master**.
* Other processes act as **workers**.
* **Workers** send messages to the master.
* The **master** receives and displays messages.

---

### Step 2: Starter Code Reference

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from process {i}: {message}")
else:
    comm.send(f"Hello from process {rank}", dest=0)
```

---

### Step 3: Required Code Changes

Students must modify the starter code to include the following:

1. **Include process rank in the message**.
2. **Include the assigned task** (for example, a data chunk number).
3. **Perform a simple computation**, such as the sum of numbers in the assigned data chunk.
4. **Send the computed result to the master process**.

---

## Expected Output

* The **master process** prints the results from all worker processes.
* Each worker’s message should include:

  * Process rank
  * Assigned task
  * Computed result (e.g., sum of numbers)
* Demonstrates successful distributed communication using message passing.

**Example Output (4 processes):**

```
Total processes: 4
Total processes: 4
Total processes: 4
Total processes: 4
Master process started.

Received from process 1:
  Assigned Task: Sum of numbers from 10 to 19
  Computed Sum: 145

Received from process 2:
  Assigned Task: Sum of numbers from 20 to 29
  Computed Sum: 245

Received from process 3:
  Assigned Task: Sum of numbers from 30 to 39
  Computed Sum: 345
```
---

## Output Screenshots

### In Jupyter Notebook (Before distribution)

<img width="713" height="432" alt="image" src="https://github.com/user-attachments/assets/b51a8821-9b19-40ff-afc7-0a9cec841ec8" />

---

### With python file and CMD (Distribution)

#### Code

<img width="606" height="665" alt="image" src="https://github.com/user-attachments/assets/089af392-f440-4179-80e4-936e46634938" />

#### Output

<img width="673" height="472" alt="image" src="https://github.com/user-attachments/assets/0f313204-77e5-45a1-ab3f-4ad4ebd7ad7b" />

---

## Discussion & Reflection

### 1. Why is message passing required in distributed systems?

Message passing is required in distributed systems because processes operate in separate memory spaces and cannot directly access each other’s data. Since there is no shared memory, communication must occur through explicit send and receive operations. This allows processes to exchange information, coordinate tasks, and synchronize execution in a controlled manner. Message passing also improves system scalability and avoids memory conflicts, making it suitable for systems that run across multiple machines or networked environments.

---

### 2. What happens if one process fails?

If one process fails in a distributed system, the overall computation may be disrupted depending on the role of the failed process. The master process may stop receiving expected messages, leading to incomplete results or program termination. In basic implementations, a single process failure can halt the entire execution. However, more advanced distributed systems implement fault tolerance mechanisms such as timeout detection, redundancy, and process recovery to maintain system reliability and minimize the impact of failures.

---

### 3. How does this model differ from shared-memory programming?

The message passing model differs from shared-memory programming in how processes communicate and manage memory. In message passing, each process has its own separate memory space and communicates by explicitly sending and receiving messages. In contrast, shared-memory programming allows multiple processes or threads to access the same memory space and communicate by reading and writing shared variables. Shared-memory systems require synchronization mechanisms such as locks or semaphores to prevent race conditions, whereas message passing avoids direct memory conflicts by design but requires structured communication between processes.

#### Differences

| Message Passing              | Shared Memory                        |
| ---------------------------- | ------------------------------------ |
| Separate memory              | Common memory                        |
| Explicit communication       | Implicit communication via variables |
| No shared variable conflicts | Requires synchronization control     |

---

## Student Remarks

First time hearing and trying out the python module MPI and was very impressed with how this works. Did not think I can do it as easily like this in one machine. I was confused at first as it was not working inside Jupyter since I thought this was needed to do the actual activity and see the output but it turns out I needed this inside my actual computer which made sense now that I thought about it. It was harder to actually setup the whole MPI than the actual assignment as I needed to add a lot of files to my PATH for the commands. I did not encounter any error throughout the activity except for the commands not working. Very interesting activity and very excited to have more activities like this now that I've setup the necessities. I learned how processes can communicate using explicit send and recv operations and how to coordinate tasks across multiple processes and aggregate results efficiently using the master-worker architecture that was provided in the assignment with additional modifications.


