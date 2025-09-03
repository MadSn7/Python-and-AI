# 🛠 Java Concurrency Practice Sheet

A structured set of **hands-on exercises** to practice concurrency in Java.  
Organized from **easy → advanced** with hints and stretch goals.  

---

## 🟢 Level 1: Warm-up

### 1. Race Condition Demo
- **Goal:** Show how multiple threads updating a shared counter cause incorrect results.  
- **Hint:** Use a normal `int` and increment inside multiple threads without `synchronized`.  
- **Stretch:** Fix using `synchronized`, then `AtomicInteger`.  

---

### 2. Thread States Logger
- **Goal:** Observe thread lifecycle (`NEW`, `RUNNABLE`, `TERMINATED`).  
- **Hint:** Use `Thread.getState()`.  
- **Stretch:** Write code that pushes a thread into `WAITING` using `wait()` and `notify()`.  

---

## 🟡 Level 2: Synchronization & Communication

### 3. Thread-Safe Counter
- **Goal:** Implement counter with `synchronized`, `ReentrantLock`, and `AtomicInteger`.  
- **Stretch:** Compare performance of the three.  

---

### 4. Producer-Consumer (Classic)
- **Goal:** Implement using `wait()`/`notify()`.  
- **Hint:** Shared buffer (list/queue), producer adds, consumer removes.  
- **Stretch:** Replace with `BlockingQueue`.  

---

### 5. Deadlock Simulation
- **Goal:** Write two threads holding different locks and waiting for each other.  
- **Stretch:** Fix deadlock using lock ordering or `tryLock()`.  

---

## 🟠 Level 3: Executor Framework & Locks

### 6. Simple Thread Pool
- **Goal:** Implement mini `ExecutorService`:
  - Task queue  
  - Worker threads consuming tasks  
- **Hint:** Use `BlockingQueue<Runnable>`.  
- **Stretch:** Add graceful shutdown logic.  

---

### 7. Scheduled Tasks
- **Goal:** Print "Hello" every 2 seconds using `ScheduledExecutorService`.  
- **Stretch:** Cancel after 10 seconds.  

---

### 8. Reader-Writer Lock Example
- **Goal:** Simulate shared cache → multiple readers, fewer writers.  
- **Hint:** Use `ReentrantReadWriteLock`.  
- **Stretch:** Add cache invalidation with `ScheduledExecutorService`.  

---

## 🔴 Level 4: Advanced Concurrency

### 9. Countdown Latch Simulation
- **Goal:** Worker threads start after all are ready.  
- **Hint:** Use `CountDownLatch`.  
- **Stretch:** Convert to `CyclicBarrier` (threads meet at barrier repeatedly).  

---

### 10. Bounded Blocking Queue
- **Goal:** Implement your own `BlockingQueue` with `wait()`/`notify()`.  
- **Stretch:** Add timeout support for `offer()` and `poll()`.  

---

### 11. CompletableFuture Demo
- **Goal:** Call three async tasks, combine results.  
- **Hint:** Use `CompletableFuture.supplyAsync()`, then `thenCombine()`.  
- **Stretch:** Handle exceptions with `exceptionally()`.  

---

## 🔵 Level 5: Expert-Level

### 12. Fork/Join Recursive Sum
- **Goal:** Sum an array of integers using `RecursiveTask`.  
- **Stretch:** Compare runtime with sequential loop.  

---

### 13. Dining Philosophers Problem
- **Goal:** Solve using `ReentrantLock`.  
- **Stretch:** Avoid deadlock using resource hierarchy or `tryLock`.  

---

### 14. Thread Dump Analysis
- **Goal:** Write code that deadlocks → run `jstack` to analyze.  
- **Stretch:** Fix by ordering locks.  

---

### 15. Custom Rate Limiter
- **Goal:** Allow max 5 requests per second.  
- **Hint:** Use `Semaphore`.  
- **Stretch:** Implement token bucket algorithm.  

---

# ✅ How to Use
1. Start with **Level 1–2** → basics and synchronization.  
2. Move to **Level 3–4** → practical tools (`ExecutorService`, locks, latches).  
3. Attempt **Level 5** → system design & real-world patterns.  
4. Always code small demos — don’t just read.  

Happy coding 🚀  